
import streamlit as st
import pandas as pd

def show():
    st.set_page_config(page_title="荧光基团查询工具", layout="wide")
    
    st.title("\U0001f52c 荧光基团光谱查询工具")
    st.markdown("""> **说明**：在下方搜索框中输入荧光基团名称（支持模糊搜索），即可查询其激发光（Excitation）和发射光（Emission）波长。例如：搜索 "DAPI" 或 "FITC" 或 "Alexa" 等关键词。""")
    
    st.divider()
    
    query = st.text_input(
        "\U0001f50d 搜索荧光基团名称",
        placeholder="请输入荧光基团名称，如 DAPI、FITC、Alexa 等...",
        label_visibility="visible"
    )
    
    if query:
        query_lower = query.lower()
        results = [
            d for d in dyes_data
            if query_lower in d["name"].lower()
        ]
        
        if results:
            st.success(f"找到 {len(results)} 条匹配结果：")
            
            table_data = []
            for i, dye in enumerate(results, 1):
                table_data.append(
                    [str(i), dye["name"], dye["excitation"], dye["emission"]]
                )
            
            st.dataframe(pd.DataFrame(table_data, columns=["序号", "荧光基团名称", "激发光 (Excitation)", "发射光 (Emission)"]))
            
            # 在结果表格下方添加 Cytomaton 光谱查看器链接
            st.divider()
            st.markdown(
                '<div style="text-align: center; padding: 12px; background-color: #f0f7ff; border-radius: 8px; border: 1px solid #4A90D9;">'
                '<a href="https://www.cytomaton.ai/tools/fluorophore-spectrum-viewer" target="_blank" '
                'style="display: inline-block; padding: 10px 24px; background-color: #4A90D9; color: white; '
                'text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 15px;">'
                '🔬 在 Cytomaton 光谱查看器中查看完整光谱</a></div>',
                unsafe_allow_html=True
            )
            st.caption("点击上方链接可跳转到 Cytomaton 光谱查看器，查看该荧光基团的详细光谱曲线图。")
        else:
            st.warning(f"未找到与 \"{query}\" 匹配的荧光基团，请尝试其他关键词。")
    else:
        st.info("\u2139\ufe0f 请在上方搜索框中输入荧光基团名称进行查询。")
        st.divider()
        
        st.subheader("\U0001f4cb 数据概览")
        st.write(f"本工具箱共收录 **{len(dyes_data)}** 个荧光基团的光谱数据。")
        st.write("以下是一些常用的荧光基团示例：")
        
        common_keywords = ["DAPI", "FITC", "GFP", "eGFP", "CFP", "YFP", "RFP",
                          "Alexa 488", "Alexa 555", "Alexa 594", "Alexa 647",
                          "Cy2", "Cy3", "Cy5", "TRITC", "mCherry", "BODIPY"]
        
        found_common = []
        for kw in common_keywords:
            for d in dyes_data:
                if kw.lower() in d["name"].lower():
                    found_common.append((d["name"], d["excitation"], d["emission"]))
                    break
        
        if found_common:
            common_table = [
                ["荧光基团", "激发光", "发射光"]
            ] + [[name, exc, emi] for name, exc, emi in found_common]
            st.dataframe(pd.DataFrame(common_table, columns=["常用荧光基团", "激发光 (nm)", "发射光 (nm)"]))


# ==========================================
# 荧光基团数据库（共 257 条）
# ==========================================
dyes_data = [
    {"name": "1,8-ANS (1-Anilinonaphthalene-8-sulfonic acid)", "excitation": "375 nm", "emission": "480 nm"},
    {"name": "1-Anilinonaphthalene-8-sulfonic acid (1,8-ANS)", "excitation": "375 nm", "emission": "479 nm"},
    {"name": "5-(and-6)-Carboxy-2\', 7\'-dichlorofluorescein pH 9.0", "excitation": "504 nm", "emission": "525 nm"},
    {"name": "5-FAM pH 9.0", "excitation": "492 nm", "emission": "518 nm"},
    {"name": "5-ROX (5-Carboxy-X-rhodamine, triethylammonium salt)", "excitation": "578 nm", "emission": "604 nm"},
    {"name": "5-ROX pH 7.0", "excitation": "578 nm", "emission": "604 nm"},
    {"name": "5-TAMRA", "excitation": "549 nm", "emission": "577 nm"},
    {"name": "5-TAMRA pH 7.0", "excitation": "553 nm", "emission": "576 nm"},
    {"name": "5-TAMRA-MeOH", "excitation": "543 nm", "emission": "567 nm"},
    {"name": "6 JOE", "excitation": "520 nm", "emission": "548 nm"},
    {"name": "6,8-Difluoro-7-hydroxy-4-methylcoumarin pH 9.0", "excitation": "358 nm", "emission": "450 nm"},
    {"name": "6-Carboxyrhodamine 6G pH 7.0", "excitation": "526 nm", "emission": "547 nm"},
    {"name": "6-Carboxyrhodamine 6G, hydrochloride", "excitation": "525 nm", "emission": "547 nm"},
    {"name": "6-HEX, SE pH 9.0", "excitation": "534 nm", "emission": "559 nm"},
    {"name": "6-TET, SE pH 9.0", "excitation": "521 nm", "emission": "542 nm"},
    {"name": "7-Amino-4-methylcoumarin pH 7.0", "excitation": "346 nm", "emission": "442 nm"},
    {"name": "7-Hydroxy-4-methylcoumarin", "excitation": "360 nm", "emission": "447 nm"},
    {"name": "7-Hydroxy-4-methylcoumarin pH 9.0", "excitation": "361 nm", "emission": "448 nm"},
    {"name": "Acridine Orange", "excitation": "431 nm", "emission": "520 nm"},
    {"name": "Alexa 350", "excitation": "343 nm", "emission": "441 nm"},
    {"name": "Alexa 405", "excitation": "401 nm", "emission": "421 nm"},
    {"name": "Alexa 430", "excitation": "431 nm", "emission": "540 nm"},
    {"name": "Alexa 488", "excitation": "493 nm", "emission": "520 nm"},
    {"name": "Alexa 532", "excitation": "528 nm", "emission": "553 nm"},
    {"name": "Alexa 546", "excitation": "562 nm", "emission": "573 nm"},
    {"name": "Alexa 555", "excitation": "553 nm", "emission": "568 nm"},
    {"name": "Alexa 568", "excitation": "576 nm", "emission": "603 nm"},
    {"name": "Alexa 594", "excitation": "590 nm", "emission": "619 nm"},
    {"name": "Alexa 647", "excitation": "653 nm", "emission": "669 nm"},
    {"name": "Alexa 660", "excitation": "664 nm", "emission": "691 nm"},
    {"name": "Alexa 680", "excitation": "679 nm", "emission": "703 nm"},
    {"name": "Alexa 700", "excitation": "696 nm", "emission": "720 nm"},
    {"name": "Alexa Fluor 430 antibody conjugate pH 7.2", "excitation": "431 nm", "emission": "540 nm"},
    {"name": "Alexa Fluor 488 antibody conjugate pH 8.0", "excitation": "499 nm", "emission": "520 nm"},
    {"name": "Alexa Fluor 488 hydrazide-water", "excitation": "493 nm", "emission": "518 nm"},
    {"name": "Alexa Fluor 532 antibody conjugate pH 7.2", "excitation": "528 nm", "emission": "553 nm"},
    {"name": "Alexa Fluor 555 antibody conjugate pH 7.2", "excitation": "553 nm", "emission": "568 nm"},
    {"name": "Alexa Fluor 568 antibody conjugate pH 7.2", "excitation": "579 nm", "emission": "603 nm"},
    {"name": "Alexa Fluor 610 R-phycoerythrin streptavidin pH 7.2", "excitation": "567 nm", "emission": "627 nm"},
    {"name": "Alexa Fluor 647 antibody conjugate pH 7.2", "excitation": "653 nm", "emission": "668 nm"},
    {"name": "Alexa Fluor 647 R-phycoerythrin streptavidin pH 7.2", "excitation": "569 nm", "emission": "666 nm"},
    {"name": "Alexa Fluor 660 antibody conjugate pH 7.2", "excitation": "663 nm", "emission": "691 nm"},
    {"name": "Alexa Fluor 680 antibody conjugate pH 7.2", "excitation": "679 nm", "emission": "702 nm"},
    {"name": "Alexa Fluor 700 antibody conjugate pH 7.2", "excitation": "696 nm", "emission": "719 nm"},
    {"name": "Allophycocyanin pH 7.5", "excitation": "651 nm", "emission": "660 nm"},
    {"name": "AMCA conjugate", "excitation": "347 nm", "emission": "444 nm"},
    {"name": "Amino Coumarin", "excitation": "345 nm", "emission": "442 nm"},
    {"name": "APC (allophycocyanin)", "excitation": "650 nm", "emission": "660 nm"},
    {"name": "Atto 647", "excitation": "644 nm", "emission": "670 nm"},
    {"name": "Auramine O", "excitation": "431 nm", "emission": "501 nm"},
    {"name": "BCECF pH 5.5", "excitation": "485 nm", "emission": "521 nm"},
    {"name": "BCECF pH 9.0", "excitation": "501 nm", "emission": "527 nm"},
    {"name": "BFP (Blue Fluorescent Protein)", "excitation": "380 nm", "emission": "439 nm"},
    {"name": "BO-PRO-1-DNA", "excitation": "462 nm", "emission": "482 nm"},
    {"name": "BO-PRO-3-DNA", "excitation": "574 nm", "emission": "604 nm"},
    {"name": "BOBO-1-DNA", "excitation": "461 nm", "emission": "484 nm"},
    {"name": "BOBO-3-DNA", "excitation": "570 nm", "emission": "605 nm"},
    {"name": "BODIPY 650/665-X, MeOH", "excitation": "646 nm", "emission": "664 nm"},
    {"name": "BODIPY FL conjugate", "excitation": "503 nm", "emission": "512 nm"},
    {"name": "BODIPY FL, MeOH", "excitation": "502 nm", "emission": "511 nm"},
    {"name": "Bodipy R6G SE", "excitation": "528 nm", "emission": "547 nm"},
    {"name": "BODIPY R6G, MeOH", "excitation": "528 nm", "emission": "547 nm"},
    {"name": "BODIPY TMR-X antibody conjugate pH 7.2", "excitation": "544 nm", "emission": "573 nm"},
    {"name": "Bodipy TMR-X conjugate", "excitation": "544 nm", "emission": "573 nm"},
    {"name": "BODIPY TMR-X, MeOH", "excitation": "544 nm", "emission": "570 nm"},
    {"name": "BODIPY TMR-X, SE", "excitation": "544 nm", "emission": "570 nm"},
    {"name": "BODIPY TR-X phallacidin pH 7.0", "excitation": "590 nm", "emission": "621 nm"},
    {"name": "BODIPY TR-X, MeOH", "excitation": "588 nm", "emission": "621 nm"},
    {"name": "BODIPY TR-X, SE", "excitation": "588 nm", "emission": "621 nm"},
    {"name": "BOPRO-1", "excitation": "462 nm", "emission": "482 nm"},
    {"name": "BOPRO-3", "excitation": "574 nm", "emission": "604 nm"},
    {"name": "Calcein", "excitation": "493 nm", "emission": "514 nm"},
    {"name": "Calcein pH 9.0", "excitation": "494 nm", "emission": "514 nm"},
    {"name": "Calcium Crimson", "excitation": "589 nm", "emission": "608 nm"},
    {"name": "Calcium Crimson Ca2+", "excitation": "590 nm", "emission": "608 nm"},
    {"name": "Calcium Green", "excitation": "506 nm", "emission": "530 nm"},
    {"name": "Calcium Green-1 Ca2+", "excitation": "506 nm", "emission": "529 nm"},
    {"name": "Calcium Orange", "excitation": "549 nm", "emission": "574 nm"},
    {"name": "Calcium Orange Ca2+", "excitation": "549 nm", "emission": "573 nm"},
    {"name": "Carboxynaphthofluorescein pH 10.0", "excitation": "600 nm", "emission": "674 nm"},
    {"name": "Cascade Blue", "excitation": "398 nm", "emission": "420 nm"},
    {"name": "Cascade Blue BSA pH 7.0", "excitation": "401 nm", "emission": "419 nm"},
    {"name": "Cascade Yellow", "excitation": "399 nm", "emission": "549 nm"},
    {"name": "Cascade Yellow antibody conjugate pH 8.0", "excitation": "399 nm", "emission": "549 nm"},
    {"name": "CFDA", "excitation": "495 nm", "emission": "517 nm"},
    {"name": "CFP (Cyan Fluorescent Protein)", "excitation": "434 nm", "emission": "474 nm"},
    {"name": "CI-NERF pH 2.5", "excitation": "504 nm", "emission": "541 nm"},
    {"name": "CI-NERF pH 6.0", "excitation": "513 nm", "emission": "538 nm"},
    {"name": "Citrine", "excitation": "515 nm", "emission": "530 nm"},
    {"name": "Coumarin", "excitation": "360 nm", "emission": "447 nm"},
    {"name": "Cy 2", "excitation": "489 nm", "emission": "503 nm"},
    {"name": "Cy 3", "excitation": "549 nm", "emission": "562 nm"},
    {"name": "Cy 3.5", "excitation": "578 nm", "emission": "591 nm"},
    {"name": "Cy 5", "excitation": "646 nm", "emission": "664 nm"},
    {"name": "Cy 5.5", "excitation": "673 nm", "emission": "692 nm"},
    {"name": "CyQUANT GR-DNA", "excitation": "502 nm", "emission": "523 nm"},
    {"name": "DansylCadaverine", "excitation": "335 nm", "emission": "524 nm"},
    {"name": "DansylCadaverine, MeOH", "excitation": "335 nm", "emission": "526 nm"},
    {"name": "DAPI", "excitation": "358 nm", "emission": "463 nm"},
    {"name": "DAPI-DNA", "excitation": "359 nm", "emission": "461 nm"},
    {"name": "Dapoxyl (2-aminoethyl) sulfonamide", "excitation": "372 nm", "emission": "582 nm"},
    {"name": "DDAO pH 9.0", "excitation": "648 nm", "emission": "657 nm"},
    {"name": "Di-8 ANEPPS", "excitation": "469 nm", "emission": "630 nm"},
    {"name": "Di-8-ANEPPS-lipid", "excitation": "469 nm", "emission": "631 nm"},
    {"name": "DiI", "excitation": "551 nm", "emission": "565 nm"},
    {"name": "DiO", "excitation": "487 nm", "emission": "501 nm"},
    {"name": "DM-NERF pH 4.0", "excitation": "493 nm", "emission": "530 nm"},
    {"name": "DM-NERF pH 7.0", "excitation": "509 nm", "emission": "537 nm"},
    {"name": "DsRed", "excitation": "563 nm", "emission": "581 nm"},
    {"name": "DTAF", "excitation": "495 nm", "emission": "517 nm"},
    {"name": "dTomato", "excitation": "554 nm", "emission": "581 nm"},
    {"name": "DyLight 350", "excitation": "332 nm", "emission": "435 nm"},
    {"name": "DyLight 405", "excitation": "399 nm", "emission": "434 nm"},
    {"name": "DyLight 488", "excitation": "493 nm", "emission": "518 nm"},
    {"name": "DyLight 549", "excitation": "555 nm", "emission": "569 nm"},
    {"name": "DyLight 594", "excitation": "592 nm", "emission": "616 nm"},
    {"name": "DyLight 633", "excitation": "624 nm", "emission": "646 nm"},
    {"name": "DyLight 649", "excitation": "652 nm", "emission": "668 nm"},
    {"name": "DyLight 680", "excitation": "678 nm", "emission": "706 nm"},
    {"name": "eCFP (Enhanced Cyan Fluorescent Protein)", "excitation": "437 nm", "emission": "476 nm"},
    {"name": "eGFP (Enhanced Green Fluorescent Protein)", "excitation": "488 nm", "emission": "509 nm"},
    {"name": "Eosin", "excitation": "524 nm", "emission": "546 nm"},
    {"name": "Eosin antibody conjugate pH 8.0", "excitation": "525 nm", "emission": "546 nm"},
    {"name": "Erythrosin-5-isothiocyanate pH 9.0", "excitation": "533 nm", "emission": "554 nm"},
    {"name": "Ethidium Bromide", "excitation": "524 nm", "emission": "605 nm"},
    {"name": "Ethidium homodimer-1-DNA", "excitation": "528 nm", "emission": "617 nm"},
    {"name": "Ethidiumhomodimer", "excitation": "528 nm", "emission": "617 nm"},
    {"name": "evoglow-Bs1", "excitation": "448 nm", "emission": "496 nm"},
    {"name": "evoglow-Bs2", "excitation": "448 nm", "emission": "496 nm"},
    {"name": "evoglow-Pp1", "excitation": "448 nm", "emission": "495 nm"},
    {"name": "eYFP (Enhanced Yellow Fluorescent Protein)", "excitation": "514 nm", "emission": "526 nm"},
    {"name": "FDA", "excitation": "495 nm", "emission": "517 nm"},
    {"name": "FITC", "excitation": "495 nm", "emission": "517 nm"},
    {"name": "FITC antibody conjugate pH 8.0", "excitation": "495 nm", "emission": "519 nm"},
    {"name": "FlAsH", "excitation": "509 nm", "emission": "529 nm"},
    {"name": "Fluo-3", "excitation": "506 nm", "emission": "527 nm"},
    {"name": "Fluo-3 Ca2+", "excitation": "506 nm", "emission": "527 nm"},
    {"name": "Fluo-4", "excitation": "494 nm", "emission": "516 nm"},
    {"name": "Fluor-Ruby", "excitation": "554 nm", "emission": "582 nm"},
    {"name": "Fluorescein", "excitation": "495 nm", "emission": "517 nm"},
    {"name": "Fluorescein 0.1 M NaOH", "excitation": "493 nm", "emission": "513 nm"},
    {"name": "Fluorescein antibody conjugate pH 8.0", "excitation": "493 nm", "emission": "517 nm"},
    {"name": "Fluorescein dextran pH 8.0", "excitation": "501 nm", "emission": "524 nm"},
    {"name": "Fluorescein pH 9.0", "excitation": "490 nm", "emission": "514 nm"},
    {"name": "Fluoro-Emerald", "excitation": "495 nm", "emission": "524 nm"},
    {"name": "FM 1-43", "excitation": "472 nm", "emission": "578 nm"},
    {"name": "FM 1-43 lipid", "excitation": "473 nm", "emission": "579 nm"},
    {"name": "FM 4-64", "excitation": "508 nm", "emission": "751 nm"},
    {"name": "FM 4-64, 2% CHAPS", "excitation": "506 nm", "emission": "751 nm"},
    {"name": "Fura Red Ca2+", "excitation": "435 nm", "emission": "670 nm"},
    {"name": "Fura Red, high Ca", "excitation": "434 nm", "emission": "659 nm"},
    {"name": "Fura Red, low Ca", "excitation": "472 nm", "emission": "673 nm"},
    {"name": "Fura-2 Ca2+sup>", "excitation": "336 nm", "emission": "505 nm"},
    {"name": "Fura-2, high Ca", "excitation": "336 nm", "emission": "504 nm"},
    {"name": "Fura-2, no Ca", "excitation": "367 nm", "emission": "515 nm"},
    {"name": "GFP (S65T)", "excitation": "489 nm", "emission": "509 nm"},
    {"name": "HcRed", "excitation": "590 nm", "emission": "614 nm"},
    {"name": "Hoechst 33258", "excitation": "352 nm", "emission": "455 nm"},
    {"name": "Hoechst 33258-DNA", "excitation": "352 nm", "emission": "455 nm"},
    {"name": "Hoechst 33342", "excitation": "352 nm", "emission": "455 nm"},
    {"name": "Indo-1 Ca2+", "excitation": "346 nm", "emission": "404 nm"},
    {"name": "Indo-1, Ca free", "excitation": "346 nm", "emission": "479 nm"},
    {"name": "Indo-1, Ca saturated", "excitation": "331 nm", "emission": "404 nm"},
    {"name": "JC-1", "excitation": "592 nm", "emission": "595 nm"},
    {"name": "JC-1 pH 8.2", "excitation": "593 nm", "emission": "595 nm"},
    {"name": "Lissaminerhodamine", "excitation": "572 nm", "emission": "590 nm"},
    {"name": "LOLO-1-DNA", "excitation": "568 nm", "emission": "580 nm"},
    {"name": "Lucifer Yellow, CH", "excitation": "428 nm", "emission": "542 nm"},
    {"name": "LysoSensor Blue", "excitation": "374 nm", "emission": "424 nm"},
    {"name": "LysoSensor Blue pH 5.0", "excitation": "374 nm", "emission": "424 nm"},
    {"name": "LysoSensor Green", "excitation": "447 nm", "emission": "504 nm"},
    {"name": "LysoSensor Green pH 5.0", "excitation": "447 nm", "emission": "502 nm"},
    {"name": "LysoSensor Yellow pH 3.0", "excitation": "389 nm", "emission": "542 nm"},
    {"name": "LysoSensor Yellow pH 9.0", "excitation": "335 nm", "emission": "530 nm"},
    {"name": "LysoTracker Blue", "excitation": "373 nm", "emission": "421 nm"},
    {"name": "LysoTracker Green", "excitation": "503 nm", "emission": "509 nm"},
    {"name": "LysoTracker Red", "excitation": "578 nm", "emission": "589 nm"},
    {"name": "Magnesium Green", "excitation": "507 nm", "emission": "530 nm"},
    {"name": "Magnesium Green Mg2+", "excitation": "507 nm", "emission": "531 nm"},
    {"name": "Magnesium Orange", "excitation": "550 nm", "emission": "575 nm"},
    {"name": "Marina Blue", "excitation": "362 nm", "emission": "464 nm"},
    {"name": "mBanana", "excitation": "540 nm", "emission": "553 nm"},
    {"name": "mCherry", "excitation": "587 nm", "emission": "610 nm"},
    {"name": "mHoneydew", "excitation": "478 nm", "emission": "562 nm"},
    {"name": "MitoTracker Green", "excitation": "490 nm", "emission": "512 nm"},
    {"name": "MitoTracker Green FM, MeOH", "excitation": "490 nm", "emission": "512 nm"},
    {"name": "MitoTracker Orange", "excitation": "551 nm", "emission": "575 nm"},
    {"name": "MitoTracker Orange, MeOH", "excitation": "551 nm", "emission": "575 nm"},
    {"name": "MitoTracker Red", "excitation": "578 nm", "emission": "599 nm"},
    {"name": "MitoTracker Red, MeOH", "excitation": "578 nm", "emission": "599 nm"},
    {"name": "mOrange", "excitation": "548 nm", "emission": "562 nm"},
    {"name": "mPlum", "excitation": "587 nm", "emission": "649 nm"},
    {"name": "mRFP", "excitation": "585 nm", "emission": "608 nm"},
    {"name": "mStrawberry", "excitation": "575 nm", "emission": "596 nm"},
    {"name": "mTangerine", "excitation": "568 nm", "emission": "585 nm"},
    {"name": "NBD-X", "excitation": "466 nm", "emission": "534 nm"},
    {"name": "NBD-X, MeOH", "excitation": "467 nm", "emission": "538 nm"},
    {"name": "NeuroTrace 500/525, green fluorescent Nissl stain-RNA", "excitation": "497 nm", "emission": "524 nm"},
    {"name": "Nile Blue, EtOH", "excitation": "631 nm", "emission": "660 nm"},
    {"name": "Nile Red", "excitation": "559 nm", "emission": "637 nm"},
    {"name": "Nile Red-lipid", "excitation": "553 nm", "emission": "636 nm"},
    {"name": "Nissl", "excitation": "497 nm", "emission": "524 nm"},
    {"name": "Oregon Green 488", "excitation": "498 nm", "emission": "526 nm"},
    {"name": "Oregon Green 488 antibody conjugate pH 8.0", "excitation": "498 nm", "emission": "526 nm"},
    {"name": "Oregon Green 514", "excitation": "512 nm", "emission": "532 nm"},
    {"name": "Oregon Green 514 antibody conjugate pH 8.0", "excitation": "513 nm", "emission": "533 nm"},
    {"name": "Pacific Blue", "excitation": "404 nm", "emission": "455 nm"},
    {"name": "Pacific Blue antibody conjugate pH 8.0", "excitation": "404 nm", "emission": "455 nm"},
    {"name": "Phycoerythrin", "excitation": "565 nm", "emission": "575 nm"},
    {"name": "PicoGreendsDNA quantitation reagent", "excitation": "502 nm", "emission": "522 nm"},
    {"name": "PO-PRO-1", "excitation": "434 nm", "emission": "457 nm"},
    {"name": "PO-PRO-1-DNA", "excitation": "435 nm", "emission": "457 nm"},
    {"name": "PO-PRO-3", "excitation": "539 nm", "emission": "571 nm"},
    {"name": "PO-PRO-3-DNA", "excitation": "539 nm", "emission": "571 nm"},
    {"name": "POPO-1", "excitation": "433 nm", "emission": "457 nm"},
    {"name": "POPO-1-DNA", "excitation": "433 nm", "emission": "458 nm"},
    {"name": "POPO-3", "excitation": "533 nm", "emission": "573 nm"},
    {"name": "Propidium Iodide", "excitation": "538 nm", "emission": "617 nm"},
    {"name": "Propidium Iodide-DNA", "excitation": "538 nm", "emission": "619 nm"},
    {"name": "R-Phycoerythrin pH 7.5", "excitation": "565 nm", "emission": "576 nm"},
    {"name": "ReAsH", "excitation": "597 nm", "emission": "608 nm"},
    {"name": "Resorufin", "excitation": "571 nm", "emission": "584 nm"},
    {"name": "Resorufin pH 9.0", "excitation": "571 nm", "emission": "584 nm"},
    {"name": "Rhod-2", "excitation": "552 nm", "emission": "577 nm"},
    {"name": "Rhod-2 Ca2+", "excitation": "553 nm", "emission": "578 nm"},
    {"name": "Rhodamine", "excitation": "551 nm", "emission": "573 nm"},
    {"name": "Rhodamine 110", "excitation": "497 nm", "emission": "520 nm"},
    {"name": "Rhodamine 110 pH 7.0", "excitation": "497 nm", "emission": "520 nm"},
    {"name": "Rhodamine 123, MeOH", "excitation": "507 nm", "emission": "529 nm"},
    {"name": "Rhodamine B", "excitation": "543 nm", "emission": "565 nm"},
    {"name": "Rhodamine Green", "excitation": "497 nm", "emission": "524 nm"},
    {"name": "Rhodamine Red-X antibody conjugate pH 8.0", "excitation": "573 nm", "emission": "591 nm"},
    {"name": "Rhodaminen Green pH 7.0", "excitation": "497 nm", "emission": "523 nm"},
    {"name": "Rhodaminephalloidin pH 7.0", "excitation": "558 nm", "emission": "575 nm"},
    {"name": "Rhodol Green antibody conjugate pH 8.0", "excitation": "499 nm", "emission": "524 nm"},
    {"name": "Sapphire", "excitation": "396 nm", "emission": "511 nm"},
    {"name": "SBFI-Na+", "excitation": "336 nm", "emission": "527 nm"},
    {"name": "Sodium Green Na+", "excitation": "507 nm", "emission": "531 nm"},
    {"name": "Sulforhodamine 101, EtOH", "excitation": "578 nm", "emission": "593 nm"},
    {"name": "SYBR Green I", "excitation": "498 nm", "emission": "522 nm"},
    {"name": "SYPRO Ruby", "excitation": "467 nm", "emission": "618 nm"},
    {"name": "SYTO 13-DNA", "excitation": "488 nm", "emission": "506 nm"},
    {"name": "SYTO 45-DNA", "excitation": "451 nm", "emission": "486 nm"},
    {"name": "SYTOX Blue-DNA", "excitation": "445 nm", "emission": "470 nm"},
    {"name": "Tetramethylrhodamine antibody conjugate pH 8.0", "excitation": "552 nm", "emission": "578 nm"},
    {"name": "Tetramethylrhodamine dextran pH 7.0", "excitation": "555 nm", "emission": "582 nm"},
    {"name": "Texas Red-X antibody conjugate pH 7.2", "excitation": "596 nm", "emission": "613 nm"},
    {"name": "TO-PRO-1-DNA", "excitation": "515 nm", "emission": "531 nm"},
    {"name": "TO-PRO-3-DNA", "excitation": "642 nm", "emission": "657 nm"},
    {"name": "TOTO-1-DNA", "excitation": "514 nm", "emission": "531 nm"},
    {"name": "TOTO-3-DNA", "excitation": "642 nm", "emission": "661 nm"},
    {"name": "TRITC", "excitation": "550 nm", "emission": "573 nm"},
    {"name": "X-Rhod-1 Ca2+", "excitation": "580 nm", "emission": "602 nm"},
    {"name": "YO-PRO-1-DNA", "excitation": "491 nm", "emission": "507 nm"},
    {"name": "YO-PRO-3-DNA", "excitation": "613 nm", "emission": "629 nm"},
    {"name": "YOYO-1-DNA", "excitation": "491 nm", "emission": "509 nm"},
    {"name": "YOYO-3-DNA", "excitation": "612 nm", "emission": "631 nm"},
]

if __name__ == "__main__":
    show()