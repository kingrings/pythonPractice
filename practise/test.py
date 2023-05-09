import time
import requests
from lxml import etree
#t=time.time()
#print(int(round(t*1000)))


# headers = {
# 	'Cookie':'vip_cps_cuid=CU1676115410598550179aa54450a6c0; vip_cps_cid=1676115410600_196e5f9f827de1d59b2c0e02b232029f; cps_share=cps_share; PAPVisitorId=472c653004562ca65b962a8e563f2dac; vip_new_old_user=1; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; user_class=a; mars_cid=1676115414402_a7342faa478349a4d9384c3962f40178; mars_sid=7f5af76a261a5de5149f10aef4034d15; mars_pid=0; visit_id=9C6FB4971854DF4ECAA534BCD2E5F2E1; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; vip_address=%257B%2522pname%2522%253A%2522%255Cu6c5f%255Cu82cf%255Cu7701%2522%252C%2522pid%2522%253A%2522103102%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522103102101%2522%257D; vip_province=103102; vip_province_name=%E6%B1%9F%E8%8B%8F%E7%9C%81; vip_city_code=103102101; vip_wh=VIP_SH; vip_ipver=31; cps=adp%3Antq8exyc%3A%40_%401676116467372%3Amig_code%3A4f6b50bf15bfa39639d85f5f1e15b10f%3Aac014miuvl0000b5sq8cc2oyplrsivsi; vip_tracker_source_from=; vipshop_passport_src=https%3A%2F%2Flist.vip.com%2Fautolist.html%3Frule_id%3D54886032%26title%3D%25E9%25AB%2598%25E8%2585%25B0%25E7%25BE%258E%25E8%25A3%2599%26refer_url%3Dhttps%253A%252F%252Fcategory.vip.com%252Fhome; pg_session_no=31; vip_access_times=%7B%22list%22%3A3%7D',
# 	'Referer': 'https://category.vip.com/suggest.php?keyword=%E6%8A%A4%E8%82%A4&ff=235|12|1|1',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
# url="https://www.vip.com/#"
#
# html=requests.get(url,headers=headers)
# print(html.text)

text='''
    <div class="cate-detail">
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52020712">女士热销分类</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52020712" data-cate2name="女士热销分类">
                        
                        <a target="_blank" class="J_category3" data-cate3id="62221605" data-cate3name="加厚保暖" data-jumper="rule" mars_exposure_module="category_all_expose_62221605" mars_sead="category_all_click_62221605" href="//list.vip.com/autolist.html?rule_id=62221605&amp;title=%E5%8A%A0%E5%8E%9A%E4%BF%9D%E6%9A%96&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">加厚保暖</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61971038" data-cate3name="冬季尚新" data-jumper="rule" mars_exposure_module="category_all_expose_61971038" mars_sead="category_all_click_61971038" href="//list.vip.com/autolist.html?rule_id=61971038&amp;title=%E5%86%AC%E5%AD%A3%E5%B0%9A%E6%96%B0&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">冬季尚新</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986298" data-cate3name="针织衫" data-jumper="rule" mars_exposure_module="category_all_expose_53986298" mars_sead="category_all_click_53986298" href="//list.vip.com/autolist.html?rule_id=53986298&amp;title=%E9%92%88%E7%BB%87%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">针织衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61971053" data-cate3name="唯品独家" data-jumper="rule" mars_exposure_module="category_all_expose_61971053" mars_sead="category_all_click_61971053" href="//list.vip.com/autolist.html?rule_id=61971053&amp;title=%E5%94%AF%E5%93%81%E7%8B%AC%E5%AE%B6&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">唯品独家</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986312" data-cate3name="休闲裤" data-jumper="rule" mars_exposure_module="category_all_expose_53986312" mars_sead="category_all_click_53986312" href="//list.vip.com/autolist.html?rule_id=53986312&amp;title=%E4%BC%91%E9%97%B2%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">休闲裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986307" data-cate3name="连衣裙" data-jumper="rule" mars_exposure_module="category_all_expose_53986307" mars_sead="category_all_click_53986307" href="//list.vip.com/autolist.html?rule_id=53986307&amp;title=%E8%BF%9E%E8%A1%A3%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">连衣裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55515022" data-cate3name="女式毛衣" data-jumper="rule" mars_exposure_module="category_all_expose_55515022" mars_sead="category_all_click_55515022" href="//list.vip.com/autolist.html?rule_id=55515022&amp;title=%E5%A5%B3%E5%BC%8F%E6%AF%9B%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女式毛衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986308" data-cate3name="外套" data-jumper="rule" mars_exposure_module="category_all_expose_53986308" mars_sead="category_all_click_53986308" href="//list.vip.com/autolist.html?rule_id=53986308&amp;title=%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986316" data-cate3name="牛仔裤" data-jumper="rule" mars_exposure_module="category_all_expose_53986316" mars_sead="category_all_click_53986316" href="//list.vip.com/autolist.html?rule_id=53986316&amp;title=%E7%89%9B%E4%BB%94%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">牛仔裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986299" data-cate3name="衬衫" data-jumper="rule" mars_exposure_module="category_all_expose_53986299" mars_sead="category_all_click_53986299" href="//list.vip.com/autolist.html?rule_id=53986299&amp;title=%E8%A1%AC%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">衬衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986306" data-cate3name="T恤" data-jumper="rule" mars_exposure_module="category_all_expose_53986306" mars_sead="category_all_click_53986306" href="//list.vip.com/autolist.html?rule_id=53986306&amp;title=T%E6%81%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">T恤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986294" data-cate3name="套装" data-jumper="rule" mars_exposure_module="category_all_expose_53986294" mars_sead="category_all_click_53986294" href="//list.vip.com/autolist.html?rule_id=53986294&amp;title=%E5%A5%97%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">套装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986314" data-cate3name="半截裙" data-jumper="rule" mars_exposure_module="category_all_expose_53986314" mars_sead="category_all_click_53986314" href="//list.vip.com/autolist.html?rule_id=53986314&amp;title=%E5%8D%8A%E6%88%AA%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">半截裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986804" data-cate3name="妈妈装" data-jumper="rule" mars_exposure_module="category_all_expose_53986804" mars_sead="category_all_click_53986804" href="//list.vip.com/autolist.html?rule_id=53986804&amp;title=%E5%A6%88%E5%A6%88%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">妈妈装</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52020711">流行裙装</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52020711" data-cate2name="流行裙装">
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886020" data-cate3name="纯色美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886020" mars_sead="category_all_click_54886020" href="//list.vip.com/autolist.html?rule_id=54886020&amp;title=%E7%BA%AF%E8%89%B2%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">纯色美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886032" data-cate3name="高腰美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886032" mars_sead="category_all_click_54886032" href="//list.vip.com/autolist.html?rule_id=54886032&amp;title=%E9%AB%98%E8%85%B0%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">高腰美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55521161" data-cate3name="半截裙" data-jumper="rule" mars_exposure_module="category_all_expose_55521161" mars_sead="category_all_click_55521161" href="//list.vip.com/autolist.html?rule_id=55521161&amp;title=%E5%8D%8A%E6%88%AA%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">半截裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886023" data-cate3name="中长款裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886023" mars_sead="category_all_click_54886023" href="//list.vip.com/autolist.html?rule_id=54886023&amp;title=%E4%B8%AD%E9%95%BF%E6%AC%BE%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">中长款裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886027" data-cate3name="碎花美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886027" mars_sead="category_all_click_54886027" href="//list.vip.com/autolist.html?rule_id=54886027&amp;title=%E7%A2%8E%E8%8A%B1%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">碎花美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886022" data-cate3name="百褶美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886022" mars_sead="category_all_click_54886022" href="//list.vip.com/autolist.html?rule_id=54886022&amp;title=%E7%99%BE%E8%A4%B6%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">百褶美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886016" data-cate3name="格纹美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886016" mars_sead="category_all_click_54886016" href="//list.vip.com/autolist.html?rule_id=54886016&amp;title=%E6%A0%BC%E7%BA%B9%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">格纹美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886031" data-cate3name="吊带美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886031" mars_sead="category_all_click_54886031" href="//list.vip.com/autolist.html?rule_id=54886031&amp;title=%E5%90%8A%E5%B8%A6%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">吊带美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886021" data-cate3name="真丝美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886021" mars_sead="category_all_click_54886021" href="//list.vip.com/autolist.html?rule_id=54886021&amp;title=%E7%9C%9F%E4%B8%9D%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">真丝美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886017" data-cate3name="旗袍美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886017" mars_sead="category_all_click_54886017" href="//list.vip.com/autolist.html?rule_id=54886017&amp;title=%E6%97%97%E8%A2%8D%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">旗袍美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54886028" data-cate3name="牛仔美裙" data-jumper="rule" mars_exposure_module="category_all_expose_54886028" mars_sead="category_all_click_54886028" href="//list.vip.com/autolist.html?rule_id=54886028&amp;title=%E7%89%9B%E4%BB%94%E7%BE%8E%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">牛仔美裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="54879403" data-cate3name="大码裙装" data-jumper="rule" mars_exposure_module="category_all_expose_54879403" mars_sead="category_all_click_54879403" href="//list.vip.com/autolist.html?rule_id=54879403&amp;title=%E5%A4%A7%E7%A0%81%E8%A3%99%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">大码裙装</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52020716">女士上装</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52020716" data-cate2name="女士上装">
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986299" data-cate3name="衬衫" data-jumper="rule" mars_exposure_module="category_all_expose_53986299" mars_sead="category_all_click_53986299" href="//list.vip.com/autolist.html?rule_id=53986299&amp;title=%E8%A1%AC%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">衬衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986306" data-cate3name="T恤" data-jumper="rule" mars_exposure_module="category_all_expose_53986306" mars_sead="category_all_click_53986306" href="//list.vip.com/autolist.html?rule_id=53986306&amp;title=T%E6%81%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">T恤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986308" data-cate3name="外套" data-jumper="rule" mars_exposure_module="category_all_expose_53986308" mars_sead="category_all_click_53986308" href="//list.vip.com/autolist.html?rule_id=53986308&amp;title=%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986298" data-cate3name="针织衫" data-jumper="rule" mars_exposure_module="category_all_expose_53986298" mars_sead="category_all_click_53986298" href="//list.vip.com/autolist.html?rule_id=53986298&amp;title=%E9%92%88%E7%BB%87%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">针织衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986296" data-cate3name="风衣" data-jumper="rule" mars_exposure_module="category_all_expose_53986296" mars_sead="category_all_click_53986296" href="//list.vip.com/autolist.html?rule_id=53986296&amp;title=%E9%A3%8E%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">风衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986315" data-cate3name="西服" data-jumper="rule" mars_exposure_module="category_all_expose_53986315" mars_sead="category_all_click_53986315" href="//list.vip.com/autolist.html?rule_id=53986315&amp;title=%E8%A5%BF%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">西服</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986297" data-cate3name="卫衣" data-jumper="rule" mars_exposure_module="category_all_expose_53986297" mars_sead="category_all_click_53986297" href="//list.vip.com/autolist.html?rule_id=53986297&amp;title=%E5%8D%AB%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">卫衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986639" data-cate3name="马夹" data-jumper="rule" mars_exposure_module="category_all_expose_53986639" mars_sead="category_all_click_53986639" href="//list.vip.com/autolist.html?rule_id=53986639&amp;title=%E9%A9%AC%E5%A4%B9&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">马夹</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59968549" data-cate3name="打底衫" data-jumper="rule" mars_exposure_module="category_all_expose_59968549" mars_sead="category_all_click_59968549" href="//list.vip.com/autolist.html?rule_id=59968549&amp;title=%E6%89%93%E5%BA%95%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">打底衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986303" data-cate3name="背心" data-jumper="rule" mars_exposure_module="category_all_expose_53986303" mars_sead="category_all_click_53986303" href="//list.vip.com/autolist.html?rule_id=53986303&amp;title=%E8%83%8C%E5%BF%83&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">背心</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986305" data-cate3name="大衣" data-jumper="rule" mars_exposure_module="category_all_expose_53986305" mars_sead="category_all_click_53986305" href="//list.vip.com/autolist.html?rule_id=53986305&amp;title=%E5%A4%A7%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">大衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986295" data-cate3name="皮衣/皮草" data-jumper="rule" mars_exposure_module="category_all_expose_53986295" mars_sead="category_all_click_53986295" href="//list.vip.com/autolist.html?rule_id=53986295&amp;title=%E7%9A%AE%E8%A1%A3%2F%E7%9A%AE%E8%8D%89&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">皮衣/皮草</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55515022" data-cate3name="毛衣" data-jumper="rule" mars_exposure_module="category_all_expose_55515022" mars_sead="category_all_click_55515022" href="//list.vip.com/autolist.html?rule_id=55515022&amp;title=%E6%AF%9B%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">毛衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986313" data-cate3name="羽绒服" data-jumper="rule" mars_exposure_module="category_all_expose_53986313" mars_sead="category_all_click_53986313" href="//list.vip.com/autolist.html?rule_id=53986313&amp;title=%E7%BE%BD%E7%BB%92%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">羽绒服</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52020713">女士裤装</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52020713" data-cate2name="女士裤装">
                        
                        <a target="_blank" class="J_category3" data-cate3id="58811183" data-cate3name="运动裤" data-jumper="rule" mars_exposure_module="category_all_expose_58811183" mars_sead="category_all_click_58811183" href="//list.vip.com/autolist.html?rule_id=58811183&amp;title=%E8%BF%90%E5%8A%A8%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">运动裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55518075" data-cate3name="西裤" data-jumper="rule" mars_exposure_module="category_all_expose_55518075" mars_sead="category_all_click_55518075" href="//list.vip.com/autolist.html?rule_id=55518075&amp;title=%E8%A5%BF%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">西裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="58811586" data-cate3name="连体裤" data-jumper="rule" mars_exposure_module="category_all_expose_58811586" mars_sead="category_all_click_58811586" href="//list.vip.com/autolist.html?rule_id=58811586&amp;title=%E8%BF%9E%E4%BD%93%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">连体裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986311" data-cate3name="打底裤" data-jumper="rule" mars_exposure_module="category_all_expose_53986311" mars_sead="category_all_click_53986311" href="//list.vip.com/autolist.html?rule_id=53986311&amp;title=%E6%89%93%E5%BA%95%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">打底裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986312" data-cate3name="休闲裤" data-jumper="rule" mars_exposure_module="category_all_expose_53986312" mars_sead="category_all_click_53986312" href="//list.vip.com/autolist.html?rule_id=53986312&amp;title=%E4%BC%91%E9%97%B2%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">休闲裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986316" data-cate3name="牛仔裤" data-jumper="rule" mars_exposure_module="category_all_expose_53986316" mars_sead="category_all_click_53986316" href="//list.vip.com/autolist.html?rule_id=53986316&amp;title=%E7%89%9B%E4%BB%94%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">牛仔裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986751" data-cate3name="短裤" data-jumper="rule" mars_exposure_module="category_all_expose_53986751" mars_sead="category_all_click_53986751" href="//list.vip.com/autolist.html?rule_id=53986751&amp;title=%E7%9F%AD%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">短裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55516985" data-cate3name="直筒裤" data-jumper="rule" mars_exposure_module="category_all_expose_55516985" mars_sead="category_all_click_55516985" href="//list.vip.com/autolist.html?rule_id=55516985&amp;title=%E7%9B%B4%E7%AD%92%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">直筒裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55518074" data-cate3name="工装裤" data-jumper="rule" mars_exposure_module="category_all_expose_55518074" mars_sead="category_all_click_55518074" href="//list.vip.com/autolist.html?rule_id=55518074&amp;title=%E5%B7%A5%E8%A3%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">工装裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55517801" data-cate3name="小脚裤" data-jumper="rule" mars_exposure_module="category_all_expose_55517801" mars_sead="category_all_click_55517801" href="//list.vip.com/autolist.html?rule_id=55517801&amp;title=%E5%B0%8F%E8%84%9A%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">小脚裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55516984" data-cate3name="阔腿裤" data-jumper="rule" mars_exposure_module="category_all_expose_55516984" mars_sead="category_all_click_55516984" href="//list.vip.com/autolist.html?rule_id=55516984&amp;title=%E9%98%94%E8%85%BF%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">阔腿裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="55517076" data-cate3name="哈伦裤" data-jumper="rule" mars_exposure_module="category_all_expose_55517076" mars_sead="category_all_click_55517076" href="//list.vip.com/autolist.html?rule_id=55517076&amp;title=%E5%93%88%E4%BC%A6%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">哈伦裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="53986314" data-cate3name="半截裙" data-jumper="rule" mars_exposure_module="category_all_expose_53986314" mars_sead="category_all_click_53986314" href="//list.vip.com/autolist.html?rule_id=53986314&amp;title=%E5%8D%8A%E6%88%AA%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">半截裙</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52047396">男式内搭</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52047396" data-cate2name="男式内搭">
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547253" data-cate3name="衬衫" data-jumper="rule" mars_exposure_module="category_all_expose_61547253" mars_sead="category_all_click_61547253" href="//list.vip.com/autolist.html?rule_id=61547253&amp;title=%E8%A1%AC%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">衬衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547258" data-cate3name="卫衣" data-jumper="rule" mars_exposure_module="category_all_expose_61547258" mars_sead="category_all_click_61547258" href="//list.vip.com/autolist.html?rule_id=61547258&amp;title=%E5%8D%AB%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">卫衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547259" data-cate3name="Polo衫" data-jumper="rule" mars_exposure_module="category_all_expose_61547259" mars_sead="category_all_click_61547259" href="//list.vip.com/autolist.html?rule_id=61547259&amp;title=Polo%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">Polo衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547254" data-cate3name="T恤" data-jumper="rule" mars_exposure_module="category_all_expose_61547254" mars_sead="category_all_click_61547254" href="//list.vip.com/autolist.html?rule_id=61547254&amp;title=T%E6%81%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">T恤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547256" data-cate3name="针织衫" data-jumper="rule" mars_exposure_module="category_all_expose_61547256" mars_sead="category_all_click_61547256" href="//list.vip.com/autolist.html?rule_id=61547256&amp;title=%E9%92%88%E7%BB%87%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">针织衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547255" data-cate3name="毛衣" data-jumper="rule" mars_exposure_module="category_all_expose_61547255" mars_sead="category_all_click_61547255" href="//list.vip.com/autolist.html?rule_id=61547255&amp;title=%E6%AF%9B%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">毛衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547257" data-cate3name="羊绒衫" data-jumper="rule" mars_exposure_module="category_all_expose_61547257" mars_sead="category_all_click_61547257" href="//list.vip.com/autolist.html?rule_id=61547257&amp;title=%E7%BE%8A%E7%BB%92%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">羊绒衫</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52047398">男式裤装</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52047398" data-cate2name="男式裤装">
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547206" data-cate3name="休闲裤" data-jumper="rule" mars_exposure_module="category_all_expose_61547206" mars_sead="category_all_click_61547206" href="//list.vip.com/autolist.html?rule_id=61547206&amp;title=%E4%BC%91%E9%97%B2%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">休闲裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547208" data-cate3name="牛仔裤" data-jumper="rule" mars_exposure_module="category_all_expose_61547208" mars_sead="category_all_click_61547208" href="//list.vip.com/autolist.html?rule_id=61547208&amp;title=%E7%89%9B%E4%BB%94%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">牛仔裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547207" data-cate3name="西裤" data-jumper="rule" mars_exposure_module="category_all_expose_61547207" mars_sead="category_all_click_61547207" href="//list.vip.com/autolist.html?rule_id=61547207&amp;title=%E8%A5%BF%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">西裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61537754" data-cate3name="工装裤" data-jumper="rule" mars_exposure_module="category_all_expose_61537754" mars_sead="category_all_click_61537754" href="//list.vip.com/autolist.html?rule_id=61537754&amp;title=%E5%B7%A5%E8%A3%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">工装裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61537755" data-cate3name="小脚裤" data-jumper="rule" mars_exposure_module="category_all_expose_61537755" mars_sead="category_all_click_61537755" href="//list.vip.com/autolist.html?rule_id=61537755&amp;title=%E5%B0%8F%E8%84%9A%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">小脚裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="10023060" data-cate3name="皮裤" data-jumper="rule" mars_exposure_module="category_all_expose_10023060" mars_sead="category_all_click_10023060" href="//list.vip.com/autolist.html?rule_id=10023060&amp;title=%E7%9A%AE%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">皮裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="10023061" data-cate3name="连体裤" data-jumper="rule" mars_exposure_module="category_all_expose_10023061" mars_sead="category_all_click_10023061" href="//list.vip.com/autolist.html?rule_id=10023061&amp;title=%E8%BF%9E%E4%BD%93%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">连体裤</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_61547159">男式外套</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="61547159" data-cate2name="男式外套">
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547167" data-cate3name="夹克/外套" data-jumper="rule" mars_exposure_module="category_all_expose_61547167" mars_sead="category_all_click_61547167" href="//list.vip.com/autolist.html?rule_id=61547167&amp;title=%E5%A4%B9%E5%85%8B%2F%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">夹克/外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040695" data-cate3name="风衣" data-jumper="rule" mars_exposure_module="category_all_expose_52040695" mars_sead="category_all_click_52040695" href="//list.vip.com/autolist.html?rule_id=52040695&amp;title=%E9%A3%8E%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">风衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040701" data-cate3name="大衣" data-jumper="rule" mars_exposure_module="category_all_expose_52040701" mars_sead="category_all_click_52040701" href="//list.vip.com/autolist.html?rule_id=52040701&amp;title=%E5%A4%A7%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">大衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040709" data-cate3name="牛仔外套" data-jumper="rule" mars_exposure_module="category_all_expose_52040709" mars_sead="category_all_click_52040709" href="//list.vip.com/autolist.html?rule_id=52040709&amp;title=%E7%89%9B%E4%BB%94%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">牛仔外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040702" data-cate3name="棉衣" data-jumper="rule" mars_exposure_module="category_all_expose_52040702" mars_sead="category_all_click_52040702" href="//list.vip.com/autolist.html?rule_id=52040702&amp;title=%E6%A3%89%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">棉衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040697" data-cate3name="羽绒服" data-jumper="rule" mars_exposure_module="category_all_expose_52040697" mars_sead="category_all_click_52040697" href="//list.vip.com/autolist.html?rule_id=52040697&amp;title=%E7%BE%BD%E7%BB%92%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">羽绒服</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040693" data-cate3name="西装" data-jumper="rule" mars_exposure_module="category_all_expose_52040693" mars_sead="category_all_click_52040693" href="//list.vip.com/autolist.html?rule_id=52040693&amp;title=%E8%A5%BF%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">西装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040694" data-cate3name="皮衣" data-jumper="rule" mars_exposure_module="category_all_expose_52040694" mars_sead="category_all_click_52040694" href="//list.vip.com/autolist.html?rule_id=52040694&amp;title=%E7%9A%AE%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">皮衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040704" data-cate3name="厚外套" data-jumper="rule" mars_exposure_module="category_all_expose_52040704" mars_sead="category_all_click_52040704" href="//list.vip.com/autolist.html?rule_id=52040704&amp;title=%E5%8E%9A%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">厚外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040698" data-cate3name="马甲/背心" data-jumper="rule" mars_exposure_module="category_all_expose_52040698" mars_sead="category_all_click_52040698" href="//list.vip.com/autolist.html?rule_id=52040698&amp;title=%E9%A9%AC%E7%94%B2%2F%E8%83%8C%E5%BF%83&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">马甲/背心</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040716" data-cate3name="套装" data-jumper="rule" mars_exposure_module="category_all_expose_52040716" mars_sead="category_all_click_52040716" href="//list.vip.com/autolist.html?rule_id=52040716&amp;title=%E5%A5%97%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">套装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040703" data-cate3name="棒球服" data-jumper="rule" mars_exposure_module="category_all_expose_52040703" mars_sead="category_all_click_52040703" href="//list.vip.com/autolist.html?rule_id=52040703&amp;title=%E6%A3%92%E7%90%83%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">棒球服</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040699" data-cate3name="短款外套" data-jumper="rule" mars_exposure_module="category_all_expose_52040699" mars_sead="category_all_click_52040699" href="//list.vip.com/autolist.html?rule_id=52040699&amp;title=%E7%9F%AD%E6%AC%BE%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">短款外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040700" data-cate3name="中长款外套" data-jumper="rule" mars_exposure_module="category_all_expose_52040700" mars_sead="category_all_click_52040700" href="//list.vip.com/autolist.html?rule_id=52040700&amp;title=%E4%B8%AD%E9%95%BF%E6%AC%BE%E5%A4%96%E5%A5%97&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">中长款外套</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040706" data-cate3name="厚羽绒" data-jumper="rule" mars_exposure_module="category_all_expose_52040706" mars_sead="category_all_click_52040706" href="//list.vip.com/autolist.html?rule_id=52040706&amp;title=%E5%8E%9A%E7%BE%BD%E7%BB%92&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">厚羽绒</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040708" data-cate3name="轻薄羽绒" data-jumper="rule" mars_exposure_module="category_all_expose_52040708" mars_sead="category_all_click_52040708" href="//list.vip.com/autolist.html?rule_id=52040708&amp;title=%E8%BD%BB%E8%96%84%E7%BE%BD%E7%BB%92&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">轻薄羽绒</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040714" data-cate3name="长款羽绒" data-jumper="rule" mars_exposure_module="category_all_expose_52040714" mars_sead="category_all_click_52040714" href="//list.vip.com/autolist.html?rule_id=52040714&amp;title=%E9%95%BF%E6%AC%BE%E7%BE%BD%E7%BB%92&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">长款羽绒</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040713" data-cate3name="短款羽绒" data-jumper="rule" mars_exposure_module="category_all_expose_52040713" mars_sead="category_all_click_52040713" href="//list.vip.com/autolist.html?rule_id=52040713&amp;title=%E7%9F%AD%E6%AC%BE%E7%BE%BD%E7%BB%92&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">短款羽绒</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547166" data-cate3name="男式风衣" data-jumper="rule" mars_exposure_module="category_all_expose_61547166" mars_sead="category_all_click_61547166" href="//list.vip.com/autolist.html?rule_id=61547166&amp;title=%E7%94%B7%E5%BC%8F%E9%A3%8E%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男式风衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="61547165" data-cate3name="男式夹克" data-jumper="rule" mars_exposure_module="category_all_expose_61547165" mars_sead="category_all_click_61547165" href="//list.vip.com/autolist.html?rule_id=61547165&amp;title=%E7%94%B7%E5%BC%8F%E5%A4%B9%E5%85%8B&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男式夹克</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_52047395">男式特色服饰</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="52047395" data-cate2name="男式特色服饰">
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040687" data-cate3name="街头潮流" data-jumper="rule" mars_exposure_module="category_all_expose_52040687" mars_sead="category_all_click_52040687" href="//list.vip.com/autolist.html?rule_id=52040687&amp;title=%E8%A1%97%E5%A4%B4%E6%BD%AE%E6%B5%81&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">街头潮流</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040689" data-cate3name="爸爸装" data-jumper="rule" mars_exposure_module="category_all_expose_52040689" mars_sead="category_all_click_52040689" href="//list.vip.com/autolist.html?rule_id=52040689&amp;title=%E7%88%B8%E7%88%B8%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">爸爸装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040688" data-cate3name="运动着装" data-jumper="rule" mars_exposure_module="category_all_expose_52040688" mars_sead="category_all_click_52040688" href="//list.vip.com/autolist.html?rule_id=52040688&amp;title=%E8%BF%90%E5%8A%A8%E7%9D%80%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">运动着装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040683" data-cate3name="中国风" data-jumper="rule" mars_exposure_module="category_all_expose_52040683" mars_sead="category_all_click_52040683" href="//list.vip.com/autolist.html?rule_id=52040683&amp;title=%E4%B8%AD%E5%9B%BD%E9%A3%8E&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">中国风</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040682" data-cate3name="大码" data-jumper="rule" mars_exposure_module="category_all_expose_52040682" mars_sead="category_all_click_52040682" href="//list.vip.com/autolist.html?rule_id=52040682&amp;title=%E5%A4%A7%E7%A0%81&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">大码</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040691" data-cate3name="迷彩风" data-jumper="rule" mars_exposure_module="category_all_expose_52040691" mars_sead="category_all_click_52040691" href="//list.vip.com/autolist.html?rule_id=52040691&amp;title=%E8%BF%B7%E5%BD%A9%E9%A3%8E&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">迷彩风</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040685" data-cate3name="时尚休闲" data-jumper="rule" mars_exposure_module="category_all_expose_52040685" mars_sead="category_all_click_52040685" href="//list.vip.com/autolist.html?rule_id=52040685&amp;title=%E6%97%B6%E5%B0%9A%E4%BC%91%E9%97%B2&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">时尚休闲</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="52040684" data-cate3name="职场精英" data-jumper="rule" mars_exposure_module="category_all_expose_52040684" mars_sead="category_all_click_52040684" href="//list.vip.com/autolist.html?rule_id=52040684&amp;title=%E8%81%8C%E5%9C%BA%E7%B2%BE%E8%8B%B1&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">职场精英</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_59505929">热销内衣</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="59505929" data-cate2name="热销内衣">
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450613" data-cate3name="无钢圈" data-jumper="rule" mars_exposure_module="category_all_expose_59450613" mars_sead="category_all_click_59450613" href="//list.vip.com/autolist.html?rule_id=59450613&amp;title=%E6%97%A0%E9%92%A2%E5%9C%88&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">无钢圈</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450545" data-cate3name="女式羊毛衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450545" mars_sead="category_all_click_59450545" href="//list.vip.com/autolist.html?rule_id=59450545&amp;title=%E5%A5%B3%E5%BC%8F%E7%BE%8A%E6%AF%9B%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女式羊毛衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450544" data-cate3name="女式羊绒衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450544" mars_sead="category_all_click_59450544" href="//list.vip.com/autolist.html?rule_id=59450544&amp;title=%E5%A5%B3%E5%BC%8F%E7%BE%8A%E7%BB%92%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女式羊绒衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450557" data-cate3name="男士保暖套装" data-jumper="rule" mars_exposure_module="category_all_expose_59450557" mars_sead="category_all_click_59450557" href="//list.vip.com/autolist.html?rule_id=59450557&amp;title=%E7%94%B7%E5%A3%AB%E4%BF%9D%E6%9A%96%E5%A5%97%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士保暖套装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450555" data-cate3name="女士保暖套装" data-jumper="rule" mars_exposure_module="category_all_expose_59450555" mars_sead="category_all_click_59450555" href="//list.vip.com/autolist.html?rule_id=59450555&amp;title=%E5%A5%B3%E5%A3%AB%E4%BF%9D%E6%9A%96%E5%A5%97%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士保暖套装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450824" data-cate3name="女士开衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450824" mars_sead="category_all_click_59450824" href="//list.vip.com/autolist.html?rule_id=59450824&amp;title=%E5%A5%B3%E5%A3%AB%E5%BC%80%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士开衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450543" data-cate3name="男式羊绒衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450543" mars_sead="category_all_click_59450543" href="//list.vip.com/autolist.html?rule_id=59450543&amp;title=%E7%94%B7%E5%BC%8F%E7%BE%8A%E7%BB%92%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男式羊绒衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450554" data-cate3name="女士保暖上衣" data-jumper="rule" mars_exposure_module="category_all_expose_59450554" mars_sead="category_all_click_59450554" href="//list.vip.com/autolist.html?rule_id=59450554&amp;title=%E5%A5%B3%E5%A3%AB%E4%BF%9D%E6%9A%96%E4%B8%8A%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士保暖上衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450831" data-cate3name="男士开衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450831" mars_sead="category_all_click_59450831" href="//list.vip.com/autolist.html?rule_id=59450831&amp;title=%E7%94%B7%E5%A3%AB%E5%BC%80%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士开衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450553" data-cate3name="女士保暖裤" data-jumper="rule" mars_exposure_module="category_all_expose_59450553" mars_sead="category_all_click_59450553" href="//list.vip.com/autolist.html?rule_id=59450553&amp;title=%E5%A5%B3%E5%A3%AB%E4%BF%9D%E6%9A%96%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士保暖裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450558" data-cate3name="男士保暖裤" data-jumper="rule" mars_exposure_module="category_all_expose_59450558" mars_sead="category_all_click_59450558" href="//list.vip.com/autolist.html?rule_id=59450558&amp;title=%E7%94%B7%E5%A3%AB%E4%BF%9D%E6%9A%96%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士保暖裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450556" data-cate3name="男士保暖上衣" data-jumper="rule" mars_exposure_module="category_all_expose_59450556" mars_sead="category_all_click_59450556" href="//list.vip.com/autolist.html?rule_id=59450556&amp;title=%E7%94%B7%E5%A3%AB%E4%BF%9D%E6%9A%96%E4%B8%8A%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士保暖上衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450559" data-cate3name="儿童保暖内衣/套装" data-jumper="rule" mars_exposure_module="category_all_expose_59450559" mars_sead="category_all_click_59450559" href="//list.vip.com/autolist.html?rule_id=59450559&amp;title=%E5%84%BF%E7%AB%A5%E4%BF%9D%E6%9A%96%E5%86%85%E8%A1%A3%2F%E5%A5%97%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">儿童保暖内衣/套装</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450751" data-cate3name="女士加绒" data-jumper="rule" mars_exposure_module="category_all_expose_59450751" mars_sead="category_all_click_59450751" href="//list.vip.com/autolist.html?rule_id=59450751&amp;title=%E5%A5%B3%E5%A3%AB%E5%8A%A0%E7%BB%92&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士加绒</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450752" data-cate3name="男士加绒" data-jumper="rule" mars_exposure_module="category_all_expose_59450752" mars_sead="category_all_click_59450752" href="//list.vip.com/autolist.html?rule_id=59450752&amp;title=%E7%94%B7%E5%A3%AB%E5%8A%A0%E7%BB%92&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士加绒</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450546" data-cate3name="女式大衣" data-jumper="rule" mars_exposure_module="category_all_expose_59450546" mars_sead="category_all_click_59450546" href="//list.vip.com/autolist.html?rule_id=59450546&amp;title=%E5%A5%B3%E5%BC%8F%E5%A4%A7%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女式大衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450382" data-cate3name="女士内裤" data-jumper="rule" mars_exposure_module="category_all_expose_59450382" mars_sead="category_all_click_59450382" href="//list.vip.com/autolist.html?rule_id=59450382&amp;title=%E5%A5%B3%E5%A3%AB%E5%86%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士内裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450381" data-cate3name="男士内裤" data-jumper="rule" mars_exposure_module="category_all_expose_59450381" mars_sead="category_all_click_59450381" href="//list.vip.com/autolist.html?rule_id=59450381&amp;title=%E7%94%B7%E5%A3%AB%E5%86%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士内裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450718" data-cate3name="聚拢" data-jumper="rule" mars_exposure_module="category_all_expose_59450718" mars_sead="category_all_click_59450718" href="//list.vip.com/autolist.html?rule_id=59450718&amp;title=%E8%81%9A%E6%8B%A2&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">聚拢</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450383" data-cate3name="男袜" data-jumper="rule" mars_exposure_module="category_all_expose_59450383" mars_sead="category_all_click_59450383" href="//list.vip.com/autolist.html?rule_id=59450383&amp;title=%E7%94%B7%E8%A2%9C&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男袜</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_59505199">特色内衣</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="59505199" data-cate2name="特色内衣">
                        
                        <a target="_blank" class="J_category3" data-cate3id="59496858" data-cate3name="男士睡衣" data-jumper="rule" mars_exposure_module="category_all_expose_59496858" mars_sead="category_all_click_59496858" href="//list.vip.com/autolist.html?rule_id=59496858&amp;title=%E7%94%B7%E5%A3%AB%E7%9D%A1%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士睡衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59496846" data-cate3name="情侣睡衣" data-jumper="rule" mars_exposure_module="category_all_expose_59496846" mars_sead="category_all_click_59496846" href="//list.vip.com/autolist.html?rule_id=59496846&amp;title=%E6%83%85%E4%BE%A3%E7%9D%A1%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">情侣睡衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59496841" data-cate3name="大码文胸" data-jumper="rule" mars_exposure_module="category_all_expose_59496841" mars_sead="category_all_click_59496841" href="//list.vip.com/autolist.html?rule_id=59496841&amp;title=%E5%A4%A7%E7%A0%81%E6%96%87%E8%83%B8&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">大码文胸</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495939" data-cate3name="安全裤" data-jumper="rule" mars_exposure_module="category_all_expose_59495939" mars_sead="category_all_click_59495939" href="//list.vip.com/autolist.html?rule_id=59495939&amp;title=%E5%AE%89%E5%85%A8%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">安全裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495975" data-cate3name="隐形胸贴" data-jumper="rule" mars_exposure_module="category_all_expose_59495975" mars_sead="category_all_click_59495975" href="//list.vip.com/autolist.html?rule_id=59495975&amp;title=%E9%9A%90%E5%BD%A2%E8%83%B8%E8%B4%B4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">隐形胸贴</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59496842" data-cate3name="情趣内衣" data-jumper="rule" mars_exposure_module="category_all_expose_59496842" mars_sead="category_all_click_59496842" href="//list.vip.com/autolist.html?rule_id=59496842&amp;title=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">情趣内衣</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_59503262">女士内衣</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="59503262" data-cate2name="女士内衣">
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495926" data-cate3name="纯棉内裤" data-jumper="rule" mars_exposure_module="category_all_expose_59495926" mars_sead="category_all_click_59495926" href="//list.vip.com/autolist.html?rule_id=59495926&amp;title=%E7%BA%AF%E6%A3%89%E5%86%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">纯棉内裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495911" data-cate3name="女士家居服" data-jumper="rule" mars_exposure_module="category_all_expose_59495911" mars_sead="category_all_click_59495911" href="//list.vip.com/autolist.html?rule_id=59495911&amp;title=%E5%A5%B3%E5%A3%AB%E5%AE%B6%E5%B1%85%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士家居服</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495921" data-cate3name="纯棉家居服" data-jumper="rule" mars_exposure_module="category_all_expose_59495921" mars_sead="category_all_click_59495921" href="//list.vip.com/autolist.html?rule_id=59495921&amp;title=%E7%BA%AF%E6%A3%89%E5%AE%B6%E5%B1%85%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">纯棉家居服</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495929" data-cate3name="塑身内衣" data-jumper="rule" mars_exposure_module="category_all_expose_59495929" mars_sead="category_all_click_59495929" href="//list.vip.com/autolist.html?rule_id=59495929&amp;title=%E5%A1%91%E8%BA%AB%E5%86%85%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">塑身内衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="58325065" data-cate3name="女士睡袍" data-jumper="rule" mars_exposure_module="category_all_expose_58325065" mars_sead="category_all_click_58325065" href="//list.vip.com/autolist.html?rule_id=58325065&amp;title=%E5%A5%B3%E5%A3%AB%E7%9D%A1%E8%A2%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士睡袍</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495679" data-cate3name="美背文胸" data-jumper="rule" mars_exposure_module="category_all_expose_59495679" mars_sead="category_all_click_59495679" href="//list.vip.com/autolist.html?rule_id=59495679&amp;title=%E7%BE%8E%E8%83%8C%E6%96%87%E8%83%B8&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">美背文胸</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59493551" data-cate3name="薄杯文胸" data-jumper="rule" mars_exposure_module="category_all_expose_59493551" mars_sead="category_all_click_59493551" href="//list.vip.com/autolist.html?rule_id=59493551&amp;title=%E8%96%84%E6%9D%AF%E6%96%87%E8%83%B8&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">薄杯文胸</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495397" data-cate3name="运动文胸" data-jumper="rule" mars_exposure_module="category_all_expose_59495397" mars_sead="category_all_click_59495397" href="//list.vip.com/autolist.html?rule_id=59495397&amp;title=%E8%BF%90%E5%8A%A8%E6%96%87%E8%83%B8&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">运动文胸</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450382" data-cate3name="女士内裤" data-jumper="rule" mars_exposure_module="category_all_expose_59450382" mars_sead="category_all_click_59450382" href="//list.vip.com/autolist.html?rule_id=59450382&amp;title=%E5%A5%B3%E5%A3%AB%E5%86%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士内裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450613" data-cate3name="无钢圈" data-jumper="rule" mars_exposure_module="category_all_expose_59450613" mars_sead="category_all_click_59450613" href="//list.vip.com/autolist.html?rule_id=59450613&amp;title=%E6%97%A0%E9%92%A2%E5%9C%88&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">无钢圈</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450718" data-cate3name="聚拢" data-jumper="rule" mars_exposure_module="category_all_expose_59450718" mars_sead="category_all_click_59450718" href="//list.vip.com/autolist.html?rule_id=59450718&amp;title=%E8%81%9A%E6%8B%A2&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">聚拢</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450379" data-cate3name="女袜" data-jumper="rule" mars_exposure_module="category_all_expose_59450379" mars_sead="category_all_click_59450379" href="//list.vip.com/autolist.html?rule_id=59450379&amp;title=%E5%A5%B3%E8%A2%9C&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女袜</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450380" data-cate3name="裤袜" data-jumper="rule" mars_exposure_module="category_all_expose_59450380" mars_sead="category_all_click_59450380" href="//list.vip.com/autolist.html?rule_id=59450380&amp;title=%E8%A3%A4%E8%A2%9C&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">裤袜</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450384" data-cate3name="女士吊带/打底背心" data-jumper="rule" mars_exposure_module="category_all_expose_59450384" mars_sead="category_all_click_59450384" href="//list.vip.com/autolist.html?rule_id=59450384&amp;title=%E5%A5%B3%E5%A3%AB%E5%90%8A%E5%B8%A6%2F%E6%89%93%E5%BA%95%E8%83%8C%E5%BF%83&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士吊带/打底背心</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450750" data-cate3name="文胸套装" data-jumper="rule" mars_exposure_module="category_all_expose_59450750" mars_sead="category_all_click_59450750" href="//list.vip.com/autolist.html?rule_id=59450750&amp;title=%E6%96%87%E8%83%B8%E5%A5%97%E8%A3%85&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">文胸套装</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_59504644">男士内衣</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="59504644" data-cate2name="男士内衣">
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495931" data-cate3name="平角裤" data-jumper="rule" mars_exposure_module="category_all_expose_59495931" mars_sead="category_all_click_59495931" href="//list.vip.com/autolist.html?rule_id=59495931&amp;title=%E5%B9%B3%E8%A7%92%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">平角裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495930" data-cate3name="组合内裤" data-jumper="rule" mars_exposure_module="category_all_expose_59495930" mars_sead="category_all_click_59495930" href="//list.vip.com/autolist.html?rule_id=59495930&amp;title=%E7%BB%84%E5%90%88%E5%86%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">组合内裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495932" data-cate3name="男士睡衣/家居服" data-jumper="rule" mars_exposure_module="category_all_expose_59495932" mars_sead="category_all_click_59495932" href="//list.vip.com/autolist.html?rule_id=59495932&amp;title=%E7%94%B7%E5%A3%AB%E7%9D%A1%E8%A1%A3%2F%E5%AE%B6%E5%B1%85%E6%9C%8D&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士睡衣/家居服</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495933" data-cate3name="男士背心/T恤" data-jumper="rule" mars_exposure_module="category_all_expose_59495933" mars_sead="category_all_click_59495933" href="//list.vip.com/autolist.html?rule_id=59495933&amp;title=%E7%94%B7%E5%A3%AB%E8%83%8C%E5%BF%83%2FT%E6%81%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士背心/T恤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450381" data-cate3name="男士内裤" data-jumper="rule" mars_exposure_module="category_all_expose_59450381" mars_sead="category_all_click_59450381" href="//list.vip.com/autolist.html?rule_id=59450381&amp;title=%E7%94%B7%E5%A3%AB%E5%86%85%E8%A3%A4&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士内裤</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450383" data-cate3name="男袜" data-jumper="rule" mars_exposure_module="category_all_expose_59450383" mars_sead="category_all_click_59450383" href="//list.vip.com/autolist.html?rule_id=59450383&amp;title=%E7%94%B7%E8%A2%9C&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男袜</a>
                        
                    </dd>
                </dl>
                
                <dl class="cate-detail-item cate-detail-item1">
                    <dt class="cate-detail-tit">
                        <i class="vipFont"></i><span mars_exposure_module="category_all_expose_59505177">秋冬好物</span>
                    </dt>
                    <dd class="cate-detail-con J_category2" data-cate2id="59505177" data-cate2name="秋冬好物">
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495938" data-cate3name="羊绒裙" data-jumper="rule" mars_exposure_module="category_all_expose_59495938" mars_sead="category_all_click_59495938" href="//list.vip.com/autolist.html?rule_id=59495938&amp;title=%E7%BE%8A%E7%BB%92%E8%A3%99&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">羊绒裙</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495936" data-cate3name="女士保暖" data-jumper="rule" mars_exposure_module="category_all_expose_59495936" mars_sead="category_all_click_59495936" href="//list.vip.com/autolist.html?rule_id=59495936&amp;title=%E5%A5%B3%E5%A3%AB%E4%BF%9D%E6%9A%96&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女士保暖</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59495937" data-cate3name="男士保暖" data-jumper="rule" mars_exposure_module="category_all_expose_59495937" mars_sead="category_all_click_59495937" href="//list.vip.com/autolist.html?rule_id=59495937&amp;title=%E7%94%B7%E5%A3%AB%E4%BF%9D%E6%9A%96&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男士保暖</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450544" data-cate3name="女式羊绒衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450544" mars_sead="category_all_click_59450544" href="//list.vip.com/autolist.html?rule_id=59450544&amp;title=%E5%A5%B3%E5%BC%8F%E7%BE%8A%E7%BB%92%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女式羊绒衫</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450546" data-cate3name="女式大衣" data-jumper="rule" mars_exposure_module="category_all_expose_59450546" mars_sead="category_all_click_59450546" href="//list.vip.com/autolist.html?rule_id=59450546&amp;title=%E5%A5%B3%E5%BC%8F%E5%A4%A7%E8%A1%A3&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">女式大衣</a>
                        
                        <a target="_blank" class="J_category3" data-cate3id="59450543" data-cate3name="男式羊绒衫" data-jumper="rule" mars_exposure_module="category_all_expose_59450543" mars_sead="category_all_click_59450543" href="//list.vip.com/autolist.html?rule_id=59450543&amp;title=%E7%94%B7%E5%BC%8F%E7%BE%8A%E7%BB%92%E8%A1%AB&amp;refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome">男式羊绒衫</a>
                        
                    </dd>
                </dl>
                
            </div>
'''
html=etree.HTML(text)
# result=etree.tostring(html)
# print(result.decode('utf-8'))


# path='//*/dl[2]/dd/a[3]/text()'
# result=html.xpath(path)
# pathTest='//*/dl[2]/dd/a[3]/@data-cate3id'
#print(result)
#print(html.xpath(pathTest))
dress=[]
hot=[]
coat=[]
trousers=[]
underwear=[]
for i in range(1,13):
    path_name=f'//*/dl[2]/dd/a[{i}]/text()'
    path_rule=f'//*/dl[2]/dd/a[{i}]/@data-cate3id'
    combine=[html.xpath(path_name),html.xpath(path_rule)]
    #print(html.xpath(path_name),html.xpath(path_rule))
    dress.append(combine)

for i in range(1,15):
    path_name=f'//*/dl[1]/dd/a[{i}]/text()'
    path_rule = f'//*/dl[1]/dd/a[{i}]/@data-cate3id'
    combine = [html.xpath(path_name), html.xpath(path_rule)]
    hot.append(combine)

for i in range(1,15):
    path_name=f'//*/dl[3]/dd/a[{i}]/text()'
    path_rule = f'//*/dl[3]/dd/a[{i}]/@data-cate3id'
    combine = [html.xpath(path_name), html.xpath(path_rule)]
    coat.append(combine)

for i in range(1,14):
    path_name=f'//*/dl[4]/dd/a[{i}]/text()'
    path_rule = f'//*/dl[4]/dd/a[{i}]/@data-cate3id'
    combine = [html.xpath(path_name), html.xpath(path_rule)]
    trousers.append(combine)

for i in range(1,16):
    path_name=f'//*/dl[11]/dd/a[{i}]/text()'
    path_rule = f'//*/dl[11]/dd/a[{i}]/@data-cate3id'
    combine = [html.xpath(path_name), html.xpath(path_rule)]
    underwear.append(combine)

print(dress)
print(hot)
print(coat)
print(trousers)
print(underwear)