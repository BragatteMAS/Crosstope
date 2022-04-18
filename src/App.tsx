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
    <main>
      <Sidebar />      
      <SearchBox />
      <Content />
    </main>
  </InstantSearch>
)

const Sidebar = () => (
<div>

</div>
)

const Content = () => (
  <div className="content">
    <div className="info" >
      <Stats/>
    </div> 
  <aside>
  <h2>Sidebar</h2> 
    <RefinementList attributeName="structure_type" withSearchBox />
    <RefinementList attributeName="source_organism" />
    <RefinementList attributeName="source_protein" />
    <RefinementList attributeName="mhc_allele" />
    <RefinementList attributeName="complex_code" />
    <RefinementList attributeName="deposition" />
    <RefinementList attributeName="release" />
    <RefinementList attributeName="last_modification" />
    <RefinementList attributeName="immunological_background" />
    <RefinementList attributeName="reference" />
    <RefinementList attributeName="structure_source" />
    <RefinementList attributeName="peptide_lenght" />
    <RefinementList attributeName="structure_type" />
  </aside>
  <Hits hitComponent={HitComponent}/>
  <div className="pagination">
    <Pagination showLast/>
  </div>
  </div>
)

const HitComponent = ({ hit }: { hit: Hit<Epitope> }) => {
  return (
    <div style={{ display: "flex", flexDirection: "column", rowGap: "6px" }}>
      <img
        style={{ width: "100%", height: "auto" }}
        src={`https://storage.googleapis.com/crosstopecloud/V5/${hit.complex_code}_V5.jpg`}
        alt={`visual representation of pMHC ${hit.sequence}`}
      />
      <Highlight attribute="sequence" href={hit.source_protein} hit={hit} />
      <Highlight attribute="source_organism" hit={hit} />
      <Highlight attribute="source_protein" hit={hit} />
      <Highlight attribute="immunological_background" hit={hit} />
      <Highlight attribute="peptide_lenght" hit={hit} />
      <a href={`https://storage.googleapis.com/crosstopecloud/Complexos/${hit.complex_code}.pdb`} download={hit.complex_code}> pdb file</a>
    </div>
  )
}

export default App