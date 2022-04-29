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
} from "react-instantsearch-dom";
import "instantsearch.css/themes/algolia.css"
import { Hit } from "react-instantsearch-core"
import './App.css';

const searchClient = algoliasearch(
  process.env.REACT_APP_ALGOLIA_APP_ID,
  process.env.REACT_APP_ALGOLIA_API_KEY
)

/* const index = searchClient.initIndex("sequences"); //alternative to index from algoliasearch */

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
    <h5> MHC Allele </h5>
      <RefinementList attribute="peptide_lenght" /> 
    <h5>Structure Type</h5> 
      <RefinementList attribute="structure_type" /> 
    <h5>Immunological background</h5>
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
          <a href={`https://storage.googleapis.com/crosstopecloud/V5/${hit.complex_code}_V5.jpg`} target="_blank" rel="noreferrer, nofollow, noopener, external" download={hit.complex_code}>
            <img
              src={`https://storage.googleapis.com/crosstopecloud/V5/${hit.complex_code}_V5.jpg`}
              style={{ width: "100%", height: "auto" }}
              alt={`visual representation of pMHC ${hit.sequence}`}
            />
          </a>
        <div className="pdf file">
          <a href={`https://storage.googleapis.com/crosstopecloud/Complexos/${hit.complex_code}.pdb`} download={hit.complex_code}>
            <img
             src="../img/pdb.svg"
             style={{float:"right",margin:"-15px", width: "42%" }}
             alt="pdb file from epitope sequence for download"
             />
          </a>
        </div >
        <div className="hit-sequence">
          <Highlight
           attribute="sequence"
           hit={hit} />
        </div>
        <div className="peptide">
          <Highlight
           attribute="peptide_lenght"
           hit={hit} />
        </div>
        <div className="hit-structure">
          <Highlight
           attribute="structure_type"
           hit={hit} />
        </div>
        <div className="immune background">
          <a href={hit.link_epitope_id_by_iedb} target="_blank" rel="noreferrer, nofollow, noopener, external" >
          <Highlight
           attribute="immunological_background"
           hit={hit} />
          </a>
        </div>
        <div className="source_protein">
          <a href={hit.link_para_source_protein} target="_blank" rel="noreferrer, nofollow, noopener, external" >
          <Highlight
          attribute="source_protein"
          hit={hit}
          />
          </a>
        <div className="source_organism">
          <a href={hit.link_para_reference} target="_blank" rel="noreferrer, nofollow, noopener, external"> 
          <Highlight
           attribute="source_organism"
           hit={hit}
          />
          </a>
        </div>
        </div>
      </div>
  </div>
  )
}

export default App
