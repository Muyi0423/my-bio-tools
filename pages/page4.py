import streamlit as st

def show():
    st.set_page_config(page_title="生物实用工具箱", layout="wide")
    
    st.title("🧰 生物科研全能工具箱")
    st.markdown("""
    > **说明**：本工具箱整合了分子生物学、序列分析、蛋白结构、药物研发及免疫学等领域的 **120+** 常用在线工具。
    """)

    # ==========================================
    # 第一部分：基础与计算（原有内容保留）
    # ==========================================
    st.header("🧬 分子生物学与酶相关")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.subheader("NEBioCalculator")
            st.caption("浓度计算器")
            st.write("DNA、RNA、Protein、sgRNA 设计在线计算。")
            st.link_button("🔗 访问", "https://nebiocalculator.neb.com/#!/protamt")
    with col2:
        with st.container(border=True):
            st.subheader("Tm Calculator")
            st.caption("Tm 退火温度计算")
            st.write("根据酶、引物浓度、序列给出 Tm 值。")
            st.link_button("🔗 访问", "https://tmcalculator.neb.com/#!/main")
    with col3:
        with st.container(border=True):
            st.subheader("Redigest")
            st.caption("双酶切工具")
            st.write("NEB 双酶切模拟工具。")
            st.link_button("🔗 访问", "https://nebcloner.neb.com/#!/redigest")

    col4, col5, col6 = st.columns(3)
    with col4:
        with st.container(border=True):
            st.subheader("Enzyme Finder")
            st.caption("找酶工具")
            st.write("查找内切酶，包含切割序列、Buffer 推荐等。")
            st.link_button("🔗 访问", "https://enzymefinder.neb.com/#!/nebheader")
    with col5:
        with st.container(border=True):
            st.subheader("NovoPro")
            st.caption("综合生物工具")
            st.write("包含蛋白质、多肽、抗体计算、配液等。")
            st.link_button("🔗 访问", "https://www.novopro.cn/tools/")
    with col6:
        st.write("") 

    st.divider()

    st.header("🧪 序列与引物分析")
    col7, col8, col9 = st.columns(3)
    with col7:
        with st.container(border=True):
            st.subheader("Primer3Plus")
            st.caption("引物设计")
            st.write("经典的在线引物设计工具。")
            st.link_button("🔗 访问", "https://www.bioinformatics.nl/cgi-bin/primer3plus/primer3plus.cgi")
    with col8:
        with st.container(border=True):
            st.subheader("Reverse Complement")
            st.caption("反向互补 (南京德泰)")
            st.write("分子工具、格式转化、序列比对。")
            st.link_button("🔗 访问", "https://www.detailbio.com/")
    with col9:
        with st.container(border=True):
            st.subheader("Bioinformatics.org")
            st.caption("序列转换工具")
            st.write("互补、反向或反向互补，忽略空格数字。")
            st.link_button("🔗 访问", "https://www.bioinformatics.org/sms/rev_comp.html")

    col10, col11, col12 = st.columns(3)
    with col10:
        with st.container(border=True):
            st.subheader("Exon-Intron Maker")
            st.caption("基因结构可视化")
            st.write("根据输入序列，自动生成外显子内含子图。")
            st.link_button("🔗 访问", "http://www.wormweb.org/exonintron")
    with col11:
        with st.container(border=True):
            st.subheader("IUPAC 缩写")
            st.caption("碱基和氨基酸缩写")
            st.write("查询标准的碱基和氨基酸缩写代码。")
            st.link_button("🔗 访问", "https://www.bioinformatics.org/sms/iupac.html")
    with col12:
        st.write("")

    st.divider()

    st.header("🧮 实验室常用计算")
    col13, col14, col15 = st.columns(3)
    with col13:
        with st.container(border=True):
            st.subheader("Molarity Calculator")
            st.caption("GraphPad 摩尔浓度")
            st.write("GraphPad 官网的摩尔浓度、稀释计算工具。")
            st.link_button("🔗 访问", "https://www.graphpad.com/quickcalcs/molarityform.cfm")
    with col14:
        with st.container(border=True):
            st.subheader("Biomath Calculators")
            st.caption("Promega 数学计算器")
            st.write("Promega 官网的 DNA 相关计算。")
            st.link_button("🔗 访问", "https://www.promega.cn/resources/tools/biomath/")
    with col15:
        with st.container(border=True):
            st.subheader("Selleck Calculator")
            st.caption("Selleck 浓度计算")
            st.write("摩尔浓度、分子量、稀释计算器。")
            st.link_button("🔗 访问", "https://www.selleck.cn/molaritycalculator.jsp")

    col16, _, _ = st.columns(3)
    with col16:
        with st.container(border=True):
            st.subheader("Beyotime Tools")
            st.caption("碧云天在线工具")
            st.write("浓度计算、蛋白相关网址汇总。")
            st.link_button("🔗 访问", "https://www.beyotime.com/tools.htm")

    st.divider()

    # ==========================================
    # 第二部分：补全的高级与专业工具（新增内容）
    # ==========================================
    
    st.header("📚 文献检索与科研")
    cols = st.columns(4)
    tools_lit = [
        ("PubMed", "https://pubmed.ncbi.nlm.nih.gov/", "生物医学文献首选"),
        ("Sci-hub", "https://sci-hub.se/", "免费下载科研论文"),
        ("Google Scholar", "https://scholar.google.com/", "谷歌学术搜索"),
        ("Web of Science", "https://www.webofscience.com/", "学术引文索引"),
        ("X-Mol", "https://www.x-mol.com/", "化学与生物资讯"),
        ("科研通", "https://www.ablesci.com/", "文献互助平台")
    ]
    for i, (name, url, desc) in enumerate(tools_lit):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("🗄️ 基因组与蛋白数据库")
    cols = st.columns(4)
    tools_db = [
        ("NCBI SRA", "https://www.ncbi.nlm.nih.gov/sra", "高通量测序原始数据"),
        ("GEO", "https://www.ncbi.nlm.nih.gov/geo/", "基因表达综合数据库"),
        ("TRRUST", "https://www.grnpedia.org/trrust/", "转录调控网络"),
        ("HPA", "https://www.proteinatlas.org/", "人类蛋白图谱"),
        ("HGNC", "https://www.genenames.org/", "基因命名委员会"),
        ("Pfam", "https://pfam.xfam.org/", "蛋白质家族"),
        ("InterPro", "https://www.ebi.ac.uk/interpro/", "蛋白结构域"),
        ("BioGRID", "https://thebiogrid.org/", "相互作用数据"),
        ("LncRNA Disease", "http://www.rnanut.net/lncrnadisease/", "LncRNA疾病关联"),
        ("MalaCards", "https://www.malacards.org/", "人类疾病数据库"),
        ("miRBase", "http://www.mirbase.org/", "miRNA序列"),
        ("AnimalTFDB", "http://bioinfo.life.hust.edu.cn/AnimalTFDB4/", "转录因子"),
        ("UCSC Genome", "https://genome.ucsc.edu/", "基因组浏览器"),
        ("Ensembl", "https://www.ensembl.org/", "基因组数据库"),
        ("STRING", "https://string-db.org/", "蛋白互作网络"),
        ("Addgene", "https://www.addgene.org/", "质粒库"),
        ("GeneCards", "https://www.genecards.org/", "基因综合信息"),
        ("UniProt", "https://www.uniprot.org/", "通用蛋白库")
    ]
    for i, (name, url, desc) in enumerate(tools_db):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("🔬 蛋白结构与功能分析")
    cols = st.columns(4)
    tools_struct = [
        ("ExPASy", "https://www.expasy.org/", "生物信息学门户"),
        ("SOPMA", "https://npsa-pbil.ibcp.fr/cgi-bin/npsa_automat.pl?page=npsa_sopma.html", "二级结构预测"),
        ("PSIPRED", "http://bioinf.cs.ucl.ac.uk/psipred/", "二级结构预测"),
        ("DAVID", "https://david.ncifcrf.gov/", "功能注释"),
        ("RCSB PDB", "https://www.rcsb.org/", "3D结构"),
        ("I-TASSER", "https://zhanggroup.org/I-TASSER/", "结构预测"),
        ("NCBI BLAST", "https://blast.ncbi.nlm.nih.gov/", "序列比对"),
        ("Clustal Omega", "https://www.ebi.ac.uk/jdispatcher/msa/clustalo", "多序列比对"),
        ("PrimerBank", "https://pga.mgh.harvard.edu/primerbank/", "qPCR引物"),
        ("Broad sgRNA", "https://portals.broadinstitute.org/gpp/public/", "sgRNA数据库"),
        ("CHOPCHOP", "https://chopchop.cbu.uib.no/", "sgRNA设计"),
        ("CRISPR Pick", "https://portals.broadinstitute.org/gppx/crispick/public", "CRISPR设计")
    ]
    for i, (name, url, desc) in enumerate(tools_struct):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("🧫 蛋白修饰与高级预测")
    cols = st.columns(4)
    tools_pred = [
        ("Kaplan-Meier", "https://kmplot.com/analysis/", "肿瘤预后分析"),
        ("I-Mutant2.0", "http://folding.biofold.org/i-mutant/i-mutant2.0.html", "稳定性预测"),
        ("ENDScript", "https://endscript.ibcp.fr/ESPript/ENDscript/", "序列比对图"),
        ("WebLogo", "http://weblogo.threeplusone.com/create.cgi", "序列标识"),
        ("Protein Sol", "https://protein-sol.manchester.ac.uk/", "溶解度预测"),
        ("Kinase.com", "http://www.kinase.com/kinase_com", "激酶分析"),
        ("NEBcutter", "https://nc3.neb.com/NEBcutter/", "酶切位点"),
        ("PeptideCutter", "https://web.expasy.org/peptide_cutter/", "酶切位点"),
        ("Prop", "https://services.healthtech.dtu.dk/services/ProP-1.0/", "性质预测"),
        ("NetNGlyc", "https://services.healthtech.dtu.dk/services/NetNGlyc-1.0/", "糖基化预测"),
        ("NetPhos", "https://services.healthtech.dtu.dk/services/NetPhos-3.1/", "磷酸化预测"),
        ("NetOGlyc", "https://services.healthtech.dtu.dk/services/NetOGlyc-4.0/", "糖基化预测"),
        ("GeneDesign", "https://academic.oup.com/nar/article/38/suppl_2/W56/1128757", "密码子优化"),
        ("Encorbio", "https://encorbio.com/protocols/Codon.htm", "密码子优化")
    ]
    for i, (name, url, desc) in enumerate(tools_pred):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("🛡️ 抗体信息学")
    cols = st.columns(4)
    tools_ab = [
        ("IMGT", "https://www.imgt.org/", "免疫遗传学"),
        ("AbYsis", "http://www.bioinf.org.uk/abs/", "抗体分析"),
        ("SAbDab", "https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/sabdab/", "抗体结构库"),
        ("CoV-AbDab", "https://opig.stats.ox.ac.uk/webapps/covabdab/", "新冠抗体库"),
        ("IEDB", "https://www.iedb.org/", "抗原表位"),
        ("BepiPred", "https://services.healthtech.dtu.dk/services/BepiPred-2.0/", "表位预测"),
        ("DNAPlotter", "https://sanger-pathogens.github.io/Artemis/DNAPlotter/", "载体绘图"),
        ("IgBLAST", "https://www.ncbi.nlm.nih.gov/igblast/", "Ig序列分析"),
        ("IMGT Repertoire", "https://www.imgt.org/genedb/", "免疫库"),
        ("Nature Antibody", "http://naturalantibody.com/nanobodies", "纳米抗体"),
        ("SDAB-DB", "http://sdab-db.ca/", "单域抗体"),
        ("DiscoTope", "https://services.healthtech.dtu.dk/services/DiscoTope-3.0/", "构象表位")
    ]
    for i, (name, url, desc) in enumerate(tools_ab):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("💊 药物与专利")
    cols = st.columns(4)
    tools_drug = [
        ("cBioPortal", "https://www.cbioportal.org/", "癌症基因组"),
        ("TCGA", "https://portal.gdc.cancer.gov/", "癌症基因组图谱"),
        ("GEPIA2", "http://gepia2.cancer-pku.cn/", "表达分析"),
        ("DrugBank", "https://go.drugbank.com/", "药物数据库"),
        ("TTD", "https://db.idrblab.net/ttd/", "治疗靶点"),
        ("ChEMBL", "https://www.ebi.ac.uk/chembl/", "药物化学"),
        ("ZINC", "http://zinc.docking.org/", "化合物库"),
        ("PubChem", "https://pubchem.ncbi.nlm.nih.gov/", "化学分子"),
        ("SwissTarget", "http://www.swisstargetprediction.ch/", "靶点预测"),
        ("PharmGKB", "https://www.pharmgkb.org/", "药物基因组")
    ]
    for i, (name, url, desc) in enumerate(tools_drug):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("📝 实验 Protocol 与资源")
    cols = st.columns(4)
    tools_proto = [
        ("Bio-protocol", "https://bio-protocol.org/cn/default.aspx", "生物实验方案"),
        ("Springer Protocols", "https://www.springer.com/gp/livingprotocols", "实验手册"),
        ("Cold Spring Harbor", "https://cshprotocols.cshlp.org/", "冷泉港实验方案"),
        ("JoVE", "https://www.jove.com/", "视频实验期刊"),
        ("Addgene Protocols", "https://www.addgene.org/protocols/", "质粒操作指南"),
        ("NEB Protocols", "https://www.neb.com/tools-and-resources/usage-guides-and-selection-charts", "NEB 实验指南"),
        ("Thermo Fisher Protocols", "https://www.thermofisher.com/cn/zh/home/life-science/antibodies/primary-antibodies/protocols.html", "赛默飞实验方案")
    ]
    for i, (name, url, desc) in enumerate(tools_proto):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

    st.divider()

    st.header("🛡️ 免疫与信号通路")
    cols = st.columns(4)
    tools_path = [
        ("KEGG", "https://www.genome.jp/kegg/", "通路数据库"),
        ("Reactome", "https://reactome.org/", "通路数据库"),
        ("WikiPathways", "https://www.wikipathways.org/", "通路数据库"),
        ("PathBank", "https://pathbank.org/", "通路数据库"),
        ("SMPDB", "http://smpdb.ca/", "小分子通路"),
        ("MSigDB", "https://www.gsea-msigdb.org/gsea/msigdb", "基因集数据库"),
        ("GSEA", "https://www.gsea-msigdb.org/gsea/index.jsp", "富集分析")
    ]
    for i, (name, url, desc) in enumerate(tools_path):
        with cols[i % 4]:
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.caption(desc)
                st.link_button("🔗 访问", url)

if __name__ == "__main__":
    show()