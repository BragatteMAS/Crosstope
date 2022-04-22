import algoliasearch from "algoliasearch/lite"
import {
  Hits,
  InstantSearch,
  Highlight,
  RefinementList,
  ClearRefinements,
  SearchBox,
  Stats,
  Pagination,
  DynamicWidgets,
  Panel,
/*   AttributesToRender,
  SortBy,
  Menu, */
} from "react-instantsearch-dom";
import "instantsearch.css/themes/algolia.css"
import { Hit } from "react-instantsearch-core"
import './App.css';

const searchClient = algoliasearch(
  process.env.REACT_APP_ALGOLIA_APP_ID,
  process.env.REACT_APP_ALGOLIA_API_KEY
)

const index = searchClient.initIndex("sequences");

/* index.setSettings({
  attributesForFaceting: [""]
}); */

type Epitope = {
  sequence: string
  epitope_id_by_iedb: string
  link_epitope_id_by_iedb: string
  complex_code: string
  deposition: string
  release: string
  last_modification: string
  structure_type: string
  mhc_allele: string
  source_protein: string
  source_organism: string
  epitope_position: string
  immunological_background: string
  reference: string
  link_para_source_protein: string
  link_para_reference: string
  id_sequence: number
  structure_source: string
  peptide_lenght: string
  link_para_structure_type: string
  objectID: string
}

const App = () => (
  <div className="ais-InstantSearch">
    <InstantSearch indexName="sequences" searchClient={searchClient}>
      <div className="left-panel">
        <ClearRefinements clearsQuery />
        <Sidebar/>
      </div>
      <div className="right-panel">
        <SearchBox />
        <Content />
      </div>
    </InstantSearch>
  </div>
)

const Sidebar = () => (
  <div className="sidebar">
    <h3> MHC Allele</h3> <h5>(peptide aminoacids)</h5>
      <RefinementList attribute="peptide_lenght" /> 
    <h3>Structure Type</h3> 
      <RefinementList attribute="structure_type" /> 
    <h3>Immunological background</h3>
      <RefinementList attribute="immunological_background"  />
  </div>
)

const Content = () => (
  <div className="content">
    <div className="info" >
      <Stats/>
    </div> 
  <Hits hitComponent={HitComponent}/>
  <div className="pagination">
    <Pagination showLast/>
  </div>
  </div>
)

const HitComponent = ({ hit }: { hit: Hit<Epitope> }) => {
  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      rowGap: "4px",
      }}>
        <div className="hit-image">
          <img
            style={{ width: "100%", height: "auto" }}
            src={`https://storage.googleapis.com/crosstopecloud/V5/${hit.complex_code}_V5.jpg`}
            alt={`visual representation of pMHC ${hit.sequence}`}
          />
        <div className="hit-sequence">
          <Highlight attribute="sequence" hit={hit} />  
        </div>
        <div className="peptide">
          <Highlight attribute="peptide_lenght" hit={hit} />
        </div>
        <div className="immune background">
          <Highlight attribute="immunological_background" hit={hit} />
        </div>
        <div className="hit-source_organism">
          <Highlight attribute="source_organism"
          src={`${hit.link_para_source_protein}`}
          hit={hit}
          />
        </div>
        <div className="hit-link_para_source_protein">
          <Highlight attribute="link_para_source_protein" hit={hit} />
        </div>
        <div className="pdf file">
          <a href={`https://storage.googleapis.com/crosstopecloud/Complexos/${hit.complex_code}.pdb`} download={hit.complex_code}> .pdb file</a>
        </div>
    </div>
  </div>
  )
}

export default App