export function tools() {
    return (
        <div id="content">
            <header>
                <h1>Crosstope tools</h1>
            </header>
            <h3>Presentation</h3>
                <p>
                    The Structural Data Bank for Cross-Reactivity is a curate repository of three-dimensional structures of MHC: epitope complexes, focused on immunogenicity, similarity relationships and cross-reactivity prediction. <br></br>
                    <a>
                        Cellular immunity has a major role in the surveillance against viral infections. Through the interaction between the T Cell Receptor (TCR) and the Major Histocompatibility Complex (MHC), Cytotoxic T Lymphocytes (CTL) are able to recognize viral peptides presented in the cells surface, and thus, eliminate the infected cells. Each TCR is able to interact with thousands of MHC:epitope complexes, but few of these interactions will trigger a CTL response. The capacity of a given T lymphocyte to recognizedifferent peptides in the cleft of a given MHC is defined as Cross-Reactivity, and it has great influence over phenomena such as heterologous immunity and molecular mimicry. <br></br>
                        The CrossTope is a curate repository of three-dimensional structures of MHC:epitope complexes, focused on immunogenicity, similarity relashionships and cross-reactivity prediction. Our main idea is that immunogenic epitopes share characteristics that stimulates a Citotoxic T Lymphocyte to respond againstdifferent peptides presented by a given MHC allele. The complexes hosted by these databank were obtained by large-scale in silico construction of three-dimensional models of MHC:peptide complexes, using a new approach developed by our group (D1-EM-D2, Antunes et al, 2010). This structural dataset allowed us to verify that the TCR-interaction surface of pMHC complexes has a shared pattern of charge distribution among complexes with recognized cross-reactivity.
                    </a>
                </p>
                
            <h3>Tools</h3>
                <div class="content">
                    <div class="div-section">
                        <span class="section"> </span>
                        <h4>Docktope</h4>
                        <div class="tool-description"> 
                            DockTope is a web-based tool, based on D1-EM-D2 approach, intended to allow the pMHC-I modeling.
                        </div>
                        <div class="Docktope-tool">
                            <a href="http://tools.iedb.org/docktope/"> <img src="./img/docktope.png" alt="" /></a>
                        </div>
                    </div>
                </div>
            <br></br>    
        
            <div class="div-section">
                <span class="section"> </span>
                    <h4>Financial Support</h4>		
                    <div class="text-financial"> 
                    Funded by a grant from Bill & Melinda Gates Foundation through the Grand Challenges Exploration Initiative (grant #53049). Supported by two Brazilian Agencies: CAPES/PNPD (23038.035722/2008-19) and CNPq.
                    </div>
                <img src="./img/financial-support.png" border="0" class="financial" />
            </div>            
        </div>
    );
}