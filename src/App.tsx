import algoliasearch from "algoliasearch/lite"
import {
  InstantSearch,
  SearchBox,
  Hits,
  Highlight,
  RefinementList,
  Stats,
  SortBy,
  Pagination,
} from "react-instantsearch-dom";
import "instantsearch.css/themes/algolia.css"
import { Hit } from "react-instantsearch-core"

const searchClient = algoliasearch(
  process.env.REACT_APP_ALGOLIA_APP_ID,
  process.env.REACT_APP_ALGOLIA_API_KEY
)

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
  <InstantSearch indexName="sequences" searchClient={searchClient}>
    <h1>CROSSTOPE</h1>
    < Sidebar />
    <SearchBox />
    <Content />
  </InstantSearch>
)

const Sidebar = () => (
<aside>
   <h2>MHC Allele (peptide aminoacids)</h2> 
    <RefinementList attribute="peptide_lenght" withSearchBox /> 
  <h2>Structure Type</h2> 
    <RefinementList attribute="structure_type" withSearchBox /> 
  <h2>Immunological background</h2>
     <RefinementList attribute="immunological_background" withSearchBox />
</aside>
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
        <img
          style={{ width: "100%", height: "auto" }}
          src={`https://storage.googleapis.com/crosstopecloud/V5/${hit.complex_code}_V5.jpg`}
          alt={`visual representation of pMHC ${hit.sequence}`}
        />
        <Highlight attribute="sequence" hit={hit} />
        <Highlight attribute="source_organism" hit={hit} />
        <Highlight attribute="source_protein"
          link={hit.link_para_source_protein}
          hit={hit} />
        <Highlight attribute="immunological_background" hit={hit} />
        <Highlight attribute="peptide_lenght" hit={hit} />
        <a href={`https://storage.googleapis.com/crosstopecloud/Complexos/${hit.complex_code}.pdb`} download={hit.complex_code}> .pdb file</a>
    </div>
  )
}

export default App