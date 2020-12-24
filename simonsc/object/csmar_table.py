from sqlalchemy import Column, String, DECIMAL, DateTime, BIGINT, SMALLINT, INTEGER, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
csmar_tables = ['bond_agency', 'bond_basiccredit', 'bond_basicinfo', 'bond_bondtype', 'bond_bs', 'bond_calpretrdinfo', 'bond_cfdm', 'bond_cfets_dquote_his_dq', 'bond_cfets_pledgedrepo_hdq', 'bond_cfetsclosingyield', 'bond_cfetsvaluationindex', 'bond_cfim', 'bond_conversion', 'bond_conversionrate', 'bond_convertinfo', 'bond_convertissue', 'bond_convertprice', 'bond_crmwinfo', 'bond_currencyswapcurve', 'bond_discloseindex', 'bond_fixreporate', 'bond_guarantorinfo', 'bond_guarantorrating', 'bond_inbankod', 'bond_info', 'bond_interestfloat', 'bond_is', 'bond_issuecost', 'bond_issuer', 'bond_issueregiinfo', 'bond_lastquotationmonth', 'bond_lastquotationweek', 'bond_lastquotationyear', 'bond_mkttrade', 'bond_nafmiipricntrlcrv', 'bond_otc_quotationhis', 'bond_otc_quotationoptimal', 'bond_payment', 'bond_pretrdinfo', 'bond_pretrdinfohistory', 'bond_quotation', 'bond_quotationderivative', 'bond_quotationlatest', 'bond_quotationmonth', 'bond_quotations', 'bond_quotationweek', 'bond_quotationyear', 'bond_ratetype', 'bond_rating', 'bond_redemption', 'bond_repayterm', 'bond_repototal', 'bond_repovariety', 'bond_shcvaluation', 'bond_shcyield', 'bond_stagesredemption', 'bond_suspentioninfo', 'bond_tenderissue', 'bond_tenderresult', 'bond_treasyield', 'cmo_pretrdinfo', 'cmo_pretrdinfohistory', 'cost_riskfree', 'ffut_calpretrdinfo', 'ffut_pretrdinfo', 'ffut_pretrdinfohistory', 'fund_allocation', 'fund_areaclass', 'fund_bwardfactor', 'fund_calpretrdinfo', 'fund_classinfochange', 'fund_custodian', 'fund_daynav', 'fund_etfconstitsec', 'fund_etfpchasredemlis', 'fund_evl_dayahay', 'fund_evl_dayamth', 'fund_evl_dayasen', 'fund_evl_dayayear', 'fund_evl_daythryear', 'fund_evl_weekahay', 'fund_evl_weekayear', 'fund_evl_weekthryear', 'fund_feeschange', 'fund_fundcodeinfo', 'fund_fundcompany', 'fund_funddividend', 'fund_fundmanager', 'fund_fwardfactor', 'fund_holderstructure', 'fund_indexreturn', 'fund_industrystockclass', 'fund_jajxrate', 'fund_listing', 'fund_mainpersonnel', 'fund_mkt_bwardquotation', 'fund_mkt_fwardquotation', 'fund_mkt_lastbwardquotem', 'fund_mkt_lastbwardquotew', 'fund_mkt_lastbwardquotey', 'fund_mkt_lastfwardquotem', 'fund_mkt_lastfwardquotew', 'fund_mkt_lastfwardquotey', 'fund_mkt_lastquotationmonth', 'fund_mkt_lastquotationweek', 'fund_mkt_lastquotationyear', 'fund_mkt_quotation', 'fund_mkt_quotationlatest', 'fund_mkt_quotationmonth', 'fund_mkt_quotationweek', 'fund_mkt_quotationyear', 'fund_mktdayreturn', 'fund_mktmonthreturn', 'fund_mktpf_pfm', 'fund_mktpf_pfm_week', 'fund_mktweekreturn', 'fund_mktyearreturn', 'fund_nav', 'fund_nav_month', 'fund_nav_pfm', 'fund_nav_pfm_month', 'fund_nav_pfm_week', 'fund_nav_pfm_year', 'fund_nav_week', 'fund_nav_year', 'fund_performance_compare', 'fund_performance_deviation', 'fund_portfolio_abs', 'fund_portfolio_bondcredit', 'fund_portfolio_bondvariety', 'fund_portfolio_currency', 'fund_portfolio_stock', 'fund_pretrdinfo', 'fund_pretrdinfohistory', 'fund_promoter', 'fund_prospectuses', 'fund_ptf_bondspe', 'fund_ptf_bsstock', 'fund_ptf_bsstocktotal', 'fund_ptf_der', 'fund_ptf_fund', 'fund_purchredchg', 'fund_quotation', 'fund_reportdate', 'fund_resolution', 'fund_sharechange', 'fund_shareholdercompany', 'fund_shsecrate', 'fund_stracontract', 'fund_stractshare', 'fund_strader', 'fund_strainfo', 'fund_stranav', 'fund_straquotation', 'fund_strbder', 'fund_strbinfo', 'fund_strbnav', 'fund_strbquotation', 'fund_strinfo', 'fund_strmder', 'fund_strmnav', 'fund_strmquotation', 'fund_strtrackamonth', 'fund_strtrackaweek', 'fund_strtrackbmonth', 'fund_strtrackbweek', 'fund_tenholders', 'fund_unitclassinfo', 'fut_calpretrdinfo', 'fut_pretrdinfo', 'fut_pretrdinfohistory', 'idx_closeweight', 'idx_closeweightfree', 'idx_indexinfo', 'idx_mkt_lastquotationweek', 'idx_mkt_quotation', 'idx_samplechange', 'idx_samplelatest', 'idx_weight', 'idx_weightnextday', 'io_calpretrdinfo', 'io_pretrdinfo', 'io_pretrdinfohistory', 'mac_area_ampimonth', 'mac_area_ampiyear', 'mac_area_cpimonth', 'mac_area_cpiyear', 'mac_area_fixedassetsidx', 'mac_area_fixedassetsidxyear', 'mac_area_gdpquarter', 'mac_area_gdpyear', 'mac_area_industrysalevalue', 'mac_area_industryvalueadd', 'mac_area_ppimonth', 'mac_area_ppiyear', 'mac_area_productoutputmonth', 'mac_area_productoutputyear', 'mac_area_purchaseidxmonth', 'mac_area_purchaseidxyear', 'mac_area_rpimonth', 'mac_area_rpiyear', 'mac_areagdp_expendyear', 'mac_areagdp_idx1978year', 'mac_areagdp_idxyear', 'mac_areagdp_incomeyear', 'mac_bondyieldsd', 'mac_fixedbaseidx', 'mac_industry_financialyear', 'mac_industry_ppimonth', 'mac_industry_ppiyear', 'mac_industry_saleinventory', 'mac_industry_valueadd', 'mac_industryvalueadd', 'mac_statsinfo_calendar', 'plate_bondchange', 'plate_bondchangelatest', 'plate_bondsamplechange', 'plate_concept', 'plate_fundchange', 'plate_fundchangelatest', 'plate_fundsamplechange', 'plate_futurechange', 'plate_futurechangelatest', 'plate_futuresamplechange', 'plate_indexchange', 'plate_indexchangelatest', 'plate_indexsamplechange', 'plate_platetree', 'plate_platetree_state2', 'plate_sochange', 'plate_sochangelatest', 'plate_sosamplechange', 'plate_stockchange', 'plate_stockchangelatest', 'plate_stocksamplechange', 'pled_agrrepamt', 'pled_agrrepdetl', 'pled_amtstat', 'pled_ltvratio', 'pled_repbysecco', 'pled_sectrdvol', 'pled_stkfrzdetl', 'pled_stkratio', 'pled_stktrdvol', 'pled_trddetl', 'pub_chnadmdivisioncode', 'pub_codingschema', 'pub_continuingcontract', 'pub_eventtype', 'pub_exchangeinfo', 'pub_indclassifysets', 'pub_indclassifyversion', 'pub_institutionidchange', 'pub_institutioninfo', 'pub_isocontrycode', 'pub_isocurrencycode', 'pub_mainconcontract', 'pub_maincontract', 'pub_personnelinfo', 'pub_pretradinginfo', 'pub_securityconstant', 'pub_securityinfo', 'sh_securityinfo', 'smt_collateral', 'smt_collaterald', 'smt_traded', 'smt_tradesumd', 'smt_underlyingsd', 'so_calpretrdinfo', 'so_pretrdinfo', 'so_pretrdinfohistory', 'stk_af_analystrank', 'stk_af_forecast', 'stk_af_ratingchange', 'stk_af_ratingstatistic', 'stk_af_targetvalue', 'stk_calendard', 'stk_dividend', 'stk_eq_ipo_coinfo', 'stk_eq_ipo_employeeinfo', 'stk_eq_ipo_info', 'stk_eq_ipo_ipocg', 'stk_eq_ipo_marketexhibit', 'stk_eq_ipo_overallot', 'stk_eq_ipo_result', 'stk_eq_rs_info', 'stk_eq_rs_plan', 'stk_eq_rs_result', 'stk_eq_seo_plan', 'stk_eq_seo_private', 'stk_eq_seo_publicinfo', 'stk_eq_seo_publicresult', 'stk_eventlist', 'stk_fin_balance', 'stk_fin_cashflow', 'stk_fin_cashflowindex', 'stk_fin_cashflowindrect', 'stk_fin_cashflowindrectttm', 'stk_fin_cashflowttm', 'stk_fin_construct', 'stk_fin_debtpay', 'stk_fin_development', 'stk_fin_dividistrib', 'stk_fin_earnpower', 'stk_fin_financialindexq', 'stk_fin_forecfin', 'stk_fin_forecfinnew', 'stk_fin_income', 'stk_fin_incomettm', 'stk_fin_ipodiscloseindex', 'stk_fin_lcdiscloseindex', 'stk_fin_operate', 'stk_fin_pershare', 'stk_fin_quitrafin', 'stk_fin_quitrafinnew', 'stk_fin_quitrasimfin', 'stk_fin_relativevalue', 'stk_fin_relforcdate', 'stk_fin_risk', 'stk_fin_simforecfin', 'stk_forecast', 'stk_guarantee_main', 'stk_guarantee_son', 'stk_guarantee_statistics', 'stk_holder_controlchart', 'stk_holder_controller', 'stk_holder_detail', 'stk_holder_equitynatureall', 'stk_holder_incrordesr', 'stk_holder_number', 'stk_holder_pledge', 'stk_holder_relation', 'stk_holder_systematics', 'stk_holder_top10', 'stk_holder_top10floating', 'stk_indfi_basis', 'stk_indfi_cashflow', 'stk_indfi_construct', 'stk_indfi_crn', 'stk_indfi_debtpay', 'stk_indfi_development', 'stk_indfi_dividistrib', 'stk_indfi_earnpower', 'stk_indfi_hhi', 'stk_indfi_indtrajectory', 'stk_indfi_lernerindex', 'stk_indfi_lpesv', 'stk_indfi_npesv', 'stk_indfi_operate', 'stk_indfi_pershare', 'stk_indfi_relativevalue', 'stk_indfi_risk', 'stk_industryclass', 'stk_institutionholderalias', 'stk_institutioninfo', 'stk_itemchange', 'stk_listedcoinfochg', 'stk_lock_shares', 'stk_lockshares_summary', 'stk_ma_assetreplace', 'stk_ma_assetstopay', 'stk_ma_assettrans', 'stk_ma_cashpayment', 'stk_ma_cdr', 'stk_ma_equitytransfer', 'stk_ma_merger', 'stk_ma_otherparty', 'stk_ma_participant', 'stk_ma_stockpayment', 'stk_ma_tenderoffer', 'stk_ma_tradingmain', 'stk_ma_tradingschedule', 'stk_ma_underlying', 'stk_mkt_adjustfactor', 'stk_mkt_blocktrade', 'stk_mkt_capitalflow', 'stk_mkt_capitalflows', 'stk_mkt_divident', 'stk_mkt_dividentnew', 'stk_mkt_exchangerate', 'stk_mkt_nightcale', 'stk_mkt_quotation', 'stk_mkt_quotationlatest', 'stk_mkt_repricefactor', 'stk_notes_accountingpolicy', 'stk_notes_adminexpense', 'stk_notes_afsfinassect', 'stk_notes_ap', 'stk_notes_apsd', 'stk_notes_ar', 'stk_notes_arsd', 'stk_notes_assetimpairment', 'stk_notes_basiccontent', 'stk_notes_billrandp', 'stk_notes_billrandpspecial', 'stk_notes_bondspayable', 'stk_notes_businesstaxappend', 'stk_notes_capitalreserve', 'stk_notes_capitalstock', 'stk_notes_cbd', 'stk_notes_cbdsd', 'stk_notes_cip', 'stk_notes_cipchange', 'stk_notes_deferredincometax', 'stk_notes_devexpense', 'stk_notes_dividendpayable', 'stk_notes_dr', 'stk_notes_drsd', 'stk_notes_equityinvest', 'stk_notes_equityinvestcoinfo', 'stk_notes_fairvalueb', 'stk_notes_financecosts', 'stk_notes_fixedassect', 'stk_notes_goodwill', 'stk_notes_govgrants', 'stk_notes_impjntfin', 'stk_notes_interestpayable', 'stk_notes_invassect', 'stk_notes_inventories', 'stk_notes_investmentinc', 'stk_notes_invexit', 'stk_notes_longtermloan', 'stk_notes_longtermprepaidfee', 'stk_notes_machabalance', 'stk_notes_monetaryfunds', 'stk_notes_nldoneyear', 'stk_notes_nomtaxrate', 'stk_notes_nonbusexp', 'stk_notes_nonbusinc', 'stk_notes_nonrecurring', 'stk_notes_oar', 'stk_notes_oarsd', 'stk_notes_ocassect', 'stk_notes_op', 'stk_notes_operateincomecosts', 'stk_notes_opsd', 'stk_notes_payrecbus', 'stk_notes_paysalary', 'stk_notes_realestate', 'stk_notes_sellexpense', 'stk_notes_shorttermloan', 'stk_notes_subjoint', 'stk_notes_surplusreserve', 'stk_notes_taxpayable', 'stk_notes_topfivebp', 'stk_notes_tradfinassect', 'stk_notes_udp', 'stk_originalholders', 'stk_personalholderalias', 'stk_pretrdinfo', 'stk_pretrdinfohistory', 'stk_relationship_background', 'stk_rpt_ralatedparty', 'stk_rpt_transactions', 'stk_rpt_transfer', 'stk_shares_structure', 'stk_shares_structure_daily', 'stk_sr_difference', 'stk_sr_equitychange', 'stk_sr_implement', 'stk_sr_indexm', 'stk_sr_repumain', 'stk_sr_schedule', 'stk_stockinfo', 'stk_suspentioninfo', 'stk_view_stockinfo', 'stk_view_stockinfohistory', 'sz_securityinfo', 'sz_securityinfohistory', 'tbl_chn_bond_infochg', 'zz_bondcloseweight', 'zz_bondtermstructure', 'zz_bondvaluation', 'zz_divisoradjustment']
Base = declarative_base()
metadata = Base.metadata


class bond_agency(Base):

    __tablename__ = 'bond_agency'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    ISSUEDATE = Column(DateTime, doc="发行日期")
    BONDISSUETYPEID = Column(String(20), doc="债券发行类别ID")
    BONDISSUETYPE = Column(String(100), doc="债券发行类别")
    AGENCYTYPEID = Column(String(20), doc="中介机构类别ID")
    AGENCYTYPE = Column(String(100), doc="中介机构类别")
    AGENCYID = Column(String(20), doc="中介机构ID")
    AGENCYNAME = Column(String(200), doc="中介机构名称")
    COMMENTS = Column(String(2000), doc="备注")
    ID_0067 = Column(BIGINT, doc="巨潮记录ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_basiccredit(Base):

    __tablename__ = 'bond_basiccredit'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    FULLNAME = Column(String(200), doc="债券全称")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="发行机构ID")
    INSTITUTIONNAME = Column(String(200), doc="发行机构")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    CREDITAMOUNT = Column(DECIMAL(20, 2), doc="授信额度")
    USEDCREDITAMOUNT = Column(DECIMAL(20, 2), doc="已使用授信额度")
    UNUSEDCREDITAMOUNT = Column(DECIMAL(20, 2), doc="未使用授信额度")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CURRENCY = Column(String(200), doc="币种")


class bond_basicinfo(Base):

    __tablename__ = 'bond_basicinfo'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    FULLNAME = Column(String(200), doc="债券全称")
    ENFULLNAME = Column(String(600), doc="债券英文全称")
    ISSUEYEAR = Column(String(8), doc="债券年度")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    BONDNATURE = Column(String(100), doc="债券类型")
    PERIODTIME = Column(String(8), doc="债券期次")
    CATEGORYTYPEID = Column(String(12), doc="品种类别ID")
    CATEGORYTYPE = Column(String(40), doc="品种类别")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="发行机构ID")
    INSTITUTIONNAME = Column(String(200), doc="发行机构全称")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    CURRENCY = Column(String(40), doc="币种")
    ISSUESHARES = Column(DECIMAL(6, 2), doc="实际发行量")
    ISSUEPRICE = Column(DECIMAL(12, 4), doc="发行价格")
    ISSUEMODEID = Column(String(12), doc="发行方式ID :废弃不用")
    ISSUEMODE = Column(String(400), doc="发行方式")
    BONDFORMID = Column(String(20), doc="债券形式ID")
    BONDFORM = Column(String(120), doc="债券形式")
    TERM = Column(DECIMAL(6, 2), doc="期限")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    ISSUEDATE = Column(DateTime, doc="发行起始日期")
    MATURITYDATE = Column(DateTime, doc="到期日期")
    INTERESTSTARTDATE = Column(DateTime, doc="计息日期")
    INTERESTENDDATE = Column(DateTime, doc="止息日期")
    PAYTYPEID = Column(String(12), doc="付息方式ID")
    PAYTYPE = Column(String(40), doc="付息方式")
    CALCULATIONTYPEID = Column(String(12), doc="计息方式ID")
    CALCULATIONTYPE = Column(String(40), doc="计息方式")
    RATETYPEID = Column(String(12), doc="利率类型ID")
    RATETYPE = Column(String(40), doc="利率类型")
    YEARPAYTIME = Column(DECIMAL(6, 2), doc="年付息次数")
    PAYMENTDATEDESCRIPTION = Column(String(1000), doc="付息日期描述")
    PARVALUERATE = Column(DECIMAL(7, 3), doc="票面利率")
    SHIBOR = Column(String(400), doc="基准利率")
    BASICRATE = Column(DECIMAL(7, 3), doc="基本利差")
    PARVALUE = Column(SMALLINT, doc="面值")
    BONDCREDITLEVEL = Column(String(12), doc="债券信用等级")
    ISSUERCREDITLEVEL = Column(String(12), doc="发行主体信用等级")
    ISREDEEM = Column(String(8), doc="可赎回性")
    REDEEMCLAUSE = Column(String(4000), doc="赎回条款")
    REDEEMDATE = Column(DateTime, doc="赎回日期")
    REDEEMPRICE = Column(DECIMAL(8, 3), doc="赎回价格")
    ISSALEBACK = Column(String(8), doc="可回售性")
    SALEBACKCLAUSE = Column(String(4000), doc="回售条款")
    SALEBACKDATE = Column(DateTime, doc="回售日期")
    SALEBACKPRICE = Column(DECIMAL(8, 3), doc="回售价格")
    REDEMPTIONDATE = Column(DateTime, doc="兑付日")
    REDEMPTIONINSTRUCTIONS = Column(String(400), doc="兑付说明")
    ISEXCHANGE = Column(String(200), doc="可调换性")
    TRANSFORMATIONCLAUSE = Column(String(200), doc="可转换条款")
    EXCHANGEBOND = Column(String(20), doc="调换债券")
    EXCHANGERATE = Column(DECIMAL(5, 2), doc="调换比例")
    EXCHANGEDATE = Column(DateTime, doc="调换日期")
    ISGUARANTEE = Column(String(8), doc="是否有担保")
    ISCROSSMARKET = Column(String(8), doc="是否跨市场")
    EXPLANATION = Column(String(600), doc="跨市场说明")
    ISSEPARATION = Column(String(8), doc="是否可分离")
    COMMENTS = Column(String(2000), doc="备注")
    ID_0063 = Column(BIGINT, doc="巨潮记录ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    OPTIONTYPE = Column(String(20), doc="行权类型")
    CALLORPUT = Column(String(10), doc="看涨看跌")
    RATEOPTIONSTARTCYCLE = Column(DECIMAL(10, 2), doc="票面利率选择权开始周期")
    RATEOPTIONFLOATCEILING = Column(DECIMAL(10, 2), doc="票面利率选择权浮动上限")
    RATEOPTIONFLOATFLOOR = Column(DECIMAL(10, 2), doc="票面利率选择权浮动下限")
    UNDERWRITEDMETHODS = Column(String(400), doc="承销方式")
    ISSUEOBJECT = Column(String(400), doc="发行对象")
    ONLINEISSUESHARES = Column(DECIMAL(20, 2), doc="网上发行数量")
    ONLINEISSUELIMIT = Column(String(400), doc="网上发行认购数量限制说明")
    ONLINEISSUESTARTDATE = Column(DateTime, doc="网上发行起始日期")
    ONLINEISSUEENDDATE = Column(DateTime, doc="网上发行截止日期")
    ISSUEENDDATE = Column(DateTime, doc="发行截止日期")


class bond_bondtype(Base):

    __tablename__ = 'bond_bondtype'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    BONDTYPEID = Column(String(20), doc="债券品种编码")
    VOLUME = Column(BIGINT, doc="成交笔数")
    VOLUMECHANGE = Column(BIGINT, doc="成交笔数增减")
    AMOUNT = Column(DECIMAL(12, 4), doc="成交额")
    AMOUNTCHANGE = Column(DECIMAL(12, 4), doc="成交额增减")
    AMOUNTRATIO = Column(DECIMAL(8, 4), doc="占总成交比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_bs(Base):

    __tablename__ = 'bond_bs'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    STOCKCODE = Column(String(12), doc="股票代码")
    ACCOUPERI = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    A001101 = Column(DECIMAL(20, 2), doc="货币资金")
    A0D110110 = Column(DECIMAL(20, 2), doc="其中:客户资金存款")
    A0B1103 = Column(DECIMAL(20, 2), doc="现金及存放中央银行款项")
    A0D1102 = Column(DECIMAL(20, 2), doc="结算备付金")
    A0D110210 = Column(DECIMAL(20, 2), doc="其中：客户备付金")
    A0B1105 = Column(DECIMAL(20, 2), doc="贵金属")
    A0B1104 = Column(DECIMAL(20, 2), doc="存放同业款项")
    A0F1106 = Column(DECIMAL(20, 2), doc="拆出资金净额")
    A001107 = Column(DECIMAL(20, 2), doc="交易性金融资产")
    A0F1108 = Column(DECIMAL(20, 2), doc="衍生金融资产")
    A001109 = Column(DECIMAL(20, 2), doc="短期投资净额")
    A0F1122 = Column(DECIMAL(20, 2), doc="买入返售金融资产净额")
    A001110 = Column(DECIMAL(20, 2), doc="应收票据净额")
    A001111 = Column(DECIMAL(20, 2), doc="应收账款净额")
    A001112 = Column(DECIMAL(20, 2), doc="预付款项净额")
    A001119 = Column(DECIMAL(20, 2), doc="应收利息净额")
    A001120 = Column(DECIMAL(20, 2), doc="应收股利净额")
    A001121 = Column(DECIMAL(20, 2), doc="其他应收款净额")
    A0I1113 = Column(DECIMAL(20, 2), doc="应收保费净额")
    A0I1114 = Column(DECIMAL(20, 2), doc="应收分保账款净额")
    A0I1115 = Column(DECIMAL(20, 2), doc="应收代位追偿款净额")
    A0I1116 = Column(DECIMAL(20, 2), doc="应收分保合同准备金净额")
    A0I111610 = Column(DECIMAL(20, 2), doc="其中:应收分保未到期责任准备金净额")
    A0I111620 = Column(DECIMAL(20, 2), doc="其中:应收分保未决赔款准备金净额")
    A0I111630 = Column(DECIMAL(20, 2), doc="其中:应收分保寿险责任准备金净额")
    A0I111640 = Column(DECIMAL(20, 2), doc="其中:应收分保长期健康险责任准备金净额")
    A001123 = Column(DECIMAL(20, 2), doc="存货净额")
    A0D1126 = Column(DECIMAL(20, 2), doc="存出保证金")
    A001124 = Column(DECIMAL(20, 2), doc="一年内到期的非流动资产")
    A001125 = Column(DECIMAL(20, 2), doc="其他流动资产")
    A0011 = Column(DECIMAL(20, 2), doc="流动资产合计")
    A0B1201 = Column(DECIMAL(20, 2), doc="发放贷款及垫款净额")
    A0I1224 = Column(DECIMAL(20, 2), doc="保户质押贷款净额")
    A0I1225 = Column(DECIMAL(20, 2), doc="定期存款")
    A001202 = Column(DECIMAL(20, 2), doc="可供出售金融资产净额")
    A001203 = Column(DECIMAL(20, 2), doc="持有至到期投资净额")
    A001204 = Column(DECIMAL(20, 2), doc="长期应收款净额")
    A001205 = Column(DECIMAL(20, 2), doc="长期股权投资净额")
    A001206 = Column(DECIMAL(20, 2), doc="长期债权投资净额")
    A001207 = Column(DECIMAL(20, 2), doc="长期投资净额")
    A0I1209 = Column(DECIMAL(20, 2), doc="存出资本保证金")
    A001211 = Column(DECIMAL(20, 2), doc="投资性房地产净额")
    A001212 = Column(DECIMAL(20, 2), doc="固定资产净额")
    A001213 = Column(DECIMAL(20, 2), doc="在建工程净额")
    A001214 = Column(DECIMAL(20, 2), doc="工程物资")
    A001215 = Column(DECIMAL(20, 2), doc="固定资产清理")
    A001216 = Column(DECIMAL(20, 2), doc="生产性生物资产净额")
    A001217 = Column(DECIMAL(20, 2), doc="油气资产净额")
    A001218 = Column(DECIMAL(20, 2), doc="无形资产净额")
    A0D121810 = Column(DECIMAL(20, 2), doc="其中:交易席位费")
    A001219 = Column(DECIMAL(20, 2), doc="开发支出")
    A001220 = Column(DECIMAL(20, 2), doc="商誉净额")
    A001221 = Column(DECIMAL(20, 2), doc="长期待摊费用")
    A0I1210 = Column(DECIMAL(20, 2), doc="独立账户资产")
    A0F1224 = Column(DECIMAL(20, 2), doc="代理业务资产")
    A001222 = Column(DECIMAL(20, 2), doc="递延所得税资产")
    A001223 = Column(DECIMAL(20, 2), doc="其他非流动资产")
    A0012 = Column(DECIMAL(20, 2), doc="非流动资产合计")
    A0F13 = Column(DECIMAL(20, 2), doc="其他资产")
    A001 = Column(DECIMAL(20, 2), doc="资产总计")
    A0B2102 = Column(DECIMAL(20, 2), doc="向中央银行借款")
    A0F2104 = Column(DECIMAL(20, 2), doc="拆入资金")
    A0B2103 = Column(DECIMAL(20, 2), doc="吸收存款及同业存放")
    A0B210310 = Column(DECIMAL(20, 2), doc="其中：同业及其他金融机构存放款项")
    A0B210320 = Column(DECIMAL(20, 2), doc="其中：吸收存款")
    A002101 = Column(DECIMAL(20, 2), doc="短期借款")
    A0D210110 = Column(DECIMAL(20, 2), doc="其中:质押借款")
    A002105 = Column(DECIMAL(20, 2), doc="交易性金融负债")
    A0F2106 = Column(DECIMAL(20, 2), doc="衍生金融负债")
    A0F2110 = Column(DECIMAL(20, 2), doc="卖出回购金融资产款")
    A0D2122 = Column(DECIMAL(20, 2), doc="代理买卖证券款")
    A0D2123 = Column(DECIMAL(20, 2), doc="代理承销证券款")
    A002107 = Column(DECIMAL(20, 2), doc="应付票据")
    A002108 = Column(DECIMAL(20, 2), doc="应付账款")
    A002109 = Column(DECIMAL(20, 2), doc="预收款项")
    A0I2124 = Column(DECIMAL(20, 2), doc="预收保费")
    A0I2111 = Column(DECIMAL(20, 2), doc="应付手续费及佣金")
    A0I2121 = Column(DECIMAL(20, 2), doc="应付分保账款")
    A002112 = Column(DECIMAL(20, 2), doc="应付职工薪酬")
    A002113 = Column(DECIMAL(20, 2), doc="应交税费")
    A002114 = Column(DECIMAL(20, 2), doc="应付利息")
    A002115 = Column(DECIMAL(20, 2), doc="应付股利")
    A0I2116 = Column(DECIMAL(20, 2), doc="应付赔付款")
    A0I2117 = Column(DECIMAL(20, 2), doc="应付保单红利")
    A0I2118 = Column(DECIMAL(20, 2), doc="保户储金及投资款")
    A0I2119 = Column(DECIMAL(20, 2), doc="保险合同准备金")
    A0I211910 = Column(DECIMAL(20, 2), doc="其中:未到期责任准备金")
    A0I211920 = Column(DECIMAL(20, 2), doc="其中:未决赔款准备金")
    A0I211930 = Column(DECIMAL(20, 2), doc="其中:寿险责任准备金")
    A0I211940 = Column(DECIMAL(20, 2), doc="其中:长期健康险责任准备金")
    A002120 = Column(DECIMAL(20, 2), doc="其他应付款")
    A002125 = Column(DECIMAL(20, 2), doc="一年内到期的非流动负债")
    A002126 = Column(DECIMAL(20, 2), doc="其他流动负债")
    A0021 = Column(DECIMAL(20, 2), doc="流动负债合计")
    A002201 = Column(DECIMAL(20, 2), doc="长期借款")
    A0D2202 = Column(DECIMAL(20, 2), doc="独立账户负债")
    A002203 = Column(DECIMAL(20, 2), doc="应付债券")
    A002204 = Column(DECIMAL(20, 2), doc="长期应付款")
    A002205 = Column(DECIMAL(20, 2), doc="专项应付款")
    A002206 = Column(DECIMAL(20, 2), doc="长期负债合计")
    A002207 = Column(DECIMAL(20, 2), doc="预计负债")
    A0F2210 = Column(DECIMAL(20, 2), doc="代理业务负债")
    A002208 = Column(DECIMAL(20, 2), doc="递延所得税负债")
    A002209 = Column(DECIMAL(20, 2), doc="其他非流动负债")
    A0022 = Column(DECIMAL(20, 2), doc="非流动负债合计")
    A0F23 = Column(DECIMAL(20, 2), doc="其他负债")
    A002 = Column(DECIMAL(20, 2), doc="负债合计")
    A003101 = Column(DECIMAL(20, 2), doc="实收资本(或股本)")
    A003102 = Column(DECIMAL(20, 2), doc="资本公积")
    A003110 = Column(DECIMAL(20, 2), doc="减：库存股")
    A003109 = Column(DECIMAL(20, 2), doc="专项储备")
    A003103 = Column(DECIMAL(20, 2), doc="盈余公积")
    A0F3104 = Column(DECIMAL(20, 2), doc="一般风险准备")
    A003105 = Column(DECIMAL(20, 2), doc="未分配利润")
    A003106 = Column(DECIMAL(20, 2), doc="外币报表折算差额")
    A003107 = Column(DECIMAL(20, 2), doc="未确认的投资损失")
    A0F3108 = Column(DECIMAL(20, 2), doc="交易风险准备")
    A0031 = Column(DECIMAL(20, 2), doc="归属于母公司所有者权益合计")
    A0032 = Column(DECIMAL(20, 2), doc="少数股东权益")
    A003 = Column(DECIMAL(20, 2), doc="所有者权益合计")
    A004 = Column(DECIMAL(20, 2), doc="负债与所有者权益总计")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_calpretrdinfo(Base):

    __tablename__ = 'bond_calpretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    ISSUEPRICE = Column(DECIMAL(12, 4), doc="发行价格")
    PARVALUERATE = Column(DECIMAL(7, 3), doc="票面利率")
    INTERESTSTARTDATE = Column(DateTime, doc="计息日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    INTERESTDAYS = Column(INTEGER, doc="计息天数")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    MINTICKSIZE = Column(DECIMAL(10, 3), doc="价格档位")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    ISDIVIDEND = Column(SMALLINT, doc="是否付息日")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_cfdm(Base):

    __tablename__ = 'bond_cfdm'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    STOCKCODE = Column(String(12), doc="股票代码")
    BEGDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    C001001 = Column(DECIMAL(20, 2), doc="销售商品、提供劳务收到的现金")
    C0B1002 = Column(DECIMAL(20, 2), doc="客户存款和同业存放款项净增加额")
    C0F1023 = Column(DECIMAL(20, 2), doc="存放央行和同业款项净减少额")
    C0B1003 = Column(DECIMAL(20, 2), doc="向中央银行借款净增加额")
    C0B1004 = Column(DECIMAL(20, 2), doc="向其他金融机构拆入资金净增加额")
    C0I1005 = Column(DECIMAL(20, 2), doc="收到原保险合同保费取得的现金")
    C0I1006 = Column(DECIMAL(20, 2), doc="收到再保险业务现金净额")
    C0I1007 = Column(DECIMAL(20, 2), doc="保户储金及投资款净增加额")
    C0D1008 = Column(DECIMAL(20, 2), doc="处置交易性金融资产净增加额")
    C0D1010 = Column(DECIMAL(20, 2), doc="拆入资金净增加额")
    C0D1011 = Column(DECIMAL(20, 2), doc="回购业务资金净增加额")
    C0F1024 = Column(DECIMAL(20, 2), doc="拆出资金净减少额")
    C0F1025 = Column(DECIMAL(20, 2), doc="买入返售款项净减少额")
    C0F1009 = Column(DECIMAL(20, 2), doc="收取利息、手续费及佣金的现金")
    C001012 = Column(DECIMAL(20, 2), doc="收到的税费返还")
    C001013 = Column(DECIMAL(20, 2), doc="收到的其他与经营活动有关的现金")
    C0011 = Column(DECIMAL(20, 2), doc="经营活动现金流入小计")
    C001014 = Column(DECIMAL(20, 2), doc="购买商品、接受劳务支付的现金")
    C0B1015 = Column(DECIMAL(20, 2), doc="客户贷款及垫款净增加额")
    C0F1026 = Column(DECIMAL(20, 2), doc="向中央银行借款净减少额")
    C0B1016 = Column(DECIMAL(20, 2), doc="存放中央银行和同业款项净增加额")
    C0I1017 = Column(DECIMAL(20, 2), doc="支付原保险合同赔付款项的现金")
    C0F1027 = Column(DECIMAL(20, 2), doc="支付再保业务现金净额")
    C0F1028 = Column(DECIMAL(20, 2), doc="保户储金及投资款净减少额")
    C0F1029 = Column(DECIMAL(20, 2), doc="拆出资金净增加额")
    C0F1030 = Column(DECIMAL(20, 2), doc="买入返售款项净增加额")
    C0F1031 = Column(DECIMAL(20, 2), doc="拆入资金净减少额")
    C0F1032 = Column(DECIMAL(20, 2), doc="卖出回购款项净减少额")
    C0F1018 = Column(DECIMAL(20, 2), doc="支付利息、手续费及佣金的现金")
    C0I1019 = Column(DECIMAL(20, 2), doc="支付保单红利的现金")
    C001020 = Column(DECIMAL(20, 2), doc="支付给职工以及为职工支付的现金")
    C001021 = Column(DECIMAL(20, 2), doc="支付的各项税费")
    C001022 = Column(DECIMAL(20, 2), doc="支付其他与经营活动有关的现金")
    C0012 = Column(DECIMAL(20, 2), doc="经营活动现金流出小计")
    C001 = Column(DECIMAL(20, 2), doc="经营活动产生的现金流量净额")
    C002001 = Column(DECIMAL(20, 2), doc="收回投资收到的现金")
    C002002 = Column(DECIMAL(20, 2), doc="取得投资收益收到的现金")
    C002003 = Column(DECIMAL(20, 2), doc="处置固定资产、无形资产和其他长期资产收回的现金净额")
    C002004 = Column(DECIMAL(20, 2), doc="处置子公司及其他营业单位收到的现金净额")
    C002005 = Column(DECIMAL(20, 2), doc="收到的其他与投资活动有关的现金")
    C0021 = Column(DECIMAL(20, 2), doc="投资活动产生的现金流入小计")
    C002006 = Column(DECIMAL(20, 2), doc="购建固定资产、无形资产和其他长期资产支付的现金")
    C002007 = Column(DECIMAL(20, 2), doc="投资支付的现金")
    C0I2008 = Column(DECIMAL(20, 2), doc="质押贷款净增加额")
    C002009 = Column(DECIMAL(20, 2), doc="取得子公司及其他营业单位支付的现金净额")
    C002010 = Column(DECIMAL(20, 2), doc="支付其他与投资活动有关的现金")
    C0022 = Column(DECIMAL(20, 2), doc="投资活动产生的现金流出小计")
    C002 = Column(DECIMAL(20, 2), doc="投资活动产生的现金流量净额")
    C003008 = Column(DECIMAL(20, 2), doc="发行证券收到的现金")
    C00300810 = Column(DECIMAL(20, 2), doc="吸收投资收到的现金")
    C0030081010 = Column(DECIMAL(20, 2), doc="其中：子公司吸收少数股东投资收到的现金")
    C003002 = Column(DECIMAL(20, 2), doc="取得借款收到的现金")
    C00300820 = Column(DECIMAL(20, 2), doc="发行债券收到的现金")
    C003004 = Column(DECIMAL(20, 2), doc="收到其他与筹资活动有关的现金")
    C0031 = Column(DECIMAL(20, 2), doc="筹资活动现金流入小计")
    C003005 = Column(DECIMAL(20, 2), doc="偿还债务支付的现金")
    C003006 = Column(DECIMAL(20, 2), doc="分配股利、利润或偿付利息支付的现金")
    C00300610 = Column(DECIMAL(20, 2), doc="其中：子公司支付给少数股东的股利、利润")
    C003007 = Column(DECIMAL(20, 2), doc="支付其他与筹资活动有关的现金")
    C0032 = Column(DECIMAL(20, 2), doc="筹资活动现金流出小计")
    C003 = Column(DECIMAL(20, 2), doc="筹资活动产生的现金流量净额")
    C004 = Column(DECIMAL(20, 2), doc="汇率变动对现金及现金等价物的影响")
    C007 = Column(DECIMAL(20, 2), doc="其他对现金的影响")
    C005 = Column(DECIMAL(20, 2), doc="现金及现金等价物净增加额")
    C008 = Column(DECIMAL(20, 2), doc="期初现金及现金等价物余额")
    C006 = Column(DECIMAL(20, 2), doc="期末现金及现金等价物余额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_cfets_dquote_his_dq(Base):

    __tablename__ = 'bond_cfets_dquote_his_dq'

    SYMBOL = Column(String(20), doc="债券代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    EXCHANGE = Column(String(120), doc="交易市场")
    SHORTNAME = Column(String(80), doc="债券简称")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="前结算价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="期初结算价格")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="期末结算价格")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高结算价格")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低结算价格")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交额")
    TRANSACTION = Column(BIGINT, doc="成交笔数")
    INSTITUTION = Column(String(120), doc="发行人名称")
    PREAVGPRICE = Column(DECIMAL(10, 4), doc="前期平均价格")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    AVGPRICE = Column(DECIMAL(10, 4), doc="本期平均价格")
    AVGFULLPRICE = Column(DECIMAL(10, 4), doc="全价平均价格")
    PRINCIPAL = Column(DECIMAL(20, 4), doc="本金额")
    CAPITALAMOUNT = Column(DECIMAL(20, 4), doc="资金额")
    REMAINPERIOD = Column(DECIMAL(10, 4), doc="待偿期")
    AVGRETURN = Column(DECIMAL(20, 6), doc="平均年收益率")
    AVGTRADINGPRICE = Column(DECIMAL(20, 4), doc="平均每笔成交量")
    SETTLEMENTDAY = Column(INTEGER, doc="结算天数")
    OPTIONTYPE = Column(String(80), doc="选择权类别")
    OPTIONDATE = Column(DateTime, doc="选择权日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_cfets_pledgedrepo_hdq(Base):

    __tablename__ = 'bond_cfets_pledgedrepo_hdq'

    SYMBOL = Column(String(20), doc="债券代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    EXCHANGE = Column(String(120), doc="交易市场")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘利率")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="期初利率")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="期末利率")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高利率")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低利率")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交额")
    TRANSACTION = Column(BIGINT, doc="成交笔数")
    AVGTRADINGPRICE = Column(DECIMAL(20, 4), doc="平均每笔交割量")
    CAPITALAMOUNT = Column(DECIMAL(20, 4), doc="资金额")
    INSTITUTION = Column(String(120), doc="发行人名称")
    PREAVGINTEREST = Column(DECIMAL(10, 6), doc="前期平均利率")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    AVGPRICEINTEREST = Column(DECIMAL(10, 6), doc="本期平均利率")
    MOVINGAVGINTEREST3M = Column(DECIMAL(10, 6), doc="3个月滑动平均利率")
    MOVINGAVGINTEREST6M = Column(DECIMAL(10, 6), doc="6个月滑动平均利率")
    MOVINGAVGINTEREST12M = Column(DECIMAL(10, 6), doc="12个月滑动平均利率")
    INTRINSICDAY = Column(DECIMAL(16, 6), doc="内含期限")
    PRINCIPAL = Column(DECIMAL(20, 4), doc="本金额")
    SETTLEMENTDAY = Column(DECIMAL(10, 4), doc="结算天数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_cfetsclosingyield(Base):

    __tablename__ = 'bond_cfetsclosingyield'

    TRADINGDATE = Column(DateTime, doc="日期")
    YEILDCURVETYPEID = Column(String(6), doc="收益率曲线类型ID")
    YEILDCURVETYPE = Column(String(40), doc="收益率曲线类型")
    CURVENAMEID = Column(String(6), doc="曲线ID")
    CURVENAME = Column(String(200), doc="曲线名称")
    TERM = Column(DECIMAL(10, 4), doc="期限")
    YIELD = Column(DECIMAL(10, 4), doc="收益率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_cfetsvaluationindex(Base):

    __tablename__ = 'bond_cfetsvaluationindex'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(10), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    TRADINGDATE = Column(DateTime, doc="估值日期")
    BONDNATUREID = Column(String(6), doc="债券类型ID")
    BONDNATURE = Column(String(100), doc="债券类型")
    VALUFULLPRICE = Column(DECIMAL(10, 4), doc="估值全价")
    VALUNETPRICE = Column(DECIMAL(10, 4), doc="估值净价")
    VALUYIELD = Column(DECIMAL(10, 4), doc="估值收益率")
    RATETYPEID = Column(String(6), doc="利率类型ID")
    RATETYPE = Column(String(40), doc="利率类型")
    VALUADJDURATION = Column(DECIMAL(10, 2), doc="估值修正久期")
    VALUCONVEXITY = Column(DECIMAL(10, 2), doc="估值凸性")
    VALUBASEPOINT = Column(DECIMAL(10, 4), doc="估值基点价值")
    VALUINTESPRDDURATION = Column(DECIMAL(10, 2), doc="估值利差久期")
    VALUINTESPRDCONVEXITY = Column(DECIMAL(10, 2), doc="估值利差凸性")
    VALURATEDURATION = Column(DECIMAL(10, 2), doc="估值利率久期")
    VALURATECONVEXITY = Column(DECIMAL(10, 2), doc="估值利率凸性")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_cfim(Base):

    __tablename__ = 'bond_cfim'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    STOCKCODE = Column(String(12), doc="股票代码")
    BEGDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    D000101 = Column(DECIMAL(20, 2), doc="净利润")
    D000117 = Column(DECIMAL(20, 2), doc="未确认的投资损失")
    D000102 = Column(DECIMAL(20, 2), doc="资产减值准备")
    D000103 = Column(DECIMAL(20, 2), doc="固定资产折旧、油气资产折耗、生产性生物资产折旧")
    D000104 = Column(DECIMAL(20, 2), doc="无形资产摊销")
    D000105 = Column(DECIMAL(20, 2), doc="长期待摊费用摊销")
    D000106 = Column(DECIMAL(20, 2), doc="处置固定资产、无形资产和其他长期资产的损失(收益以“－”号填列）")
    D000107 = Column(DECIMAL(20, 2), doc="固定资产报废损失(收益以“－”号填列）")
    D000108 = Column(DECIMAL(20, 2), doc="公允价值变动损失(收益以“－”号填列）")
    D000109 = Column(DECIMAL(20, 2), doc="财务费用(收益以“－”号填列）")
    D000110 = Column(DECIMAL(20, 2), doc="投资损失(收益以“－”号填列）")
    D000111 = Column(DECIMAL(20, 2), doc="递延所得税资产减少（增加以“－”号填列）")
    D000112 = Column(DECIMAL(20, 2), doc="递延所得税负债增加（减少以“－”号填列）")
    D000113 = Column(DECIMAL(20, 2), doc="存货的减少（增加以“－”号填列）")
    D000114 = Column(DECIMAL(20, 2), doc="经营性应收项目的减少（增加以“－”号填列）")
    D000115 = Column(DECIMAL(20, 2), doc="经营性应付项目的增加（减少以“－”号填列）")
    D000116 = Column(DECIMAL(20, 2), doc="其他")
    D0001 = Column(DECIMAL(20, 2), doc="经营活动产生的现金流量净额")
    D000201 = Column(DECIMAL(20, 2), doc="债务转为资本")
    D000202 = Column(DECIMAL(20, 2), doc="一年内到期的可转换公司债券")
    D000203 = Column(DECIMAL(20, 2), doc="融资租赁固定资产")
    D000204 = Column(DECIMAL(20, 2), doc="现金的期末余额")
    D000205 = Column(DECIMAL(20, 2), doc="现金的期初余额")
    D000206 = Column(DECIMAL(20, 2), doc="现金等价物的期末余额")
    D000207 = Column(DECIMAL(20, 2), doc="现金等价物的期初余额")
    D0002 = Column(DECIMAL(20, 2), doc="现金及现金等价物净增加额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_conversion(Base):

    __tablename__ = 'bond_conversion'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    EVENTTYPE = Column(String(40), doc="事件类型")
    EVENTTYPEID = Column(String(12), doc="事件类型ID")
    CONVERTPRICE = Column(DECIMAL(10, 2), doc="本次转股价格")
    CONVERTAMOUNT = Column(DECIMAL(20, 2), doc="本次转股金额")
    CONVERTVOLUME = Column(DECIMAL(20, 0), doc="本次转股数量")
    CONVERTRATIO = Column(DECIMAL(20, 6), doc="本次转股比例")
    TOTALAMOUNT = Column(DECIMAL(20, 2), doc="累计转股金额")
    TOTALVOLUME = Column(DECIMAL(20, 0), doc="累计转股数量")
    TOTALRATIO = Column(DECIMAL(20, 6), doc="累计转股比例")
    ISSUESHARES = Column(DECIMAL(20, 2), doc="可转债发行总额")
    REMAINAMOUNT = Column(DECIMAL(20, 2), doc="可转债剩余金额")
    TOTNUMSHARES = Column(DECIMAL(20, 0), doc="转股后总股本")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_conversionrate(Base):

    __tablename__ = 'bond_conversionrate'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    CONVERSIONRATE = Column(DECIMAL(10, 4), doc="标准券折算率")
    EXCHANGE = Column(String(100), doc="交易市场")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    APPLYSTARTDATE = Column(DateTime, primary_key=True, doc="开始适用日")
    APPLYENDDATE = Column(DateTime, doc="结束适用日")
    DECLAREDATE = Column(DateTime, doc="比例公布日")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_convertinfo(Base):

    __tablename__ = 'bond_convertinfo'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    SHORTNAME = Column(String(80), doc="债券简称")
    PYSHORTNAME = Column(String(40), doc="拼音简称")
    FULLNAME = Column(String(400), doc="债券全称")
    ENFULLNAME = Column(String(600), doc="债券英文全称")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    EXCHANGE = Column(String(120), doc="交易市场")
    BONDYEAR = Column(String(8), doc="债券年度")
    BONDTYPEID = Column(String(12), doc="品种类别ID")
    BONDTYPE = Column(String(100), doc="品种类别")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="发行机构ID")
    ISSUERFULLNAME = Column(String(200), doc="发行机构全称")
    OBJECTSTOCKCODE = Column(String(20), doc="可转换股票代码")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    CURRENCY = Column(String(40), doc="币种")
    ISSUEQUANTITY = Column(DECIMAL(10, 2), doc="实际发行量")
    ISSUEPRICE = Column(DECIMAL(7, 2), doc="发行价格")
    ISSUETYPEID = Column(String(100), doc="发行方式ID :废弃不用")
    ISSUETYPE = Column(String(400), doc="发行方式")
    BONDTERM = Column(DECIMAL(6, 2), doc="期限")
    LISTDATE = Column(DateTime, doc="上市日期")
    ISSUEDATE = Column(DateTime, doc="发行日期")
    MATURITYDATE = Column(DateTime, doc="到期日期")
    STARTDATE = Column(DateTime, doc="计息日期")
    ENDDATE = Column(DateTime, doc="止息日期")
    INTERESTPAYTYPEID = Column(String(12), doc="付息方式ID")
    INTERESTPAYTYPE = Column(String(100), doc="付息方式")
    INTERESTID = Column(String(12), doc="利率类型ID")
    INTEREST = Column(String(100), doc="利率类型")
    INTERESTTYPEID = Column(String(12), doc="计息方式ID")
    INTERESTTYPE = Column(String(100), doc="计息方式")
    PAYINTERESTFREQUENCY = Column(SMALLINT, doc="年付息次数")
    PAYINTERESTDATE = Column(String(200), doc="付息日期描述")
    INTERESTRATE = Column(DECIMAL(7, 3), doc="票面利率")
    BENCHMARKRATE = Column(DECIMAL(7, 3), doc="基准利率")
    BASEYIELDSPREAD = Column(DECIMAL(7, 3), doc="基本利差")
    PARVALUE = Column(INTEGER, doc="面值")
    CREDITRATE = Column(String(12), doc="信用等级")
    CONVERTSTARTDATE = Column(DateTime, doc="转股起始日期")
    CONVERTENDDATE = Column(DateTime, doc="转股截止日期")
    CONVERTSTARTPRICE = Column(DECIMAL(8, 4), doc="初始转股价格")
    PRICEADJUSTTERMS = Column(LONGTEXT, doc="转股价格调整条款")
    PRICEDOWNWARDADJUSTTERMS = Column(LONGTEXT, doc="转股价向下修正条款")
    ISCALL = Column(String(8), doc="可赎回性")
    CALLTERMS = Column(LONGTEXT, doc="赎回条款")
    CALLSTARTDATE = Column(DateTime, doc="可赎回起始日期")
    CALLENDDATE = Column(DateTime, doc="可赎回截止日期")
    CALLCONDITION = Column(LONGTEXT, doc="赎回条件")
    CALLPRICE = Column(LONGTEXT, doc="赎回价格")
    ISPUT = Column(String(8), doc="可回售性")
    PUTTERMS = Column(LONGTEXT, doc="回售条款")
    PUTSTARTDATE = Column(DateTime, doc="回售起始日期")
    PUTCONDITION = Column(LONGTEXT, doc="回售条件")
    PUTPRICE = Column(LONGTEXT, doc="回售价格")
    ADDITIONALPUTTERMS = Column(LONGTEXT, doc="附加回售条款")
    CREDITSTATUS = Column(LONGTEXT, doc="资信状况")
    BONDSECURITYSTEP = Column(LONGTEXT, doc="偿债措施")
    COMPENSATEINTERESTTERMS = Column(LONGTEXT, doc="补偿利息条款")
    PUTENDDATE = Column(DateTime, doc="回售截止日期")
    UPDATEID = Column(BIGINT, doc="数据ID")
    ISADJDEPOINTERATE = Column(String(20), doc="是否随存款利率调整")
    RELATIVETRANS = Column(DECIMAL(10, 2), doc="相对转股期")
    ADJUSTMENTSTARTDATE = Column(DateTime, doc="修正起始时间")
    ADJUSTMENTENDDATE = Column(DateTime, doc="修正结束时间")
    MAXTRIAMECLSTIMEINTE = Column(DECIMAL(10, 2), doc="触发修正条款最大时间区间")
    CALCUTRIAMECLSTIMEINTE = Column(DECIMAL(10, 2), doc="触发修正条款计算时间区间")
    TRIGGERRATIO = Column(DECIMAL(10, 2), doc="触发比例")
    RELATIVEREDEEMPERIOD = Column(DECIMAL(10, 2), doc="相对赎回期")
    MAXREDETRICALCUTIMEINTE = Column(DECIMAL(10, 2), doc="赎回触发计算最大时间区间")
    REDEEMTRICALCUTIMEINTE = Column(DECIMAL(10, 2), doc="赎回触发计算时间区间")
    REDEEMTRIRATIO = Column(DECIMAL(10, 2), doc="赎回触发比例")
    RELATIVERETURNPERIOD = Column(DECIMAL(10, 2), doc="相对回售期")
    ANNUALRETURNNUM = Column(String(100), doc="每年回售次数")
    MAXRETUTRICALCUTIMEINTE = Column(DECIMAL(10, 2), doc="回售触发计算最大时间区间")
    RETURNTRICALCUTIMEINTE = Column(DECIMAL(10, 2), doc="回售触发计算时间区间")
    RETURNTRIRATIO = Column(DECIMAL(10, 2), doc="回售触发比例")


class bond_convertissue(Base):

    __tablename__ = 'bond_convertissue'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(10), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    EXCHANGE = Column(String(40), doc="交易市场")
    HOLDERSMEETINGDECLAREDATE = Column(DateTime, doc="股东大会公告日")
    APPROVALDATE = Column(DateTime, doc="发审委审批通过日期")
    ISSUEDECLAREDATE = Column(DateTime, doc="发行公告日")
    PLAEQUITYREGISTERDATE = Column(DateTime, doc="老股东配售股权登记日")
    PLACINGDATE = Column(DateTime, doc="老股东配售日期")
    PLACINGPAYDATE = Column(DateTime, doc="老股东配售缴款日")
    OFFLINEISSUEDATE = Column(DateTime, doc="网下向机构投资者发行日期")
    ONLINEISSUEDATE = Column(DateTime, doc="网上发行日期")
    ONLINESCCSSRTDCLRDATE = Column(DateTime, doc="网上中签率公告日")
    ONLINESCCSSDCLRDATE = Column(DateTime, doc="网上中签结果公告日")
    ISSUERESULTDECLAREDATE = Column(DateTime, doc="发行结果公告日")
    PLACINGEXPLANATION = Column(String(4000), doc="老股东配售说明")
    PLACINGCODE = Column(String(10), doc="老股东配售代码")
    PLACINGSHORTNAME = Column(String(80), doc="老股东配售简称")
    PLACINGPRICE = Column(DECIMAL(20, 2), doc="老股东配售价格")
    PERPLACINGAMOUNT = Column(DECIMAL(20, 4), doc="每股配售额")
    PLACINGSHARES = Column(DECIMAL(20, 2), doc="向老股东配售数量")
    ONLINESUBSCRIPTIONCODE = Column(String(10), doc="网上发行申购代码")
    ONLINESUBSCRIPTIONNAME = Column(String(80), doc="网上发行申购名称")
    ONLINESUBSCRIPTIONPRICE = Column(DECIMAL(20, 2), doc="网上发行申购价格")
    ONLINEISSUESHARES1 = Column(DECIMAL(20, 2), doc="网上发行数量（不含优先配售）")
    ONLINEISSUESHARES2 = Column(DECIMAL(20, 2), doc="网下向机构投资者发行数量（不含优先配售）")
    PURCHASEAMOUNT1 = Column(DECIMAL(20, 2), doc="原非流通股股东有效申购金额")
    ALLOTTEDAMOUNT1 = Column(DECIMAL(20, 2), doc="原非流通股股东获配金额")
    PURCHASEAMOUNT2 = Column(DECIMAL(20, 2), doc="原流通股股东有效申购金额")
    AVAILABLEAMOUNT = Column(DECIMAL(20, 4), doc="原流通股股东可配售额")
    ALLOTTEDAMOUNT2 = Column(DECIMAL(20, 2), doc="原流通股股东获配金额")
    ONLINEPURCHASEHOUSEHOLDERS = Column(DECIMAL(20, 2), doc="网上有效申购户数")
    ONLINEPURCHASEAMOUNT = Column(DECIMAL(20, 2), doc="网上有效申购金额")
    ONLINEALLOTTEDAMOUNT = Column(DECIMAL(20, 2), doc="网上获配金额")
    ONLINEALLOTTEDRATIO = Column(DECIMAL(20, 4), doc="网上获配比例")
    ONLINEOVERSUBSCRIRATIO = Column(DECIMAL(20, 4), doc="网上发行超额认购倍数（不含优先配售）")
    ONLINESUCCESSRATIO = Column(DECIMAL(18, 8), doc="网上中签率")
    ISONLYONLINE = Column(String(20), doc="是否仅通过网上发行")
    OFFLINEPURCHAHSHLDRS = Column(DECIMAL(20, 2), doc="网下有效申购户数")
    OFFLINEPURCHASENUM = Column(DECIMAL(20, 2), doc="网下有效申购手数（不含优先配售）")
    OFFLINEPURCHASEAMOUNT = Column(DECIMAL(20, 2), doc="网下有效申购金额")
    OFFLINEALLOTTEDAMOUNT = Column(DECIMAL(20, 2), doc="网下获配金额")
    OFFLINESUCCESSRATIO = Column(DECIMAL(18, 8), doc="网下中签率")
    UNDERWRITINGBALANCE = Column(DECIMAL(20, 2), doc="包销余额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_convertprice(Base):

    __tablename__ = 'bond_convertprice'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    CHANGEDATE = Column(DateTime, doc="实施日期")
    CONVERTPRICE = Column(DECIMAL(10, 4), doc="转股价格")
    CONVERTPRICETYPE = Column(String(100), doc="转股价格类型")
    CONVERTPRICETYPEID = Column(String(20), doc="转股价格类型ID")
    PRICEBEFORE = Column(DECIMAL(10, 4), doc="变动前转股价格")
    ADJUSTREASON = Column(String(400), doc="变动原因")
    COMMENTS = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_crmwinfo(Base):

    __tablename__ = 'bond_crmwinfo'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    WARRANTCODE = Column(String(10), doc="凭证代码")
    WARRANTSHORTNAME = Column(String(80), doc="凭证简称")
    WARRANTFULLNAME = Column(String(200), doc="凭证全称")
    ACCEPTNOTICENUMBER = Column(String(100), doc="接受创设通知编号")
    OBJECTDEBT = Column(String(200), doc="标的债务")
    CREDITEVENT = Column(String(1000), doc="信用事件")
    SETTLEMENT = Column(String(100), doc="结算方式")
    CREDITPROTECTTERM = Column(BIGINT, doc="信用保护期限")
    CREDITPROTECTRATIO = Column(DECIMAL(10, 2), doc="信用保护费费率")
    WARRANTRECORDDATE = Column(DateTime, doc="凭证登记日")
    LISTEDDATE = Column(DateTime, doc="上市流通日")
    PLANNOTIONALPRINCIPAL = Column(DECIMAL(20, 2), doc="计划创设名义本金总额")
    ACTUALNOTIONALPRINCIPAL = Column(DECIMAL(20, 2), doc="实际创设名义本金总额")
    PARVALUE = Column(DECIMAL(10, 2), doc="面值")
    CREATIONINTITUTION = Column(String(200), doc="创设机构")
    TRUSTEEINSTITUTION = Column(String(200), doc="托管机构")
    BOOKBUILDINGDATE = Column(DateTime, doc="簿记建档日")
    CREDITPROTECTPAYDATE = Column(String(500), doc="信用保护费支付日")
    CREDITPROTECTSTARTDATE = Column(DateTime, doc="信用保护起始日")
    CREDITPROTECTENDDATE = Column(DateTime, doc="信用保护到期日")
    PAYTYPE = Column(String(100), doc="付费方式")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CURRENCY = Column(String(200), doc="币种")


class bond_currencyswapcurve(Base):

    __tablename__ = 'bond_currencyswapcurve'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    CURRESWAPCURVETYPEID = Column(String(6), doc="货币掉期曲线类型ID")
    CURRESWAPCURVETYPE = Column(String(200), doc="货币掉期曲线类型")
    TERM = Column(BIGINT, doc="期限")
    PRICETYPEID = Column(String(6), doc="价格类型ID")
    PRICETYPE = Column(String(40), doc="价格类型")
    PRICE = Column(DECIMAL(10, 2), doc="价格")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_discloseindex(Base):

    __tablename__ = 'bond_discloseindex'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    PROFITPARENTRECURRING = Column(DECIMAL(20, 2), doc="归属于上市公司股东的扣除非经常性损益的净利润")
    NONRECURRING = Column(DECIMAL(20, 2), doc="非经常性损益")
    EPSCHANGERATIO = Column(DECIMAL(20, 4), doc="基本每股收益本年比上年增减")
    EPSRECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的基本每股收益")
    DILUTEDEPSCHANGERATIO = Column(DECIMAL(20, 4), doc="稀释每股收益本年比上年增减")
    DILUTEDEPSRECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的稀释每股收益")
    ROE = Column(DECIMAL(20, 4), doc="加权平均净资产收益率")
    ROERECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的加权平均净资产收益率")
    OPERATECASHFLOWPERSHARE = Column(DECIMAL(20, 2), doc="每股经营活动产生的现金流量净额")
    NAVPARENT = Column(DECIMAL(20, 2), doc="归属于上市公司股东的每股净资产")
    DEBTTOASSETRATIO = Column(DECIMAL(20, 4), doc="资产负债率")
    DEBTTOASSETRATIOPARENT = Column(DECIMAL(20, 4), doc="母公司资产负债率")
    CURRENTRATIO = Column(DECIMAL(20, 2), doc="流动比率")
    QUICKRATIO = Column(DECIMAL(20, 2), doc="速动比率")
    RECEIVABLESTURNOVER = Column(DECIMAL(20, 4), doc="应收账款周转率")
    INVENTORYTURNOVER = Column(DECIMAL(20, 4), doc="存货周转率")
    EBITDA = Column(DECIMAL(20, 2), doc="息税折旧摊销前利润")
    INTERESTCOVERAGERATIO = Column(DECIMAL(20, 2), doc="利息保障倍数")
    INTANGIBLETOEQUITY = Column(DECIMAL(20, 4), doc="无形资产（扣除土地使用权）占净资产比例")
    ASSETTURNOVER = Column(DECIMAL(20, 4), doc="总资产周转率")
    NETCASHFLOWPERSHARE = Column(DECIMAL(20, 2), doc="每股净现金流量")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_fixreporate(Base):

    __tablename__ = 'bond_fixreporate'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(10), doc="交易代码")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    EXCHANGE = Column(String(40), doc="交易市场")
    TERM = Column(String(20), doc="期限")
    REPOFIXRATE = Column(DECIMAL(10, 4), doc="回购定盘利率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_guarantorinfo(Base):

    __tablename__ = 'bond_guarantorinfo'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SYMBOL = Column(String(10), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    EXCHANGE = Column(String(40), doc="交易市场")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    GUARANTORID = Column(DECIMAL(20, 0), doc="担保人ID")
    GUARANTORNAME = Column(String(200), doc="担保人名称")
    GUARANTORINTRODUCTION = Column(String(4000), doc="担保人简介")
    GUARANTORNATUREID = Column(String(6), doc="担保人性质ID")
    GUARANTORNATURE = Column(String(200), doc="担保人性质")
    GUARANTEETYPEID = Column(String(6), doc="担保方式ID")
    GUARANTEETYPE = Column(String(100), doc="担保方式")
    GUARANTEETERM = Column(String(400), doc="担保期限")
    GUARANTEERANGE = Column(String(400), doc="担保范围")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GUARANTEELETTERCONTENT = Column(LONGTEXT)


class bond_guarantorrating(Base):

    __tablename__ = 'bond_guarantorrating'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SYMBOL = Column(String(10), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    EXCHANGE = Column(String(40), doc="交易市场")
    GUARANTORID = Column(DECIMAL(20, 0), doc="担保人ID")
    GUARANTORNAME = Column(String(200), doc="担保人名称")
    RATINGDATE = Column(DateTime, doc="评级日期")
    RATINGINSTITUTION = Column(String(200), doc="评级机构")
    RATINGINSTITUTIONID = Column(DECIMAL(20, 0), doc="评级机构ID")
    RATING = Column(String(50), doc="信用级别")
    RATINGID = Column(String(6), doc="信用级别编码")
    RATINGPROSPECT = Column(String(100), doc="评级展望")
    RATINGPROSPECTID = Column(String(6), doc="评级展望编码")
    VIEWS = Column(String(4000), doc="评级观点")
    ANALYST = Column(String(400), doc="分析师")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_inbankod(Base):

    __tablename__ = 'bond_inbankod'

    TRADINGDATE = Column(DateTime, doc="日期标识")
    TIMETYPE = Column(String(8), doc="期限类别")
    INITIALRATE = Column(DECIMAL(18, 4), doc="期初利率")
    HIGHRATE = Column(DECIMAL(18, 4), doc="最高利率")
    LOWRATE = Column(DECIMAL(18, 4), doc="最低利率")
    FINALRATE = Column(DECIMAL(18, 4), doc="期末利率")
    FLUCTUATION = Column(DECIMAL(18, 4), doc="当日涨跌幅")
    AVGINTERESTRATE = Column(DECIMAL(18, 4), doc="加权平均利率")
    POINTRATECHANGE = Column(DECIMAL(18, 4), doc="基点升降")
    AMOUNT = Column(DECIMAL(18, 4), doc="成交金额")
    AMOUNTCHANGE = Column(DECIMAL(18, 4), doc="成交额增减")
    TICKCOUNT = Column(DECIMAL(18, 4), doc="成交笔数")
    TICKCOUNTCHANGE = Column(DECIMAL(18, 4), doc="成交笔数增减")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_info(Base):

    __tablename__ = 'bond_info'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    SHORTNAME = Column(String(80), doc="债券简称")
    PYSHORTNAME = Column(String(80), doc="拼音简称")
    FULLNAME = Column(String(200), doc="债券全称")
    ENFULLNAME = Column(String(600), doc="债券英文全称")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    EXCHANGE = Column(String(120), doc="交易市场")
    TYPEID = Column(String(12), doc="证券类别ID")
    TYPE = Column(String(100), doc="证券类别")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="发行机构ID")
    INSTITUTION = Column(String(200), doc="发行机构")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    PLANDELISTEDDATE = Column(DateTime, doc="法定退市日期")
    DELISTEDDATE = Column(DateTime, doc="摘牌日")
    CURRENCYCODE = Column(String(6), doc="币种编码")
    CURRENCY = Column(String(40), doc="币种")
    ISIN = Column(String(40), doc="ISIN代码")
    ISEXPIREID = Column(String(20), doc="目前状态ID")
    ISEXPIRE = Column(String(40), doc="目前状态")
    STATUSID = Column(String(12), doc="上市状态ID")
    STATUS = Column(String(100), doc="上市状态")
    ISSUEPRICE = Column(DECIMAL(12, 4), doc="发行价格")
    INITIALISSUESHARES = Column(DECIMAL(6, 2), doc="初始发行量")
    COMMENTS = Column(String(600), doc="备注")
    ID_0007 = Column(BIGINT, doc="巨潮记录ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INTERESTBASIS = Column(String(7), doc="计息基础")
    FIRSTPAYINTERESTDATE = Column(DateTime, doc="第一次付息日")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class bond_interestfloat(Base):

    __tablename__ = 'bond_interestfloat'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    INTERESTRATETYPEID = Column(String(12), doc="利率类型ID")
    INTERESTRATETYPE = Column(String(40), doc="利率类型")
    TERM = Column(DECIMAL(5, 2), doc="期限")
    INTERESTSTARTDATE = Column(DateTime, doc="计息开始日")
    INTERESTENDDATE = Column(DateTime, doc="计息结束日")
    INTERESTSPREAD = Column(DECIMAL(7, 3), doc="基本利差")
    BENCHMARKRATE = Column(DECIMAL(7, 3), doc="基准利率")
    BENCHMARKRATETYPE = Column(String(200), doc="基准利率类型")
    BENCHMARKRATETYPEID = Column(String(12), doc="基准利率类型ID")
    INTERESTRATE = Column(DECIMAL(7, 3), doc="实际利率")
    COMMENTS = Column(String(1000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_is(Base):

    __tablename__ = 'bond_is'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    STOCKCODE = Column(String(12), doc="股票代码")
    BEGDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    B0011 = Column(DECIMAL(20, 2), doc="营业总收入")
    B001101 = Column(DECIMAL(20, 2), doc="营业收入")
    BBD1102 = Column(DECIMAL(20, 2), doc="利息净收入")
    BBD110210 = Column(DECIMAL(20, 2), doc="利息收入")
    BBD110220 = Column(DECIMAL(20, 2), doc="利息支出")
    B0D1104 = Column(DECIMAL(20, 2), doc="手续费及佣金净收入")
    B0D110410 = Column(DECIMAL(20, 2), doc="其中：代理买卖证券业务净收入")
    B0D110420 = Column(DECIMAL(20, 2), doc="其中:证券承销业务净收入")
    B0D110430 = Column(DECIMAL(20, 2), doc="其中：受托客户资产管理业务净收入")
    B0D110440 = Column(DECIMAL(20, 2), doc="手续费及佣金收入")
    B0D110450 = Column(DECIMAL(20, 2), doc="手续费及佣金支出")
    B0I1103 = Column(DECIMAL(20, 2), doc="已赚保费")
    B0I110310 = Column(DECIMAL(20, 2), doc="保险业务收入")
    B0I11031010 = Column(DECIMAL(20, 2), doc="其中：分保费收入")
    B0I110320 = Column(DECIMAL(20, 2), doc="减：分出保费")
    B0I110330 = Column(DECIMAL(20, 2), doc="减：提取未到期责任准备金")
    B0F1105 = Column(DECIMAL(20, 2), doc="其他业务收入")
    B0012 = Column(DECIMAL(20, 2), doc="营业总成本")
    B001201 = Column(DECIMAL(20, 2), doc="营业成本")
    B0I1202 = Column(DECIMAL(20, 2), doc="退保金")
    B0I1203 = Column(DECIMAL(20, 2), doc="赔付支出净额")
    B0I120310 = Column(DECIMAL(20, 2), doc="赔付支出")
    B0I120320 = Column(DECIMAL(20, 2), doc="减：摊回赔付支出")
    B0I1204 = Column(DECIMAL(20, 2), doc="提取保险责任准备金净额")
    B0I120410 = Column(DECIMAL(20, 2), doc="提取保险责任准备金")
    B0I120420 = Column(DECIMAL(20, 2), doc="减：摊回保险责任准备金")
    B0I1205 = Column(DECIMAL(20, 2), doc="保单红利支出")
    B0I1206 = Column(DECIMAL(20, 2), doc="分保费用")
    B0I1214 = Column(DECIMAL(20, 2), doc="保险业务手续费及佣金支出")
    B001207 = Column(DECIMAL(20, 2), doc="营业税金及附加")
    B0F1208 = Column(DECIMAL(20, 2), doc="业务及管理费")
    B0I1215 = Column(DECIMAL(20, 2), doc="减：摊回分保费用")
    B001209 = Column(DECIMAL(20, 2), doc="销售费用")
    B001210 = Column(DECIMAL(20, 2), doc="管理费用")
    B001211 = Column(DECIMAL(20, 2), doc="财务费用")
    B001212 = Column(DECIMAL(20, 2), doc="资产减值损失")
    B0F1213 = Column(DECIMAL(20, 2), doc="其他业务成本")
    B001301 = Column(DECIMAL(20, 2), doc="公允价值变动收益")
    B001302 = Column(DECIMAL(20, 2), doc="投资收益")
    B00130210 = Column(DECIMAL(20, 2), doc="其中：对联营企业和合营企业的投资收益")
    B001303 = Column(DECIMAL(20, 2), doc="汇兑收益")
    B001304 = Column(DECIMAL(20, 2), doc="其他业务利润")
    B0013 = Column(DECIMAL(20, 2), doc="营业利润")
    B0014 = Column(DECIMAL(20, 2), doc="营业外收入")
    B0015 = Column(DECIMAL(20, 2), doc="营业外支出")
    B00150010 = Column(DECIMAL(20, 2), doc="其中：非流动资产处置净损益")
    B001 = Column(DECIMAL(20, 2), doc="利润总额")
    B0021 = Column(DECIMAL(20, 2), doc="所得税费用")
    B0022 = Column(DECIMAL(20, 2), doc="未确认的投资损失")
    B0023 = Column(DECIMAL(20, 2), doc="影响净利润的其他项目")
    B002 = Column(DECIMAL(20, 2), doc="净利润")
    B0024 = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润")
    B0025 = Column(DECIMAL(20, 2), doc="少数股东损益")
    B003 = Column(DECIMAL(20, 4), doc="基本每股收益")
    B004 = Column(DECIMAL(20, 4), doc="稀释每股收益")
    B005 = Column(DECIMAL(20, 2), doc="其他综合收益(损失)")
    B006 = Column(DECIMAL(20, 2), doc="综合收益总额")
    B0061 = Column(DECIMAL(20, 2), doc="归属于母公司所有者的综合收益总额")
    B0062 = Column(DECIMAL(20, 2), doc="归属于少数股东的综合收益总额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_issuecost(Base):

    __tablename__ = 'bond_issuecost'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(10), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    EXCHANGE = Column(String(40), doc="交易市场")
    ISSUEDATE = Column(DateTime, doc="发行日期")
    TOTALISSUEEXPENSE = Column(DECIMAL(20, 2), doc="发行费用合计")
    ISSUERATIO = Column(DECIMAL(10, 2), doc="发行费率")
    UNDESPOFEE = Column(DECIMAL(20, 2), doc="承销保荐费用")
    ACCOUNTANTFEE = Column(DECIMAL(20, 2), doc="会计师费用")
    LAWYERFEE = Column(DECIMAL(20, 2), doc="律师费用")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CURRENCY = Column(String(200), doc="币种")


class bond_issuer(Base):

    __tablename__ = 'bond_issuer'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="发行人ID")
    INSTITUTIONNAME = Column(String(200), doc="发行人名称")
    INSTITUTIONNAME_EN = Column(String(600), doc="发行人英文名称")
    SHORTNAME = Column(String(100), doc="发行人简称")
    SHORTNAME_EN = Column(String(300), doc="发行人英文简称")
    ISLISTED = Column(String(12), doc="是否上市公司")
    ISSUERTYPEID = Column(String(20), doc="机构分类ID")
    ISSUERTYPE = Column(String(100), doc="机构分类")
    ISSUERNATUREID = Column(String(20), doc="发行人性质ID")
    ISSUERNATURE = Column(String(100), doc="发行人性质")
    LEGALREPRESENTATIVE = Column(String(200), doc="法人代表")
    GENERALMANAGER = Column(String(100), doc="总经理")
    SECRETARY = Column(String(100), doc="董事会秘书")
    SECURITYCONSULTANT = Column(String(200), doc="证券事务代表")
    FIRSTTIMEREGISTER = Column(String(400), doc="首次注册登记地点")
    REGISTERADDRESS = Column(String(400), doc="注册地址")
    PROVINCE = Column(String(100), doc="注册地所在省份")
    PROVINCECODE = Column(String(20), doc="注册地所在省份编码")
    REGISTERADDRESSZIPCODE = Column(String(20), doc="注册地邮编")
    OFFICEADDRESS = Column(String(400), doc="办公地址")
    ZIPCODE = Column(String(20), doc="办公地邮编")
    REGISTERCAPITAL = Column(BIGINT, doc="注册资本")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    CURRENCY = Column(String(100), doc="币种")
    ESTABLISHDATE = Column(DateTime, doc="成立日期")
    BUSINESSSCOPEMAIN = Column(String(4000), doc="经营范围-主营")
    BUSINESSSCOPEPART = Column(String(4000), doc="经营范围-兼营")
    PHONE = Column(String(100), doc="联系电话")
    FAX = Column(String(100), doc="传真")
    EMAIL = Column(String(200), doc="电子邮箱")
    WEBSITE = Column(String(400), doc="网址")
    INTRODUCTION = Column(String(4000), doc="公司简介")
    DISCLOSEWEBSITE = Column(String(200), doc="信息披露网址")
    DISCLOSEPAPER = Column(String(200), doc="信息披露报纸")
    ASHARESSHORTNAME = Column(String(20), doc="已发行A股简称")
    ASHARESSYMBOL = Column(String(20), doc="已发行A股代码")
    BSHARESSHORTNAME = Column(String(20), doc="已发行B股简称")
    BSHARESSYMBOL = Column(String(20), doc="已发行B股代码")
    COMMENTS = Column(String(4000), doc="备注")
    ID_0117 = Column(BIGINT, doc="巨潮记录ID")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_issueregiinfo(Base):

    __tablename__ = 'bond_issueregiinfo'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="发行机构ID")
    INSTITUTIONNAME = Column(String(200), doc="发行机构")
    BONDNATUREID = Column(String(6), doc="债券类型ID")
    BONDNATURE = Column(String(100), doc="债券类型")
    REGISTERFILENUM = Column(String(200), doc="注册文件编号")
    MEETINGDATE = Column(DateTime, doc="注册会议召开日期")
    INITIALREGISTCAPITAL = Column(DECIMAL(20, 2), doc="初始注册金额")
    REGISTCAPITAL_AFTER = Column(DECIMAL(20, 2), doc="变更后注册金额")
    CHANGEDATE = Column(DateTime, doc="变更日期")
    INSCRIPTIONDATE = Column(DateTime, doc="注册通知书落款日期")
    VALIDITYPERIOD = Column(String(200), doc="有效期限")
    ISSTAGING = Column(String(20), doc="是否可分期")
    LEADUNDERWRITER = Column(String(2000), doc="主承销商")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CURRENCY = Column(String(200), doc="币种")


class bond_lastquotationmonth(Base):

    __tablename__ = 'bond_lastquotationmonth'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGMONTH = Column(String(14), primary_key=True, doc="交易月份")
    FILLING = Column(SMALLINT, doc="填充标识")
    OPENPRICE = Column(DECIMAL(10, 3), doc="月开盘价")
    OPENDATE = Column(DateTime, doc="月开盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="月收盘价")
    CLOSEDATE = Column(DateTime, doc="月收盘日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="上月收盘价")
    PRVCLOSEDATE = Column(DateTime, doc="上月收盘日")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="月最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="月最低价")
    HIGHDATE = Column(DateTime, doc="月最高价日")
    LOWDATE = Column(DateTime, doc="月最低价日")
    HIGHVOLUME = Column(BIGINT, doc="月最高成交量")
    LOWVOLUME = Column(BIGINT, doc="月最低成交量")
    HIGHAMOUNT = Column(DECIMAL(20, 3), doc="月最高成交额")
    LOWAMOUNT = Column(DECIMAL(20, 3), doc="月最低成交额")
    VOLUME = Column(DECIMAL(15, 4), doc="月总成交数量")
    AMOUNT = Column(DECIMAL(20, 3), doc="月总成交金额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="月均价")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 3), doc="月最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 3), doc="月最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="月最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="月最低收盘价日")
    CHANGE = Column(DECIMAL(10, 3), doc="月涨跌")
    CHANGERATIO = Column(DECIMAL(10, 5), doc="月涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="月振幅")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="月换手率")
    AVERAGETURNOVERRATE = Column(DECIMAL(16, 6), doc="月平均换手率")
    TRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_lastquotationweek(Base):

    __tablename__ = 'bond_lastquotationweek'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(20), doc="交易周份")
    FILLING = Column(SMALLINT, doc="填充标识")
    LATESTTRADINGDATE = Column(DateTime, doc="周前一交易日")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="周前收盘价")
    OPENPRICE = Column(DECIMAL(10, 3), doc="周开盘价")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="周最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="周最低价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    LOWDATE = Column(DateTime, doc="周最低价日")
    HIGHVOLUME = Column(BIGINT, doc="周最高成交量")
    LOWVOLUME = Column(BIGINT, doc="周最低成交量")
    HIGHAMOUNT = Column(DECIMAL(20, 3), doc="周最高成交额")
    LOWAMOUNT = Column(DECIMAL(20, 3), doc="周最低成交额")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="周收盘价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 3), doc="周最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 3), doc="周最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    CHANGE = Column(DECIMAL(10, 3), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(16, 6), doc="周涨跌幅")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="周换手率")
    AVERAGETURNOVERRATE = Column(DECIMAL(16, 6), doc="周平均换手率")
    VOLUME = Column(DECIMAL(15, 4), doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 3), doc="周成交额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="周均价")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="周振幅")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_lastquotationyear(Base):

    __tablename__ = 'bond_lastquotationyear'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), doc="交易年份")
    FILLING = Column(SMALLINT, doc="填充标识")
    OPENPRICE = Column(DECIMAL(10, 3), doc="年开盘价")
    OPENDATE = Column(DateTime, doc="年开盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="年收盘价")
    CLOSEDATE = Column(DateTime, doc="年收盘日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="上年收盘价")
    PRVCLOSEDATE = Column(DateTime, doc="上年收盘日")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="年最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="年最低价")
    HIGHDATE = Column(DateTime, doc="年最高价日")
    LOWDATE = Column(DateTime, doc="年最低价日")
    HIGHVOLUME = Column(BIGINT, doc="年最高成交量")
    LOWVOLUME = Column(BIGINT, doc="年最低成交量")
    HIGHAMOUNT = Column(DECIMAL(20, 3), doc="年最高成交额")
    LOWAMOUNT = Column(DECIMAL(20, 3), doc="年最低成交额")
    VOLUME = Column(DECIMAL(15, 4), doc="年总成交数量")
    AMOUNT = Column(DECIMAL(20, 3), doc="年总成交金额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="年均价")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 3), doc="年最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 3), doc="年最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="年最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="年最低收盘价日")
    CHANGE = Column(DECIMAL(10, 3), doc="年涨跌")
    CHANGERATIO = Column(DECIMAL(10, 5), doc="年涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="年振幅")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="年换手率")
    AVERAGETURNOVERRATE = Column(DECIMAL(16, 6), doc="年平均换手率")
    TRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_mkttrade(Base):

    __tablename__ = 'bond_mkttrade'

    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    VOLUME = Column(BIGINT, doc="成交笔数")
    VOLUMECHANGE = Column(BIGINT, doc="成交笔数增减")
    AMOUNT = Column(DECIMAL(12, 4), doc="成交额")
    AMOUNTCHANGE = Column(DECIMAL(12, 4), doc="成交额增减")
    AVAILABLESPECIES = Column(INTEGER, doc="可交易债券种数")
    TRADINGSPECIES = Column(INTEGER, doc="成交债券种数")
    MEMBER = Column(INTEGER, doc="参与成员数")
    MEMBERCHANGE = Column(BIGINT, doc="参与家数增减")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_nafmiipricntrlcrv(Base):

    __tablename__ = 'bond_nafmiipricntrlcrv'

    TRADINGDATE = Column(DateTime, doc="日期")
    RATINGTYPEID = Column(String(6), doc="评级类型ID")
    RATINGTYPE = Column(String(40), doc="评级类型")
    TERM = Column(BIGINT, doc="期限")
    RATE = Column(DECIMAL(10, 2), doc="利率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_otc_quotationhis(Base):

    __tablename__ = 'bond_otc_quotationhis'

    SYMBOL = Column(String(20), doc="债券代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SHORTNAME = Column(String(80), doc="债券简称")
    QOUTEDATE = Column(DateTime, doc="报价日期")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    BIDNETPRICE = Column(DECIMAL(10, 3), doc="银行买入净价")
    ASKNETPRICE = Column(DECIMAL(10, 3), doc="银行卖出净价")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    BIDFULLPRICE = Column(DECIMAL(10, 3), doc="银行买入全价")
    ASKFULLPRICE = Column(DECIMAL(10, 3), doc="银行卖出全价")
    PREBIDFULLPRICE = Column(DECIMAL(10, 3), doc="前银行买入全价")
    BIDCHANGE = Column(DECIMAL(10, 3), doc="银行买入全价涨跌")
    BIDCHANGERATIO = Column(DECIMAL(10, 4), doc="银行买入全价涨跌幅")
    PREASKFULLPRICE = Column(DECIMAL(10, 3), doc="前银行卖出全价")
    ASKCHANGE = Column(DECIMAL(10, 3), doc="银行卖出全价涨跌")
    ASKCHANGERATIO = Column(DECIMAL(10, 4), doc="银行卖出全价涨跌幅")
    REMAININGYEARS = Column(DECIMAL(10, 4), doc="剩余期限")
    DAYAMOUNTBAYIN = Column(DECIMAL(12, 4), doc="日买入额")
    YEARAMOUNTBAYIN = Column(DECIMAL(12, 4), doc="年度累计买入额")
    DAYAMOUNTSELLOUT = Column(DECIMAL(12, 4), doc="日卖出额")
    YEARAMOUNTSELLOUT = Column(DECIMAL(12, 4), doc="年度累计卖出额")
    REFERENCEYTM = Column(DECIMAL(10, 4), doc="到期收益率(参考)")
    BONDTYPEID = Column(String(16), doc="债券类别ID")
    BONDTYPE = Column(String(160), doc="债券类别")
    QUOTEBANK = Column(String(80), doc="报价银行")
    INSTITUTIONID = Column(String(24), doc="报价银行ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_otc_quotationoptimal(Base):

    __tablename__ = 'bond_otc_quotationoptimal'

    SYMBOL = Column(String(20), doc="债券代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SHORTNAME = Column(String(80), doc="债券简称")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    BAYFULLPRICE = Column(DECIMAL(10, 3), doc="投资者买入价格")
    SELLFULLPRICE = Column(DECIMAL(10, 3), doc="投资者卖出价格(全价)")
    PREBAYFULLPRICE = Column(DECIMAL(10, 3), doc="前投资者买入价格")
    PRESELLFULLPRICE = Column(DECIMAL(10, 3), doc="前投资者卖出价格(全价)")
    CHANGE = Column(DECIMAL(10, 3), doc="投资者买入价格涨跌")
    CHANGERATIO = Column(DECIMAL(10, 4), doc="投资者买入价格涨跌幅")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    REMAININGYEARS = Column(DECIMAL(10, 4), doc="剩余期限")
    REFERENCEYTM = Column(DECIMAL(10, 4), doc="到期收益率(参考)")
    QUOTEBANK = Column(String(80), doc="报价银行")
    INSTITUTIONID = Column(String(24), doc="报价银行ID")
    QOUTEDATE = Column(DateTime, doc="报价日期")
    BONDTYPEID = Column(String(16), doc="债券类别ID")
    BONDTYPE = Column(String(160), doc="债券类别")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_payment(Base):

    __tablename__ = 'bond_payment'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    BONDFORMID = Column(String(20), doc="债券形式ID")
    BONDFORM = Column(String(120), doc="债券形式")
    INTERESTRATE = Column(DECIMAL(7, 3), doc="债券利率")
    INTERESTRATETYPEID = Column(String(12), doc="利率类型ID")
    INTERESTRATETYPE = Column(String(40), doc="利率类型")
    INTERESTSTARTDATE = Column(DateTime, doc="本年度计息开始日")
    INTERESTENDDATE = Column(DateTime, doc="本年度计息结束日")
    RIGHTDATE = Column(DateTime, doc="债权登记日")
    PAYINTERESTSTARTDATE = Column(DateTime, doc="集中付息开始日")
    PAYINTERESTENDDATE = Column(DateTime, doc="集中付息终止日")
    EXDIVIDENDTRADINGDATE = Column(DateTime, doc="除息交易日")
    ISTAXFREE = Column(String(4), doc="是否免税")
    INTERESTTAXRATE = Column(DECIMAL(7, 3), doc="利息税率")
    ID_0075 = Column(BIGINT, doc="巨潮记录ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_pretrdinfo(Base):

    __tablename__ = 'bond_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    ISSUEPRICE = Column(DECIMAL(7, 2), doc="发行价格")
    PARVALUERATE = Column(DECIMAL(7, 3), doc="票面利率")
    INTERESTSTARTDATE = Column(DateTime, doc="计息日期")
    LATESTCLOSE = Column(DECIMAL(20, 3), doc="前收盘价格")
    INTERESTDAYS = Column(INTEGER, doc="计息天数")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    MINTICKSIZE = Column(DECIMAL(10, 3), doc="价格档位")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    ISDIVIDEND = Column(SMALLINT, doc="是否付息日")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_pretrdinfohistory(Base):

    __tablename__ = 'bond_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    ISSUEPRICE = Column(DECIMAL(7, 2), doc="发行价格")
    PARVALUERATE = Column(DECIMAL(7, 3), doc="票面利率")
    INTERESTSTARTDATE = Column(DateTime, doc="计息日期")
    LATESTCLOSE = Column(DECIMAL(20, 3), doc="前收盘价格")
    INTERESTDAYS = Column(INTEGER, doc="计息天数")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    MINTICKSIZE = Column(DECIMAL(10, 3), doc="价格档位")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    ISDIVIDEND = Column(SMALLINT, doc="是否付息日")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_quotation(Base):

    __tablename__ = 'bond_quotation'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    MINTICKSIZE = Column(DECIMAL(10, 3), doc="价格档位")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 3), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="最低价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前一交易日收盘价")
    AMOUNT = Column(DECIMAL(20, 3), doc="成交额")
    VOLUME = Column(BIGINT, doc="成交量")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="换手率")
    CHANGE = Column(DECIMAL(10, 3), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(16, 6), doc="涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="振幅")
    INTERESTDAYS = Column(INTEGER, doc="计息天数")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    GROSSPRICE = Column(DECIMAL(10, 3), doc="收盘全价")
    REMAININGYEARS = Column(DECIMAL(8, 3), doc="剩余年限")
    STOCKPRICE = Column(DECIMAL(10, 3), doc="正股价格")
    STOCKCHANGERATIO = Column(DECIMAL(16, 6), doc="正股涨跌幅")
    CONVERSIONPRICE = Column(DECIMAL(10, 3), doc="转股价格")
    CONVERSIONRATIO = Column(DECIMAL(20, 6), doc="转股比例")
    CONVERSIONVALUE = Column(DECIMAL(20, 6), doc="转换价值")
    CONVERTIBLEPREMIUMRATE = Column(DECIMAL(20, 6), doc="转股溢价率")
    CHANGETOISSUEPRICE = Column(DECIMAL(10, 3), doc="相对发行价涨跌")
    CHANGERATIOTOISSUE = Column(DECIMAL(16, 6), doc="相对发行价涨跌幅")
    AVGPRICE = Column(DECIMAL(10, 3), doc="均价")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    FILLING = Column(SMALLINT, doc="填充标识")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_quotationderivative(Base):

    __tablename__ = 'bond_quotationderivative'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    INTEREST = Column(DECIMAL(16, 6), doc="年利息")
    YEARPAYTIME = Column(DECIMAL(6, 2), doc="年付息次数")
    REMAININGYEARS = Column(DECIMAL(8, 3), doc="剩余年限")
    ISSUEPRICE = Column(DECIMAL(12, 4), doc="发行价格")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    GROSSPRICE = Column(DECIMAL(10, 3), doc="收盘全价")
    FIRSTGROSSPRICE = Column(DECIMAL(10, 3), doc="上市首日收盘价全价")
    ISSUEYIELDTOMATURITY = Column(DECIMAL(20, 6), doc="发行到期收益率")
    GROSSYTM = Column(DECIMAL(20, 6), doc="日收盘全价到期收益率")
    CLOSINGYTM = Column(DECIMAL(20, 6), doc="日收盘到期收益率")
    FIRSTDAYYTM = Column(DECIMAL(20, 6), doc="上市首日到期收益率")
    DURATION = Column(DECIMAL(20, 6), doc="久期")
    ADJUSTMENTDURATION = Column(DECIMAL(20, 6), doc="修正久期")
    CONVEXITY = Column(DECIMAL(20, 6), doc="凸度")
    CURRENTYIELD = Column(DECIMAL(20, 6), doc="现期收益率")
    INTERESTRETURNS = Column(DECIMAL(20, 6), doc="利息回报率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_quotationlatest(Base):

    __tablename__ = 'bond_quotationlatest'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    MINTICKSIZE = Column(DECIMAL(10, 3), doc="价格档位")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 3), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="最低价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前一交易日收盘价")
    AMOUNT = Column(DECIMAL(20, 3), doc="成交额")
    VOLUME = Column(BIGINT, doc="成交量")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="换手率")
    CHANGE = Column(DECIMAL(10, 3), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(16, 6), doc="涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="振幅")
    INTERESTDAYS = Column(INTEGER, doc="计息天数")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    GROSSPRICE = Column(DECIMAL(10, 3), doc="收盘全价")
    REMAININGYEARS = Column(DECIMAL(8, 3), doc="剩余年限")
    STOCKPRICE = Column(DECIMAL(10, 3), doc="正股价格")
    STOCKCHANGERATIO = Column(DECIMAL(16, 6), doc="正股涨跌幅")
    CONVERSIONPRICE = Column(DECIMAL(10, 3), doc="转股价格")
    CONVERSIONRATIO = Column(DECIMAL(20, 6), doc="转股比例")
    CONVERSIONVALUE = Column(DECIMAL(20, 6), doc="转换价值")
    CONVERTIBLEPREMIUMRATE = Column(DECIMAL(20, 6), doc="转股溢价率")
    CHANGETOISSUEPRICE = Column(DECIMAL(10, 3), doc="相对发行价涨跌")
    CHANGERATIOTOISSUE = Column(DECIMAL(16, 6), doc="相对发行价涨跌幅")
    AVGPRICE = Column(DECIMAL(10, 3), doc="均价")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_quotationmonth(Base):

    __tablename__ = 'bond_quotationmonth'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGMONTH = Column(String(14), doc="交易月份")
    OPENPRICE = Column(DECIMAL(10, 3), doc="月开盘价")
    OPENDATE = Column(DateTime, doc="月开盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="月收盘价")
    CLOSEDATE = Column(DateTime, doc="月收盘日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="上月收盘价")
    PRVCLOSEDATE = Column(DateTime, doc="上月收盘日")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="月最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="月最低价")
    HIGHDATE = Column(DateTime, doc="月最高价日")
    LOWDATE = Column(DateTime, doc="月最低价日")
    HIGHVOLUME = Column(BIGINT, doc="月最高成交量")
    LOWVOLUME = Column(BIGINT, doc="月最低成交量")
    HIGHAMOUNT = Column(DECIMAL(20, 3), doc="月最高成交额")
    LOWAMOUNT = Column(DECIMAL(20, 3), doc="月最低成交额")
    VOLUME = Column(DECIMAL(15, 4), doc="月总成交数量")
    AMOUNT = Column(DECIMAL(20, 3), doc="月总成交金额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="月均价")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 3), doc="月最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 3), doc="月最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="月最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="月最低收盘价日")
    CHANGE = Column(DECIMAL(10, 3), doc="月涨跌")
    CHANGERATIO = Column(DECIMAL(10, 5), doc="月涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="月振幅")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="月换手率")
    AVERAGETURNOVERRATE = Column(DECIMAL(16, 6), doc="月平均换手率")
    TRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    FILLING = Column(SMALLINT, doc="填充标识")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_quotations(Base):

    __tablename__ = 'bond_quotations'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="证券代码")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    SHORTNAME = Column(String(80), doc="债券简称")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 3), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="最低价")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 3), doc="成交金额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="均价")
    CHANGE = Column(DECIMAL(10, 3), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(16, 6), doc="涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="振幅")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_quotationweek(Base):

    __tablename__ = 'bond_quotationweek'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(14), doc="交易周份")
    LATESTTRADINGDATE = Column(DateTime, doc="周前一交易日")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="周前收盘价")
    OPENPRICE = Column(DECIMAL(10, 3), doc="周开盘价")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="周最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="周最低价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    LOWDATE = Column(DateTime, doc="周最低价日")
    HIGHVOLUME = Column(BIGINT, doc="周最高成交量")
    LOWVOLUME = Column(BIGINT, doc="周最低成交量")
    HIGHAMOUNT = Column(DECIMAL(20, 3), doc="周最高成交额")
    LOWAMOUNT = Column(DECIMAL(20, 3), doc="周最低成交额")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="周收盘价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 3), doc="周最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 3), doc="周最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    AVERAGECLOSEPRICE = Column(DECIMAL(10, 3), doc="周均收盘价")
    CHANGE = Column(DECIMAL(10, 3), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(16, 6), doc="周涨跌幅")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="周换手率")
    AVERAGETURNOVERRATE = Column(DECIMAL(16, 6), doc="周平均换手率")
    VOLUME = Column(DECIMAL(15, 4), doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 3), doc="周成交额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="周均价")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="周振幅")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    FILLING = Column(SMALLINT, doc="填充标识")
    UPDATEID = Column(BIGINT, primary_key=True)


class bond_quotationyear(Base):

    __tablename__ = 'bond_quotationyear'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    BONDNATUREID = Column(String(12), doc="债券类型ID")
    EXCHANGECODE = Column(String(20), doc="交易市场编码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), doc="交易年份")
    OPENPRICE = Column(DECIMAL(10, 3), doc="年开盘价")
    OPENDATE = Column(DateTime, doc="年开盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="年收盘价")
    CLOSEDATE = Column(DateTime, doc="年收盘日期")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="上年收盘价")
    PRVCLOSEDATE = Column(DateTime, doc="上年收盘日")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="年最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="年最低价")
    HIGHDATE = Column(DateTime, doc="年最高价日")
    LOWDATE = Column(DateTime, doc="年最低价日")
    HIGHVOLUME = Column(BIGINT, doc="年最高成交量")
    LOWVOLUME = Column(BIGINT, doc="年最低成交量")
    HIGHAMOUNT = Column(DECIMAL(20, 3), doc="年最高成交额")
    LOWAMOUNT = Column(DECIMAL(20, 3), doc="年最低成交额")
    VOLUME = Column(DECIMAL(15, 4), doc="年总成交数量")
    AMOUNT = Column(DECIMAL(20, 3), doc="年总成交金额")
    AVGPRICE = Column(DECIMAL(10, 3), doc="年均价")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 3), doc="年最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 3), doc="年最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="年最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="年最低收盘价日")
    CHANGE = Column(DECIMAL(10, 3), doc="年涨跌")
    CHANGERATIO = Column(DECIMAL(10, 5), doc="年涨跌幅")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="年振幅")
    TURNOVERRATE = Column(DECIMAL(16, 6), doc="年换手率")
    AVERAGETURNOVERRATE = Column(DECIMAL(16, 6), doc="年平均换手率")
    TRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    FILLING = Column(SMALLINT, doc="填充标识")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_ratetype(Base):

    __tablename__ = 'bond_ratetype'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    RATETYPEID = Column(String(20), doc="计息方式编码")
    VOLUME = Column(BIGINT, doc="成交笔数")
    VOLUMECHANGE = Column(BIGINT, doc="成交笔数增减")
    AMOUNT = Column(DECIMAL(12, 4), doc="成交额")
    AMOUNTCHANGE = Column(DECIMAL(12, 4), doc="成交额增减")
    AMOUNTRATIO = Column(DECIMAL(8, 4), doc="占总成交比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_rating(Base):

    __tablename__ = 'bond_rating'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    RATINGDATE = Column(DateTime, doc="评级日期")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    INSTITUTIONNAME = Column(String(200), doc="发债机构")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="发债机构ID")
    RATINGINSTITUTION = Column(String(200), doc="评级机构")
    RATINGINSTITUTIONID = Column(DECIMAL(20, 0), doc="评级机构ID")
    SHORTTERMRATING = Column(String(100), doc="债项信用级别")
    SHORTTERMRATINGID = Column(String(60), doc="标准债项信用级别编码")
    SHORTTERMRATINGSTANDARD = Column(String(100), doc="标准债项信用级别")
    LONGTERMRATING = Column(String(100), doc="发债主体信用级别")
    LONGTERMRATINGID = Column(String(60), doc="标准发债主体信用级别编码")
    LONGTERMRATINGSTANDARD = Column(String(100), doc="标准发债主体信用级别")
    RATINGPROSPECT = Column(String(100), doc="评级展望")
    RATINGPROSPECTID = Column(String(60), doc="评级展望编码")
    VIEWS = Column(String(4000), doc="评级观点")
    ANALYST = Column(String(400), doc="分析员")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    SYMBOL = Column(String(20), doc="债券代码")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    BONDRATETYPE = Column(SMALLINT, doc="债项评级类型")
    RATINGWATCH = Column(String(100), doc="评级观察")
    RATINGWATCHID = Column(String(30), doc="评级观察编码")


class bond_redemption(Base):

    __tablename__ = 'bond_redemption'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="债券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    STARTDATEK = Column(DateTime, doc="兑付起始日")
    ENDDATE = Column(DateTime, doc="兑付终止日")
    REGISTRATIONDATE = Column(DateTime, doc="兑付登记日")
    REPAYTYPEID = Column(String(20), doc="偿还方式ID")
    REPAYTYPE = Column(String(100), doc="偿还方式")
    SUMPRINCIPALINTEREST = Column(DECIMAL(18, 8), doc="兑付本息和(每百元)")
    TOTAL = Column(DECIMAL(18, 8), doc="兑付总额")
    COMMISSIONRATE = Column(DECIMAL(18, 8), doc="兑付手续费率")
    ID_0075 = Column(BIGINT, doc="巨潮记录ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_repayterm(Base):

    __tablename__ = 'bond_repayterm'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    REPAYTERMID = Column(String(20), doc="待偿期编码")
    VOLUME = Column(BIGINT, doc="成交笔数")
    VOLUMECHANGE = Column(BIGINT, doc="成交笔数增减")
    AMOUNT = Column(DECIMAL(12, 4), doc="成交额")
    AMOUNTCHANGE = Column(DECIMAL(12, 4), doc="成交额增减")
    AMOUNTRATIO = Column(DECIMAL(8, 4), doc="占总成交比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_repototal(Base):

    __tablename__ = 'bond_repototal'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGTYPEID = Column(String(20), doc="交易类型编码")
    AVGINTERESTRATE = Column(DECIMAL(8, 4), doc="加权平均利率")
    BASISPOINTCHANGE = Column(DECIMAL(8, 4), doc="基点升降")
    AMOUNT = Column(DECIMAL(12, 4), doc="成交额")
    AMOUNTCHANGE = Column(DECIMAL(12, 4), doc="成交额增减")
    VOLUME = Column(BIGINT, doc="成交笔数")
    VOLUMECHANGE = Column(BIGINT, doc="成交笔数增减")
    MEMBER = Column(BIGINT, doc="参与家数")
    MEMBERCHANGE = Column(BIGINT, doc="参与家数增减")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_repovariety(Base):

    __tablename__ = 'bond_repovariety'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRANSACTIONTYPEID = Column(String(12), doc="交易类型ID")
    SYMBOL = Column(String(20), doc="交易代码")
    BEGININTERESTRATE = Column(DECIMAL(9, 4), doc="期初利率")
    HIGHINTERESTRATE = Column(DECIMAL(9, 4), doc="最高利率")
    LOWINTERESTRATE = Column(DECIMAL(9, 4), doc="最低利率")
    ENDINTERESTRATE = Column(DECIMAL(9, 4), doc="期末利率")
    AVGINTERESTRATE = Column(DECIMAL(9, 4), doc="加权平均利率")
    BASISPOINTCHANGE = Column(DECIMAL(9, 4), doc="基点升降")
    AMOUNT = Column(DECIMAL(9, 4), doc="成交额")
    AMOUNTCHANGE = Column(DECIMAL(9, 4), doc="成交额增减")
    VOLUME = Column(INTEGER, doc="成交笔数")
    RATIOCHANGE = Column(DECIMAL(9, 4), doc="当日涨跌幅")
    VOLUMECHANGE = Column(INTEGER, doc="成交笔数增减")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_shcvaluation(Base):

    __tablename__ = 'bond_shcvaluation'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(10), doc="债券代码")
    SHORTNAME = Column(String(100), doc="债券简称")
    TRADINGDATE = Column(DateTime, doc="估值日期")
    EXCHANGECODE = Column(String(10), doc="交易市场编码")
    EXCHANGE = Column(String(40), doc="交易市场")
    REMAINPERIOD = Column(DECIMAL(10, 4), doc="待偿期")
    DAILYVALUFULLPRICE = Column(DECIMAL(30, 4), doc="日间估价全价")
    DAILYACCRUEDINTEREST = Column(DECIMAL(30, 4), doc="日间应计利息")
    VALUNETPRICE = Column(DECIMAL(30, 4), doc="估价净价")
    VALUYIELD = Column(DECIMAL(30, 4), doc="估价收益率")
    VALUADJDURATION = Column(DECIMAL(30, 4), doc="估价修正久期")
    VALUCONVEXITY = Column(DECIMAL(30, 4), doc="估价凸性")
    VALUBASEPOINT = Column(DECIMAL(30, 4), doc="估价基点价值")
    VALUINTESPRDDURATION = Column(DECIMAL(30, 4), doc="估价利差久期")
    VALUINTESPRDCONVEXITY = Column(DECIMAL(30, 4), doc="估价利差凸性")
    ACTFULLPRICE = Column(DECIMAL(30, 4), doc="真实全价")
    ACTNETPRICE = Column(DECIMAL(30, 4), doc="真实净价")
    ACTYIELD = Column(DECIMAL(30, 4), doc="真实收益率")
    ACTADJDURATION = Column(DECIMAL(30, 4), doc="真实修正久期")
    ACTCONVEXITY = Column(DECIMAL(30, 4), doc="真实凸性")
    ACTBASEPOINT = Column(DECIMAL(30, 4), doc="真实基点价值")
    ACTINTESPRDDURATION = Column(DECIMAL(30, 4), doc="真实利差久期")
    ACTINTESPRDCONVEXITY = Column(DECIMAL(30, 4), doc="真实利差凸性")
    RELIABILITY = Column(String(20), doc="可信度")
    VALURATEDURATION = Column(DECIMAL(30, 4), doc="估价利率久期")
    VALURATECONVEXITY = Column(DECIMAL(30, 4), doc="估价利率凸性")
    ACTRATEDURATION = Column(DECIMAL(30, 4), doc="真实利率久期")
    ACTRATECONVEXITY = Column(DECIMAL(30, 4), doc="真实利率凸性")
    FNLVALUFULLPRICE = Column(DECIMAL(30, 4), doc="日终估价全价")
    FNLACCRUEDINTEREST = Column(DECIMAL(30, 4), doc="日终应计利息")
    REMAININGPRINCIPAL = Column(DECIMAL(30, 4), doc="剩余本金")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_shcyield(Base):

    __tablename__ = 'bond_shcyield'

    TRADINGDATE = Column(DateTime, doc="曲线日期")
    CURVENAMEID = Column(String(6), doc="曲线ID")
    CURVENAME = Column(String(200), doc="曲线名称")
    CURVESTANDARDTERM = Column(DECIMAL(10, 2), doc="曲线标准期限")
    TERMDESCRIPTION = Column(String(10), doc="期限描述")
    YEILDCURVETYPEID = Column(String(6), doc="收益率曲线类型ID")
    YEILDCURVETYPE = Column(String(40), doc="收益率曲线类型")
    YIELD = Column(DECIMAL(10, 4), doc="收益率")
    VALUEN = Column(DECIMAL(10, 4), doc="N值")
    VALUEK = Column(DECIMAL(10, 4), doc="K值")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_stagesredemption(Base):

    __tablename__ = 'bond_stagesredemption'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(10), doc="债券代码")
    STAGEN = Column(BIGINT, doc="第N期")
    STAGENREPAYMENTRATIO = Column(DECIMAL(10, 2), doc="第N期偿还比例")
    THENCALCULATIONYEAREND = Column(BIGINT, doc="第N个计算年度末")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_suspentioninfo(Base):

    __tablename__ = 'bond_suspentioninfo'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    SYMBOL = Column(String(12), doc="债券代码")
    SHORTNAME = Column(String(40), doc="债券简称")
    EXCHANGECODE = Column(String(20), doc="交易所代码")
    ANNOUNCEMENTDATE = Column(DateTime, doc="停牌公告日期")
    SUSPENTIONDATE = Column(DateTime, primary_key=True, doc="停牌开始日期")
    SUSPENSTIONTIME = Column(String(12), primary_key=True, doc="停牌时间")
    RESUMPTIONDATE = Column(DateTime, doc="复牌日期")
    RESUMPTIONTIME = Column(String(12), doc="复牌时间")
    RESANNOUNCEMENTDATE = Column(DateTime, doc="复牌公告日期")
    REASON = Column(String(400), doc="停牌原因")
    UPDATEID = Column(BIGINT, doc="数据ID")


class bond_tenderissue(Base):

    __tablename__ = 'bond_tenderissue'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    ANNOUNCEMENTDATE = Column(DateTime, doc="公告日期")
    PLANEDISSUEQUANTITY = Column(DECIMAL(20, 4), doc="计划发行总额")
    TENDERISSUETYPEID = Column(String(100), doc="招标方式ID")
    TENDERISSUETYPE = Column(String(200), doc="招标方式")
    TENDERBIDID = Column(String(100), doc="招标标的ID")
    TENDERBID = Column(String(200), doc="招标标的")
    TENDERTIME = Column(String(100), doc="招标时间")
    PAYMENTDATE = Column(DateTime, doc="缴款日")
    CHARGESTANDARD = Column(String(100), doc="手续费标准")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    TENDEROBJECT = Column(String(400), doc="招标对象")
    WINNINGTYPEEXPLANATION = Column(String(400), doc="中标确定方式说明")
    TENDERRATEFLOOR = Column(DECIMAL(10, 2), doc="招标利率下限")
    TENDERRATECEILING = Column(DECIMAL(10, 2), doc="招标利率上限")
    BASBIDUNIT = Column(DECIMAL(20, 2), doc="基本投标单位")
    PERLOWTENDERVOLUME = Column(DECIMAL(20, 2), doc="每标位最低投标量")
    PERHIGHTENDERVOLUME = Column(DECIMAL(20, 2), doc="每标位最高投标量")
    TENDEREXPLANATION = Column(String(4000), doc="投标说明")


class bond_tenderresult(Base):

    __tablename__ = 'bond_tenderresult'

    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    ANNOUNCEMENTDATE = Column(DateTime, doc="公告日期")
    TENDERID = Column(String(40), doc="招投标书编号")
    PAYMENTAMOUNT = Column(DECIMAL(20, 2), doc="缴款总金额")
    ACTUALISSUEDAMOUNT = Column(DECIMAL(20, 4), doc="实际发行总额")
    BASICUNDERWRITEAMOUNT = Column(DECIMAL(20, 4), doc="基本承购总额")
    TENDERAMOUNT = Column(DECIMAL(20, 4), doc="招标总量")
    ACCEPTEDNUMBER = Column(BIGINT, doc="应标家数")
    BIDDERNUMBER = Column(BIGINT, doc="投标家数")
    BIDDINGNUMBER = Column(BIGINT, doc="投标笔数")
    VALIDBIDDINGNUMBER = Column(BIGINT, doc="有效笔数")
    INVALIDBIDDINGNUMBER = Column(BIGINT, doc="无效笔数")
    VALIDBIDDINGAMOUNT = Column(DECIMAL(20, 2), doc="有效投标总量")
    BIDDINGPRICE_HIGH = Column(DECIMAL(10, 4), doc="最高投标价位")
    BIDDINGPRICE_LOW = Column(DECIMAL(10, 4), doc="最低投标价位")
    WINBIDDINGAMOUNT = Column(DECIMAL(20, 4), doc="中标总量")
    WINBIDDERNUM = Column(BIGINT, doc="中标家数")
    WINBIDDINGNUM = Column(BIGINT, doc="中标笔数")
    SELFSUPPORTEDAMOUNT = Column(DECIMAL(20, 4), doc="自营中标总量")
    WININGINGPRICE_HIGH = Column(DECIMAL(10, 4), doc="最高中标价位")
    WININGINGPRICE_LOW = Column(DECIMAL(10, 4), doc="最低中标价位")
    MARGINWININGHIGHPRAMT = Column(DECIMAL(20, 4), doc="边际中标价位投标总量")
    MARGINWININGLOWPRAMT = Column(DECIMAL(20, 4), doc="边际中标价位中标总量")
    FINALISSUEPRICE = Column(DECIMAL(10, 2), doc="最终发行价格")
    REFERENCEYIELD = Column(DECIMAL(10, 4), doc="参考收益率")
    FINALCOUPONRATE = Column(DECIMAL(10, 4), doc="最终票面利率")
    AVERAGEWININGRATE = Column(DECIMAL(10, 4), doc="全场中标利率")
    AVERAGEWININGPRICE = Column(DECIMAL(10, 4), doc="全场中标价格")
    AVERAGEWININGSPREAD = Column(DECIMAL(10, 4), doc="全场中标利差")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class bond_treasyield(Base):

    __tablename__ = 'bond_treasyield'

    TRADINGDATE = Column(DateTime, doc="日期")
    CURVETYPEID = Column(String(6), doc="收益率曲线类型ID")
    CURVETYPE = Column(String(100), doc="收益率曲线类型")
    REMAININGYEARS = Column(DECIMAL(18, 4), doc="剩余年限")
    YIELD = Column(DECIMAL(18, 8), doc="收益率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class cmo_pretrdinfo(Base):

    __tablename__ = 'cmo_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), doc="交易代码")
    EXCHANGESYMBOL = Column(String(20), doc="交易所原始代码")
    EXCHANGECODE = Column(String(6), doc="交易所代码")
    OPTIONTYPE = Column(String(20), doc="期权类型")
    CALLORPUT = Column(String(10), doc="合约类型")
    STRIKEPRICE = Column(DECIMAL(10, 4), doc="行权价")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSYMBOL = Column(String(10), doc="标的期货交易代码")
    UNDERLYINGSHORTNAME = Column(String(20), doc="标的期货简称")
    LISTEDDATE = Column(DateTime, doc="行权起始日")
    EXPIREDATE = Column(DateTime, doc="行权到期日")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(10, 3), doc="标的期货前收盘")
    UNDERLYINGPRESETTLEPRICE = Column(DECIMAL(10, 3), doc="标的期货前结算")
    UNDERLYINGPREPOSITION = Column(DECIMAL(20, 0), doc="标的期货昨持仓量")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价格")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价格")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 4), doc="前结算价")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 4), doc="开盘基准价")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="单位保证金")
    MINCHANGEUNIT = Column(DECIMAL(10, 4), doc="最小变动单位")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    STATUS = Column(String(20), doc="交易状态")
    UPDATEID = Column(BIGINT, doc="数据ID")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")


class cmo_pretrdinfohistory(Base):

    __tablename__ = 'cmo_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), doc="交易代码")
    EXCHANGESYMBOL = Column(String(20), doc="交易所原始代码")
    EXCHANGECODE = Column(String(6), doc="交易所代码")
    OPTIONTYPE = Column(String(20), doc="期权类型")
    CALLORPUT = Column(String(10), doc="合约类型")
    STRIKEPRICE = Column(DECIMAL(10, 4), doc="行权价")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSYMBOL = Column(String(10), doc="标的期货交易代码")
    UNDERLYINGSHORTNAME = Column(String(20), doc="标的期货简称")
    LISTEDDATE = Column(DateTime, doc="行权起始日")
    EXPIREDATE = Column(DateTime, doc="行权到期日")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(10, 3), doc="标的期货前收盘")
    UNDERLYINGPRESETTLEPRICE = Column(DECIMAL(10, 3), doc="标的期货前结算")
    UNDERLYINGPREPOSITION = Column(DECIMAL(20, 0), doc="标的期货昨持仓量")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价格")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价格")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 4), doc="前结算价")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 4), doc="开盘基准价")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="单位保证金")
    MINCHANGEUNIT = Column(DECIMAL(10, 4), doc="最小变动单位")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    STATUS = Column(String(20), doc="交易状态")
    UPDATEID = Column(BIGINT, doc="数据ID")


class cost_riskfree(Base):

    __tablename__ = 'cost_riskfree'

    BENCHMARKID = Column(String(12), doc="无风险利率基准ID")
    BENCHMARK = Column(String(200), doc="无风险利率基准")
    TRADINGDATE = Column(DateTime, doc="统计日期")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    INTERESTRATEDAILY = Column(DECIMAL(18, 6), doc="日度化无风险利率")
    INTERESTRATEWEEKLY = Column(DECIMAL(18, 6), doc="周度化无风险利率")
    INTERESTRATEMONTHLY = Column(DECIMAL(18, 6), doc="月度化无风险利率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class ffut_calpretrdinfo(Base):

    __tablename__ = 'ffut_calpretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPPERLMTPRC = Column(DECIMAL(9, 3), doc="涨停价格")
    LOWERLMTPRC = Column(DECIMAL(9, 3), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 3), doc="前结算价")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 3), doc="开盘基准价")
    UPDATEID = Column(BIGINT, doc="数据ID")
    UPDATEID2 = Column(BIGINT, doc="数据ID2")
    SOURCETABLE = Column(String(100), doc="源表")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    MINCHANGEUNIT = Column(DECIMAL(10, 3), doc="最小变动单位")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")


class ffut_pretrdinfo(Base):

    __tablename__ = 'ffut_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPPERLMTPRC = Column(DECIMAL(9, 3), doc="涨停价格")
    LOWERLMTPRC = Column(DECIMAL(9, 3), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 3), doc="前结算价")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 3), doc="开盘基准价")
    UPDATEID = Column(BIGINT, doc="数据ID")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    CLIENTPOSITIONLIMIT = Column(DECIMAL(20, 0), doc="客户持仓量限制")
    MINCHANGEUNIT = Column(DECIMAL(10, 3), doc="最小变动单位")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")


class ffut_pretrdinfohistory(Base):

    __tablename__ = 'ffut_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPPERLMTPRC = Column(DECIMAL(9, 3), doc="涨停价格")
    LOWERLMTPRC = Column(DECIMAL(9, 3), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 3), doc="前结算价")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 3), doc="开盘基准价")
    UPDATEID = Column(BIGINT, doc="数据ID")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    CLIENTPOSITIONLIMIT = Column(DECIMAL(20, 0), doc="客户持仓量限制")
    MINCHANGEUNIT = Column(DECIMAL(10, 3), doc="最小变动单位")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")


class fund_allocation(Base):

    __tablename__ = 'fund_allocation'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(String(4), doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    CROSSCODE = Column(String(2), doc="横表编码")
    CROSSNAME = Column(String(30), doc="横表名称")
    CROSSNAME_EN = Column(String(30), doc="横表名称(英文)")
    EQUITY = Column(DECIMAL(20, 2), doc="权益类投资")
    STOCKAMOUNT = Column(DECIMAL(20, 2), doc="其中股票金额")
    COMMONSTOCK = Column(DECIMAL(20, 2), doc="其中普通股")
    DEPOSITORYRECEIPTS = Column(DECIMAL(20, 2), doc="其中存托凭证")
    REIT = Column(DECIMAL(20, 2), doc="其中房地产信托")
    FUNDVALUE = Column(DECIMAL(20, 2), doc="基金投资")
    FIXEDINCOME = Column(DECIMAL(20, 2), doc="固定收益类投资")
    BONDAMOUNT = Column(DECIMAL(20, 2), doc="其中债券金额")
    ABSVALUE = Column(DECIMAL(20, 2), doc="其中资产支持证券")
    PRECIOUSMETALS = Column(DECIMAL(20, 2), doc="贵金属投资")
    DERIVATIVE = Column(DECIMAL(20, 2), doc="金融衍生品投资")
    FORWARD = Column(DECIMAL(20, 2), doc="其中远期")
    FUTURE = Column(DECIMAL(20, 2), doc="其中期货")
    INTERIMOPTION = Column(DECIMAL(20, 2), doc="其中期权")
    WARRANT = Column(DECIMAL(20, 2), doc="其中权证")
    SWAP = Column(DECIMAL(20, 2), doc="其中互换")
    STRUCTUREDPRODUCT = Column(DECIMAL(20, 2), doc="结构性投资产品")
    BUYINGBACKTHESALE = Column(DECIMAL(20, 2), doc="买入返售金融资产")
    BUYOUTREPO = Column(DECIMAL(20, 2), doc="其中买断式回购的买入返售金融资产")
    MONEYMARKETINSTRUMENT = Column(DECIMAL(20, 2), doc="货币市场工具")
    TOTALDEPOSITRESERVE = Column(DECIMAL(20, 2), doc="银行存款和清算备付金合计")
    OTHERSASSET = Column(DECIMAL(20, 2), doc="资产组合其他资产")
    TOTALASSET = Column(DECIMAL(20, 2), doc="资产组合合计")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class fund_areaclass(Base):

    __tablename__ = 'fund_areaclass'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    RANK = Column(INTEGER, doc="排名")
    AREACODE = Column(String(20), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    FAIRVALUE = Column(DECIMAL(20, 2), doc="公允价值")
    PROPORTION = Column(DECIMAL(10, 4), doc="占基金资产净值比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_bwardfactor(Base):

    __tablename__ = 'fund_bwardfactor'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    BWARDFACTOR = Column(DECIMAL(12, 6), doc="后复权因子")
    CUMULATEBWARDFACTOR = Column(DECIMAL(12, 6), doc="后累计复权因子")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_calpretrdinfo(Base):

    __tablename__ = 'fund_calpretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), primary_key=True, doc="证券代码")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    EXCHANGECODE = Column(String(12), doc="交易所代码")
    SHORTNAME = Column(String(100), doc="基金简称")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    TRADINGSHORTNAME = Column(String(100), doc="证券简称")
    INCEPTIONSHARES = Column(DECIMAL(20, 2), doc="基金成立时份额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_classinfochange(Base):

    __tablename__ = 'fund_classinfochange'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(40), doc="基金代码")
    ANNOUNCEMENTDATE = Column(DateTime, doc="公告日期")
    CHANGEDITEM = Column(String(100), doc="变更属性")
    VALUEBEFORE = Column(String(1000), doc="变更前值")
    CODEBEFORE = Column(String(200), doc="变更前(编码|英文)")
    VALUEAFTER = Column(String(1000), doc="变更后值")
    CODEAFTER = Column(String(200), doc="变更后(编码|英文)")
    COMMENTS = Column(String(1000), doc="备注")
    CHANGEDATE = Column(DateTime, doc="实施日期")
    EVENTTYPE = Column(String(40), doc="事件类型编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    MASTERFUNDCODE = Column(String(40))


class fund_custodian(Base):

    __tablename__ = 'fund_custodian'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    FULLNAME = Column(String(120), doc="公司名称")
    ESTABLISHDATE = Column(DateTime, doc="公司成立日期")
    REGISTERCAPITAL = Column(DECIMAL(20, 2), doc="公司注册资本")
    ORGANIZATIONTYPEID = Column(String(100), doc="公司组织形式编码")
    ORGANIZATIONTYPE = Column(String(100), doc="公司组织形式")
    COMPANYPROPERTIES = Column(String(100), doc="公司属性")
    LEGALREPRESENTATIVE = Column(String(100), doc="公司法定代表人")
    TEL = Column(String(100), doc="公司电话号码")
    ZIPCODE = Column(String(100), doc="公司邮编")
    FAX = Column(String(100), doc="公司传真")
    WSBSITE = Column(String(100), doc="公司网址")
    REGISTERADDRESS = Column(String(200), doc="公司注册地址")
    OFFICEADDRESS = Column(String(200), doc="公司办公地址")
    BUSINESSLICENSENO = Column(String(40), doc="公司营业执照注册号")
    CONTACTS = Column(String(100), doc="公司联系人")
    MAIL = Column(String(80), doc="公司电子邮箱")
    APPROVALNO = Column(String(200), doc="基金托管业务批准文号")
    DISCLOSEPERSON = Column(String(100), doc="管理公司信息披露负责人")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_daynav(Base):

    __tablename__ = 'fund_daynav'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="基金代码")
    SHORTNAME = Column(String(100), doc="基金简称")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="基金份额累计净值")
    ACHIEVERETURN = Column(DECIMAL(19, 4), doc="每万份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(19, 3), doc="7日年化收益率")
    MILLIONACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百万份基金已实现收益")
    HUNDREDACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百份基金已实现收益")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_etfconstitsec(Base):

    __tablename__ = 'fund_etfconstitsec'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(12), doc="基金代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SECURITYID = Column(DECIMAL(20, 0), doc="成分证券ID")
    SECURITYCODE = Column(String(40), doc="成分证券代码")
    SECURITYNAME = Column(String(100), doc="成分证券简称")
    SECURITYNUM = Column(DECIMAL(20, 0), doc="成分证券数量")
    CASHSUBSTSIGNID = Column(String(12), doc="现金替代标志ID")
    CASHSUBSTSIGN = Column(String(20), doc="现金替代标志")
    CASHSUBSTPREMPROP = Column(DECIMAL(10, 2), doc="申购现金替代溢价比例")
    FIXEDSUBSTAMOUNT = Column(DECIMAL(20, 2), doc="固定替代金额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    RDMCASHSUBSTPREMPROP = Column(DECIMAL(10, 2), doc="赎回现金替代溢价比例")


class fund_etfpchasredemlis(Base):

    __tablename__ = 'fund_etfpchasredemlis'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    SYMBOL = Column(String(12), doc="基金代码")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    CATEGORYID = Column(String(12), doc="基金类型ID")
    CATEGORY = Column(String(40), doc="基金类别")
    NAVENDDATE = Column(DateTime, doc="净值截止日期")
    CASHDIFFERENCE = Column(DECIMAL(20, 2), doc="现金差额")
    MINUNITNAV = Column(DECIMAL(20, 2), doc="最小申购、赎回单位净值")
    CASHESTIMATE = Column(DECIMAL(20, 2), doc="预估现金部分")
    CASHSUBSTPROPCEILING = Column(DECIMAL(10, 2), doc="现金替代比例上限")
    ISPUBIOPV = Column(SMALLINT, doc="是否需要公布IOPV")
    MINUNIT = Column(DECIMAL(20, 0), doc="最小申购、赎回单位")
    MINUNITDIVID = Column(DECIMAL(20, 2), doc="最小申购赎回单位现金红利")
    ISOPENPCHAS = Column(SMALLINT, doc="是否允许申购")
    ISOPENREDEE = Column(SMALLINT, doc="是否允许赎回")
    PURCHASECEILING = Column(DECIMAL(20, 0), doc="当天累计可申购的基金份额上限")
    REDEEMCEILING = Column(DECIMAL(20, 0), doc="当天累计可赎回的基金份额上限")
    SYNSECURNUM = Column(BIGINT, doc="申购赎回组合证券数")
    UPDATEID = Column(BIGINT, doc="数据ID")
    NAV = Column(DECIMAL(10, 4), doc="基金份额净值")
    IOPV = Column(DECIMAL(10, 4), doc="基金份额参考净值")
    OVERFLOWRATE = Column(DECIMAL(10, 4), doc="溢折率")
    DISCOUNTWATERRATE = Column(DECIMAL(10, 4), doc="贴水率")


class fund_evl_dayahay(Base):

    __tablename__ = 'fund_evl_dayahay'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_evl_dayamth(Base):

    __tablename__ = 'fund_evl_dayamth'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_evl_dayasen(Base):

    __tablename__ = 'fund_evl_dayasen'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_evl_dayayear(Base):

    __tablename__ = 'fund_evl_dayayear'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_evl_daythryear(Base):

    __tablename__ = 'fund_evl_daythryear'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, primary_key=True, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_evl_weekahay(Base):

    __tablename__ = 'fund_evl_weekahay'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_evl_weekayear(Base):

    __tablename__ = 'fund_evl_weekayear'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_evl_weekthryear(Base):

    __tablename__ = 'fund_evl_weekthryear'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATELAST = Column(DateTime, doc="区间结束日期")
    TRADINGDATEFIRST = Column(DateTime, doc="区间开始日期")
    SYMBOL = Column(String(20), doc="基金代码")
    CATEGORYID = Column(String(40), doc="基金类别ID")
    AVGRETURN = Column(DECIMAL(16, 4), doc="平均收益率")
    AVGRETURNRNK = Column(INTEGER, doc="平均收益率同类基金排名")
    NUMBERTORNKAVGRETURN = Column(INTEGER, doc="参与平均收益率排名的同类基金数")
    STDRETURN = Column(DECIMAL(16, 4), doc="收益率标准差")
    STDRETURNRNK = Column(INTEGER, doc="标准差同类基金排名")
    NUMBERTORNKSTDRETURN = Column(INTEGER, doc="参与标准差排名的同类基金数")
    SHARPE = Column(DECIMAL(16, 4), doc="Sharpe率")
    SHARPERNK = Column(INTEGER, doc="Sharpe率同类基金排名")
    NUMBERTORNKSHARPE = Column(INTEGER, doc="参与Sharpe率排名的同类基金数")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIOAVGRETURN = Column(DECIMAL(16, 4), doc="市场组合平均收益率")
    BETA = Column(DECIMAL(16, 4), doc="Beta值")
    BETARNK = Column(INTEGER, doc="Beta值同类基金排名")
    NUMBERTORNKBETA = Column(INTEGER, doc="参与Beta值排名的同类基金数")
    ALPHA = Column(DECIMAL(16, 4), doc="詹森指数-Alpha值")
    ALPHARNK = Column(INTEGER, doc="Alpha值同类基金排名")
    NUMBERTORNKALPHA = Column(INTEGER, doc="参与Alpha值排名的同类基金数")
    TREYNOR = Column(DECIMAL(16, 4), doc="特雷诺指数")
    TREYNORRNK = Column(INTEGER, doc="特雷诺指数同类基金排名")
    NUMBERTORNKTREYNOR = Column(INTEGER, doc="参与特雷诺指数排名的同类基金数")
    TMTIMING = Column(DECIMAL(16, 4), doc="TM模型择时能力gamma")
    TMTIMINGRNK = Column(INTEGER, doc="TM模型择时能力同类基金排名")
    NUMBERTORNKTMTIMING = Column(INTEGER, doc="参与TM模型择时能力gamma排名的同类基金数")
    TMSTKSLCT = Column(DECIMAL(16, 4), doc="TM模型选股能力alpha")
    TMSTKSLCTRNK = Column(INTEGER, doc="TM模型选股能力同类基金排名")
    NUMBERTORNKTMSTKSLCT = Column(INTEGER, doc="参与TM模型选股能力alpha排名的同类基金数")
    CLBEARTIMING = Column(DECIMAL(16, 4), doc="CL模型熊市择时能力gamma1")
    CLBEARTIMINGRNK = Column(INTEGER, doc="CL模型熊市择时能力同类基金排名")
    NUMBERTORNKCLBEARTIMING = Column(INTEGER, doc="参与CL模型熊市择时能力gamma1排名的同类基金数")
    CLBULLTIMING = Column(DECIMAL(16, 4), doc="CL模型牛市择时能力gamma2")
    CLBULLTIMINGRNK = Column(INTEGER, doc="CL模型牛市择时能力同类基金排名")
    NUMBERTORNKCLBULLTIMING = Column(INTEGER, doc="参与CL模型牛市择时能力gamma2排名的同类基金数")
    CLTIMING = Column(DECIMAL(16, 4), doc="CL模型择时能力gamma")
    CLTIMINGRNK = Column(INTEGER, doc="CL模型择时能力同类基金排名")
    NUMBERTORNKCLTIMING = Column(INTEGER, doc="参与CL模型择时能力gamma排名的同类基金数")
    CLSTKSLCT = Column(DECIMAL(16, 4), doc="CL模型选股能力alpha")
    CLSTKSLCTRNK = Column(INTEGER, doc="CL模型选股能力同类基金排名")
    NUMBERTORNKCLSTKSLCT = Column(INTEGER, doc="参与CL模型选股能力alpha排名的同类基金数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_feeschange(Base):

    __tablename__ = 'fund_feeschange'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    TYPEOFFEE = Column(String(40), doc="费率类型")
    NAMEOFFEE = Column(String(100), doc="费率名称")
    PROPORTIONOFFEE = Column(String(40), doc="费率比例")
    AMOUNTOFFEE = Column(String(100), doc="费率金额")
    DESCRIPTIONOFTERM = Column(String(200), doc="期限说明")
    EFFECTIVEDATE = Column(DateTime, doc="有效起始日")
    EXPIREDDATE = Column(DateTime, doc="失效日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_fundcodeinfo(Base):

    __tablename__ = 'fund_fundcodeinfo'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(40), doc="基金代码")
    FUNDCODE = Column(String(40), doc="基金相关代码")
    FUNDCODETYPEID = Column(String(100), doc="代码类型编码")
    FUNDCODETYPE = Column(String(100), doc="代码类型")
    EXCHAANGEID = Column(String(100), doc="交易市场")
    FREQUENCY = Column(String(100), doc="频度属性")
    NOTE = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_fundcompany(Base):

    __tablename__ = 'fund_fundcompany'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    FULLNAME = Column(String(120), doc="公司名称")
    ESTABLISHDATE = Column(DateTime, doc="公司成立日期")
    REGISTERCAPITAL = Column(DECIMAL(20, 2), doc="公司注册资本")
    ORGANIZATIONTYPEID = Column(String(100), doc="公司组织形式编码")
    ORGANIZATIONTYPE = Column(String(100), doc="公司组织形式")
    COMPANYPROPERTIES = Column(String(100), doc="公司属性")
    LEGALREPRESENTATIVE = Column(String(100), doc="公司法定代表人")
    TEL = Column(String(100), doc="公司电话号码")
    ZIPCODE = Column(String(100), doc="公司邮编")
    FAX = Column(String(100), doc="公司传真")
    WSBSITE = Column(String(100), doc="公司网址")
    REGISTERADDRESS = Column(String(200), doc="公司注册地址")
    OFFICEADDRESS = Column(String(200), doc="公司办公地址")
    BUSINESSLICENSENO = Column(String(40), doc="公司营业执照注册号")
    CONTACTS = Column(String(100), doc="公司联系人")
    MAIL = Column(String(80), doc="公司电子邮箱")
    DISCLOSEPERSON = Column(String(100), doc="管理公司信息披露负责人")
    FUNDNUM = Column(INTEGER, doc="公司管理基金数量")
    OPENFUNDNUM = Column(INTEGER, doc="公司管理开放式基金数量")
    CLOSEFUNDNUM = Column(INTEGER, doc="公司管理封闭式基金数量")
    CLOSEFULLNAME = Column(String(400), doc="公司管理封闭式基金名称")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    OPENFULLNAME = Column(LONGTEXT)


class fund_funddividend(Base):

    __tablename__ = 'fund_funddividend'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    ANNOUNCEMENTDATE = Column(DateTime, doc="分配方案公告日期")
    BENCHDATE = Column(DateTime, doc="收益分配基准日")
    TOTALDIVIDENDDISTRI = Column(DECIMAL(19, 2), doc="基准日按分红比例应分配金额")
    RECORDDATE = Column(DateTime, doc="权益登记日")
    SECONDARYEXDIVIDENDDATE = Column(DateTime, doc="场内除息日")
    PRIMARYEXDIVIDENDDATE = Column(DateTime, doc="场外除息日")
    SECONDARYPAYDATE_DIVIDEND = Column(DateTime, doc="场内现金红利发放日")
    PRIMARYPAYDATE_DIVIDEND = Column(DateTime, doc="场外现金红利发放日")
    DIVIDENDREINVESTMENTDATE = Column(DateTime, doc="红利转再投资日")
    REDEMPTIONSTARTDATE = Column(DateTime, doc="再投资赎回起始日")
    DISTRIBUTIONTYPECODE = Column(String(40), doc="分配类型编码")
    DIVIDENDPERSHARE = Column(DECIMAL(20, 6), doc="每份分红数")
    DIVIDENDNUMBER = Column(String(400), doc="年度分红次数说明")
    CURRENCYCODE = Column(String(6), doc="币种编码")
    CURRENCY = Column(String(100), doc="币种")
    DIVIDENDOBJECT = Column(String(4000), doc="分红对象")
    ISCHANGEPLAN = Column(String(4), doc="方案是否变更")
    CONTENT_CHANGEPLAN = Column(String(1000), doc="方案更改内容")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    DISTRIBUTIONPLAN = Column(String(4000), doc="分配方案")


class fund_fundmanager(Base):

    __tablename__ = 'fund_fundmanager'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    FUNDCOMPANYID = Column(DECIMAL(20, 0), doc="基金管理公司ID")
    FUNDCOMPANYNAME = Column(String(200), doc="基金管理公司名称")
    FULLNAME = Column(String(100), doc="姓名")
    GENDER = Column(String(2), doc="性别")
    BIRTHDATE = Column(DateTime, doc="出生日期")
    APPROVEDSERVICESTARTDATE = Column(DateTime, doc="证监会核准高管任职资格的日期")
    SERVICESTARTDATE = Column(DateTime, doc="任职日期")
    SERVICEENDDATE = Column(DateTime, doc="离职日期")
    POSITIONSTATE = Column(String(2), doc="在职状态")
    DEGREEID = Column(String(40), doc="学历编码")
    DEGREE = Column(String(200), doc="学历")
    NATIONALITYID = Column(String(12), doc="国籍编码")
    NATIONALITY = Column(String(40), doc="国籍")
    RESIGNREASONID = Column(String(12), doc="离任原因编码")
    RESIGNREASON = Column(String(4000), doc="离任原因")
    BUSINESSDURATION = Column(SMALLINT, doc="证券从业年限")
    RESUME = Column(LONGTEXT, doc="简历")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    FUNDMANAGERID = Column(DECIMAL(20, 0), doc="基金经理ID")


class fund_fwardfactor(Base):

    __tablename__ = 'fund_fwardfactor'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    FWARDFACTOR = Column(DECIMAL(12, 6), doc="前复权因子")
    CUMULATEFWARDFACTOR = Column(DECIMAL(12, 6), doc="前累计复权因子")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_holderstructure(Base):

    __tablename__ = 'fund_holderstructure'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    ENDDATE = Column(DateTime, doc="截止日期")
    HOLDERNUMBER = Column(DECIMAL(20, 2), doc="基金份额持有人户数")
    AVERAGESHARES = Column(DECIMAL(20, 2), doc="平均每户持有基金份额")
    TOTALHOLDERNUMBER = Column(DECIMAL(20, 2), doc="总产品持有人户数")
    TOTALAVERAGESHARES = Column(DECIMAL(20, 2), doc="总产品平均每户持有基金份额")
    INSTITUTIONSHARES = Column(DECIMAL(20, 2), doc="机构投资者持有的基金份额")
    INSTITUTIONRATIO = Column(DECIMAL(10, 4), doc="机构投资占总份额比例")
    INDIVIDUALSHARES = Column(DECIMAL(20, 2), doc="个人投资者持有的基金份额")
    INDIVIDUALRATIO = Column(DECIMAL(10, 4), doc="个人投资占总份额比例")
    PRACTITIONERSSHARE = Column(DECIMAL(20, 2), doc="基金从业人员持有基金份额")
    PRACTITIONERSRATIO = Column(DECIMAL(10, 4), doc="基金从业人员持有基金份额占总份额比例")
    OTHERSHARES = Column(DECIMAL(20, 2), doc="其他持有人持有基金份额")
    OTHERRATIO = Column(DECIMAL(10, 4), doc="其他持有人持有比例")
    TOTALINSTITUTIONSHARES = Column(DECIMAL(20, 2), doc="总产品机构投资者持有的基金份额")
    TOTALINSTITUTIONRATIO = Column(DECIMAL(10, 4), doc="总产品机构投资者持有的基金份额占总份额比例")
    TOTALINDIVIDUALSHARES = Column(DECIMAL(20, 2), doc="总产品个人投资者持有的基金份额")
    TOTALINDIVIDUALRATIO = Column(DECIMAL(10, 4), doc="总产品个人投资者持有的基金份额占总份额比例")
    TOTALPRACTITIONERSSHARE = Column(DECIMAL(20, 2), doc="总产品基金从业人员持有基金份额")
    TOTALPRACTITIONERSRATIO = Column(DECIMAL(10, 4), doc="总产品基金从业人员持有基金份额占总份额比例")
    RELATIONCODE = Column(String(100), doc="基金关系编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_indexreturn(Base):

    __tablename__ = 'fund_indexreturn'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(12), doc="指数代码")
    INDEXFULLNAME = Column(String(200), doc="指数名称")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 3), doc="开盘价")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="最低价")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(18, 2), doc="交易金额")
    INDEXRETURN = Column(DECIMAL(12, 6), doc="基金指数回报率(%)")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_industrystockclass(Base):

    __tablename__ = 'fund_industrystockclass'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    INVESTMENTTYPE = Column(SMALLINT, doc="投资类型分类")
    INDCLASSIFYSYSTEMCODE = Column(String(40), doc="行业分类标准编码")
    INDUSTRYCODE = Column(String(20), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    FAIRVALUE = Column(DECIMAL(20, 2), doc="行业分类公允价值")
    FAIRVALUETONAV = Column(DECIMAL(20, 2), doc="占基金资产净值比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_jajxrate(Base):

    __tablename__ = 'fund_jajxrate'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    FUNDNAME = Column(String(150), doc="基金名称")
    FUNDTYPE = Column(String(60), doc="基金类型")
    REPPD = Column(SMALLINT, doc="报告周期")
    INFOPUBDT = Column(DateTime, doc="信息发布日期")
    PROFITCAP = Column(SMALLINT, doc="盈利能力")
    PRFMCSTA = Column(SMALLINT, doc="业绩稳定性")
    ANTIRISKCAP = Column(SMALLINT, doc="抗风险能力")
    REFTRKCAP = Column(SMALLINT, doc="基准跟踪能力")
    EXCEARNING = Column(SMALLINT, doc="超额收益")
    TIMINGCAP = Column(SMALLINT, doc="择时能力")
    STKSELCAP = Column(SMALLINT, doc="选股能力")
    OVLCOST = Column(SMALLINT, doc="整体费用")
    JARATE = Column(SMALLINT, doc="济安最新评级")
    CHANGERATE = Column(String(20), doc="评级变动")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_listing(Base):

    __tablename__ = 'fund_listing'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    LSTSTPBDT = Column(DateTime, doc="上市公告书发表日期")
    EXCHANGECODE = Column(String(40), doc="上市交易所")
    LISTINGDATE = Column(DateTime, doc="上市日期")
    LISTINGRECOMMENDER = Column(String(1000), doc="上市推荐人")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="发行总市值")
    UNITSISSUEDSHARE = Column(DECIMAL(20, 2), doc="基金单位发行总份额")
    NEGOTIABLESHARE = Column(DECIMAL(20, 2), doc="本次可流通份额")
    CHANGELIMIT = Column(DECIMAL(20, 2), doc="涨跌幅限制")
    MASTERBROKER = Column(String(1000), doc="主交易商")
    VERIFICATIONINSTITUTION = Column(String(200), doc="基金验资机构")
    ISSUEEXPENSES = Column(DECIMAL(20, 2), doc="总发行费用")
    ONLINEEXPENSESOFFERING = Column(DECIMAL(20, 2), doc="上网发行费")
    ISSUERCOORDINATIONCOSTS = Column(DECIMAL(20, 2), doc="发行人协调费")
    RECOMMENDERFORLISTINGFEE = Column(DECIMAL(20, 2), doc="上市推荐人费")
    SOLICITORFEE = Column(DECIMAL(20, 2), doc="律师费")
    ACCOUNTINGCOST = Column(DECIMAL(20, 2), doc="会计师费")
    INITIALLISTINGFEE = Column(DECIMAL(20, 2), doc="上市初费")
    EXPENSESOTHER = Column(DECIMAL(20, 2), doc="其他发行费用")
    ISSUEEXPENSESBALANCE = Column(DECIMAL(20, 2), doc="发行费用余额")
    HOLDERNUMBER = Column(DECIMAL(20, 2), doc="基金持有人户数")
    STATUSID = Column(String(40), doc="上市状态编码")
    STATUS = Column(String(40), doc="上市状态")
    DELISTEDDATE = Column(DateTime, doc="退市日期")
    DELISTEDEXPLANATION = Column(String(4000), doc="退市说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mainpersonnel(Base):

    __tablename__ = 'fund_mainpersonnel'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    FUNDCOMPANYID = Column(DECIMAL(20, 0), doc="基金管理公司ID")
    FUNDCOMPANYNAME = Column(String(200), doc="基金管理公司名称")
    EXECUTIVESNAME = Column(String(100), doc="高管姓名")
    GENDER = Column(String(2), doc="性别")
    BIRTHDATE = Column(DateTime, doc="出生日期")
    POSITIONID = Column(String(200), doc="职务编码")
    POSITION = Column(String(200), doc="职务名称")
    PROFESSIONALTITLEID = Column(String(100), doc="职称编码")
    PROFESSIONALTITLE = Column(String(100), doc="职称")
    ORIGINALPOSITION = Column(String(200), doc="原始职务名称")
    APPROVEDSERVICESTARTDATE = Column(DateTime, doc="证监会核准高管任职资格的日期")
    SERVICESTARTDATE = Column(DateTime, doc="任职日期")
    SERVICEENDDATE = Column(DateTime, doc="离职日期")
    POSITIONSTATE = Column(String(2), doc="在职状态")
    DEGREEID = Column(String(40), doc="学历编码")
    DEGREE = Column(String(200), doc="学历")
    NATIONALITYID = Column(String(12), doc="国籍编码")
    NATIONALITY = Column(String(40), doc="国籍")
    RESIGNREASONID = Column(String(12), doc="离任原因编码")
    RESIGNREASON = Column(String(4000), doc="离任原因")
    BUSINESSDURATION = Column(SMALLINT, doc="证券从业年限")
    RESUME = Column(LONGTEXT, doc="简历")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    PERSONID = Column(DECIMAL(20, 0), doc="人员ID")


class fund_mkt_bwardquotation(Base):

    __tablename__ = 'fund_mkt_bwardquotation'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="均价")
    CHANGE = Column(DECIMAL(10, 4), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="换手率")
    AMPLITUDE = Column(DECIMAL(10, 6), doc="振幅")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_fwardquotation(Base):

    __tablename__ = 'fund_mkt_fwardquotation'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="均价")
    CHANGE = Column(DECIMAL(10, 4), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="换手率")
    AMPLITUDE = Column(DECIMAL(10, 6), doc="振幅")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mkt_lastbwardquotem(Base):

    __tablename__ = 'fund_mkt_lastbwardquotem'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGMONTH = Column(String(14), primary_key=True, doc="交易月份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRVCLOSEDATE = Column(DateTime, doc="上月收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上月收盘价")
    OPENDATE = Column(DateTime, doc="月开盘日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="月开盘价")
    HIGHDATE = Column(DateTime, doc="月最高价日")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="月最高价")
    LOWDATE = Column(DateTime, doc="月最低价日")
    LOWPRICE = Column(DECIMAL(10, 4), doc="月最低价")
    CLOSEDATE = Column(DateTime, doc="月收盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="月收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="月最高收盘价日")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最高收盘价")
    LOWCLOSEDATE = Column(DateTime, doc="月最低收盘价日")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最低收盘价")
    VOLUME = Column(BIGINT, doc="月成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="月成交金额")
    TRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="月均价")
    CHANGE = Column(DECIMAL(10, 4), doc="月涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="月涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="月振幅")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastbwardquotew(Base):

    __tablename__ = 'fund_mkt_lastbwardquotew'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(14), primary_key=True, doc="交易周份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRVCLOSEDATE = Column(DateTime, doc="上周收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上周收盘价")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="周开盘价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="周最高价")
    LOWDATE = Column(DateTime, doc="周最低价日")
    LOWPRICE = Column(DECIMAL(10, 4), doc="周最低价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="周收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最高收盘价")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最低收盘价")
    VOLUME = Column(BIGINT, doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="周成交金额")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="周均价")
    CHANGE = Column(DECIMAL(10, 4), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="周涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="周振幅")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastbwardquotey(Base):

    __tablename__ = 'fund_mkt_lastbwardquotey'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), primary_key=True, doc="交易年份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRVCLOSEDATE = Column(DateTime, doc="上年收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上年收盘价")
    OPENDATE = Column(DateTime, doc="年开盘日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="年开盘价")
    HIGHDATE = Column(DateTime, doc="年最高价日")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="年最高价")
    LOWDATE = Column(DateTime, doc="年最低价日")
    LOWPRICE = Column(DECIMAL(10, 4), doc="年最低价")
    CLOSEDATE = Column(DateTime, doc="年收盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="年收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="年最高收盘价日")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最高收盘价")
    LOWCLOSEDATE = Column(DateTime, doc="年最低收盘价日")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最低收盘价")
    VOLUME = Column(BIGINT, doc="年成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="年成交金额")
    TRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="年均价")
    CHANGE = Column(DECIMAL(10, 4), doc="年涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="年涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="年振幅")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastfwardquotem(Base):

    __tablename__ = 'fund_mkt_lastfwardquotem'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGMONTH = Column(String(14), primary_key=True, doc="交易月份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRVCLOSEDATE = Column(DateTime, doc="上月收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上月收盘价")
    OPENDATE = Column(DateTime, doc="月开盘日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="月开盘价")
    HIGHDATE = Column(DateTime, doc="月最高价日")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="月最高价")
    LOWDATE = Column(DateTime, doc="月最低价日")
    LOWPRICE = Column(DECIMAL(10, 4), doc="月最低价")
    CLOSEDATE = Column(DateTime, doc="月收盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="月收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="月最高收盘价日")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最高收盘价")
    LOWCLOSEDATE = Column(DateTime, doc="月最低收盘价日")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最低收盘价")
    VOLUME = Column(BIGINT, doc="月成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="月成交金额")
    TRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="月均价")
    CHANGE = Column(DECIMAL(10, 4), doc="月涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="月涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="月振幅")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastfwardquotew(Base):

    __tablename__ = 'fund_mkt_lastfwardquotew'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(14), primary_key=True, doc="交易周份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRVCLOSEDATE = Column(DateTime, doc="上周收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上周收盘价")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="周开盘价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="周最高价")
    LOWDATE = Column(DateTime, doc="周最低价日")
    LOWPRICE = Column(DECIMAL(10, 4), doc="周最低价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="周收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最高收盘价")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最低收盘价")
    VOLUME = Column(BIGINT, doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="周成交金额")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="周均价")
    CHANGE = Column(DECIMAL(10, 4), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="周涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="周振幅")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastfwardquotey(Base):

    __tablename__ = 'fund_mkt_lastfwardquotey'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), primary_key=True, doc="交易年份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRVCLOSEDATE = Column(DateTime, doc="上年收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上年收盘价")
    OPENDATE = Column(DateTime, doc="年开盘日期")
    OPENPRICE = Column(DECIMAL(10, 4), doc="年开盘价")
    HIGHDATE = Column(DateTime, doc="年最高价日")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="年最高价")
    LOWDATE = Column(DateTime, doc="年最低价日")
    LOWPRICE = Column(DECIMAL(10, 4), doc="年最低价")
    CLOSEDATE = Column(DateTime, doc="年收盘日期")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="年收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="年最高收盘价日")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最高收盘价")
    LOWCLOSEDATE = Column(DateTime, doc="年最低收盘价日")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最低收盘价")
    VOLUME = Column(BIGINT, doc="年成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="年成交金额")
    TRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    AVGPRICE = Column(DECIMAL(10, 4), doc="年均价")
    CHANGE = Column(DECIMAL(10, 4), doc="年涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="年涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="年振幅")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastquotationmonth(Base):

    __tablename__ = 'fund_mkt_lastquotationmonth'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGMONTH = Column(String(14), primary_key=True, doc="交易月份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    OPENDATE = Column(DateTime, doc="月开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上月收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上月收盘价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="月开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="月最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="月最低价")
    HIGHDATE = Column(DateTime, doc="月最高价日")
    LOWDATE = Column(DateTime, doc="月最低价日")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="月收盘价")
    CLOSEDATE = Column(DateTime, doc="月收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最低收盘价")
    AVGPRICE = Column(DECIMAL(10, 4), doc="月均价")
    CHANGE = Column(DECIMAL(10, 4), doc="月涨跌")
    CHANGERATIO = Column(DECIMAL(10, 4), doc="月涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="月换手率")
    AVGTURNOVERRATE = Column(DECIMAL(10, 6), doc="月平均换手率")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="月振幅")
    HIGHCLOSEDATE = Column(DateTime, doc="月最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="月最低收盘价日")
    COVERT = Column(DECIMAL(10, 6), doc="月溢价")
    COVERTRATE = Column(DECIMAL(10, 6), doc="月溢价率")
    TRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastquotationweek(Base):

    __tablename__ = 'fund_mkt_lastquotationweek'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(14), primary_key=True, doc="交易周份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上周收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上周收盘价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="周开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="周最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="周最低价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    LOWDATE = Column(DateTime, doc="周最低价日")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="周收盘价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最低收盘价")
    AVGPRICE = Column(DECIMAL(10, 4), doc="周均价")
    CHANGE = Column(DECIMAL(10, 4), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="周涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="周换手率")
    AVGTURNOVERRATE = Column(DECIMAL(10, 6), doc="周平均换手率")
    VOLUME = Column(BIGINT, doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="周成交金额")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="周振幅")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    COVERT = Column(DECIMAL(10, 6), doc="周溢价")
    COVERTRATE = Column(DECIMAL(10, 6), doc="周溢价率")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_lastquotationyear(Base):

    __tablename__ = 'fund_mkt_lastquotationyear'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), primary_key=True, doc="交易年份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    OPENDATE = Column(DateTime, doc="年开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上年收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上年收盘价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="年开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="年最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="年最低价")
    HIGHDATE = Column(DateTime, doc="年最高价日")
    LOWDATE = Column(DateTime, doc="年最低价日")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="年收盘价")
    CLOSEDATE = Column(DateTime, doc="年收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最低收盘价")
    AVGPRICE = Column(DECIMAL(10, 4), doc="年均价")
    CHANGE = Column(DECIMAL(10, 4), doc="年涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="年涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="年换手率")
    AVGTURNOVERRATE = Column(DECIMAL(10, 6), doc="年平均换手率")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="年振幅")
    HIGHCLOSEDATE = Column(DateTime, doc="年最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="年最低收盘价日")
    COVERT = Column(DECIMAL(10, 6), doc="年溢价")
    COVERTRATE = Column(DECIMAL(10, 6), doc="年溢价率")
    TRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_quotation(Base):

    __tablename__ = 'fund_mkt_quotation'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    STATECODE = Column(String(40), doc="交易状态编码")
    AVGPRICE = Column(DECIMAL(10, 4), doc="均价")
    CHANGE = Column(DECIMAL(10, 4), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="换手率")
    AMPLITUDE = Column(DECIMAL(10, 6), doc="振幅")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    COVERT = Column(DECIMAL(10, 4), doc="溢价")
    COVERTRATE = Column(DECIMAL(10, 4), doc="溢价率")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    COMPARABLEPRICE = Column(DECIMAL(10, 6), doc="考虑现金红利的收盘价可比价格")
    SIMPLECOMPARABLEPRICE = Column(DECIMAL(10, 6), doc="不考虑现金红利的收盘价可比价格")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="总市值")
    CIRCULATEDSHARE = Column(DECIMAL(20, 2), doc="场内流通份额")


class fund_mkt_quotationlatest(Base):

    __tablename__ = 'fund_mkt_quotationlatest'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    STATECODE = Column(String(40), doc="交易状态编码")
    AVGPRICE = Column(DECIMAL(10, 4), doc="均价")
    CHANGE = Column(DECIMAL(10, 4), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="换手率")
    AMPLITUDE = Column(DECIMAL(10, 6), doc="振幅")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    COVERT = Column(DECIMAL(10, 4), doc="溢价")
    COVERTRATE = Column(DECIMAL(10, 4), doc="溢价率")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    COMPARABLEPRICE = Column(DECIMAL(10, 6), doc="考虑现金红利的收盘价可比价格")
    SIMPLECOMPARABLEPRICE = Column(DECIMAL(10, 6), doc="不考虑现金红利的收盘价可比价格")
    UPDATEID = Column(BIGINT, doc="数据ID")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="总市值")
    CIRCULATEDSHARE = Column(DECIMAL(20, 2), doc="场内流通份额")


class fund_mkt_quotationmonth(Base):

    __tablename__ = 'fund_mkt_quotationmonth'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    TRADINGMONTH = Column(String(14), doc="交易月份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    OPENDATE = Column(DateTime, doc="月开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上月收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上月收盘价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="月开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="月最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="月最低价")
    HIGHDATE = Column(DateTime, doc="月最高价日")
    LOWDATE = Column(DateTime, doc="月最低价日")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="月收盘价")
    CLOSEDATE = Column(DateTime, doc="月收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="月最低收盘价")
    AVGPRICE = Column(DECIMAL(10, 4), doc="月均价")
    CHANGE = Column(DECIMAL(10, 4), doc="月涨跌")
    CHANGERATIO = Column(DECIMAL(10, 4), doc="月涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="月换手率")
    AVGTURNOVERRATE = Column(DECIMAL(10, 6), doc="月平均换手率")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="月振幅")
    HIGHCLOSEDATE = Column(DateTime, doc="月最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="月最低收盘价日")
    COVERT = Column(DECIMAL(10, 6), doc="月溢价")
    COVERTRATE = Column(DECIMAL(10, 6), doc="月溢价率")
    TRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_quotationweek(Base):

    __tablename__ = 'fund_mkt_quotationweek'

    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    TRADINGWEEK = Column(String(14), doc="交易周份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上周收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上周收盘价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="周开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="周最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="周最低价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    LOWDATE = Column(DateTime, doc="周最低价日")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="周收盘价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="周最低收盘价")
    AVGPRICE = Column(DECIMAL(10, 4), doc="周均价")
    CHANGE = Column(DECIMAL(10, 4), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="周涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="周换手率")
    AVGTURNOVERRATE = Column(DECIMAL(10, 6), doc="周平均换手率")
    VOLUME = Column(BIGINT, doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="周成交金额")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="周振幅")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    COVERT = Column(DECIMAL(10, 6), doc="周溢价")
    COVERTRATE = Column(DECIMAL(10, 6), doc="周溢价率")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mkt_quotationyear(Base):

    __tablename__ = 'fund_mkt_quotationyear'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), doc="交易年份")
    SYMBOL = Column(String(12), doc="证券代码")
    FILLING = Column(String(20), doc="填充标识")
    OPENDATE = Column(DateTime, doc="年开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上年收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(10, 4), doc="上年收盘价")
    OPENPRICE = Column(DECIMAL(10, 4), doc="年开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="年最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="年最低价")
    HIGHDATE = Column(DateTime, doc="年最高价日")
    LOWDATE = Column(DateTime, doc="年最低价日")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="年收盘价")
    CLOSEDATE = Column(DateTime, doc="年收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(10, 4), doc="年最低收盘价")
    AVGPRICE = Column(DECIMAL(10, 4), doc="年均价")
    CHANGE = Column(DECIMAL(10, 4), doc="年涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="年涨跌幅")
    TURNOVERRATE = Column(DECIMAL(10, 6), doc="年换手率")
    AVGTURNOVERRATE = Column(DECIMAL(10, 6), doc="年平均换手率")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    AMPLITUDE = Column(DECIMAL(10, 2), doc="年振幅")
    HIGHCLOSEDATE = Column(DateTime, doc="年最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="年最低收盘价日")
    COVERT = Column(DECIMAL(10, 6), doc="年溢价")
    COVERTRATE = Column(DECIMAL(10, 6), doc="年溢价率")
    TRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    RETURNDAILY = Column(DECIMAL(10, 6), doc="考虑现金红利基金日回报率")
    SIMPLERETURNDAILY = Column(DECIMAL(10, 6), doc="不考虑现金红利基金日回报率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mktdayreturn(Base):

    __tablename__ = 'fund_mktdayreturn'

    MARKETTYPEID = Column(String(12), doc="基金市场类型编码")
    MARKETTYPE = Column(String(100), doc="基金市场类型")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    FILLING = Column(String(20), doc="填充标识")
    DAYTRDVOLUME = Column(DECIMAL(20, 2), doc="日交易量")
    DAYTRDVALUE = Column(DECIMAL(24, 4), doc="日交易金额")
    DAYCALFNDNUM = Column(INTEGER, doc="计算日市场回报率的有效基金数量")
    DAYAVERETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的日市场回报率（等权平均法）")
    DAYAVERETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的日市场回报率（等权平均法）")
    DAYWHTRETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的日市场回报率（总市值加权平均法）")
    DAYWHTRETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的日市场回报率（总市值加权平均法）")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mktmonthreturn(Base):

    __tablename__ = 'fund_mktmonthreturn'

    MARKETTYPEID = Column(String(12), doc="基金市场类型编码")
    MARKETTYPE = Column(String(100), doc="基金市场类型")
    TRADINGMONTH = Column(String(14), doc="交易月份")
    MTHCLOSEDATE = Column(DateTime, doc="月收盘日")
    MTHTRADINGDAYS = Column(SMALLINT, doc="月交易天数")
    MTHTRDVOLUME = Column(DECIMAL(20, 2), doc="月交易量")
    MTHTRDVALUE = Column(DECIMAL(24, 4), doc="月交易金额")
    MTHFNDVALUE = Column(DECIMAL(24, 4), doc="月市场基金总市值")
    MTHCALFNDNUM = Column(INTEGER, doc="计算月市场回报率的有效基金数量")
    MTHAVERETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的月市场回报率（等权平均法）")
    MTHAVERETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的月市场回报率（等权平均法）")
    MTHWHTRETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的月市场回报率（总市值加权平均法）")
    MTHWHTRETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的月市场回报率（总市值加权平均法）")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mktpf_pfm(Base):

    __tablename__ = 'fund_mktpf_pfm'

    TRADINGDATE = Column(DateTime, doc="统计日期")
    MKTPORTFOLIOID = Column(String(40), doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIORETURN = Column(DECIMAL(18, 6), doc="市场组合日回报率")
    MKTPFRISKPREMIUM = Column(DECIMAL(18, 6), doc="市场组合日风险溢价")
    MKTPFRISKPREMIUMSQUARE = Column(DECIMAL(18, 6), doc="市场组合日风险溢价的平方")
    MINMKTZERO = Column(DECIMAL(18, 6), doc="市场组合日风险溢价与0孰小")
    MAXMKTZERO = Column(DECIMAL(18, 6), doc="市场组合日风险溢价与0孰大")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mktpf_pfm_week(Base):

    __tablename__ = 'fund_mktpf_pfm_week'

    TRADINGDATE = Column(DateTime, primary_key=True, doc="统计日期")
    MKTPORTFOLIOID = Column(String(40), primary_key=True, doc="市场组合ID")
    MKTPORTFOLIO = Column(String(200), doc="市场组合名称")
    MKTPORTFOLIORETURN = Column(DECIMAL(18, 6), doc="市场组合周回报率")
    MKTPFRISKPREMIUM = Column(DECIMAL(18, 6), doc="市场组合周风险溢价")
    MKTPFRISKPREMIUMSQUARE = Column(DECIMAL(18, 6), doc="市场组合周风险溢价的平方")
    MINMKTZERO = Column(DECIMAL(18, 6), doc="市场组合周风险溢价与0孰小")
    MAXMKTZERO = Column(DECIMAL(18, 6), doc="市场组合周风险溢价与0孰大")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_mktweekreturn(Base):

    __tablename__ = 'fund_mktweekreturn'

    MARKETTYPEID = Column(String(12), doc="基金市场类型编码")
    MARKETTYPE = Column(String(100), doc="基金市场类型")
    TRADINGWEEK = Column(String(14), doc="交易周份")
    WKCLOSEDATE = Column(DateTime, doc="周收盘日")
    WKTRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    WKTRDVOLUME = Column(DECIMAL(20, 2), doc="周交易量")
    WKTRDVALUE = Column(DECIMAL(24, 4), doc="周交易金额")
    WKFNDVALUE = Column(DECIMAL(24, 4), doc="周市场基金总市值")
    WKCALFNDNUM = Column(INTEGER, doc="计算周市场回报率的有效基金数量")
    WKAVERETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的周市场回报率（等权平均法）")
    WKAVERETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的周市场回报率（等权平均法）")
    WKWHTRETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的周市场回报率（总市值加权平均法）")
    WKWHTRETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的周市场回报率（总市值加权平均法）")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_mktyearreturn(Base):

    __tablename__ = 'fund_mktyearreturn'

    MARKETTYPEID = Column(String(12), doc="基金市场类型编码")
    MARKETTYPE = Column(String(100), doc="基金市场类型")
    TRADINGYEAR = Column(String(14), doc="交易年份")
    YRCLOSEDATE = Column(DateTime, doc="年收盘日")
    YRTRADINGDAYS = Column(SMALLINT, doc="年交易天数")
    YRTRDVOLUME = Column(DECIMAL(20, 2), doc="年交易量")
    YRTRDVALUE = Column(DECIMAL(24, 4), doc="年交易金额")
    YRFNDVALUE = Column(DECIMAL(24, 4), doc="年市场基金总市值")
    YRCALFNDNUM = Column(INTEGER, doc="计算年市场回报率的有效基金数量")
    YRAVERETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的年市场回报率（等权平均法）")
    YRAVERETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的年市场回报率（等权平均法）")
    YRWHTRETREINV = Column(DECIMAL(10, 6), doc="考虑现金红利再投资的年市场回报率（总市值加权平均法）")
    YRWHTRETNONREINV = Column(DECIMAL(10, 6), doc="不考虑现金红利再投资的年市场回报率（总市值加权平均法）")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_nav(Base):

    __tablename__ = 'fund_nav'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="基金份额累计净值")
    ACHIEVERETURN = Column(DECIMAL(19, 4), doc="每万份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(19, 3), doc="7日年化收益率")
    FREQUENCY = Column(String(100), doc="频度属性")
    MARKETSTATUS = Column(String(100), doc="时间属性")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    MILLIONACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百万份基金已实现收益")
    CURRENCYCODE = Column(String(6), doc="货币编码")
    CURRENCY = Column(String(100), doc="币种")
    HUNDREDACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百份基金已实现收益")
    FUNDID = Column(DECIMAL(20, 0))


class fund_nav_month(Base):

    __tablename__ = 'fund_nav_month'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGMONTH = Column(String(14), doc="交易月份")
    SYMBOL = Column(String(20), doc="基金代码")
    STARTDATE = Column(DateTime, doc="月开始日期")
    PRVNAV = Column(DECIMAL(10, 4), doc="上月份额净值")
    PRVACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="上月份额累计净值")
    PRVACHIEVERETURN = Column(DECIMAL(10, 4), doc="上月每万份基金已实现收益")
    PRVANNUALIZEDYIELD = Column(DECIMAL(10, 4), doc="上月7日月化收益率")
    NAV = Column(DECIMAL(10, 4), doc="月份额净值")
    RETURNNAV = Column(DECIMAL(10, 4), doc="月份额净值增长率")
    ACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="月份额累计净值")
    RETURNACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="月份额累计净值增长率")
    ACHIEVERETURN = Column(DECIMAL(10, 4), doc="月每万份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(10, 4), doc="月7日月化收益率")
    TRADINGDAYS = Column(SMALLINT, doc="月净值批露天数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_nav_pfm(Base):

    __tablename__ = 'fund_nav_pfm'

    TRADINGDATE = Column(DateTime, doc="统计日期")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="基金份额累计净值")
    NAVGROWTHRATE = Column(DECIMAL(20, 6), doc="基金份额净值增长率")
    ACCUMULATIVENAVGROWTH = Column(DECIMAL(20, 6), doc="基金份额累计净值增长率")
    ADJUSTFACTOR = Column(DECIMAL(20, 6), doc="复权因子")
    ACCADJUSTFACTOR = Column(DECIMAL(20, 6), doc="累计复权因子")
    ADJUSTEDNAV = Column(DECIMAL(22, 6), doc="复权单位净值")
    ADJUSTEDNAVGROWTH = Column(DECIMAL(20, 6), doc="复权单位净值日增长率")
    RISKPREMIUM = Column(DECIMAL(20, 6), doc="复权净值日风险溢价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_nav_pfm_month(Base):

    __tablename__ = 'fund_nav_pfm_month'

    TRADINGDATE = Column(DateTime, doc="统计日期")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="月份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="月份额累计净值")
    ACCUMULATIVENAVGROWTH = Column(DECIMAL(20, 6), doc="基金份额累计净值月增长率")
    ADJUSTEDNAV = Column(DECIMAL(22, 6), doc="复权单位净值")
    ADJUSTEDNAVGROWTH = Column(DECIMAL(20, 6), doc="复权单位净值月增长率")
    RISKPREMIUM = Column(DECIMAL(20, 6), doc="复权净值月风险溢价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    TRADINGMONTH = Column(String(14), doc="交易月份")


class fund_nav_pfm_week(Base):

    __tablename__ = 'fund_nav_pfm_week'

    TRADINGDATE = Column(DateTime, doc="统计日期")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="周份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="周份额累计净值")
    ACCUMULATIVENAVGROWTH = Column(DECIMAL(20, 6), doc="基金份额累计净值周增长率")
    ADJUSTEDNAV = Column(DECIMAL(22, 6), doc="复权单位净值")
    ADJUSTEDNAVGROWTH = Column(DECIMAL(20, 6), doc="复权单位净值周增长率")
    RISKPREMIUM = Column(DECIMAL(20, 6), doc="复权净值周风险溢价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    TRADINGWEEK = Column(String(14), doc="交易周份")


class fund_nav_pfm_year(Base):

    __tablename__ = 'fund_nav_pfm_year'

    TRADINGDATE = Column(DateTime, doc="统计日期")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="年份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="年份额累计净值")
    ACCUMULATIVENAVGROWTH = Column(DECIMAL(20, 6), doc="基金份额累计净值年增长率")
    ADJUSTEDNAV = Column(DECIMAL(22, 6), doc="复权单位净值")
    ADJUSTEDNAVGROWTH = Column(DECIMAL(20, 6), doc="复权单位净值年增长率")
    RISKPREMIUM = Column(DECIMAL(20, 6), doc="复权净值年风险溢价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    TRADINGYEAR = Column(String(8), doc="交易年份")


class fund_nav_week(Base):

    __tablename__ = 'fund_nav_week'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(14), doc="交易周份")
    SYMBOL = Column(String(20), doc="基金代码")
    STARTDATE = Column(DateTime, doc="周开始日期")
    PRVNAV = Column(DECIMAL(10, 4), doc="上周份额净值")
    PRVACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="上周份额累计净值")
    PRVACHIEVERETURN = Column(DECIMAL(10, 4), doc="上周每万份基金已实现收益")
    PRVANNUALIZEDYIELD = Column(DECIMAL(10, 4), doc="上周7日年化收益率")
    NAV = Column(DECIMAL(10, 4), doc="周份额净值")
    RETURNNAV = Column(DECIMAL(10, 4), doc="周份额净值增长率")
    ACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="周份额累计净值")
    RETURNACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="周份额累计净值增长率")
    ACHIEVERETURN = Column(DECIMAL(10, 4), doc="周每万份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(10, 4), doc="周7日年化收益率")
    TRADINGDAYS = Column(SMALLINT, doc="周净值批露天数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_nav_year(Base):

    __tablename__ = 'fund_nav_year'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGYEAR = Column(String(14), doc="交易年份")
    SYMBOL = Column(String(20), doc="基金代码")
    STARTDATE = Column(DateTime, doc="年开始日期")
    PRVNAV = Column(DECIMAL(10, 4), doc="上年份额净值")
    PRVACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="上年份额累计净值")
    PRVACHIEVERETURN = Column(DECIMAL(10, 4), doc="上年每万份基金已实现收益")
    PRVANNUALIZEDYIELD = Column(DECIMAL(10, 4), doc="上年7日年化收益率")
    NAV = Column(DECIMAL(10, 4), doc="年份额净值")
    RETURNNAV = Column(DECIMAL(10, 4), doc="年份额净值增长率")
    ACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="年份额累计净值")
    RETURNACCUMULATIVENAV = Column(DECIMAL(10, 4), doc="年份额累计净值增长率")
    ACHIEVERETURN = Column(DECIMAL(10, 4), doc="年每万份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(10, 4), doc="年7日年化收益率")
    TRADINGDAYS = Column(SMALLINT, doc="年净值批露天数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_performance_compare(Base):

    __tablename__ = 'fund_performance_compare'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STAGE = Column(String(100), doc="阶段")
    NAVGROWTH = Column(DECIMAL(13, 4), doc="净值增长率")
    NAVGROWTHSTDEV = Column(DECIMAL(13, 4), doc="净值增长率标准差")
    RETURN = Column(DECIMAL(13, 4), doc="净值收益率")
    RETURNSTDEV = Column(DECIMAL(13, 4), doc="净值收益率标准差")
    BENCHMARKRETURN = Column(DECIMAL(13, 4), doc="业绩比较基准收益率")
    BENCHMARKRETURNSTDEV = Column(DECIMAL(13, 4), doc="业绩比较基准收益率标准差")
    NAVGROWTHMINUSBENCHMARK = Column(DECIMAL(13, 4), doc="净值增长率减去业绩比较基准收益率")
    NAVGROWTHSTDEVMINUSBENCHMARK = Column(DECIMAL(13, 4), doc="净值增长率标准差减去业绩比较基准收益率标准差")
    RETURNMINUSBENCHMARK = Column(DECIMAL(13, 4), doc="净值收益率减去业绩比较基准收益率")
    RETURNSTDEVMINUSBENCHMARK = Column(DECIMAL(13, 4), doc="净值收益率标准差减去业绩比较基准收益率标准差")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    SYMBOL = Column(String(20), doc="基金代码")


class fund_performance_deviation(Base):

    __tablename__ = 'fund_performance_deviation'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    DEVIATIONTIMES = Column(DECIMAL(20, 2), doc="报告期内偏离度的绝对值在0.5％（含）以上的次数")
    OCCURRINGTIMES = Column(DECIMAL(20, 2), doc="报告期内偏离度的绝对值在0.25％（含）-0.5％间的次数")
    MAXDEVIATION = Column(DECIMAL(10, 4), doc="报告期内偏离度的最高值")
    MINDEVIATION = Column(DECIMAL(10, 4), doc="报告期内偏离度的最低值")
    MEANDEVIATION = Column(DECIMAL(10, 4), doc="报告期内每个工作日偏离度的绝对值的简单平均值")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_portfolio_abs(Base):

    __tablename__ = 'fund_portfolio_abs'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="统计截止日期")
    RANK = Column(INTEGER, doc="排名")
    FULLNAME = Column(String(300), doc="资产支持证券品种名称")
    SYMBOL = Column(String(20), doc="证券代码")
    SHARES = Column(DECIMAL(20, 2), doc="持有数量")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="持有市值")
    PROPORTION = Column(DECIMAL(10, 4), doc="占净值比例 （%）")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_portfolio_bondcredit(Base):

    __tablename__ = 'fund_portfolio_bondcredit'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    BONDCREDITRATING = Column(String(100), doc="债券信用等级")
    FAIRVALUE = Column(DECIMAL(19, 2), doc="公允价值")
    FAIRTONAV = Column(DECIMAL(18, 2), doc="占基金资产净值的比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_portfolio_bondvariety(Base):

    __tablename__ = 'fund_portfolio_bondvariety'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(String(4), doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    CROSSCODE = Column(String(2), doc="横表编码")
    CROSSNAME_EN = Column(String(30), doc="横表名称（英文）")
    TREASURYBOND = Column(DECIMAL(20, 2), doc="国家债券")
    CENTRALBANKBILLS = Column(DECIMAL(20, 2), doc="央行票据")
    FINANCIALBONDS = Column(DECIMAL(20, 2), doc="金融债券")
    POLICYFINANCIALBONDS = Column(DECIMAL(20, 2), doc="其中政策性金融债")
    CORPORATEBONDS = Column(DECIMAL(20, 2), doc="企业债券")
    SHORTTERMFINANCINGBILLS = Column(DECIMAL(20, 2), doc="企业短期融资券")
    CONVERTIBLEBONDS = Column(DECIMAL(20, 2), doc="可转债")
    OTHERBOND = Column(DECIMAL(20, 2), doc="其他债券")
    TOTALBOND = Column(DECIMAL(20, 2), doc="债券合计")
    FLOATINGRATEBONDS = Column(DECIMAL(20, 2), doc="剩余存续期超过397天的浮动利率债券")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CROSSNAME = Column(String(30))
    UPDATETIME_EN = Column(DateTime)


class fund_portfolio_currency(Base):

    __tablename__ = 'fund_portfolio_currency'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(String(4), doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    CROSSCODE = Column(SMALLINT, doc="横表编码")
    CROSSNAME = Column(String(60), doc="横表名称")
    DAY30 = Column(DECIMAL(10, 4), doc="30天以内资产占基金资产净值的比例")
    DAY30MATURITY397 = Column(DECIMAL(10, 4), doc="其中：30天以内剩余存续期超过397天的浮动利率债占基金资产净值的比例")
    DAY60 = Column(DECIMAL(10, 4), doc="30天(含)-60天资产占基金资产净值的比例")
    DAY60MATURITY397 = Column(DECIMAL(10, 4), doc="其中30天(含)-60天：剩余存续期超过397天的浮动利率债占基金资产净值的比例")
    DAY90 = Column(DECIMAL(10, 4), doc="60天(含)-90天资产占基金资产净值的比例")
    DAY90MATURITY397 = Column(DECIMAL(10, 4), doc="其中：60天(含)-90天剩余存续期超过397天的浮动利率债占基金资产净值的比例")
    DAY180 = Column(DECIMAL(10, 4), doc="90天(含)-180天资产占基金资产净值的比例")
    DAY180MATURITY397 = Column(DECIMAL(10, 4), doc="其中：90天(含)-180天剩余存续期超过397天的浮动利率债占基金资产净值的比例")
    DAY397 = Column(DECIMAL(10, 4), doc="180天(含)-397天(含)资产占基金资产净值的比例")
    DAY397MATURITY397 = Column(DECIMAL(10, 4), doc="其中：180天(含)-397天(含)剩余存续期超过397天的浮动利率债占基金资产净值的比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    DAY120 = Column(DECIMAL(10, 4), doc="90天(含)-120天资产占基金资产净值的比例（%）")
    DAY120MATURITY397 = Column(DECIMAL(10, 4), doc="其中：90天(含)-120天剩余存续期超过397天的浮动利率债占基金资产净值的比例（%）")
    DAY397TWO = Column(DECIMAL(10, 4), doc="120天(含)-397天(含)资产占基金资产净值的比例（%）")
    DAY397MATURITY397TWO = Column(DECIMAL(10, 4), doc="其中：120天(含)-397天(含)剩余存续期超过397天的浮动利率债占基金资产净值的比例（%）")


class fund_portfolio_stock(Base):

    __tablename__ = 'fund_portfolio_stock'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="统计截止日期")
    INVESTMENTTYPE = Column(SMALLINT, doc="投资类型分类")
    RANK = Column(INTEGER, doc="排名")
    SYMBOL = Column(String(60), doc="股票代码")
    SHARES = Column(DECIMAL(20, 2), doc="持股数量")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="持股市值")
    PROPORTION = Column(DECIMAL(10, 4), doc="占净值比例 ")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    STOCKNAME = Column(String(400), doc="股票名称")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")


class fund_pretrdinfo(Base):

    __tablename__ = 'fund_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), primary_key=True, doc="证券代码")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    SHORTNAME = Column(String(100), doc="基金简称")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    TRADINGSHORTNAME = Column(String(100), doc="证券简称")
    INCEPTIONSHARES = Column(DECIMAL(20, 2), doc="基金成立时份额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_pretrdinfohistory(Base):

    __tablename__ = 'fund_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), primary_key=True, doc="证券代码")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    SHORTNAME = Column(String(100), doc="基金简称")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    TRADINGSHORTNAME = Column(String(100), doc="证券简称")
    INCEPTIONSHARES = Column(DECIMAL(20, 2), doc="基金成立时份额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    MINTICKSIZE = Column(DECIMAL(10, 4), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_promoter(Base):

    __tablename__ = 'fund_promoter'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    FULLNAME = Column(String(120), doc="公司名称")
    ESTABLISHDATE = Column(DateTime, doc="公司成立日期")
    REGISTERCAPITAL = Column(DECIMAL(20, 2), doc="公司注册资本")
    ORGANIZATIONTYPEID = Column(String(100), doc="公司组织形式编码")
    ORGANIZATIONTYPE = Column(String(100), doc="公司组织形式")
    COMPANYPROPERTIES = Column(String(100), doc="公司属性")
    LEGALREPRESENTATIVE = Column(String(100), doc="公司法定代表人")
    TEL = Column(String(100), doc="公司电话号码")
    ZIPCODE = Column(String(100), doc="公司邮编")
    FAX = Column(String(100), doc="公司传真")
    WSBSITE = Column(String(100), doc="公司网址")
    REGISTERADDRESS = Column(String(200), doc="公司注册地址")
    OFFICEADDRESS = Column(String(200), doc="公司办公地址")
    BUSINESSLICENSENO = Column(String(40), doc="公司营业执照注册号")
    MAIL = Column(String(80), doc="公司电子邮箱")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CONTACTS = Column(String(100))


class fund_prospectuses(Base):

    __tablename__ = 'fund_prospectuses'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    IPOSTPBDT = Column(DateTime, doc="招募说明书发表日期")
    ACCOUNTINGFIRMID = Column(DECIMAL(20, 0), doc="会计师事务所ID")
    ACCOUNTINGFIRMNAME = Column(String(200), doc="会计师事务所名称")
    ACCOUNTANT = Column(String(200), doc="经办会计师")
    LAWFIRMID = Column(DECIMAL(20, 0), doc="律师事务所ID")
    LAWFIRMNAME = Column(String(200), doc="律师事务所名称")
    LAWYER = Column(String(200), doc="经办律师")
    ISSUEMODE = Column(String(40), doc="募集方式")
    STARTDATE = Column(DateTime, doc="募集起始日")
    ENDDATE = Column(DateTime, doc="募集截止日")
    ISSUEPRICE = Column(DECIMAL(10, 4), doc="发行价格")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    CURRENCY = Column(String(100), doc="发行价格币种")
    SUBSCRIPTIONMODE = Column(String(240), doc="认购方式")
    INDIVIDUALINVESTORS = Column(DECIMAL(16, 2), doc="个人投资者认购下限")
    INSTITUTIONALINVESTORS = Column(DECIMAL(16, 2), doc="机构投资者认购下限")
    ISSUESIZE = Column(DECIMAL(20, 2), doc="募集规模下限")
    OBJECT = Column(String(200), doc="募集对象")
    INCEPTIONTNA = Column(DECIMAL(20, 2), doc="设立募集期募集的基金份额")
    PURCHASEHOUSEHOLDERS = Column(BIGINT, doc="总有效申购户数")
    NETSALES = Column(DECIMAL(20, 4), doc="发行净销售额")
    INTEREST = Column(DECIMAL(20, 4), doc="银行利息")
    ACTUALTOTALFLOTATIONCOSTS = Column(DECIMAL(20, 4), doc="总发行费用")
    PROMOTERSUBSCRIPTION = Column(DECIMAL(20, 4), doc="基金发起人认购基金单位份额")
    SUCCESSRATE = Column(DECIMAL(20, 4), doc="中签率")
    OVERSUBSCRIPTIONRATIO = Column(DECIMAL(20, 4), doc="发行超额认购倍数")
    RELEASECOORDINATOR = Column(String(100), doc="发行协调人")
    UPDATEID = Column(BIGINT, doc="数据ID")
    ISSUEMODEID = Column(String(40), doc="募集方式编码")
    MAXISSUESIZE = Column(DECIMAL(20, 2), doc="募集规模上限")


class fund_ptf_bondspe(Base):

    __tablename__ = 'fund_ptf_bondspe'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    SPECIESNAME = Column(String(200), doc="债券品种")
    FAIRVALUE = Column(DECIMAL(20, 2), doc="公允价值")
    AMORTIZEDCOST = Column(DECIMAL(20, 2), doc="摊余成本")
    FAIRVALUETONAV = Column(DECIMAL(20, 2), doc="占基金资产净值比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_ptf_bsstock(Base):

    __tablename__ = 'fund_ptf_bsstock'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    CHANGETYPE = Column(String(2), doc="变动类型")
    RANK = Column(INTEGER, doc="排名")
    SYMBOL = Column(String(60), doc="股票代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    STOCKNAME = Column(String(400), doc="股票名称")
    NAMEENG = Column(String(800), doc="公司名称(英文)")
    BSVALUE = Column(DECIMAL(20, 2), doc="买卖金额")
    PROPORTION = Column(DECIMAL(10, 4), doc="占基金资产净值比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_ptf_bsstocktotal(Base):

    __tablename__ = 'fund_ptf_bsstocktotal'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    BUYVALUE = Column(DECIMAL(20, 2), doc="买入股票的成本总额")
    SELLVALUE = Column(DECIMAL(20, 2), doc="卖出股票的收入总额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_ptf_der(Base):

    __tablename__ = 'fund_ptf_der'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    RANK = Column(INTEGER, doc="排名")
    TYPEID = Column(String(40), doc="衍生品类别ID")
    TYPE = Column(String(200), doc="衍生品类别")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DERIVATIVENAME = Column(String(400), doc="衍生品名称")
    FAIRVALUE = Column(DECIMAL(20, 2), doc="公允价值")
    PROPORTION = Column(DECIMAL(10, 4), doc="占基金资产净值比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_ptf_fund(Base):

    __tablename__ = 'fund_ptf_fund'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    RANK = Column(INTEGER, doc="排名")
    TYPEID = Column(String(40), doc="基金类型ID")
    TYPE = Column(String(200), doc="基金类型")
    MODELID = Column(String(40), doc="运作方式ID")
    MODEL = Column(String(1000), doc="运作方式")
    MANAGER = Column(String(1000), doc="基金管理人")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    FUNDNAME = Column(String(400), doc="基金名称")
    FAIRVALUE = Column(DECIMAL(20, 2), doc="公允价值")
    PROPORTION = Column(DECIMAL(10, 4), doc="占基金资产净值比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    SYMBOL = Column(String(20), doc="基金代码")


class fund_purchredchg(Base):

    __tablename__ = 'fund_purchredchg'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    MASTERFUNDCODE = Column(String(6), doc="基金主代码")
    SYMBOL = Column(String(6), doc="基金代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    PURCHASESTATUS = Column(SMALLINT, doc="申购状态")
    REDEEMSTATUS = Column(SMALLINT, doc="赎回状态")
    SUSPLARGEPURMAX = Column(DECIMAL(20, 2), doc="暂停大额申购上限")
    CHANGEDATE = Column(DateTime, doc="变更日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CURRENCY = Column(String(3), doc="币种")


class fund_quotation(Base):

    __tablename__ = 'fund_quotation'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="证券代码")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    AVGPRICE = Column(DECIMAL(10, 4), doc="均价")
    CHANGE = Column(DECIMAL(10, 4), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 6), doc="涨跌幅")
    AMPLITUDE = Column(DECIMAL(10, 6), doc="振幅")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_reportdate(Base):

    __tablename__ = 'fund_reportdate'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    REPORTTYPEID = Column(SMALLINT, doc="报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="统计截止日期")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")


class fund_resolution(Base):

    __tablename__ = 'fund_resolution'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), primary_key=True, doc="基金代码")
    DECLAREDATE = Column(DateTime, primary_key=True, doc="公告日期")
    SPLITDATE = Column(DateTime, doc="折算基准日")
    SPLITRECORDDATE = Column(DateTime, doc="拆分折算日")
    SPLITDOBJECT = Column(String(200), doc="拆分对象")
    RESULTANNOUNCEMENT = Column(DateTime, doc="拆分结果公告日")
    SPLITNAV_BEFORE = Column(DECIMAL(20, 6), doc="拆分前基金份额净值")
    SHARESBEFORE = Column(DECIMAL(20, 2), doc="拆分前份额")
    SHARESAFTER = Column(DECIMAL(20, 2), doc="拆分后份额")
    SHARESAFTERADJUST = Column(DECIMAL(19, 6), doc="拆分后基金份额净值调整")
    CURRENCYCODE = Column(String(6), doc="币种编码")
    CURRENCY = Column(String(100), doc="币种")
    SPLITRATIO = Column(DECIMAL(19, 6), doc="基金份额分拆比例")
    SPLITDESCRIPTION = Column(String(4000), doc="拆分说明")
    UPDATEID = Column(BIGINT, doc="数据ID")
    CONVERSIONRATIO = Column(DECIMAL(19, 10), doc="折算比例")


class fund_sharechange(Base):

    __tablename__ = 'fund_sharechange'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    ESTABLISHDATESHARES = Column(DECIMAL(20, 2), doc="基金合同生效日总份额")
    TOTALBEGINNINGFUNDSHARE = Column(DECIMAL(20, 2), doc="本期期初份额")
    TOTALPURCHASEFUNDSHARE = Column(DECIMAL(20, 2), doc="本期申购份额")
    TOTALREDEMPTIONFUNDSHARE = Column(DECIMAL(20, 2), doc="本期赎回份额")
    FUNDSPLITCHANGESHARE = Column(DECIMAL(20, 2), doc="本期基金拆分变动份额")
    ENDDATESHARES = Column(DECIMAL(20, 2), doc="期末总份额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_shareholdercompany(Base):

    __tablename__ = 'fund_shareholdercompany'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    FUNDCOMPANYID = Column(DECIMAL(20, 0), doc="基金管理公司ID")
    FUNDCOMPANYNAME = Column(String(200), doc="基金管理公司名称")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    TOTALSHARE = Column(DECIMAL(20, 2), doc="股本")
    INSTITUTIONHOLDERID = Column(DECIMAL(20, 0), doc="管理公司股东ID")
    FULLNAME = Column(String(200), doc="管理公司股东名称")
    SHARES = Column(DECIMAL(20, 2), doc="管理公司股东持股数量")
    PERCENTAGEHOLDING = Column(DECIMAL(10, 4), doc="持股比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_shsecrate(Base):

    __tablename__ = 'fund_shsecrate'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    FUNDNAME = Column(String(150), doc="基金名称")
    FUNDTYPE = Column(String(60), doc="基金类型")
    REPPD = Column(SMALLINT, doc="报告周期")
    INFOPUBDT = Column(DateTime, doc="信息发布日期")
    NAV = Column(DECIMAL(20, 4), doc="单位净值")
    NAVGROWTHLASTQTR = Column(DECIMAL(10, 4), doc="上季度净值增长率")
    GROWTHTOBCHMKLASTQTR = Column(DECIMAL(10, 4), doc="上季度相对基准增长率")
    NAVGROWTHTHISQTR = Column(DECIMAL(10, 4), doc="本季度净值增长率")
    GROWTHTOBCHMKTHISQTR = Column(DECIMAL(10, 4), doc="本季度相对基准增长率")
    NAVGROWTHLASTYR = Column(DECIMAL(10, 4), doc="上一年净值增长率")
    GROWTHTOBCHMKLASTYR = Column(DECIMAL(10, 4), doc="上一年相对基准增长率")
    NAVGROWTHTHISYR = Column(DECIMAL(10, 4), doc="本年以来净值增长率")
    GROWTHTOBCHMKTHISYR = Column(DECIMAL(10, 4), doc="本年以来相对基准增长率")
    NAVGROWTH3YR = Column(DECIMAL(10, 4), doc="三年净值增长率")
    GROWTHTOBCHMK3YR = Column(DECIMAL(10, 4), doc="三年相对基准增长率")
    NAVGROWTH5YR = Column(DECIMAL(10, 4), doc="五年净值增长率")
    GROWTHTOBCHMK5YR = Column(DECIMAL(10, 4), doc="五年相对基准增长率")
    NAVGROWTHSINSET = Column(DECIMAL(10, 4), doc="成立以来净值增长率")
    GROWTHTOBCHMKSINSET = Column(DECIMAL(10, 4), doc="成立以来相对基准增长率")
    COMPRT3YR = Column(SMALLINT, doc="最新综合评级(三年)")
    CHANGERATE3YR = Column(String(20), doc="评级变动(三年)")
    STKSELABI3YR = Column(SMALLINT, doc="选证能力(三年)")
    TIMINGABI3YR = Column(SMALLINT, doc="择时能力(三年)")
    SHARP3YR = Column(SMALLINT, doc="夏普比率(三年)")
    COMPRT5YR = Column(SMALLINT, doc="最新综合评级(五年)")
    CHANGERATE5YR = Column(String(20), doc="评级变动(五年)")
    STKSELABI5YR = Column(SMALLINT, doc="选证能力(五年)")
    TIMINGABI5YR = Column(SMALLINT, doc="择时能力(五年)")
    SHARP5YR = Column(SMALLINT, doc="夏普比率(五年)")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_stracontract(Base):

    __tablename__ = 'fund_stracontract'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="A类份额ID")
    SYMBOL = Column(String(12), doc="A类份额代码")
    ANNOUNCEMENTDATE = Column(DateTime, doc="公告日期")
    IMPLEMENTATIONDATE = Column(DateTime, doc="实施日期")
    CONTRACTRETURNRATE = Column(DECIMAL(10, 6), doc="约定年基准收益率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_stractshare(Base):

    __tablename__ = 'fund_stractshare'

    ENDDATE = Column(DateTime, doc="截止日期")
    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    MASTERFUNDCODE = Column(String(40), doc="基金代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(40), doc="指数代码")
    ACTIVESHARE = Column(DECIMAL(10, 6), doc="主动份额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strader(Base):

    __tablename__ = 'fund_strader'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="基金代码")
    COVERT = Column(DECIMAL(10, 4), doc="溢价")
    COVERTRATE = Column(DECIMAL(10, 4), doc="溢价率")
    NAVCHANGERATIO = Column(DECIMAL(10, 6), doc="净值涨跌幅")
    CPCHANGERATIO = Column(DECIMAL(10, 6), doc="收盘涨跌幅")
    CONTRACTRETURNRATE = Column(DECIMAL(10, 6), doc="约定收益率")
    IMPLICITYIELD = Column(DECIMAL(10, 6), doc="隐含收益率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strainfo(Base):

    __tablename__ = 'fund_strainfo'

    AFUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="A类份额ID")
    ASYMBOL = Column(String(12), doc="A类份额代码")
    ASHORTNAME = Column(String(100), doc="A类份额简称")
    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    ISPRIMARYMARKET = Column(SMALLINT, doc="是否一级市场交易")
    ISSECONDARYMARKET = Column(SMALLINT, doc="是否二级市场交易")
    PARVALUE = Column(DECIMAL(10, 4), doc="面值")
    CURRENCYCODE = Column(String(40), doc="面值币种编码")
    INCEPTIONDATE = Column(DateTime, doc="份额成立日期")
    MATURITYDATE = Column(DateTime, doc="份额到期日")
    DURATION = Column(SMALLINT, doc="封闭年限")
    CYCLE = Column(String(40), doc="申购赎回周期")
    CLOSEDSTARTDATE = Column(DateTime, doc="封闭期起始日期")
    CLOSEDENDDATE = Column(DateTime, doc="封闭期截止日期")
    LISTINGDATE = Column(DateTime, doc="上市日期")
    EXCHANGECODE = Column(String(40), doc="上市交易所")
    TRANSITIONSTARTDATE = Column(DateTime, doc="转换开始日期")
    PURCHASESTARTDATE = Column(DateTime, doc="申购起始日")
    REDEEMSTARTDATE = Column(DateTime, doc="赎回起始日")
    PURCHASESTATUS = Column(String(40), doc="申购状态")
    REDEEMSTATUS = Column(String(40), doc="赎回状态")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_stranav(Base):

    __tablename__ = 'fund_stranav'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="基金份额累计净值")
    ACHIEVERETURN = Column(DECIMAL(19, 4), doc="每万份基金已实现收益")
    MILLIONACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百万份基金已实现收益")
    HUNDREDACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(19, 3), doc="7日年化收益率")
    FREQUENCY = Column(String(100), doc="频度属性")
    MARKETSTATUS = Column(String(100), doc="时间属性")
    CURRENCYCODE = Column(String(6), doc="货币编码")
    CURRENCY = Column(String(100), doc="币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_straquotation(Base):

    __tablename__ = 'fund_straquotation'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="基金代码")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    FILLING = Column(String(20), doc="填充标识")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strbder(Base):

    __tablename__ = 'fund_strbder'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="基金代码")
    COVERT = Column(DECIMAL(10, 4), doc="溢价")
    COVERTRATE = Column(DECIMAL(10, 4), doc="溢价率")
    NAVCHANGERATIO = Column(DECIMAL(10, 6), doc="净值涨跌幅")
    CPCHANGERATIO = Column(DECIMAL(10, 6), doc="收盘涨跌幅")
    NAVLEVERAGE = Column(DECIMAL(10, 6), doc="净值杠杆率")
    CPLEVERAGE = Column(DECIMAL(10, 6), doc="价格杠杆率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strbinfo(Base):

    __tablename__ = 'fund_strbinfo'

    BFUNDCLASSID = Column(DECIMAL(20, 0), primary_key=True, doc="B类份额ID")
    BSYMBOL = Column(String(12), doc="B类份额代码")
    BSHORTNAME = Column(String(100), doc="B类份额简称")
    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    ISPRIMARYMARKET = Column(SMALLINT, doc="是否一级市场交易")
    ISSECONDARYMARKET = Column(SMALLINT, doc="是否二级市场交易")
    PARVALUE = Column(DECIMAL(10, 4), doc="面值")
    CURRENCYCODE = Column(String(40), doc="面值币种编码")
    INCEPTIONDATE = Column(DateTime, doc="份额成立日期")
    MATURITYDATE = Column(DateTime, doc="份额到期日")
    DURATION = Column(SMALLINT, doc="封闭年限")
    CYCLE = Column(String(40), doc="申购赎回周期")
    CLOSEDSTARTDATE = Column(DateTime, doc="封闭期起始日期")
    CLOSEDENDDATE = Column(DateTime, doc="封闭期截止日期")
    LISTINGDATE = Column(DateTime, doc="上市日期")
    EXCHANGECODE = Column(String(40), doc="上市交易所")
    TRANSITIONSTARTDATE = Column(DateTime, doc="转换开始日期")
    PURCHASESTARTDATE = Column(DateTime, doc="申购起始日")
    REDEEMSTARTDATE = Column(DateTime, doc="赎回起始日")
    PURCHASESTATUS = Column(String(40), doc="申购状态")
    REDEEMSTATUS = Column(String(40), doc="赎回状态")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_strbnav(Base):

    __tablename__ = 'fund_strbnav'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="基金份额累计净值")
    ACHIEVERETURN = Column(DECIMAL(19, 4), doc="每万份基金已实现收益")
    MILLIONACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百万份基金已实现收益")
    HUNDREDACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(19, 3), doc="7日年化收益率")
    FREQUENCY = Column(String(100), doc="频度属性")
    MARKETSTATUS = Column(String(100), doc="时间属性")
    CURRENCYCODE = Column(String(6), doc="货币编码")
    CURRENCY = Column(String(100), doc="币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strbquotation(Base):

    __tablename__ = 'fund_strbquotation'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="基金代码")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    FILLING = Column(String(20), doc="填充标识")
    OPENPRICE = Column(DECIMAL(10, 4), doc="开盘价")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="最低价")
    CLOSEPRICE = Column(DECIMAL(10, 4), doc="收盘价")
    VOLUME = Column(DECIMAL(18, 2), doc="成交量")
    AMOUNT = Column(DECIMAL(20, 4), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 4), doc="前收盘价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strinfo(Base):

    __tablename__ = 'fund_strinfo'

    FUNDID = Column(DECIMAL(20, 0), primary_key=True, doc="基金ID")
    MASTERFUNDCODE = Column(String(12), doc="母基金代码")
    FULLNAME = Column(String(200), doc="基金全称")
    AFUNDCLASSID = Column(DECIMAL(20, 0), doc="A类份额ID")
    ASYMBOL = Column(String(12), doc="A类份额代码")
    ASHORTNAME = Column(String(100), doc="A类份额简称")
    BFUNDCLASSID = Column(DECIMAL(20, 0), doc="B类份额ID")
    BSYMBOL = Column(String(12), doc="B类份额代码")
    BSHORTNAME = Column(String(100), doc="B类份额简称")
    FUNDCOMPANY = Column(String(200), doc="基金管理公司名称")
    CATEGORYID = Column(String(100), doc="基金类别ID")
    FUNDSTATUS = Column(String(40), doc="基金状态")
    ACONTRACTRETURNRATE = Column(String(400), doc="A类份额约定收益率")
    RGLCONVTDATE = Column(String(400), doc="定期份额折算基准日")
    RGLCONVTFREQUENCY = Column(String(200), doc="定期折算频率")
    IRGLCONVUPPER = Column(DECIMAL(10, 6), doc="触发不定期份额折算条件的基础份额净值上限")
    IRGLCONVLOWER = Column(DECIMAL(10, 6), doc="触发不定期份额折算条件的B份额净值下限")
    ASHARERATIO = Column(DECIMAL(10, 6), doc="A类份额初始配比")
    BSHARERATIO = Column(DECIMAL(10, 6), doc="B类份额初始配比")
    EFFECTIVEDATE = Column(DateTime, doc="基金合同生效日期")
    CONVTLOFDATE = Column(DateTime, doc="转为LOF日期")
    LISTINGDATE = Column(DateTime, doc="上市日期")
    EXCHANGECODE = Column(String(40), doc="上市交易所")
    ISETF = Column(SMALLINT, doc="母基金是否ETF")
    ISINDEXFUND = Column(SMALLINT, doc="母基金是否指数基金")
    INDEXID = Column(DECIMAL(20, 0), doc="挂钩指数ID")
    INDEXCODE = Column(String(20), doc="挂钩指数代码")
    INDEXFULLNAME = Column(String(200), doc="指数中文全称")
    UPDATEID = Column(BIGINT, doc="数据ID")


class fund_strmder(Base):

    __tablename__ = 'fund_strmder'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="基金代码")
    COVERT = Column(DECIMAL(10, 4), doc="溢价")
    COVERTRATE = Column(DECIMAL(10, 4), doc="溢价率")
    NAVCHANGERATIO = Column(DECIMAL(10, 6), doc="净值涨跌幅")
    CPCHANGERATIO = Column(DECIMAL(10, 6), doc="收盘涨跌幅")
    INDEXCLOSEPRICE = Column(DECIMAL(18, 3), doc="跟踪指数收盘价")
    INDEXCHANGERATIO = Column(DECIMAL(18, 6), doc="跟踪指数涨跌幅")
    NAVTRACKINGERROR = Column(DECIMAL(10, 6), doc="净值增长相对指数偏离")
    CPTRACKINGERROR = Column(DECIMAL(10, 6), doc="收盘涨跌相对指数偏离")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strmnav(Base):

    __tablename__ = 'fund_strmnav'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="基金代码")
    NAV = Column(DECIMAL(20, 4), doc="基金净值")
    ACCUMULATIVENAV = Column(DECIMAL(20, 4), doc="基金累计净值")
    ACHIEVERETURN = Column(DECIMAL(19, 4), doc="每万份基金已实现收益")
    MILLIONACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百万份基金已实现收益")
    HUNDREDACHIEVERETURN = Column(DECIMAL(19, 4), doc="每百份基金已实现收益")
    ANNUALIZEDYIELD = Column(DECIMAL(19, 3), doc="7日年化收益率")
    CURRENCYCODE = Column(String(6), doc="货币编码")
    CURRENCY = Column(String(100), doc="币种")
    FREQUENCY = Column(String(100), doc="频度属性")
    MARKETSTATUS = Column(String(100), doc="时间属性")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strmquotation(Base):

    __tablename__ = 'fund_strmquotation'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="基金代码")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    FILLING = Column(String(20), doc="填充标识")
    OPEN = Column(DECIMAL(10, 3), doc="今开盘价")
    HIGH = Column(DECIMAL(10, 3), doc="今最高价")
    LOW = Column(DECIMAL(10, 3), doc="今最低价")
    CLOSE = Column(DECIMAL(10, 3), doc="今收盘价")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 0), doc="成交金额")
    LASTCLOSE = Column(DECIMAL(10, 3), doc="昨收盘价")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strtrackamonth(Base):

    __tablename__ = 'fund_strtrackamonth'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(40), doc="基金代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    INDEXCODE = Column(String(40), doc="挂钩指数代码")
    CPTRACKINGERROR = Column(DECIMAL(10, 6), doc="不考虑现金红利收盘涨跌相对指数偏离")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strtrackaweek(Base):

    __tablename__ = 'fund_strtrackaweek'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(40), doc="基金代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    INDEXCODE = Column(String(40), doc="挂钩指数代码")
    CPTRACKINGERROR = Column(DECIMAL(10, 6), doc="不考虑现金红利收盘涨跌相对指数偏离")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strtrackbmonth(Base):

    __tablename__ = 'fund_strtrackbmonth'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(40), doc="基金代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    INDEXCODE = Column(String(40), doc="挂钩指数代码")
    CPTRACKINGERROR = Column(DECIMAL(10, 6), doc="不考虑现金红利收盘涨跌相对指数偏离")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_strtrackbweek(Base):

    __tablename__ = 'fund_strtrackbweek'

    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(40), doc="基金代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    INDEXCODE = Column(String(40), doc="挂钩指数代码")
    CPTRACKINGERROR = Column(DECIMAL(10, 6), doc="不考虑现金红利收盘涨跌相对指数偏离")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_tenholders(Base):

    __tablename__ = 'fund_tenholders'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    REPORTTYPEID = Column(SMALLINT, doc="定期报告类别编码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    RANKING = Column(INTEGER, doc="排名")
    HOLDERNAME = Column(String(300), doc="持有人名称")
    HOLDERSSHARE = Column(DECIMAL(19, 2), doc="持有份额")
    HOLDEROFLISTING = Column(DECIMAL(10, 4), doc="占上市总份额的比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class fund_unitclassinfo(Base):

    __tablename__ = 'fund_unitclassinfo'

    FUNDID = Column(DECIMAL(20, 0), doc="基金ID")
    FUNDCLASSID = Column(DECIMAL(20, 0), doc="基金份额类别ID")
    SYMBOL = Column(String(20), doc="基金代码")
    FRONTENDCODE = Column(String(20), doc="基金前端代码")
    BACKENDCODE = Column(String(20), doc="基金后端代码")
    EXPIRED = Column(String(20), doc="基金净值代码")
    FULLNAME = Column(String(200), doc="基金全称")
    SHORTNAME = Column(String(100), doc="基金简称")
    TRADINGSHORTNAME = Column(String(100), doc="场内简称")
    RELATIONCODE = Column(String(12), doc="基金关系编码;S0401=基金；S0402=分级基金A；S0403=分级基金B；S0404=分级基金C；S0405=分级基金A/B；S0406=封转开基金")
    RELATION = Column(String(40), doc="基金关系")
    PARVALUE = Column(DECIMAL(10, 4), doc="面值")
    CURRENCYCODE = Column(String(40), doc="面值币种;RMB=人民币")
    INCEPTIONDATE = Column(DateTime, doc="份额成立日期")
    MATURITYDATE = Column(DateTime, doc="份额到期日")
    DURATION = Column(DECIMAL(6, 2), doc="封闭年限")
    CYCLE = Column(String(40), doc="申购赎回周期")
    CLOSEDSTARTDATE = Column(DateTime, doc="封闭期起始日期")
    CLOSEDENDDATE = Column(DateTime, doc="封闭期截止日期")
    LISTINGDATE = Column(DateTime, doc="上市日期")
    EXCHANGECODE = Column(String(40), doc="上市交易所")
    TRANSITIONSTARTDATE = Column(DateTime, doc="转换开始日期")
    AFTERTRANSITIONSYMBOL = Column(String(100), doc="封转开交叉代码")
    ISPRIMARYMARKET = Column(SMALLINT, doc="是否一级市场交易;1=是；2=否")
    ISSECONDARYMARKET = Column(SMALLINT, doc="是否二级市场交易;1=是；2=否")
    SALESFEE = Column(DECIMAL(5, 3), doc="销售服务费率")
    ISIN = Column(String(24), doc="ISIN代码")
    PURCHASESTARTDATE = Column(DateTime, doc="申购起始日")
    REDEEMSTARTDATE = Column(DateTime, doc="赎回起始日")
    PURCHASESTATUS = Column(String(40), doc="申购状态;1=开放;2=暂停")
    REDEEMSTATUS = Column(String(40), doc="赎回状态;1=开放;2=暂停")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    MASTERFUNDCODE = Column(String(40), doc="基金主代码")
    GTASYMBOL = Column(String(100), doc="国泰安代码")
    EXPANDSHORTNAME = Column(String(100), doc="扩位证券简称")
    TRANSEXPLANATION = Column(String(4000), doc="基金转型说明")


class fut_calpretrdinfo(Base):

    __tablename__ = 'fut_calpretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), primary_key=True, doc="交易代码")
    EXCHANGESYMBOL = Column(String(20), doc="交易所原始代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPPERLMTPRC = Column(DECIMAL(9, 3), doc="涨停价格")
    LOWERLMTPRC = Column(DECIMAL(9, 3), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 3), doc="前结算价")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 3), doc="开盘基准价")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    MINCHANGEUNIT = Column(DECIMAL(10, 3), doc="最小变动单位")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")


class fut_pretrdinfo(Base):

    __tablename__ = 'fut_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), doc="交易代码")
    EXCHANGESYMBOL = Column(String(20), primary_key=True, doc="交易所原始代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPPERLMTPRC = Column(DECIMAL(9, 3), doc="涨停价格")
    LOWERLMTPRC = Column(DECIMAL(9, 3), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 3), doc="前结算价")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 3), doc="开盘基准价")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")
    CLIENTPOSITIONLIMIT = Column(DECIMAL(20, 0), doc="客户持仓量限制")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    MINCHANGEUNIT = Column(DECIMAL(10, 3), doc="最小变动单位")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")


class fut_pretrdinfohistory(Base):

    __tablename__ = 'fut_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    SYMBOL = Column(String(20), doc="交易代码")
    EXCHANGESYMBOL = Column(String(20), primary_key=True, doc="交易所原始代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPPERLMTPRC = Column(DECIMAL(9, 3), doc="涨停价格")
    LOWERLMTPRC = Column(DECIMAL(9, 3), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(10, 3), doc="前结算价")
    BENCHMARKOPENPRICE = Column(DECIMAL(10, 3), doc="开盘基准价")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")
    CLIENTPOSITIONLIMIT = Column(DECIMAL(20, 0), doc="客户持仓量限制")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    MINCHANGEUNIT = Column(DECIMAL(10, 3), doc="最小变动单位")
    CONTRACTMULTIPLE = Column(BIGINT, doc="合约乘数")


class idx_closeweight(Base):

    __tablename__ = 'idx_closeweight'

    SYMBOL = Column(String(20), doc="指数代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SAMPLESECURITYCODE = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    WEIGHT = Column(DECIMAL(10, 4), doc="权重")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class idx_closeweightfree(Base):

    __tablename__ = 'idx_closeweightfree'

    SYMBOL = Column(String(30), doc="指数代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SAMPLESECURITYCODE = Column(String(20), doc="样本证券代码")
    WEIGHT = Column(DECIMAL(10, 4), doc="权重")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class idx_indexinfo(Base):

    __tablename__ = 'idx_indexinfo'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    INDEXFULLNAME = Column(String(200), doc="指数中文名称")
    INDEXFULLNAME_EN = Column(String(400), doc="指数英文名称")
    INDEXSHORTNAME = Column(String(100), doc="指数中文简称")
    INDEXSHORTNAME_EN = Column(String(200), doc="指数英文简称")
    LAUNCHDATE = Column(DateTime, doc="推出日期")
    BENCHMARKDATE = Column(DateTime, doc="指数基期")
    BENCHMARKPOINT = Column(DECIMAL(18, 4), doc="指数基点")
    WEIGHTINGMETHODID = Column(String(12), doc="加权方式编码")
    WEIGHTINGMETHOD = Column(String(100), doc="加权方式")
    FORMULATIONINSTITUTIONID = Column(DECIMAL(20, 0), doc="编制机构ID")
    FORMULATIONINSTITUTION = Column(String(200), doc="编制机构")
    RELEASINGINSTITUTIONID = Column(DECIMAL(20, 0), doc="发布机构ID")
    RELEASINGINSTITUTION = Column(String(200), doc="发布机构")
    SAMPLETYPEID = Column(String(12), doc="按样本分类编码")
    SAMPLETYPE = Column(String(100), doc="按样本分类")
    INDEXTYPEID = Column(String(12), doc="指数类型编码")
    INDEXTYPE = Column(String(100), doc="指数类型")
    EXCHANGEID = Column(String(100), doc="样本所属市场编码")
    EXCHANGENAME = Column(String(200), doc="样本所属市场名称")
    CALCULATINGMETHOD = Column(String(2000), doc="计算方法")
    ADJUSTINGCYCLE = Column(String(12), doc="样本调整周期")
    ISIN = Column(String(40), doc="ISIN编码")
    ENDDATE = Column(DateTime, doc="停用日期")
    UPDATEID = Column(BIGINT, doc="数据ID")
    SAMPLESCOPE = Column(String(4000), doc="样本范围")
    PYSHORTNAME = Column(String(100))
    COUNTRYCODE_3 = Column(String(12))
    CURRENCYCODE = Column(String(12))
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class idx_mkt_lastquotationweek(Base):

    __tablename__ = 'idx_mkt_lastquotationweek'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRADINGWEEK = Column(String(16), doc="交易周份")
    FILLING = Column(SMALLINT, doc="填充标识")
    OPENDATE = Column(DateTime, doc="周开盘日期")
    PRVCLOSEDATE = Column(DateTime, doc="上周收盘日")
    PRVCLOSEPRICE = Column(DECIMAL(18, 3), doc="上周收盘价")
    OPENPRICE = Column(DECIMAL(18, 3), doc="周开盘价")
    HIGHPRICE = Column(DECIMAL(18, 3), doc="周最高价")
    LOWPRICE = Column(DECIMAL(18, 3), doc="周最低价")
    HIGHDATE = Column(DateTime, doc="周最高价日")
    LOWDATE = Column(DateTime, doc="周最低价日")
    CLOSEPRICE = Column(DECIMAL(18, 3), doc="周收盘价")
    CLOSEDATE = Column(DateTime, doc="周收盘日期")
    HIGHCLOSEPRICE = Column(DECIMAL(18, 3), doc="周最高收盘价")
    LOWCLOSEPRICE = Column(DECIMAL(18, 3), doc="周最低收盘价")
    HIGHCLOSEDATE = Column(DateTime, doc="周最高收盘价日")
    LOWCLOSEDATE = Column(DateTime, doc="周最低收盘价日")
    VOLUME = Column(DECIMAL(20, 2), doc="周成交量")
    AMOUNT = Column(DECIMAL(20, 2), doc="周成交额")
    CHANGE = Column(DECIMAL(18, 3), doc="周涨跌")
    CHANGERATIO = Column(DECIMAL(18, 6), doc="周涨跌幅")
    TRADINGDAYS = Column(SMALLINT, doc="周交易天数")
    EXCHANGECODE = Column(String(40), doc="市场编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class idx_mkt_quotation(Base):

    __tablename__ = 'idx_mkt_quotation'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    FILLING = Column(String(20), doc="填充标识")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    LATESTCLOSE = Column(DECIMAL(18, 2), doc="前收盘指数")
    OPENPRICE = Column(DECIMAL(18, 2), doc="开盘指数")
    CLOSEPRICE = Column(DECIMAL(18, 2), doc="最高指数")
    HIGHPRICE = Column(DECIMAL(18, 2), doc="最低指数")
    LOWPRICE = Column(DECIMAL(18, 2), doc="收盘指数")
    VOLUME = Column(DECIMAL(18, 2), doc="成份证券成交量")
    AMOUNT = Column(DECIMAL(18, 2), doc="成份证券成交金额")
    CHANGE = Column(DECIMAL(18, 2), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(18, 6), doc="涨跌幅")
    UPDATEID = Column(BIGINT, doc="数据ID")
    TOTALSHARES = Column(DECIMAL(30, 0))
    TOTALMARKETVALUE = Column(DECIMAL(30, 2))
    CRICULATIONSHARES = Column(DECIMAL(30, 0))
    CRICULATIONMARKETVALUE = Column(DECIMAL(30, 2))
    SAMPLENUMBER = Column(DECIMAL(20, 0))
    EXCHANGECODE = Column(String(40), doc="市场编码")


class idx_samplechange(Base):

    __tablename__ = 'idx_samplechange'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    CHANGEDATE = Column(DateTime, doc="变更日期")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    SAMPLESECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SAMPLESECURITYCODE = Column(String(20), doc="样本证券代码")
    CHANGINGMETHODID = Column(String(12), doc="变动方式编码")
    CHANGINGMETHOD = Column(String(100), doc="变动方式")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    SAMPLESECURITYNAME = Column(String(200), doc="样本证券简称")
    SAMPLETYPEID = Column(String(12), doc="样本分类编码")
    SAMPLETYPE = Column(String(100), doc="样本分类")


class idx_samplelatest(Base):

    __tablename__ = 'idx_samplelatest'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SAMPLESECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SAMPLESECURITYCODE = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    SAMPLETYPEID = Column(String(12), doc="样本分类编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    WEIGHT = Column(DECIMAL(10, 4), doc="权重")


class idx_weight(Base):

    __tablename__ = 'idx_weight'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    SAMPLESECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SAMPLESECURITYCODE = Column(String(20), doc="样本证券代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    WEIGHT = Column(DECIMAL(10, 4), doc="权重")
    UPDATEID = Column(BIGINT, primary_key=True)
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")


class idx_weightnextday(Base):

    __tablename__ = 'idx_weightnextday'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(20), doc="指数代码")
    SAMPLESECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SAMPLESECURITYCODE = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    EXCHANGECODE = Column(String(40), doc="样本证券所属交易所")
    TRADINGCURRENCY = Column(String(6), doc="交易货币")
    EXCHANGERATE = Column(DECIMAL(9, 4), doc="汇率")
    TOTALSHARES = Column(BIGINT, doc="总股本")
    CATEGORIZEDINCLUSIONFACTOR = Column(DECIMAL(10, 6), doc="归档后自由流通比例")
    SHARESININDEX = Column(BIGINT, doc="计算用股本")
    CAPFACTOR = Column(DECIMAL(9, 6), doc="权重因子")
    CLOSE = Column(DECIMAL(12, 3), doc="前一日收盘价")
    REFERENCEOPENPRICE = Column(DECIMAL(12, 3), doc="调整后开盘参考价")
    TOTALMARKETCAPITALIZATION = Column(DECIMAL(20, 2), doc="总市值")
    MARKETCAPININDEX = Column(DECIMAL(20, 2), doc="计算用市值")
    WEIGHT = Column(DECIMAL(10, 4), doc="权重")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class io_calpretrdinfo(Base):

    __tablename__ = 'io_calpretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    EXCHANGECODE = Column(String(20), primary_key=True, doc="交易所代码")
    SYMBOL = Column(String(40), doc="交易代码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    SHORTNAME = Column(String(60), doc="合约简称")
    PYSHORTNAME = Column(String(40), doc="拼音简称")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(100), doc="标的证券简称")
    UNDERLYINGNAME = Column(String(40), doc="标的证券名称")
    UNDERLYINGINDEXTYPEID = Column(String(12), doc="标的指数分类编码")
    UNDERLYINGINDEXTYPE = Column(String(100), doc="标的指数类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约乘数")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    LATESTCLOSEPRICE = Column(DECIMAL(11, 4), doc="昨收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="昨结算价")
    PREPOSITION = Column(DECIMAL(20, 3), doc="昨持仓量")
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    UPPERLMTPRC = Column(DECIMAL(11, 4), doc="涨停价")
    LOWERLMTPRC = Column(DECIMAL(11, 4), doc="跌停价")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="当日单张初始保证金")
    MINCHANGEUNIT = Column(DECIMAL(11, 4), doc="最小变动单位")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class io_pretrdinfo(Base):

    __tablename__ = 'io_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    EXCHANGECODE = Column(String(20), primary_key=True, doc="交易所代码")
    SYMBOL = Column(String(40), doc="交易代码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    SHORTNAME = Column(String(60), doc="合约简称")
    PYSHORTNAME = Column(String(40), doc="拼音简称")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(100), doc="标的证券简称")
    UNDERLYINGNAME = Column(String(40), doc="标的证券名称")
    UNDERLYINGINDEXTYPEID = Column(String(12), doc="标的指数分类编码")
    UNDERLYINGINDEXTYPE = Column(String(100), doc="标的指数类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约乘数")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    LATESTCLOSEPRICE = Column(DECIMAL(11, 4), doc="昨收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="昨结算价")
    PREPOSITION = Column(DECIMAL(20, 3), doc="昨持仓量")
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    UPPERLMTPRC = Column(DECIMAL(11, 4), doc="涨停价")
    LOWERLMTPRC = Column(DECIMAL(11, 4), doc="跌停价")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="当日单张初始保证金")
    MINCHANGEUNIT = Column(DECIMAL(11, 4), doc="最小变动单位")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class io_pretrdinfohistory(Base):

    __tablename__ = 'io_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    EXCHANGECODE = Column(String(20), primary_key=True, doc="交易所代码")
    SYMBOL = Column(String(40), doc="交易代码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    SHORTNAME = Column(String(60), doc="合约简称")
    PYSHORTNAME = Column(String(40), doc="拼音简称")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(100), doc="标的证券简称")
    UNDERLYINGNAME = Column(String(40), doc="标的证券名称")
    UNDERLYINGINDEXTYPEID = Column(String(12), doc="标的指数分类编码")
    UNDERLYINGINDEXTYPE = Column(String(100), doc="标的指数类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约乘数")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    LATESTCLOSEPRICE = Column(DECIMAL(11, 4), doc="昨收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="昨结算价")
    PREPOSITION = Column(DECIMAL(20, 3), doc="昨持仓量")
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    UPPERLMTPRC = Column(DECIMAL(11, 4), doc="涨停价")
    LOWERLMTPRC = Column(DECIMAL(11, 4), doc="跌停价")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="当日单张初始保证金")
    MINCHANGEUNIT = Column(DECIMAL(11, 4), doc="最小变动单位")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_area_ampimonth(Base):

    __tablename__ = 'mac_area_ampimonth'

    SGNMONTH = Column(String(7), doc="统计月度")
    DATASIGN = Column(String(2), doc="数据标识")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="农业生产资料项目编码")
    ITEM = Column(String(100), doc="农业生产资料项目名称")
    AMPI = Column(DECIMAL(10, 4), doc="农业生产资料价格指数")
    AMPIMOM = Column(DECIMAL(10, 4), doc="农业生产资料价格环比指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_ampiyear(Base):

    __tablename__ = 'mac_area_ampiyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="农业生产资料项目编码")
    ITEM = Column(String(100), doc="农业生产资料项目名称")
    AMPI = Column(DECIMAL(10, 4), doc="农业生产资料价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_cpimonth(Base):

    __tablename__ = 'mac_area_cpimonth'

    DECLAREDATE = Column(DateTime, doc="公布日期")
    SGNMONTH = Column(String(14), doc="统计月度")
    DATASIGN = Column(String(4), doc="数据标识")
    OBJECTID = Column(String(4), doc="统计对象编码")
    AREACODE = Column(String(20), doc="地区代码")
    ITEMID = Column(String(20), doc="居民消费项目编码")
    CPI = Column(DECIMAL(10, 4), doc="居民消费价格指数")
    CPIMOM = Column(DECIMAL(10, 4), doc="居民消费价格环比指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_cpiyear(Base):

    __tablename__ = 'mac_area_cpiyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    OBJECTID = Column(String(2), doc="统计对象编码")
    OBJECTNAME = Column(String(100), doc="统计对象名称")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="居民消费项目编码")
    ITEM = Column(String(100), doc="居民消费项目名称")
    CPI = Column(DECIMAL(10, 4), doc="居民消费价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_fixedassetsidx(Base):

    __tablename__ = 'mac_area_fixedassetsidx'

    SGNQUARTER = Column(String(7), doc="统计季度")
    DATASIGN = Column(String(2), doc="数据标识")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    FIXEDASSETSIDX = Column(DECIMAL(10, 4), doc="固定资产投资价格指数")
    CONSTRUCTIDX = Column(DECIMAL(10, 4), doc="建筑安装工程价格指数")
    EQUIPMENTIDX = Column(DECIMAL(10, 4), doc="设备工器具购置价格指数")
    OTHERSIDX = Column(DECIMAL(10, 4), doc="其他费用价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_fixedassetsidxyear(Base):

    __tablename__ = 'mac_area_fixedassetsidxyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    FIXEDASSETSIDX = Column(DECIMAL(10, 4), doc="固定资产投资价格指数")
    CONSTRUCTIDX = Column(DECIMAL(10, 4), doc="建筑安装工程价格指数")
    EQUIPMENTIDX = Column(DECIMAL(10, 4), doc="设备工器具购置价格指数")
    OTHERSIDX = Column(DECIMAL(10, 4), doc="其他费用价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_gdpquarter(Base):

    __tablename__ = 'mac_area_gdpquarter'

    DECLAREDATE = Column(DateTime, doc="公布日期")
    SGNQUARTER = Column(String(14), primary_key=True, doc="统计季度")
    AREACODE = Column(String(20), primary_key=True, doc="地区代码")
    GDP = Column(DECIMAL(18, 4), doc="国内生产总值")
    GDP_PRIMARY = Column(DECIMAL(18, 4), doc="国内生产总值-第一产业")
    GDP_SECONDARY = Column(DECIMAL(18, 4), doc="国内生产总值-第二产业")
    GDP_TERTIARY = Column(DECIMAL(18, 4), doc="国内生产总值-第三产业")
    GDPYOY = Column(DECIMAL(10, 4), doc="国内生产总值同比")
    GDP_PRIMARYYOY = Column(DECIMAL(10, 4), doc="国内生产总值同比-第一产业")
    GDP_SECONDARYYOY = Column(DECIMAL(10, 4), doc="国内生产总值同比-第二产业")
    GDP_TERTIARYYOY = Column(DECIMAL(10, 4), doc="国内生产总值同比-第三产业")
    GDPMOM = Column(DECIMAL(10, 4), doc="国内生产总值环比")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_area_gdpyear(Base):

    __tablename__ = 'mac_area_gdpyear'

    SGNYEAR = Column(String(8), doc="统计年度")
    AREACODE = Column(String(20), doc="地区代码")
    GNI = Column(DECIMAL(18, 4), doc="国民总收入")
    GDP = Column(DECIMAL(18, 4), doc="国内生产总值")
    GDP_PRIMARY = Column(DECIMAL(18, 4), doc="国内生产总值-第一产业")
    GDP_SECONDARY = Column(DECIMAL(18, 4), doc="国内生产总值-第二产业")
    GDP_INDUSTRY = Column(DECIMAL(18, 4), doc="国内生产总值-工业")
    GDP_CONSTRUCTION = Column(DECIMAL(18, 4), doc="国内生产总值-建筑业")
    GDP_TERTIARY = Column(DECIMAL(18, 4), doc="国内生产总值-第三产业")
    GDP_TRANSPORT = Column(DECIMAL(18, 4), doc="国内生产总值-交通运输、仓储和邮政业")
    GDP_WHOLESALE = Column(DECIMAL(18, 4), doc="国内生产总值-批发和零售业")
    GDP_HOTELS = Column(DECIMAL(18, 4), doc="国内生产总值-住宿和餐饮业")
    GDP_FINANCIAL = Column(DECIMAL(18, 4), doc="国内生产总值-金融业")
    GDP_REALESTATE = Column(DECIMAL(18, 4), doc="国内生产总值-房地产业")
    GDP_OTHERS = Column(DECIMAL(18, 4), doc="国内生产总值-其他服务业")
    COMPOSIT_PRIMIND = Column(DECIMAL(10, 4), doc="第一产业占比")
    COMPOSIT_SECIND = Column(DECIMAL(10, 4), doc="第二产业占比")
    COMPOSIT_TERIND = Column(DECIMAL(10, 4), doc="第三产业占比")
    GDP_PERCAPITA = Column(DECIMAL(18, 4), doc="人均国内生产总值")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_industrysalevalue(Base):

    __tablename__ = 'mac_area_industrysalevalue'

    SGNMONTH = Column(String(14), doc="统计月度")
    DATASIGN = Column(String(4), doc="数据标识")
    AREACODE = Column(String(20), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    INDUSTRYID = Column(String(20), doc="行业内部编码")
    INDUSTRY = Column(String(100), doc="行业名称")
    SALEVALUE = Column(DECIMAL(18, 4), doc="工业销售产值")
    SALEVALUEYOY = Column(DECIMAL(10, 4), doc="工业销售产值同比")
    EXPORTDELIVERY = Column(DECIMAL(18, 4), doc="出口交货值")
    EXPORTDELIVERYYOY = Column(DECIMAL(10, 4), doc="出口交货值同比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_industryvalueadd(Base):

    __tablename__ = 'mac_area_industryvalueadd'

    SGNMONTH = Column(String(14), doc="统计月度")
    DATASIGN = Column(String(4), doc="数据标识")
    AREACODE = Column(String(20), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    VALUEADD = Column(DECIMAL(18, 4), doc="工业增加值")
    VALUEADDYOY = Column(DECIMAL(10, 4), doc="工业增加值同比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_ppimonth(Base):

    __tablename__ = 'mac_area_ppimonth'

    DECLAREDATE = Column(DateTime, doc="公布日期")
    SGNMONTH = Column(String(7), doc="统计月度")
    DATASIGN = Column(String(2), doc="数据标识")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="工业品项目编码")
    ITEM = Column(String(100), doc="工业品项目名称")
    PPI = Column(DECIMAL(10, 4), doc="工业品出厂价格指数")
    PPIMOM = Column(DECIMAL(10, 4), doc="工业品出厂价格环比指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_ppiyear(Base):

    __tablename__ = 'mac_area_ppiyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="工业品项目编码")
    ITEM = Column(String(100), doc="工业品项目名称")
    PPI = Column(DECIMAL(10, 4), doc="工业品出厂价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_productoutputmonth(Base):

    __tablename__ = 'mac_area_productoutputmonth'

    SGNMONTH = Column(String(14), doc="统计月度")
    DATASIGN = Column(String(4), doc="数据标识")
    AREACODE = Column(String(20), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    PRODID = Column(BIGINT, doc="产品内部编码")
    PORDNAME = Column(String(200), doc="产品名称")
    UNITNAME = Column(String(40), doc="单位名称")
    PRODOUTPUT = Column(DECIMAL(18, 4), doc="产量")
    PRODOUTPUTYOY = Column(DECIMAL(15, 4), doc="产量同比")
    PERIODOUTPUT = Column(DECIMAL(18, 4), doc="上年同期产量")
    PERIODOUTPUTYOY = Column(DECIMAL(10, 4), doc="上年同期产量同比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_productoutputyear(Base):

    __tablename__ = 'mac_area_productoutputyear'

    SGNYEAR = Column(String(8), doc="统计年度")
    AREACODE = Column(String(20), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    PRODID = Column(BIGINT, doc="产品内部编码")
    PORDNAME = Column(String(200), doc="产品名称")
    UNITNAME = Column(String(40), doc="单位名称")
    PRODOUTPUT = Column(DECIMAL(18, 4), doc="产量")
    PRODOUTPUTYOY = Column(DECIMAL(10, 4), doc="产量同比")
    PERIODOUTPUT = Column(DECIMAL(18, 4), doc="上年同期产量")
    PERIODOUTPUTYOY = Column(DECIMAL(10, 4), doc="上年同期产量同比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_purchaseidxmonth(Base):

    __tablename__ = 'mac_area_purchaseidxmonth'

    DECLAREDATE = Column(DateTime, doc="公布日期")
    SGNMONTH = Column(String(7), doc="统计月度")
    DATASIGN = Column(String(2), doc="数据标识")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="工业品项目编码")
    ITEM = Column(String(100), doc="工业品项目名称")
    PURCHASEIDX = Column(DECIMAL(10, 4), doc="工业品购进价格指数")
    PURCHASEIDXMOM = Column(DECIMAL(10, 4), doc="工业品购进价格环比指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_purchaseidxyear(Base):

    __tablename__ = 'mac_area_purchaseidxyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="工业品项目编码")
    ITEM = Column(String(100), doc="工业品项目名称")
    PURCHASEIDX = Column(DECIMAL(10, 4), doc="工业品购进价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_rpimonth(Base):

    __tablename__ = 'mac_area_rpimonth'

    SGNMONTH = Column(String(7), doc="统计月度")
    DATASIGN = Column(String(2), doc="数据标识")
    OBJECTID = Column(String(2), doc="统计对象编码")
    OBJECTNAME = Column(String(100), doc="统计对象名称")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="商品零售项目编码")
    ITEM = Column(String(100), doc="商品零售项目名称")
    RPI = Column(DECIMAL(10, 4), doc="商品零售价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_area_rpiyear(Base):

    __tablename__ = 'mac_area_rpiyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    OBJECTID = Column(String(2), doc="统计对象编码")
    OBJECTNAME = Column(String(100), doc="统计对象名称")
    AREACODE = Column(String(10), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    ITEMID = Column(String(10), doc="商品零售项目编码")
    ITEM = Column(String(100), doc="商品零售项目名称")
    RPI = Column(DECIMAL(10, 4), doc="商品零售价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_areagdp_expendyear(Base):

    __tablename__ = 'mac_areagdp_expendyear'

    SGNYEAR = Column(String(8), primary_key=True, doc="统计年度")
    AREACODE = Column(String(20), primary_key=True, doc="地区代码")
    GDPEXPEND = Column(DECIMAL(18, 4), doc="支出法国内生产总值")
    GDP_FINCOMSUMEXPEND = Column(DECIMAL(18, 4), doc="支出法国内生产总值-最终消费支出")
    GDP_HOUSEHOLDEXPEND = Column(DECIMAL(18, 4), doc="支出法国内生产总值-居民消费支出")
    GDP_RUARLHOLDEXPEND = Column(DECIMAL(18, 4), doc="支出法国内生产总值-农村居民消费支出")
    GDP_UHOUSEHOLDEXPEND = Column(DECIMAL(18, 4), doc="支出法国内生产总值-城镇居民消费支出")
    GDP_GOVEXPEND = Column(DECIMAL(18, 4), doc="支出法国内生产总值-政府消费支出")
    GDP_GROSSCAPITALFORMAT = Column(DECIMAL(18, 4), doc="支出法国内生产总值-资本形成总额")
    GDP_GROSSFIXEDFORMAT = Column(DECIMAL(18, 4), doc="支出法国内生产总值-固定资本形成总额")
    GDP_GROSSINVENTORYFORMAT = Column(DECIMAL(18, 4), doc="支出法国内生产总值-存货增加")
    GDP_NETEXPORT = Column(DECIMAL(18, 4), doc="支出法国内生产总值-货物和服务净出口")
    FINALCOMSUMRATE = Column(DECIMAL(10, 4), doc="最终消费率")
    CAPITALFORMATRATE = Column(DECIMAL(10, 4), doc="资本形成率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_areagdp_idx1978year(Base):

    __tablename__ = 'mac_areagdp_idx1978year'

    SGNYEAR = Column(String(8), primary_key=True, doc="统计年度")
    GNI = Column(DECIMAL(10, 4), doc="国民总收入指数")
    GDP = Column(DECIMAL(10, 4), doc="国内生产总值指数")
    GDP_PRIMARY = Column(DECIMAL(10, 4), doc="国内生产总值指数-第一产业")
    GDP_SECONDARY = Column(DECIMAL(10, 4), doc="国内生产总值指数-第二产业")
    GDP_INDUSTRY = Column(DECIMAL(10, 4), doc="国内生产总值指数-工业")
    GDP_CONSTRUCTION = Column(DECIMAL(10, 4), doc="国内生产总值指数-建筑业")
    GDP_TERTIARY = Column(DECIMAL(10, 4), doc="国内生产总值指数-第三产业")
    GDP_TRANSPORT = Column(DECIMAL(10, 4), doc="国内生产总值指数-交通运输、仓储和邮政业")
    GDP_WHOLESALE = Column(DECIMAL(10, 4), doc="国内生产总值指数-批发和零售业")
    GDP_HOTELS = Column(DECIMAL(10, 4), doc="国内生产总值指数-住宿和餐饮业")
    GDP_FINANCIAL = Column(DECIMAL(10, 4), doc="国内生产总值指数-金融业")
    GDP_REALESTATE = Column(DECIMAL(10, 4), doc="国内生产总值指数-房地产业")
    GDP_OTHERS = Column(DECIMAL(10, 4), doc="国内生产总值指数-其他")
    GDP_PERCAPITA = Column(DECIMAL(10, 4), doc="人均国内生产总值指数")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_areagdp_idxyear(Base):

    __tablename__ = 'mac_areagdp_idxyear'

    SGNYEAR = Column(String(8), primary_key=True, doc="统计年度")
    AREACODE = Column(String(20), primary_key=True, doc="地区代码")
    GNI = Column(DECIMAL(10, 4), doc="国民总收入指数")
    GDP = Column(DECIMAL(10, 4), doc="国内生产总值指数")
    GDP_PRIMARY = Column(DECIMAL(10, 4), doc="国内生产总值指数-第一产业")
    GDP_SECONDARY = Column(DECIMAL(10, 4), doc="国内生产总值指数-第二产业")
    GDP_INDUSTRY = Column(DECIMAL(10, 4), doc="国内生产总值指数-工业")
    GDP_CONSTRUCTION = Column(DECIMAL(10, 4), doc="国内生产总值指数-建筑业")
    GDP_TERTIARY = Column(DECIMAL(10, 4), doc="国内生产总值指数-第三产业")
    GDP_TRANSPORT = Column(DECIMAL(10, 4), doc="国内生产总值指数-交通运输、仓储和邮政业")
    GDP_WHOLESALE = Column(DECIMAL(10, 4), doc="国内生产总值指数-批发和零售业")
    GDP_HOTELS = Column(DECIMAL(10, 4), doc="国内生产总值指数-住宿和餐饮业")
    GDP_FINANCIAL = Column(DECIMAL(10, 4), doc="国内生产总值指数-金融业")
    GDP_REALESTATE = Column(DECIMAL(10, 4), doc="国内生产总值指数-房地产业")
    GDP_OTHERS = Column(DECIMAL(10, 4), doc="国内生产总值指数-其他")
    GDP_PERCAPITA = Column(DECIMAL(10, 4), doc="人均国内生产总值指数")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_areagdp_incomeyear(Base):

    __tablename__ = 'mac_areagdp_incomeyear'

    SGNYEAR = Column(String(8), primary_key=True, doc="统计年度")
    AREACODE = Column(String(20), primary_key=True, doc="地区代码")
    GDPINCOME = Column(DECIMAL(18, 4), doc="收入法国内生产总值")
    GDP_EMPLOYCOMPENSAT = Column(DECIMAL(18, 4), doc="劳动者报酬")
    GDP_NETTAXONPRODUCT = Column(DECIMAL(18, 4), doc="生产税净额")
    GDP_FADEPRECIAT = Column(DECIMAL(18, 4), doc="固定资产折旧")
    GDP_OPERATSURPLUS = Column(DECIMAL(18, 4), doc="营业盈余")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_bondyieldsd(Base):

    __tablename__ = 'mac_bondyieldsd'

    STATSDATE = Column(DateTime, doc="统计日期")
    ONEYEARBONDYIELD = Column(DECIMAL(10, 4), doc="1年期国债收益率")
    TENYEARBONDYIELD = Column(DECIMAL(10, 4), doc="10年期国债收益率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_fixedbaseidx(Base):

    __tablename__ = 'mac_fixedbaseidx'

    SGNYEAR = Column(String(8), doc="统计年度")
    ITEMID = Column(String(20), doc="价格指数编码")
    FIXEDBASEIDX = Column(DECIMAL(10, 4), doc="定基指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_industry_financialyear(Base):

    __tablename__ = 'mac_industry_financialyear'

    SGNYEAR = Column(String(8), doc="统计年度")
    AREACODE = Column(String(20), doc="地区代码")
    AREANAME = Column(String(100), doc="地区名称")
    INDUSTRYID = Column(String(20), doc="行业内部编码")
    INDUSTRY = Column(String(100), doc="行业名称")
    SCALETYPEID = Column(String(4), doc="统计规模类型代码")
    SCALETYPE = Column(String(100), doc="统计规模类型")
    REGISTEREDTYPEID = Column(String(4), doc="统计经济类型代码")
    REGISTEREDTYPE = Column(String(100), doc="统计经济类型")
    ENTERPRISENUM = Column(DECIMAL(18, 4), doc="企业单位数")
    TOTALINDUSTRY = Column(DECIMAL(18, 4), doc="工业总产值")
    TOTALASSETS = Column(DECIMAL(18, 4), doc="资产总计")
    TOTALCURRENTASSETS = Column(DECIMAL(18, 4), doc="流动资产合计")
    FIXEDASSETSPRICE = Column(DECIMAL(18, 4), doc="固定资产原价")
    FIXEDASSETSNETVALUE = Column(DECIMAL(18, 4), doc="固定资产净值")
    TOTALLIABILITIES = Column(DECIMAL(18, 4), doc="负债合计")
    TOTALCURRENTLIABILITIES = Column(DECIMAL(18, 4), doc="流动负债合计")
    TOTALOWNEREQUITY = Column(DECIMAL(18, 4), doc="所有者权益")
    SALEREVENUE = Column(DECIMAL(18, 4), doc="主营业务收入")
    SALECOST = Column(DECIMAL(18, 4), doc="主营业务成本")
    SALETAXADD = Column(DECIMAL(18, 4), doc="主营业务税金及附加")
    TOTALPROFIT = Column(DECIMAL(18, 4), doc="利润总额")
    VALUEADDTAX = Column(DECIMAL(18, 4), doc="本年应交增值税")
    EMPLOYNUM = Column(DECIMAL(18, 4), doc="全部从业人员年平均人数")
    AVGCURRENTASSETS = Column(DECIMAL(18, 4), doc="流动资产平均余额")
    AVGFIXEDASSETS = Column(DECIMAL(18, 4), doc="固定资产净值平均余额")
    PAIDCAPITAL = Column(DECIMAL(18, 4), doc="实收资本")
    LONGTERMLIABILITY = Column(DECIMAL(18, 4), doc="长期负债合计")
    SALEPROFIT = Column(DECIMAL(18, 4), doc="产品销售利润")
    VALUEADD = Column(DECIMAL(18, 4), doc="工业增加值")
    ASSETSCONTRIBUTIONRATIO = Column(DECIMAL(10, 4), doc="总资产贡献率")
    ASSETLIABILITYRATIO = Column(DECIMAL(10, 4), doc="资产负债率")
    CURRENTASSETTURNOVER = Column(DECIMAL(10, 4), doc="流动资产周转次数")
    COSTRATIO = Column(DECIMAL(10, 4), doc="成本费用利润率")
    SALERATIO = Column(DECIMAL(10, 4), doc="产品销售率")
    EMPLOYRATIO = Column(DECIMAL(10, 4), doc="全员劳动生产率")
    VALUEADDRATE = Column(DECIMAL(10, 4), doc="工业增加值率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_industry_ppimonth(Base):

    __tablename__ = 'mac_industry_ppimonth'

    SGNMONTH = Column(String(7), doc="统计月度")
    INDUSTRYID = Column(String(10), doc="行业内部编码")
    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业")
    PPI = Column(DECIMAL(10, 4), doc="工业品出厂价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_industry_ppiyear(Base):

    __tablename__ = 'mac_industry_ppiyear'

    SGNYEAR = Column(String(4), doc="统计年度")
    INDUSTRYID = Column(String(10), doc="行业内部编码")
    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业")
    PPI = Column(DECIMAL(10, 4), doc="工业品出厂价格指数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_industry_saleinventory(Base):

    __tablename__ = 'mac_industry_saleinventory'

    SGNQUARTER = Column(String(14), primary_key=True, doc="统计季度")
    PRODID = Column(BIGINT, primary_key=True, doc="产品内部编码")
    PORDNAME = Column(String(200), doc="产品名称")
    UNITNAME = Column(String(40), doc="单位名称")
    SALEVOLUME = Column(DECIMAL(18, 4), doc="累计销售量")
    SALEOUTPUTRATIO = Column(DECIMAL(10, 4), doc="按实物量计算产销率")
    STOCKINCRSRATIO = Column(DECIMAL(10, 4), doc="期末库存比年初增长")
    CHANGESALEOUTPUTRATIO = Column(DECIMAL(10, 4), doc="产销率比上年同期增减")
    UPDATEID = Column(BIGINT, doc="数据ID")


class mac_industry_valueadd(Base):

    __tablename__ = 'mac_industry_valueadd'

    SGNMONTH = Column(String(14), doc="统计月度")
    DATASIGN = Column(String(4), doc="数据标识")
    INDUSTRYID = Column(String(20), doc="行业内部编码")
    INDUSTRY = Column(String(100), doc="行业名称")
    VALUEADD = Column(DECIMAL(18, 4), doc="工业增加值")
    VALUEADDYOY = Column(DECIMAL(10, 4), doc="工业增加值同比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class mac_industryvalueadd(Base):

    __tablename__ = 'mac_industryvalueadd'

    DECLAREDATE = Column(DateTime, doc="公布日期")
    SGNMONTH = Column(String(14), doc="统计月度")
    DATASIGN = Column(String(4), doc="数据标识")
    VALUEADD = Column(DECIMAL(18, 4), doc="工业增加值")
    LIGHTINDUSTRY = Column(DECIMAL(18, 4), doc="工业增加值-轻工业")
    HEAVYINDUSTRY = Column(DECIMAL(18, 4), doc="工业增加值-重工业")
    STATEOWNED = Column(DECIMAL(18, 4), doc="工业增加值-国有及国有控股企业")
    PRIVATE = Column(DECIMAL(18, 4), doc="工业增加值-私营企业")
    COLLECTIVE = Column(DECIMAL(18, 4), doc="工业增加值-集体企业")
    STOCKCOOPERATE = Column(DECIMAL(18, 4), doc="工业增加值-股份合作企业")
    JOINTSTOCK = Column(DECIMAL(18, 4), doc="工业增加值-股份制企业")
    FOREIGN = Column(DECIMAL(18, 4), doc="工业增加值-外商及港台投资企业")
    VALUEADDYOY = Column(DECIMAL(10, 4), doc="工业增加值同比")
    LIGHTINDUSTYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-轻工业")
    HEAVYINDUSTYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-重工业")
    STATEOWNEDYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-国有及国有控股企业")
    PRIVATEYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-私营企业")
    COLLECTIVEYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-集体企业")
    STOCKCOOPERATEYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-股份合作企业")
    JOINTSTOCKYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-股份制企业")
    FOREIGNYOY = Column(DECIMAL(10, 4), doc="工业增加值同比-外商及港台投资企业")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    VALUEADDMOM = Column(DECIMAL(10, 4), doc="工业增加值环比")


class mac_statsinfo_calendar(Base):

    __tablename__ = 'mac_statsinfo_calendar'

    DECLAREDATE = Column(DateTime, primary_key=True, doc="公布日期")
    WEEKMARK = Column(String(2), doc="星期标示")
    CONTENT = Column(String(100), primary_key=True, doc="信息发布内容")
    UPDATEID = Column(BIGINT, doc="数据ID")


class plate_bondchange(Base):

    __tablename__ = 'plate_bondchange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_bondchangelatest(Base):

    __tablename__ = 'plate_bondchangelatest'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_bondsamplechange(Base):

    __tablename__ = 'plate_bondsamplechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    ENTERDATE = Column(DateTime, doc="纳入日期")
    OUTDATE = Column(DateTime, doc="纳出日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_concept(Base):

    __tablename__ = 'plate_concept'

    CONCEPTID = Column(DECIMAL(22, 0), doc="概念编码")
    CONCEPTNAME = Column(String(100), doc="概念名称")
    CONCEPTNAME_EN = Column(String(200), doc="概念英文名称")
    SECURITYID = Column(DECIMAL(20, 0), doc="概念成分股代码ID")
    SYMBOL = Column(String(20), doc="概念成分股代码")
    USESIGN = Column(SMALLINT, doc="使用标识")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class plate_fundchange(Base):

    __tablename__ = 'plate_fundchange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_fundchangelatest(Base):

    __tablename__ = 'plate_fundchangelatest'

    PLATEID = Column(DECIMAL(22, 0), primary_key=True, doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), primary_key=True, doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_fundsamplechange(Base):

    __tablename__ = 'plate_fundsamplechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    ENTERDATE = Column(DateTime, doc="纳入日期")
    OUTDATE = Column(DateTime, doc="纳出日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_futurechange(Base):

    __tablename__ = 'plate_futurechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(String(40), doc="样本证券ID")
    SYMBOL = Column(String(12), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_futurechangelatest(Base):

    __tablename__ = 'plate_futurechangelatest'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(String(40), doc="样本证券ID")
    SYMBOL = Column(String(12), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_futuresamplechange(Base):

    __tablename__ = 'plate_futuresamplechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    ENTERDATE = Column(DateTime, doc="纳入日期")
    OUTDATE = Column(DateTime, doc="纳出日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_indexchange(Base):

    __tablename__ = 'plate_indexchange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(30), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_indexchangelatest(Base):

    __tablename__ = 'plate_indexchangelatest'

    PLATEID = Column(DECIMAL(22, 0), primary_key=True, doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(30), primary_key=True, doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_indexsamplechange(Base):

    __tablename__ = 'plate_indexsamplechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(30), doc="样本证券代码")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    ENTERDATE = Column(DateTime, doc="纳入日期")
    OUTDATE = Column(DateTime, doc="纳出日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_platetree(Base):

    __tablename__ = 'plate_platetree'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    PLATETREEID = Column(DECIMAL(22, 0), doc="板块树PID")
    PLATETITLE = Column(String(200), doc="板块名称")
    PLATECODE = Column(String(40), doc="板块代码")
    PLATETYPECODE = Column(String(12), doc="板块种类编码")
    SECURITYTYPECODE = Column(String(12), doc="证券分类编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    NODELEVEL = Column(String(12))
    ISLASTNODE = Column(String(2))
    UPDATETIME_EN = Column(DateTime)
    PLATETITLE_EN = Column(String(40), doc="板块树英文名称")


class plate_platetree_state2(Base):

    __tablename__ = 'plate_platetree_state2'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYTYPECODE = Column(String(12), doc="证券分类编码")
    PLATETYPECODE = Column(String(12), doc="板块种类编码")
    PLATETREEID = Column(DECIMAL(22, 0), doc="板块树PID")
    PLATETITLE = Column(String(200), doc="板块名称")
    PLATETITLE_EN = Column(String(40), doc="板块树英文名称")
    PLATECODE = Column(String(40), doc="板块代码")
    NODELEVEL = Column(String(12), doc="节点级别")
    ISLASTNODE = Column(String(2), doc="是否为叶子节点")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class plate_sochange(Base):

    __tablename__ = 'plate_sochange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(40), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_sochangelatest(Base):

    __tablename__ = 'plate_sochangelatest'

    PLATEID = Column(DECIMAL(22, 0), primary_key=True, doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(40), primary_key=True, doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_sosamplechange(Base):

    __tablename__ = 'plate_sosamplechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(40), doc="样本证券代码")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    ENTERDATE = Column(DateTime, doc="纳入日期")
    OUTDATE = Column(DateTime, doc="纳出日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_stockchange(Base):

    __tablename__ = 'plate_stockchange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_stockchangelatest(Base):

    __tablename__ = 'plate_stockchangelatest'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    SAMPLESECURITYNAME = Column(String(100), doc="样本证券简称")
    EXCHANGECODE = Column(String(100), doc="上市市场编码 ")
    CHANGETYPECODE = Column(String(12), doc="变动类型编码")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class plate_stocksamplechange(Base):

    __tablename__ = 'plate_stocksamplechange'

    PLATEID = Column(DECIMAL(22, 0), doc="板块树ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="样本证券ID")
    SYMBOL = Column(String(20), doc="样本证券代码")
    EXCHANGECODE = Column(String(100), doc="上市市场编码")
    ENTERDATE = Column(DateTime, doc="纳入日期")
    OUTDATE = Column(DateTime, doc="纳出日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class pled_agrrepamt(Base):

    __tablename__ = 'pled_agrrepamt'

    EXCHANGECODE = Column(String(6), doc="交易所")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    INITIALAMOUNT = Column(DECIMAL(15, 2), doc="初始交易金额")
    REPAMOUNT = Column(DECIMAL(15, 2), doc="购回交易金额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_agrrepdetl(Base):

    __tablename__ = 'pled_agrrepdetl'

    EVENTID = Column(BIGINT, doc="事件ID")
    EVENTSEQ = Column(INTEGER, doc="进展序号")
    SYMBOL = Column(String(6), doc="股票代码")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SHORTNAME = Column(String(100), doc="证券简称")
    INSTITUTIONNAME = Column(String(200), doc="上市公司全称")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    SHAREHOLDERNAME = Column(String(200), doc="股东名称")
    SHAREHOLDERID = Column(DECIMAL(20, 0), doc="股东ID")
    SHAREHOLDERTYPECODE = Column(String(6), doc="股东性质编码")
    SHAREHOLDERTYPE = Column(String(100), doc="股东性质")
    RELATIONTOCOMCODE = Column(String(20), doc="上市公司关系编码")
    RELATIONTOCOM = Column(String(100), doc="上市公司关系")
    HOLDRANKING = Column(INTEGER, doc="股东排名")
    SECCOM = Column(String(200), doc="证券公司")
    SECCOMID = Column(DECIMAL(20, 0), doc="证券公司ID")
    SELLDATE = Column(DateTime, doc="卖出日期")
    REPODATE = Column(DateTime, doc="购回日期")
    TERM = Column(INTEGER, doc="期限")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    CHANGEREASONCODE = Column(String(20), doc="变动原因编码")
    CHANGEREASON = Column(String(100), doc="变动原因")
    CHANGENUM = Column(BIGINT, doc="变动数量")
    UNREPSHARES = Column(BIGINT, doc="待购回数量")
    NUMBEFORTRD = Column(BIGINT, doc="交易前持有上市公司股份")
    NUMAFTERTRD = Column(BIGINT, doc="交易后持有上市公司股份")
    TOTNUMSHARES = Column(BIGINT, doc="上市公司总股份")
    RATIOBEFORTRD = Column(DECIMAL(5, 2), doc="交易前占上市公司股份比例（%）")
    RATIOAFTERTRD = Column(DECIMAL(5, 2), doc="交易后占上市公司股份比例（%）")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    ISLASTESTRECORD = Column(String(1), doc="最新进展标识")
    ISLOCKEDSHARES = Column(String(1), doc="限售股标识")
    AMOUNT = Column(DECIMAL(12, 4), doc="金额")
    NOTE = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_amtstat(Base):

    __tablename__ = 'pled_amtstat'

    EXCHANGECODE = Column(String(6), doc="交易所")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    INITIALAMOUNT = Column(DECIMAL(15, 2), doc="初始交易金额")
    REPAMOUNT = Column(DECIMAL(15, 2), doc="购回交易金额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_ltvratio(Base):

    __tablename__ = 'pled_ltvratio'

    EXCHANGECODE = Column(String(6), doc="交易所")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="结束日期")
    TRADINGWEEK = Column(String(7), doc="周份")
    TRADABLESHARESLTVRATIO = Column(DECIMAL(5, 2), doc="无限售条件股份质押率")
    LOCKEDSHARESLTVRATIO = Column(DECIMAL(5, 2), doc="有限售条件股份质押率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_repbysecco(Base):

    __tablename__ = 'pled_repbysecco'

    EXCHANGECODE = Column(String(6), doc="交易所")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    DAYSCALE = Column(DECIMAL(16, 3), doc="当日规模")
    INITIALAMOUNT = Column(DECIMAL(16, 3), doc="初始交易金额")
    UNREPAMOUNT = Column(DECIMAL(16, 3), doc="未到期交易金额")
    REPAMOUNT = Column(DECIMAL(16, 3), doc="到期购回交易金额")
    NUMDURATIONTYPE = Column(SMALLINT, doc="存续期限品种数量")
    DURATIONTYPE = Column(String(1000), doc="具体存续期限品种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_sectrdvol(Base):

    __tablename__ = 'pled_sectrdvol'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    SECURITYTYPECODE = Column(String(6), doc="证券类别编码")
    SECURITYTYPE = Column(String(20), doc="证券类别")
    EXCHANGECODE = Column(String(6), doc="交易所")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    INITIALVOLUME = Column(BIGINT, doc="初始交易数量")
    REPVOLUME = Column(BIGINT, doc="购回交易数量")
    UNREPTRADABLESHARES = Column(BIGINT, doc="待购回无限售条件证券余量")
    UNREPLOCKEDSHARES = Column(BIGINT, doc="待购回有限售条件证券余量")
    UNREPSHARES = Column(BIGINT, doc="待购回余量")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_stkfrzdetl(Base):

    __tablename__ = 'pled_stkfrzdetl'

    EVENTID = Column(BIGINT, doc="事件ID")
    EVENTSEQ = Column(INTEGER, doc="进展序号")
    SYMBOL = Column(String(6), doc="股票代码")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SHORTNAME = Column(String(100), doc="证券简称")
    INSTITUTIONNAME = Column(String(200), doc="上市公司全称")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    SHAREHOLDERNAME = Column(String(200), doc="股东名称")
    SHAREHOLDERID = Column(String(100), doc="股东ID")
    SHAREHOLDERTYPECODE = Column(String(50), doc="股东性质编码")
    SHAREHOLDERTYPE = Column(String(100), doc="股东性质")
    RELATIONTOCOMCODE = Column(String(20), doc="上市公司关系编码")
    RELATIONTOCOM = Column(String(100), doc="上市公司关系")
    HOLDRANKING = Column(INTEGER, doc="股东排名")
    SHAREHOLDERSIDECODE = Column(String(6), doc="股东涉及方向编码")
    SHAREHOLDERSIDE = Column(String(100), doc="股东涉及方向")
    PARTYINVOVED = Column(String(600), doc="涉及方")
    PARTYINVOVEDID = Column(String(100), doc="涉及方ID")
    PARTYINVOVEDTYPECODE = Column(String(100), doc="涉及方性质编码")
    PARTYINVOVEDTYPE = Column(String(600), doc="涉及方性质")
    PARTYINVOVEDSIDECODE = Column(String(6), doc="涉及方方向编码")
    PARTYINVOVEDSIDE = Column(String(100), doc="涉及方方向")
    TRIALINSTITUTIONS = Column(String(200), doc="执行机构")
    TRIALINSTITUTIONSID = Column(String(100), doc="执行机构ID")
    REFNUMBER = Column(String(200), doc="文号")
    EXECUTEREASONCODE = Column(String(50), doc="执行原因编码")
    EXECUTEREASON = Column(String(4000), doc="执行原因")
    STARTDATE = Column(DateTime, doc="起始日期")
    ENDDATE = Column(DateTime, doc="结束日期")
    TERM = Column(DECIMAL(4, 2), doc="期限")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    CHANGEREASONCODE = Column(String(20), doc="变动原因编码")
    CHANGEREASON = Column(String(100), doc="变动原因")
    CHANGENUM = Column(BIGINT, doc="变动数量")
    NUMAFTERCHG = Column(BIGINT, doc="剩余冻结数量")
    NUMHOLDEROWN = Column(BIGINT, doc="持有上市公司股份")
    RATIO1 = Column(DECIMAL(5, 2), doc="占其持有上市公司股份比例（%）")
    TOTNUMSHARES = Column(BIGINT, doc="上市公司总股份")
    RATIO2 = Column(DECIMAL(5, 2), doc="占上市公司总股份比例（%）")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    ISLASTESTRECORD = Column(String(1), doc="最新进展标识")
    ISLOCKEDSHARES = Column(String(1), doc="限售股标识")
    AMOUNT = Column(DECIMAL(12, 4), doc="金额")
    LAEVENTID = Column(DECIMAL(20, 0), doc="诉讼仲裁事件ID")
    ISRESPOND = Column(String(1), doc="股东方是否回应")
    ISINFLUENCED = Column(String(1), doc="是否对上市公司产生重大影响")
    DESCRIPTION = Column(String(4000), doc="事件描述")
    NOTE = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_stkratio(Base):

    __tablename__ = 'pled_stkratio'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    SECURITYTYPECODE = Column(String(6), doc="证券类别编码")
    SECURITYTYPE = Column(String(20), doc="证券类别")
    EXCHANGECODE = Column(String(6), doc="交易所")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="结束日期")
    TRADINGWEEK = Column(String(7), doc="周份")
    TRADABLESHARES = Column(DECIMAL(12, 2), doc="无限售股份质押数量")
    LOCKEDSHARES = Column(DECIMAL(12, 2), doc="有限售股份质押数量")
    TOTPLEDSHARES = Column(DECIMAL(12, 2), doc="质押数量总量")
    TOTSHARESA = Column(DECIMAL(12, 2), doc="A股总股本")
    PLEDTIMES = Column(INTEGER, doc="质押笔数")
    PLEDRATIO = Column(DECIMAL(5, 2), doc="质押比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class pled_stktrdvol(Base):

    __tablename__ = 'pled_stktrdvol'

    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="结束日期")
    TRADINGWEEK = Column(String(7), doc="周份")
    PLEDTIMES = Column(INTEGER, doc="本期办理质押笔数")
    PLEDVOLUME = Column(DECIMAL(12, 2), doc="本期办理质押数量")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pled_trddetl(Base):

    __tablename__ = 'pled_trddetl'

    EVENTID = Column(BIGINT, doc="事件ID")
    EVENTSEQ = Column(INTEGER, doc="进展序号")
    SYMBOL = Column(String(6), doc="股票代码")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SHORTNAME = Column(String(100), doc="证券简称")
    INSTITUTIONNAME = Column(String(200), doc="上市公司全称")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    PLEDGOR = Column(String(200), doc="出质方")
    PLEDGORID = Column(DECIMAL(20, 0), doc="出质方ID")
    PLEDGORTYPECODE = Column(String(6), doc="出质方性质编码")
    PLEDGORTYPE = Column(String(100), doc="出质方性质")
    RELATIONTOCOMCODE = Column(String(20), doc="出质方与上市公司关系编码")
    RELATIONTOCOM = Column(String(100), doc="出质方与上市公司关系")
    HOLDRANKING = Column(INTEGER, doc="股东排名")
    PLEDGEE = Column(String(200), doc="质权方")
    PLEDGEEID = Column(DECIMAL(20, 0), doc="质权方ID")
    PLEDGEECATERGORYCODE = Column(String(6), doc="质权方分类编码")
    PLEDGEECATERGORY = Column(String(100), doc="质权方分类")
    STARTDATE = Column(DateTime, doc="起始日期")
    ENDDATE = Column(DateTime, doc="结束日期")
    PLEDTERM = Column(DECIMAL(4, 2), doc="期限")
    PURPOSECODE = Column(String(50), doc="用途编码")
    PURPOSE = Column(String(100), doc="用途")
    INVESTPROJECTCODE = Column(String(50), doc="投向编码")
    INVESTPROJECT = Column(String(100), doc="投向")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    CHANGEREASONCODE = Column(String(20), doc="变动原因编码")
    CHANGEREASON = Column(String(100), doc="变动原因")
    NUMBEFORECHG = Column(BIGINT, doc="初始数量")
    CHANGENUM = Column(BIGINT, doc="数量增减")
    NUMAFTERCHG = Column(BIGINT, doc="剩余质押数量")
    NUMHOLDEROWN = Column(BIGINT, doc="持有上市公司股份")
    RATIO1 = Column(DECIMAL(5, 2), doc="占其持有上市公司股份比例（%）")
    TOTNUMSHARES = Column(BIGINT, doc="上市公司总股份")
    RATIO2 = Column(DECIMAL(5, 2), doc="占上市公司总股份比例（%）")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    ISLASTESTRECORD = Column(String(1), doc="最新进展标识")
    ISLOCKEDSHARES = Column(String(1), doc="限售股标识")
    AMOUNT = Column(DECIMAL(12, 4), doc="借款金额")
    JOINTPLEDGESEQ = Column(INTEGER, doc="联合质押序列")
    NOTE = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pub_chnadmdivisioncode(Base):

    __tablename__ = 'pub_chnadmdivisioncode'

    DIVISIONCODE = Column(String(12), primary_key=True, doc="行政区划代码")
    DIVISIONNAME = Column(String(100), doc="区划名称")
    DIVISIONNAME_EN = Column(String(200), doc="区划英文名称")
    P_DIVISIONCODE = Column(String(12), doc="上级区划代码")
    UPDATEID = Column(BIGINT, doc="数据ID")
    ADM_LEVEL = Column(String(4))
    AREAID = Column(BIGINT)
    ENDDATE = Column(DateTime, primary_key=True)


class pub_codingschema(Base):

    __tablename__ = 'pub_codingschema'

    CODE = Column(String(12), primary_key=True, doc="编码")
    CODINGSCHEMAID = Column(String(6), primary_key=True, doc="编码体系ID")
    CODINGSCHEMA = Column(String(40), doc="编码体系")
    VALUE = Column(String(200), doc="编码中文值")
    VALUE_EN = Column(String(800), doc="编码英文值")
    PARENTCODE = Column(String(12), doc="父编码")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_continuingcontract(Base):

    __tablename__ = 'pub_continuingcontract'

    SECURITYID = Column(DECIMAL(20, 0))
    SYMBOL = Column(String(20))
    EXCHANGECODE = Column(String(40))
    TRADINGDATE = Column(DateTime)
    UNDERLYINGASSETSCODE = Column(String(20))
    OLDUNDERLYINGASSETSCODE = Column(String(20))
    CONTINUESIGN = Column(String(20))
    UPDATEID = Column(BIGINT, primary_key=True)
    VARIETYID = Column(DECIMAL(20, 0))


class pub_eventtype(Base):

    __tablename__ = 'pub_eventtype'

    EVENTTYPECODE = Column(String(12), primary_key=True, doc="事件类型编码")
    SUBJECT = Column(String(20), doc="主题代码")
    EVENTTYPE = Column(String(40), doc="事件类型中文")
    EVENTTYPE_EN = Column(String(100), doc="事件类型英文")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_exchangeinfo(Base):

    __tablename__ = 'pub_exchangeinfo'

    EXCHANGECODE = Column(String(20), primary_key=True, doc="交易所|市场编码")
    EXCHANGE = Column(String(40), doc="交易所|市场中文名称")
    EXCHANGE_EN = Column(String(100), doc="交易所|市场英文名称")
    COUNTRYREGIONCODE = Column(String(6), doc="国家区域3位英文代码")
    NOTE = Column(String(1000), doc="备注")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_indclassifysets(Base):

    __tablename__ = 'pub_indclassifysets'

    INDUSTRYCODE = Column(String(20), primary_key=True, doc="行业编码")
    INDCLASSIFYSYSTEM = Column(String(100), doc="行业分类标准")
    INDCLASSIFYSYSTEMCODE = Column(String(40), primary_key=True, doc="行业分类标准编码")
    INDUSTRYNAME = Column(String(200), doc="行业中文名称")
    INDUSTRYNAME_EN = Column(String(400), doc="行业英文名称")
    P_INDUSTRYCODE = Column(String(20), doc="父类行业编码")
    UPDATEID = Column(BIGINT, doc="数据ID")
    INDUSTRYID = Column(INTEGER, doc="行业ID")
    RANK = Column(SMALLINT, doc="行业层级")


class pub_indclassifyversion(Base):

    __tablename__ = 'pub_indclassifyversion'

    INDCLASSIFYSYSTEMCODE = Column(String(40), primary_key=True, doc="行业分类标准编码")
    INDCLASSIFYSYSTEM = Column(String(100), doc="行业分类标准")
    INDCLASSIFYSYSTEM_EN = Column(String(200), doc="行业分类标准英文")
    IMPLEMENTDATE = Column(DateTime, doc="标准实行日期")
    ABANDONDATE = Column(DateTime, doc="标准中止日期")
    INSTITUTIONID = Column(String(40), doc="行业分类标准发布机构id")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_institutionidchange(Base):

    __tablename__ = 'pub_institutionidchange'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="机构ID")
    INSTITUTIONNAME = Column(String(200), doc="机构名称")
    CHANGEDATE = Column(DateTime, doc="变更日期")
    REASON = Column(String(100), doc="变更原因")
    STATUS = Column(String(100), doc="机构状态")
    INSTITUTIONID2 = Column(DECIMAL(20, 0), doc="变更前机构ID")
    INSTITUTIONNAME2 = Column(String(200), doc="变更前机构名称")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pub_institutioninfo(Base):

    __tablename__ = 'pub_institutioninfo'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="机构ID")
    SHORTNAME = Column(String(100), doc="机构简称")
    FULLNAME = Column(String(200), doc="机构名称")
    ENSHORTNAME = Column(String(400), doc="英文简称")
    ENNAME = Column(String(400), doc="英文名称")
    CATEGORY = Column(String(100), doc="机构分类")
    CATEGORYID = Column(String(12), doc="机构分类代码")
    OWNSHIP = Column(String(100), doc="所有权性质")
    OWNSHIPID = Column(String(12), doc="所有权性质编码")
    ESTABLISHDATE = Column(DateTime, doc="成立日期")
    LEGALREPRESENTATIVE = Column(String(100), doc="法人代表")
    REGISTERCAPITAL = Column(BIGINT, doc="注册资本")
    CURRENCY = Column(String(100), doc="货币种类")
    CURRENCYCODE = Column(String(12), doc="货币编码")
    REGISTERADDRESS = Column(String(400), doc="注册地址")
    OFFICEADDRESS = Column(String(400), doc="办公地址")
    ZIPCODE = Column(String(20), doc="办公地邮政编码")
    WEBSITE = Column(String(400), doc="网址")
    EMAIL = Column(String(400), doc="电子邮箱")
    ISLISTED = Column(String(2), doc="是否上市公司")
    REGION = Column(String(100), doc="区域（国家）名称")
    REGIONCODE = Column(String(6), doc="区域（国家）编码")
    MAINBUSINESS = Column(String(2000), doc="主营业务")
    BUSINESSSCOPE = Column(String(4000), doc="经营范围")
    DESCRIPTION = Column(String(4000), doc="机构简介")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_isocontrycode(Base):

    __tablename__ = 'pub_isocontrycode'

    COUNTRYCODE_3 = Column(String(6), primary_key=True, doc="国家区域3位英文代码")
    COUNTRYCODE_NUM = Column(String(12), doc="国家区域数字代码")
    COUNTRYREGIONNAME = Column(String(100), doc="国家区域名称")
    COUNTRYREGIONNAME_EN = Column(String(200), doc="国家区域英文名称")
    COUNTRYCODE_2 = Column(String(12), doc="国家区域2位英文代码")
    CURRENCYCODE = Column(String(6), doc="货币三位英文编码")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_isocurrencycode(Base):

    __tablename__ = 'pub_isocurrencycode'

    CURRENCYCODE = Column(String(6), primary_key=True, doc="货币三位英文编码")
    CURRENCYCODENUM = Column(String(6), doc="货币数字代码")
    CURRENCYNAME = Column(String(200), doc="货币中文名称")
    CURRENCYNAME_EN = Column(String(200), doc="货币英文名称")
    UPDATEID = Column(BIGINT, doc="数据ID")


class pub_mainconcontract(Base):

    __tablename__ = 'pub_mainconcontract'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(20), doc="交易代码")
    SHORTNAME = Column(String(20), doc="证券简称")
    SIGNTYPEID = Column(SMALLINT, doc="主力连续分类")
    EXCHANGECODE = Column(String(40), doc="交易所代码")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSYMBOL = Column(String(20), doc="标的证券代码")
    VARIETYID = Column(DECIMAL(20, 0), doc="品种ID")
    UNDERLYINGASSETSCODE = Column(String(20), doc="标的品种编码")
    OLDUNDERLYINGASSETSCODE = Column(String(20), doc="标的品种编码(旧)")
    MODEID = Column(String(20), doc="主力合约规则ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pub_maincontract(Base):

    __tablename__ = 'pub_maincontract'

    SECURITYID = Column(DECIMAL(20, 0))
    SYMBOL = Column(String(20))
    EXCHANGECODE = Column(String(40))
    TRADINGDATE = Column(DateTime)
    UNDERLYINGASSETSCODE = Column(String(20))
    OLDUNDERLYINGASSETSCODE = Column(String(20))
    NEXTTRADINGDATE = Column(DateTime)
    MODEID = Column(String(20))
    UPDATEID = Column(BIGINT, primary_key=True)
    VARIETYID = Column(DECIMAL(20, 0))


class pub_personnelinfo(Base):

    __tablename__ = 'pub_personnelinfo'

    PERSONID = Column(DECIMAL(21, 0), doc="人员id")
    FULLNAME = Column(String(200), doc="人员名称")
    FULLNAME_EN = Column(String(400), doc="人员英文名称")
    GENDER = Column(String(2), doc="性别")
    BIRTHYEAR = Column(SMALLINT, doc="出生年份")
    BEGINYEARSECURITY = Column(SMALLINT, doc="从事证券开始年份")
    DEGREEID_H = Column(String(12), doc="最高学历id")
    DEGREE_H = Column(String(100), doc="最高学历")
    PROFESSIONALTITLEID = Column(String(200), doc="职称id")
    PROFESSIONALTITLE = Column(String(200), doc="职称")
    CERTIFICATEID = Column(String(200), doc="专业技术资格id")
    CERTIFICATE = Column(String(200), doc="专业技术资格")
    NATIONALITYCODE = Column(String(6), doc="国籍编码")
    NATIONALITY = Column(String(100), doc="国籍")
    RESUME = Column(LONGTEXT, doc="个人简历")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="相关机构id")
    COMMENTS = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pub_pretradinginfo(Base):

    __tablename__ = 'pub_pretradinginfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    DECLAREDATE = Column(DateTime, doc="业务发生日期")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    SHORTNAME = Column(String(100), doc="证券简称")
    FUNDSHORTNAME = Column(String(100), doc="基金简称")
    SYMBOL = Column(String(40), primary_key=True, doc="交易代码")
    EXCHANGESYMBOL = Column(String(40), doc="交易所原始代码")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    UPLIMIT = Column(DECIMAL(11, 4), doc="涨停价格")
    DOWNLIMIT = Column(DECIMAL(11, 4), doc="跌停价格")
    LATESTCLOSEPRICE = Column(DECIMAL(11, 4), doc="前收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="前结算价")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    EXDIVIDENDPRICE = Column(DECIMAL(10, 3), doc="除权除息后的前收盘价")
    ISSUEPRICE = Column(DECIMAL(7, 2), doc="发行价格")
    PARVALUERATE = Column(DECIMAL(7, 3), doc="票面利率")
    INTERESTSTARTDATE = Column(DateTime, doc="计息日期")
    INTERESTDAYS = Column(INTEGER, doc="计息天数")
    ACCRUEDINTEREST = Column(DECIMAL(16, 6), doc="应计利息")
    MINTICKSIZE = Column(DECIMAL(11, 4), doc="价格档位")
    ISEXDIVIDENDDATE = Column(SMALLINT, doc="是否付息日")
    INCEPTIONSHARES = Column(DECIMAL(20, 2), doc="基金成立时份额")
    NAV = Column(DECIMAL(20, 4), doc="基金份额净值")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    INDUSTRYCODE = Column(String(40), doc="所属行业")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    ISTRADE = Column(SMALLINT, doc="是否交易")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    CHANGERATIOLIMITTYPEID = Column(SMALLINT, doc="涨跌幅限制类型")
    ISLASTTRADINGDATE = Column(SMALLINT, doc="是否最后交易日")
    UPDATEID = Column(BIGINT, doc="数据ID")
    SECURITYTYPECODE = Column(String(20), doc="证券分类编码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSECURITYSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(20), doc="标的证券简称")
    UNDERLYINGTYPE = Column(String(20), doc="标的证券类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约单位")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="单位保证金")
    SECURITYSTATUSUSFLAG = Column(String(20), doc="期权合约状态信息标签")
    CLIENTPOSITIONLIMIT = Column(DECIMAL(20, 0), doc="客户持仓量限制")
    UNDERLYINGNAME = Column(String(40))
    UNDERLYINGINDEXTYPEID = Column(String(12))
    MINCHANGEUNIT = Column(DECIMAL(11, 4))
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    EPS = Column(DECIMAL(8, 4), doc="本年每股利润")
    ENDDATE = Column(DateTime, doc="截止日期")
    NAVPERSHARE = Column(DECIMAL(8, 4), doc="每股净资产")
    PARENTEPS = Column(DECIMAL(8, 4), doc="归属于母公司股东每股利润")


class pub_securityconstant(Base):

    __tablename__ = 'pub_securityconstant'

    SECURITYTYPECODE = Column(String(20), doc="证券类别编码")
    EXCHANGECODE = Column(String(12), doc="交易所代码")
    SECURITYSUBTYPECODE = Column(String(20), doc="证券分类明细品种编码")
    INDEXNAME = Column(String(100), doc="常量指标名称")
    INDEXID = Column(String(16), doc="常量指标编码")
    INDEXVALUE = Column(String(100), doc="常量指标值")
    INDEXUNIT = Column(String(20), doc="常量指标单位")
    STARTDATE = Column(DateTime, doc="启用日期")
    ENDDATE = Column(DateTime, doc="失效日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class pub_securityinfo(Base):

    __tablename__ = 'pub_securityinfo'

    SECURITYID = Column(DECIMAL(20, 0))
    SYMBOL = Column(String(40))
    EXCHANGECODE = Column(String(36))
    TYPEID = Column(String(12))
    SHORTNAME = Column(String(100))
    FULLNAME = Column(String(200))
    ENSHORTNAME = Column(String(300))
    ENNAME = Column(String(600))
    INSTITUTIONID = Column(DECIMAL(20, 0))
    LISTEDDATE = Column(DateTime)
    DELISTEDDATE = Column(DateTime)
    CURRENCYCODE = Column(String(6))
    ISIN = Column(String(40))
    STATUSID = Column(String(12))
    ISSUEPRICE = Column(DECIMAL(12, 4))
    UPDATEID = Column(BIGINT, primary_key=True)
    EXCHANGESYMBOL = Column(String(40), doc="交易所原始代码")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class sh_securityinfo(Base):

    __tablename__ = 'sh_securityinfo'

    SYMBOL = Column(String(20), doc="证券代码")
    ISIN = Column(String(40), doc="ISIN代码")
    UPDATEDATE = Column(DateTime, doc="记录更新日期")
    UPDATETIME1 = Column(String(10), doc="记录更新时间")
    SYMBOLNAME = Column(String(100), doc="中文证券名称")
    SYMBOLNAME_EN = Column(String(100), doc="英文证券名称")
    UNDERLYINGSECURITYSYMBOL = Column(String(20), doc="基础证券代码")
    MARKETTYPE = Column(String(20), doc="市场种类")
    SYMBOLTYPE = Column(String(20), doc="证券类别")
    SUBSYMBOLTYPE = Column(String(12), doc="证券子类别")
    CURRENCYTYPE = Column(String(6), doc="货币种类")
    LISTEDSHARES = Column(DECIMAL(30, 0), doc="可流通证券已上市数量")
    UNLISTEDSHARES = Column(DECIMAL(30, 0), doc="可流通证券未上市数量")
    UNCRICULATIONSHARES = Column(DECIMAL(30, 0), doc="非流通股数量")
    LISTEDDATE = Column(String(20), doc="上市日期")
    SETCODE = Column(String(12), doc="产品集SET编号")
    BUYPERSHARES = Column(DECIMAL(20, 0), doc="买数量单位")
    SELLPERSHARES = Column(DECIMAL(20, 0), doc="卖数量单位")
    DECLAREFLOOR = Column(DECIMAL(20, 0), doc="申报数量下限")
    DECLARECEILING = Column(DECIMAL(20, 0), doc="申报数量上限")
    LATESTCLOSE = Column(DECIMAL(20, 3), doc="前收盘价格")
    PRICESTALL = Column(DECIMAL(20, 3), doc="价格档位")
    CHANGELIMITTYPE = Column(String(4), doc="涨跌幅限制类型")
    RISECEILINGPRICE = Column(DECIMAL(20, 3), doc="涨幅上限价格")
    DECLINEFLOORPRICE = Column(DECIMAL(20, 3), doc="跌幅下限价格")
    EXRSCALE = Column(DECIMAL(20, 6), doc="除权比例")
    EXDAMOUNT = Column(DECIMAL(20, 6), doc="除息金额")
    FINANCING = Column(String(4), doc="融资标的标志")
    SECURITIESLENDING = Column(String(4), doc="融券标的标志")
    PRODSTATUSID = Column(String(40), doc="产品状态标志")
    NOTE = Column(String(200), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class smt_collateral(Base):

    __tablename__ = 'smt_collateral'

    EXCHANGECODE = Column(String(20), doc="交易所编码      ")
    IMPLEMENTDATE = Column(DateTime, doc="实施日期      ")
    SECURITYTYPE = Column(String(40), doc="证券类别      ")
    SECURITYSUBTYPE = Column(String(120), doc="证券类别细分  ")
    HIGHESTDISCOUNT = Column(DECIMAL(6, 2), doc="最高折算率    ")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    FINANCETRADINGMARGIN = Column(DECIMAL(6, 2), doc="融资保证金比例")
    SHORTTRADINGMARGIN = Column(DECIMAL(6, 2), doc="融券保证金比例")


class smt_collaterald(Base):

    __tablename__ = 'smt_collaterald'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    EXCHANGECODE = Column(String(20), doc="市场编码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="证券代码")
    SHORTNAME = Column(String(40), doc="证券简称")
    SECURITYTYPEID = Column(String(12), doc="证券类型编码")
    HIGHESTDISCOUNT = Column(DECIMAL(6, 2), doc="最高折算率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class smt_traded(Base):

    __tablename__ = 'smt_traded'

    TRADINGDATE = Column(DateTime, doc="交易日期     ")
    EXCHANGECODE = Column(String(20), doc="市场编码     ")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID       ")
    SYMBOL = Column(String(20), doc="证券代码   ")
    SHORTNAME = Column(String(100), doc="证券中文简称   ")
    BUYVALUE = Column(BIGINT, doc="融资买入额   ")
    REPAYVALUE = Column(BIGINT, doc="融资偿还额   ")
    BALANCEVALUE = Column(BIGINT, doc="融资余额     ")
    SELLSHARES = Column(BIGINT, doc="融券卖出量   ")
    REPAYSHARES = Column(BIGINT, doc="融券偿还量   ")
    BALANCESHARES = Column(BIGINT, doc="融券余量     ")
    BALANCESHARESVALUE = Column(BIGINT, doc="融券余额     ")
    SMTBALANCEVALUE = Column(BIGINT, doc="融资融券余额 ")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class smt_tradesumd(Base):

    __tablename__ = 'smt_tradesumd'

    TRADINGDATE = Column(DateTime, doc="信用交易日期            ")
    EXCHANGECODE = Column(String(20), doc="交易所编码              ")
    BUYVALUE = Column(BIGINT, doc="融资买入额              ")
    REPAYVALUE = Column(BIGINT, doc="融资偿还额              ")
    BALANCEVALUE = Column(BIGINT, doc="融资余额                ")
    SELLSHARES = Column(BIGINT, doc="融券卖出量              ")
    REPAYSHARES = Column(BIGINT, doc="融券偿还量              ")
    BALANCESHARES = Column(BIGINT, doc="融券余量                ")
    BALANCESHARESVALUE = Column(BIGINT, doc="融券余额                ")
    SMTBALANCEVALUE = Column(BIGINT, doc="融资融券余额            ")
    FINANCESTOCKNUMBER = Column(BIGINT, doc="当日发生融资的股票数量  ")
    LENDINGSTOCKNUMBER = Column(BIGINT, doc="当日发生融券的股票数量  ")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class smt_underlyingsd(Base):

    __tablename__ = 'smt_underlyingsd'

    EXCHANGECODE = Column(String(20), doc="交易所编码     ")
    TRADINGDATE = Column(DateTime, doc="信用交易日期   ")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID         ")
    SYMBOL = Column(String(20), doc="证券代码       ")
    SHORTNAME = Column(String(100), doc="证券中文简称   ")
    FINANCEAVAILABLE = Column(String(2), doc="可融资标识     ")
    SHORTAVAILABLE = Column(String(2), doc="可融券标识     ")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    TODAYFINANCEAVAILABLE = Column(String(2), doc="当日可融资标识")
    TODAYSHORTAVAILABLE = Column(String(2), doc="当日可融券标识")


class so_calpretrdinfo(Base):

    __tablename__ = 'so_calpretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    SYMBOL = Column(String(40), primary_key=True, doc="交易代码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    SHORTNAME = Column(String(40), doc="合约简称")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSECURITYSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(20), doc="标的证券简称")
    UNDERLYINGTYPE = Column(String(20), doc="标的证券类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约单位")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="昨结算价")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="单位保证金")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    SECURITYSTATUSUSFLAG = Column(String(20), doc="期权合约状态信息标签")
    UPDATEID = Column(BIGINT, doc="数据ID")
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    TICKSIZE = Column(DECIMAL(10, 4), doc="最小变动单位")


class so_pretrdinfo(Base):

    __tablename__ = 'so_pretrdinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    SYMBOL = Column(String(40), primary_key=True, doc="交易代码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    SHORTNAME = Column(String(40), doc="合约简称")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSECURITYSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(20), doc="标的证券简称")
    UNDERLYINGTYPE = Column(String(20), doc="标的证券类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约单位")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="昨结算价")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="单位保证金")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    SECURITYSTATUSUSFLAG = Column(String(20), doc="期权合约状态信息标签")
    UPDATEID = Column(BIGINT, doc="数据ID")
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    TICKSIZE = Column(DECIMAL(10, 4), doc="最小报价单位")
    UPDATEVERSION = Column(String(20), doc="合约版本号")
    MARGINRATIOPARAM1 = Column(DECIMAL(10, 3), doc="保证金计算比例参数一")
    MARGINRATIOPARAM2 = Column(DECIMAL(10, 3), doc="保证金计算比例参数二")
    ROUNDLOT = Column(BIGINT, doc="整手数")
    LMTORDMINFLOOR = Column(BIGINT, doc="单笔限价申报下限")
    LMTORDMAXFLOOR = Column(BIGINT, doc="单笔限价申报上限")
    MKTORDMINFLOOR = Column(BIGINT, doc="单笔市价申报下限")
    MKTORDMAXFLOOR = Column(BIGINT, doc="单笔市价申报上限")


class so_pretrdinfohistory(Base):

    __tablename__ = 'so_pretrdinfohistory'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    EXCHANGECODE = Column(String(12), primary_key=True, doc="交易所代码")
    SYMBOL = Column(String(40), primary_key=True, doc="交易代码")
    CONTRACTCODE = Column(String(40), doc="合约编码")
    SHORTNAME = Column(String(40), doc="合约简称")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    UNDERLYINGSECURITYID = Column(DECIMAL(20, 0), doc="标的证券ID")
    UNDERLYINGSECURITYSYMBOL = Column(String(20), doc="标的证券交易代码")
    UNDERLYINGSHORTNAME = Column(String(20), doc="标的证券简称")
    UNDERLYINGTYPE = Column(String(20), doc="标的证券类型")
    UNDERLYINGPRECLOSEPRICE = Column(DECIMAL(11, 4), doc="标的证券前收盘")
    OPTIONTYPE = Column(String(20), doc="欧式美式")
    CALLORPUT = Column(String(20), doc="认购认沽")
    CONTRACTMULTIPLIERUNIT = Column(BIGINT, doc="合约单位")
    STRIKEPRICE = Column(DECIMAL(11, 4), doc="行权价")
    LISTEDDATE = Column(DateTime, doc="首日上市日期")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    EXERCISEDATE = Column(DateTime, doc="行权日")
    DELIVERYDATE = Column(DateTime, doc="交收日")
    EXPIREDATE = Column(DateTime, doc="到期日")
    PRECLOSEPRICE = Column(DECIMAL(10, 4), doc="昨收盘价")
    PRESETTLEPRICE = Column(DECIMAL(11, 4), doc="昨结算价")
    PREPOSITION = Column(DECIMAL(20, 0), doc="昨持仓量")
    LIMITUP = Column(DECIMAL(10, 4), doc="涨停价")
    LIMITDOWN = Column(DECIMAL(10, 4), doc="跌停价")
    MARGINUNIT = Column(DECIMAL(11, 4), doc="单位保证金")
    BENCHMARKOPENPRICE = Column(DECIMAL(11, 4), doc="开盘基准价")
    SECURITYSTATUSUSFLAG = Column(String(20), doc="期权合约状态信息标签")
    UPDATEID = Column(BIGINT, doc="数据ID")
    PREVOLUME = Column(DECIMAL(20, 0), doc="昨成交量")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    INTERESTRATE = Column(DECIMAL(18, 6), doc="无风险利率")
    REMAININGDAYS = Column(INTEGER, doc="剩余天数")
    TICKSIZE = Column(DECIMAL(10, 4), doc="最小报价单位")
    UPDATEVERSION = Column(String(20), doc="合约版本号")
    MARGINRATIOPARAM1 = Column(DECIMAL(10, 3), doc="保证金计算比例参数一")
    MARGINRATIOPARAM2 = Column(DECIMAL(10, 3), doc="保证金计算比例参数二")
    ROUNDLOT = Column(BIGINT, doc="整手数")
    LMTORDMINFLOOR = Column(BIGINT, doc="单笔限价申报下限")
    LMTORDMAXFLOOR = Column(BIGINT, doc="单笔限价申报上限")
    MKTORDMINFLOOR = Column(BIGINT, doc="单笔市价申报下限")
    MKTORDMAXFLOOR = Column(BIGINT, doc="单笔市价申报上限")


class stk_af_analystrank(Base):

    __tablename__ = 'stk_af_analystrank'

    RATINGYEAR = Column(SMALLINT, doc="评比年度")
    INDUSTRYCODE = Column(String(20), doc="行业编码")
    INDUSTRYNAME = Column(String(100), doc="行业名称")
    INDUSTRYNAME_EN = Column(String(200), doc="行业名称_英")
    RANKING = Column(SMALLINT, doc="排名")
    INSTITUTIONNAME = Column(String(200), doc="研究机构")
    INSTITUTIONNAME_EN = Column(String(400), doc="研究机构_英")
    INSTITUTIONID = Column(String(200), doc="研究机构ID")
    ANALYST = Column(String(200), doc="分析师")
    ANALYST_EN = Column(String(600), doc="分析师_英")
    ANALYSTID = Column(String(2000), doc="分析师ID")
    COMMENTS = Column(String(400), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class stk_af_forecast(Base):

    __tablename__ = 'stk_af_forecast'

    REPORTID = Column(DECIMAL(20, 0), doc="研究报告ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="股票代码")
    REPORTDATE = Column(DateTime, doc="报告日")
    FORECASTYEAR = Column(DateTime, doc="预测年度")
    FORECASTTARGETID = Column(String(20), doc="预测指标编码")
    FORECASTTARGET = Column(String(100), doc="预测指标")
    FORECASTTARGET_EN = Column(String(200), doc="预测指标_EN")
    TARGETVALUE = Column(DECIMAL(24, 6), doc="指标值")
    LASTTARGETVALUE = Column(DECIMAL(24, 6), doc="上期指标值")
    INSTITUTIONNAME = Column(String(200), doc="研究机构")
    INSTITUTIONNAME_EN = Column(String(400))
    INSTITUTIONID = Column(String(200))
    ANALYST = Column(String(200), doc="分析师")
    ANALYST_EN = Column(String(600))
    ANALYSTID = Column(String(2000))
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    LASTREPORTDATE = Column(DateTime, doc="上期报告日")


class stk_af_ratingchange(Base):

    __tablename__ = 'stk_af_ratingchange'

    REPORTID = Column(DECIMAL(20, 0), primary_key=True, doc="研究报告ID")
    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    SYMBOL = Column(String(20), doc="股票代码")
    SHORTNAME = Column(String(20), doc="证券简称")
    SHORTNAME_EN = Column(String(40), doc="证券简称_英")
    REPORTDATE = Column(DateTime, doc="报告日")
    RATERESULT = Column(String(100), doc="评级结论")
    STANDARDRATING = Column(String(12), doc="标准化评级")
    STANDARDRATING_EN = Column(String(100), doc="标准化评级_英")
    RATERESULTID = Column(String(20), doc="标准化评级编码")
    RATINGCHANGE = Column(String(20), doc="评级变动")
    RATINGCHANGE_EN = Column(String(40), doc="评级变动_英")
    RATINGCHANGEID = Column(String(20), doc="评级变动编码")
    RATINGMARK = Column(String(4000), doc="评级基准")
    INSTITUTIONNAME = Column(String(200), doc="研究机构")
    INSTITUTIONNAME_EN = Column(String(400), doc="研究机构_英")
    INSTITUTIONID = Column(String(200), doc="研究机构ID")
    ANALYST = Column(String(200), doc="分析师")
    ANALYST_EN = Column(String(600), doc="分析师_英")
    ANALYSTID = Column(String(2000), doc="分析师ID")
    SUMMARY = Column(String(4000), doc="摘要")
    FILESTORAGEPATH = Column(String(400), doc="报告存贮路径")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_af_ratingstatistic(Base):

    __tablename__ = 'stk_af_ratingstatistic'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="股票代码")
    STATISTICDATE = Column(DateTime, doc="统计日")
    STATISTICDAYS = Column(String(20), doc="统计区间")
    STATISTICDAYSID = Column(String(20), doc="统计区间ID")
    BUY = Column(INTEGER, doc="买入")
    OUTPERFORM = Column(INTEGER, doc="增持")
    NEUTRAL = Column(INTEGER, doc="中性")
    UNDERPERFORM = Column(INTEGER, doc="减持")
    SELL = Column(INTEGER, doc="卖出")
    RATESUM = Column(INTEGER, doc="评级数")
    MASSRATING = Column(String(12), doc="众数评级")
    MASSRATINGID = Column(String(20), doc="众数评级ID")
    RATERESULT = Column(String(12), doc="综合评级")
    RATERESULTID = Column(String(20), doc="综合评级ID")
    RATINGCHANGE = Column(String(20), doc="综合评级变动")
    RATINGCHANGEID = Column(String(20), doc="综合评级变动ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    AVGRATE = Column(DECIMAL(8, 4))


class stk_af_targetvalue(Base):

    __tablename__ = 'stk_af_targetvalue'

    REPORTID = Column(DECIMAL(20, 0), doc="研究报告ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="股票代码")
    REPORTDATE = Column(DateTime, doc="报告日")
    OBJECTPRICEMAX = Column(DECIMAL(6, 2), doc="目标价格上限")
    OBJECTPRICEMIN = Column(DECIMAL(6, 2), doc="目标价格下限")
    PRICETERM = Column(String(100), doc="目标价期限")
    PRICETERMID = Column(String(20), doc="目标价期限编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONNAME = Column(String(200), doc="研究机构")
    INSTITUTIONNAME_EN = Column(String(400))
    INSTITUTIONID = Column(String(200))
    ANALYST = Column(String(200), doc="分析师")
    ANALYST_EN = Column(String(600))
    ANALYSTID = Column(String(2000))


class stk_calendard(Base):

    __tablename__ = 'stk_calendard'

    CALENDARDATE = Column(DateTime, primary_key=True, doc="日历日期")
    EXCHANGECODE = Column(String(40), primary_key=True, doc="交易所编码")
    ISOPEN = Column(String(2), doc="开市与否")
    WEEKDAY = Column(SMALLINT, doc="星期")
    UPDATEID = Column(BIGINT)


class stk_dividend(Base):

    __tablename__ = 'stk_dividend'

    SECURITYID = Column(DECIMAL(20, 0))
    SYMBOL = Column(String(20))
    DIVDENDYEAR = Column(SMALLINT)
    RANK = Column(SMALLINT)
    TERMCODE = Column(String(12))
    ISDIVIDEND = Column(String(2))
    DECLAREDATE = Column(DateTime)
    DIVDENDPLAN = Column(String(1000))
    DIVIDEND_EN = Column(String(1000))
    IMPLEMENTATIONCONTENT = Column(String(1000))
    IMPLEMENTATIONCONTENT_EN = Column(String(1000))
    OBJECT = Column(String(1000))
    OBJECT_EN = Column(String(1000))
    SCHEDULE = Column(String(40))
    HOLDERSMEETINGDATE = Column(DateTime)
    HOLDERSMEETINGDECLAREDATE = Column(DateTime)
    IMPLEMENTATIONDATE = Column(DateTime)
    PLANBONUSRATIO = Column(DECIMAL(10, 6))
    PLANCONVERSIONRATIO = Column(DECIMAL(10, 6))
    PLANDIVIDENTBT = Column(DECIMAL(10, 6))
    BONUSRATIO = Column(DECIMAL(10, 6))
    CONVERSIONRATIO = Column(DECIMAL(10, 6))
    DIVIDENTBT = Column(DECIMAL(10, 6))
    DIVIDENTAT = Column(DECIMAL(10, 6))
    RECORDDATE = Column(DateTime)
    EXDIVIDENDDATE = Column(DateTime)
    FINALTRADINGDATE = Column(DateTime)
    PAYMENTDATE = Column(DateTime)
    ADDSHARESLISTINGDATE = Column(DateTime)
    EXCHANGERATEDATE = Column(DateTime)
    DISTRIBUTIONBASESHARES = Column(DECIMAL(20, 0))
    CURRENCY = Column(String(40))
    PLANCHANGEDESCRIPTION = Column(String(1000))
    NODIVIDENDREASON = Column(String(1000))
    ADDSHARES = Column(DECIMAL(20, 2))
    TOTALDIVIDENDDISTRI = Column(DECIMAL(20, 4))
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    EVENTID = Column(BIGINT, doc="事件ID")
    PROPOSDATE = Column(DateTime, doc="提议日期")
    PROPOSER = Column(String(1000), doc="提议人")
    PROPOSBONUSRATIO = Column(DECIMAL(10, 6), doc="每10股送股数（提）")
    PROPOSCONVERSIONRATIO = Column(DECIMAL(10, 6), doc="每10股转增股数（提）")
    PROPOSDIVIDENTBT = Column(DECIMAL(10, 6), doc="每10股派现税前（提）")
    PROPOSCONTENT = Column(String(1000), doc="提议内容")
    PROPOSCONTENT_EN = Column(String(1000), doc="提议内容(英文)")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class stk_eq_ipo_coinfo(Base):

    __tablename__ = 'stk_eq_ipo_coinfo'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    CROSSSYMBOL = Column(String(12), doc="AB股交叉码")
    SHORTNAME = Column(String(16), doc="证券简称")
    INDUSTRYID = Column(String(8), doc="行业代码A")
    INDUSTRYOLDNAME = Column(String(100), doc="行业名称A")
    INDUSTRYCODE = Column(String(10), doc="行业代码B")
    INDUSTRYNAME = Column(String(100), doc="行业名称B")
    EXCHANGECODE = Column(String(20), doc="上市交易所")
    FULLNAME = Column(String(160), doc="公司名称")
    ENNAME = Column(String(300), doc="公司英文名称")
    ESTABLISHDATE = Column(DateTime, doc="公司成立日期")
    IPODATE = Column(DateTime, doc="首次招股日期")
    LISTEDDATE = Column(DateTime, doc="公司上市日期")
    REGISTERADDRESS = Column(String(400), doc="公司注册地")
    REGISTERCITY = Column(String(100), doc="公司注册所在地")
    LEGALREPRESENTATIVE = Column(String(40), doc="法定代表人")
    RETIREDNUMBER = Column(INTEGER, doc="上市时公司职工人数")
    DIRECTORNUMBER = Column(INTEGER, doc="上市时公司董事会人数")
    SUPERVISORNUMBER = Column(INTEGER, doc="上市时公司监事会人数")
    INDCLASSIFYSYSTEMCODE = Column(String(40), doc="行业分类标准编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    REGISTEREDCAPITAL = Column(BIGINT, doc="注册资本")
    MAINBUSSINESS = Column(String(2000), doc="主营业务")
    BUSSINESSRANGE = Column(String(4000), doc="公司经营范围")
    COHISTORY = Column(String(4000), doc="公司历史沿革")
    SOCIALCREDITCODE = Column(String(20), doc="统一社会信用代码")


class stk_eq_ipo_employeeinfo(Base):

    __tablename__ = 'stk_eq_ipo_employeeinfo'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    STATISTICALSCOPEID = Column(String(20), doc="统计范围ID")
    STATISTICALSCOPE = Column(String(20), doc="统计范围")
    STATISTICALCOVERAGEID = Column(String(20), doc="统计口径ID")
    STATISTICALCOVERAGE = Column(String(20), doc="统计口径")
    POSITIONTYPE = Column(String(100), doc="人员类型名称")
    POSITIONTYPE_EN = Column(String(400), doc="人员类型名称_英")
    EMPLOYEENUMBER = Column(INTEGER, doc="人数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class stk_eq_ipo_info(Base):

    __tablename__ = 'stk_eq_ipo_info'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    ISIPO = Column(String(2), doc="是否首次发行")
    IPO1DECLAREDATE = Column(DateTime, doc="招股意向书公告日期")
    SIGNDATE = Column(DateTime, doc="招股说明书签署日期")
    IPO2DECLAREDATE = Column(DateTime, doc="招股说明书发表日期")
    PUBLICATIONS = Column(String(200), doc="招股说明书发表刊物")
    PUBLICATIONS_EN = Column(String(400), doc="招股说明书发表刊物_英")
    WEBSITE = Column(String(200), doc="招股说明书发表网站")
    ROADSHOWWEBSITE = Column(String(400), doc="路演网站")
    ROADSHOWSTARTDATE = Column(DateTime, doc="路演开始日期")
    ROADSHOWENDDATE = Column(DateTime, doc="路演截止日期")
    STARTDATE = Column(DateTime, doc="招股开始日期")
    ENDDATE = Column(DateTime, doc="招股截至日期")
    ONLINESTARTDATE = Column(DateTime, doc="网上申购开始日期")
    ONLINEENDDATE = Column(DateTime, doc="网上申购截止日期")
    OFFLINESTARTDATE = Column(DateTime, doc="网下配售起始日")
    OFFLINEENDDATE = Column(DateTime, doc="网下配售截止日")
    SECONDARYMARKETISSUEDATE = Column(DateTime, doc="二级市场配售日期")
    IPO3DECLAREDATE = Column(DateTime, doc="发行定价公告日期")
    OTHERISSUEDATE = Column(DateTime, doc="其他发行日期")
    CALCULATIONDATE = Column(DateTime, doc="市值计算日")
    IPO4DECLAREDATE = Column(DateTime, doc="上市公告书发表日期")
    PUBLICATIONS2 = Column(String(200), doc="上市公告书发表刊物")
    PUBLICATIONS2_EN = Column(String(400), doc="上市公告书发表刊物_英")
    WEBSITE2 = Column(String(200), doc="上市公告书发表网站")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    PARVALUE = Column(DECIMAL(10, 2), doc="每股面值")
    CURRENCYCODE = Column(String(12), doc="货币编码")
    CURRENCY = Column(String(20), doc="货币")
    ISSUESHARES = Column(DECIMAL(20, 0), doc="总发行规模")
    ISSUESHARESPRIVATE = Column(DECIMAL(20, 0), doc="非公开发行股份数")
    ISSUESHARESPUBLIC = Column(DECIMAL(20, 0), doc="公开招股数量")
    OPTIONSIGN = Column(String(2), doc="超额配售选择权标志")
    PRICE = Column(DECIMAL(10, 2), doc="招股价格人民币")
    PRICEPUBLIC = Column(DECIMAL(10, 2), doc="发行价格人民币")
    PRICESPECIAL = Column(DECIMAL(10, 2), doc="特别发行价格人民币")
    ISSUEOBJECT = Column(String(1000), doc="发行对象")
    ISSUEMODEID = Column(String(100), doc="发行方式ID")
    ISSUEMODE = Column(String(100), doc="发行方式")
    PRICEMODEID = Column(String(40), doc="发行定价方式ID")
    PRICEMODE = Column(String(40), doc="发行定价方式")
    UNDERWRITEDMETHODSID = Column(String(12), doc="承销方式ID")
    UNDERWRITEDMETHODS = Column(String(20), doc="承销方式")
    PE1 = Column(DECIMAL(10, 4), doc="发行前加权平均市盈率")
    PE1CEILING = Column(DECIMAL(10, 4), doc="发行前加权平均市盈率上限")
    PE1FLOOR = Column(DECIMAL(10, 4), doc="发行前加权平均市盈率下限")
    PE2 = Column(DECIMAL(10, 4), doc="发行前全面摊薄市盈率")
    PE2CEILING = Column(DECIMAL(10, 4), doc="发行前全面摊薄市盈率上限")
    PE2FLOOR = Column(DECIMAL(10, 4), doc="发行前全面摊薄市盈率下限")
    PE3 = Column(DECIMAL(10, 4), doc="加权发行市盈率")
    PE4 = Column(DECIMAL(10, 4), doc="摊薄发行市盈率")
    NAV1 = Column(DECIMAL(10, 4), doc="发行前每股净资产")
    NAV2 = Column(DECIMAL(10, 4), doc="发行后每股净资产")
    EPS1 = Column(DECIMAL(10, 4), doc="发行前每股收益")
    EPS2 = Column(DECIMAL(10, 4), doc="发行后每股收益")
    PB = Column(DECIMAL(10, 4), doc="发行市净率")
    ACTUALISSUESHARES = Column(DECIMAL(20, 0), doc="实际发行总量")
    ACTUALRAISEDSHARESPRIVATE = Column(DECIMAL(20, 0), doc="实际非公开发行总股数")
    ACTUALRAISEDSHARESLEGALENTITY = Column(DECIMAL(20, 0), doc="定向募集法人股")
    ACTUALRAISEDSHARESSTAFF = Column(DECIMAL(20, 0), doc="定向募集职工股")
    ACTUALRAISEDSHARESSPECIAL = Column(DECIMAL(20, 0), doc="特别发行数量")
    ACTUALRAISEDSHARESPUBLIC = Column(DECIMAL(20, 0), doc="实际公开发行总股数")
    EXPECTRAISEFUND = Column(DECIMAL(20, 2), doc="预计募集资金总额")
    EXPECTRAISENETFUND = Column(DECIMAL(20, 2), doc="预计募集资金净额")
    EXPECTEXPENSE = Column(DECIMAL(20, 2), doc="预计发行总费用")
    RAISEFUND = Column(DECIMAL(20, 2), doc="实际募集资金总额人民币")
    RAISENETFUND = Column(DECIMAL(20, 2), doc="实际募集资金净额人民币")
    EXPENSE = Column(DECIMAL(20, 2), doc="实际发行总费用人民币")
    EXPENSEPERSHARE = Column(DECIMAL(10, 4), doc="每股发行费用人民币")
    PRICESPECIALINFOREIGN = Column(DECIMAL(10, 2), doc="特别发行价格外币")
    CURRENCYCODE1 = Column(String(12), doc="特别发行价格外币编码")
    CURRENCY1 = Column(String(100), doc="特别发行价格外币币种")
    PRICEPUBLICINFOREIGN = Column(DECIMAL(10, 2), doc="公开发行价格外币")
    CURRENCYCODE2 = Column(String(12), doc="公开发行价格外币编码")
    CURRENCY2 = Column(String(100), doc="公开发行价格外币币种")
    RAISEFUNDINFOREIGN = Column(DECIMAL(20, 2), doc="实际募集资金总额外币")
    RAISENETFUNDINFOREIGN = Column(DECIMAL(20, 2), doc="实际募集资金净额外币")
    EXPENSEINFOREIGN = Column(DECIMAL(20, 2), doc="实际发行总费用外币")
    EXPENSEPERSHAREINFOREIGN = Column(DECIMAL(10, 4), doc="每股发行费用外币")
    REGISTEREDCAPITAL1 = Column(DECIMAL(20, 2), doc="公司招股时注册资本")
    REGISTEREDCAPITAL2 = Column(DECIMAL(20, 2), doc="公司上市时注册资本")
    BANK = Column(String(400), doc="公司的收款银行")
    BANK_EN = Column(String(1000))
    ACCOUNTS = Column(String(400), doc="公司的银行帐号")
    TAXRATE = Column(DECIMAL(8, 2), doc="发行时所得税税率")
    TAXRATETYPEID = Column(String(20), doc="发行时所得税税率类型ID")
    TAXRATETYPE = Column(String(20), doc="发行时所得税税率类型")
    TAXRATETYPE_EN = Column(String(100), doc="发行时所得税税率类型_英")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)
    INQUIRYDECLAREDATE = Column(DateTime, doc="初步询价公告日")
    INQUIRYSTARTDATE = Column(DateTime, doc="初步询价起始日")
    INQUIRYENDDATE = Column(DateTime, doc="初步询价截止日")
    OFFLINEPRICEDATE = Column(DateTime, doc="网下定价日")
    ROADSHOWDECLAREDATE = Column(DateTime, doc="网上路演公告日")
    ISSUEDECLAREDATE = Column(DateTime, doc="发行公告日")
    DIVIDENDPOLICY = Column(String(4000), doc="股利分配政策")


class stk_eq_ipo_ipocg(Base):

    __tablename__ = 'stk_eq_ipo_ipocg'

    SYMBOL = Column(String(6), doc="股票代码")
    IPODATE = Column(DateTime, doc="招股日期")
    CONATURE = Column(String(100), doc="公司性质")
    ISPE = Column(String(1), doc="是否有私募（或风投）")
    FIRSTPENAME = Column(String(100), doc="第一大私募名称")
    FIRSTPESHARES = Column(DECIMAL(20, 0), doc="第一大私募持股数")
    FIRSTPESHARERATIO = Column(DECIMAL(10, 4), doc="第一大私募持股比率")
    DIRECTORNUMBER = Column(SMALLINT, doc="董事会成员数量")
    INDDIRECTORNUM = Column(SMALLINT, doc="独立董事数量")
    ISPARTTIME = Column(String(1), doc="董事长与总经理兼任情况")
    AUDITCOMMEMBERNUM = Column(SMALLINT, doc="审计委员会成员数量")
    AUDITCOMINDDIRNUM = Column(SMALLINT, doc="审计委员会独立董事数量")
    REMASSCOMMEMBERNUM = Column(SMALLINT, doc="薪酬与考核委员会成员数量")
    REMASSCOMINDDIRNUM = Column(SMALLINT, doc="薪酬与考核委员会独立董事数量")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class stk_eq_ipo_marketexhibit(Base):

    __tablename__ = 'stk_eq_ipo_marketexhibit'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    CURRENCY = Column(String(12))
    OPENPRICE = Column(DECIMAL(9, 3), doc="首日开盘价")
    HIGHPRICE = Column(DECIMAL(9, 3), doc="首日最高价")
    LOWPRICE = Column(DECIMAL(9, 3), doc="首日最低价")
    CLOSEPRICE = Column(DECIMAL(9, 3), doc="首日收盘价")
    VOLUME = Column(BIGINT, doc="首日交易股数")
    AMOUNT = Column(DECIMAL(16, 2), doc="首日交易金额")
    RETURN = Column(DECIMAL(12, 6), doc="上市首日的个股回报率")
    ADJUSTEDRETURN = Column(DECIMAL(12, 6), doc="上市首日经市场调整的个股回报率")
    PE = Column(DECIMAL(8, 2), doc="上市首日市盈率")
    PB = Column(DECIMAL(8, 2), doc="上市首日市净率")
    TURNOVERRATE = Column(DECIMAL(10, 5), doc="上市首日换手率")
    MARKETRETURN = Column(DECIMAL(12, 6), doc="上市首日的市场回报率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_eq_ipo_overallot(Base):

    __tablename__ = 'stk_eq_ipo_overallot'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="最后行使日期")
    AVERAGEPRICE = Column(DECIMAL(10, 2), doc="行权中竞价交易购买股票均价")
    SHARES = Column(DECIMAL(20, 0), doc="行权中竞价交易购买股票数量")
    OVERALLOTMENTSHARES = Column(DECIMAL(20, 0), doc="超额发行股份数")
    OVERALLOTMENTRATIO = Column(DECIMAL(8, 4), doc="超额配售率")
    ISFULLAMOUNT = Column(String(2), doc="是否全额")
    FUNDADDED = Column(DECIMAL(20, 2), doc="增加的募集资金")
    EXPENSEADDED = Column(DECIMAL(20, 2), doc="增加的募集资金费用")
    RAISEFUND = Column(DECIMAL(20, 2), doc="行权后募集资金总额人民币")
    RAISENETFUND = Column(DECIMAL(20, 2), doc="行权后募集资金净额人民币")
    RAISEFUNDINFOREIGNCURRENCY = Column(DECIMAL(20, 2), doc="行权后募集资金总额外币")
    RAISENETFUNDINFOREIGNCURRENCY = Column(DECIMAL(20, 2), doc="行权后募集资金净额外币")
    CURRENCYCODE = Column(String(12), doc="外币币种编码")
    CURRENCY = Column(String(20), doc="外币币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_eq_ipo_result(Base):

    __tablename__ = 'stk_eq_ipo_result'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    SUBSCRIPTIONCODE1 = Column(String(16), doc="申购代码1")
    SHORTNAME1 = Column(String(40), doc="申购简称1")
    SHORTNAME1_EN = Column(String(40), doc="申购简称1_英")
    SUBSCRIPTIONCODE2 = Column(String(16), doc="申购代码2")
    SHORTNAME2 = Column(String(40), doc="申购简称2")
    SHORTNAME2_EN = Column(String(40), doc="申购简称2_英")
    SUBSCRIPTIONCODE3 = Column(String(16), doc="申购代码3")
    SHORTNAME3 = Column(String(40), doc="申购简称3")
    SHORTNAME3_EN = Column(String(40), doc="申购简称3_英")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    DECLAREDATE = Column(DateTime, doc="中签率公告日期")
    PRICESCOPE = Column(String(100), doc="申购价格范围")
    ONLINEISSUE = Column(DECIMAL(20, 0), doc="网上发行数量")
    ONLINEISSUETOTOTALISSUE = Column(DECIMAL(10, 4), doc="网上发行占发行总量的比例")
    ONLINEPURCHASEHOUSEHOLDERS = Column(BIGINT, doc="网上有效申购户数")
    ONLINEPURCHASESHARES = Column(DECIMAL(20, 0), doc="网上有效申购股数")
    ONLINESUCCESSRATE = Column(DECIMAL(12, 6), doc="网上发行中签率")
    ONLINEOVERSUBSCRIPTIONRATIO = Column(DECIMAL(10, 4), doc="网上超额认购倍数")
    OFFLINEISSUE = Column(DECIMAL(20, 0), doc="网下配售数量")
    OFFLINEISSUETOTOTALISSUE = Column(DECIMAL(10, 4), doc="网下配售占发行总量的比例")
    OFFLINEPURCHASESHARES = Column(DECIMAL(20, 0), doc="网下有效申购股数")
    OFFLINEPURCHASEHOUSEHOLDERS = Column(BIGINT, doc="网下有效申购户数")
    OFFLINESUCCESSRATE = Column(DECIMAL(12, 6), doc="网下配售比例")
    OFFLINEOVERSUBSCRIPTIONRATIO = Column(DECIMAL(10, 4), doc="网下配售超额认购倍数")
    ISSUEMARKET = Column(DECIMAL(20, 0), doc="市值配售数量")
    ISSUEMARKETTOTOTALISSUE = Column(DECIMAL(10, 4), doc="市值配售占发行总量的比例")
    PURCHASESHARESMARKET = Column(DECIMAL(20, 0), doc="市值配售有效申购股数")
    PURCHASEHOUSEHOLDERSMARKET = Column(BIGINT, doc="市值配售有效申购户数")
    SUCCESSRATEMARKET = Column(DECIMAL(12, 6), doc="市值配售中签率")
    OVERSUBSCRIPTIONRATIOMARKET = Column(DECIMAL(10, 4), doc="市值配售超额认购倍数")
    ISSUESTRATEGIC = Column(DECIMAL(20, 0), doc="战略投资者配售数量")
    ISSUESTRATEGICTOTOTALISSUE = Column(DECIMAL(10, 4), doc="战略投资者配售占发行总量的比例")
    OVERALLOTMENTSHARES = Column(DECIMAL(20, 0), doc="超额配售股份数")
    OBJECTOVERALLOTMENT = Column(String(400), doc="超额配售发行对象")
    OBJECTOVERALLOTMENT_EN = Column(String(800), doc="超额配售发行对象_英")
    PURCHASESHARES = Column(DECIMAL(20, 0), doc="总有效申购股数")
    PURCHASEHOUSEHOLDERS = Column(BIGINT, doc="总有效申购户数")
    OVERSUBSCRIPTIONRATIO = Column(DECIMAL(10, 4), doc="总超额认购倍数")
    SUCCESSRATE = Column(DECIMAL(12, 6), doc="总中签率")
    CALLBACKSIGN = Column(String(2), doc="回拨机制适用性")
    CALLBACKTYPEID = Column(String(12), doc="回拨方式ID")
    CALLBACKTYPE = Column(String(40), doc="回拨方式")
    CALLBACKSHARES = Column(DECIMAL(20, 0), doc="回拨数量")
    STOPISSUESIGN = Column(String(2), doc="发行中止标志")
    LISTEDSHARES = Column(DECIMAL(20, 0), doc="本次上市流通股数")
    EXISTINGSTATEOWNEDSHARES = Column(DECIMAL(16, 4), doc="其中：国有股存量实际发行数量")
    PUBLICSHARES = Column(DECIMAL(16, 4), doc="其中：社会公众实际发行数量")
    STAFFSHARES = Column(DECIMAL(16, 4), doc="其中：员工实际发行数量")
    STRATEGICINVESTORSHARES = Column(DECIMAL(16, 4), doc="其中：战略投资者实际配售数量")
    FUNDSHARES = Column(DECIMAL(16, 4), doc="其中：基金实际配售数量")
    INSURANCECOMPANYSHARES = Column(DECIMAL(16, 4), doc="其中：保险公司实际配售数量")
    LEGALENTITYSHARES = Column(DECIMAL(16, 4), doc="其中：一般法人实际配售数量")
    UNDERWRITINGBALANCESHARES = Column(DECIMAL(20, 0), doc="承销余额")
    OTHERSHARES = Column(DECIMAL(16, 4), doc="其中：其他发行数量")
    LOCKUPPERIODLEGALENTITY = Column(String(40), doc="向一般法人配售股份锁定期")
    LOCKUPPERIODINSURANCE = Column(String(40), doc="向保险公司配售股份锁定期")
    LOCKUPPERIODFUND = Column(String(40), doc="向基金配售股份锁定期")
    LOCKUPPERIODSTRATEGICINVESTOR = Column(String(40), doc="向战略投资者配售股份锁定期")
    LOCKUPPERIODOTHERSHARES = Column(String(40), doc="其他发行股份锁定期")
    FUNDSHARESTOTOTAL = Column(DECIMAL(12, 8), doc="被基金所持比率")
    SHAREHOLDERS = Column(BIGINT, doc="持股户数")
    SHAREHOLDERSOVER1000 = Column(BIGINT, doc="持有1000股以上户数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)
    ONLINEDISTRNUM = Column(DECIMAL(20, 0), doc="网上发行配号总数")
    OFFLINEDECLAREDATE = Column(DateTime, doc="网下配售结果公告日")
    ONLINEVERIFICDATE = Column(DateTime, doc="网上申购资金验资日")
    OFFLINEVERIFICDATE = Column(DateTime, doc="网下申购资金验资日")
    OFFLINEISSUEPAYMENTDATE = Column(DateTime, doc="网下发行缴款日")
    ISSUERESULTDECLAREDATE = Column(DateTime, doc="发行结果公告日")
    RAISEFUNDARRIVALDATE = Column(DateTime, doc="募集资金到帐日期")
    RAISEFUNDARRIVAAMOUNT = Column(DECIMAL(20, 2), doc="募集资金到帐金额")


class stk_eq_rs_info(Base):

    __tablename__ = 'stk_eq_rs_info'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    DECLAREDATE = Column(DateTime, doc="配股说明书公告日期")
    SIGNDATE = Column(DateTime, doc="配股说明书签署日期")
    PUBLICATIONS = Column(String(200), doc="配股说明书发表刊物")
    PUBLICATIONS_EN = Column(String(400), doc="配股说明书发表刊物_英")
    WEBSITE = Column(String(200), doc="配股说明书发布网站")
    TRUSTEESHIPENDDATE = Column(DateTime, doc="停止托管日")
    TRUSTEESHIPTRANSFERDATE = Column(DateTime, doc="转托管日")
    LASTTRADINGDATE = Column(DateTime, doc="最后交易日")
    REGISTERDATE = Column(DateTime, doc="股权登记日")
    EXRIGHTDATE = Column(DateTime, doc="除权基准日")
    UNDERWRITEDSTARTDATE = Column(DateTime, doc="承销开始日")
    UNDERWRITEDENDDATE = Column(DateTime, doc="承销截止日")
    PAYMENTSTARTDATE = Column(DateTime, doc="配股缴款起始日")
    PAYMENTENDDATE = Column(DateTime, doc="配股缴款截止日")
    LISTEDDECLAREDATE = Column(DateTime, doc="上市公告书发表日期")
    LISTEDDATE = Column(DateTime, doc="配股上市流通日")
    OFFERINGTYPE = Column(String(20), doc="配售方式")
    PE = Column(DECIMAL(12, 6), doc="配股市盈率")
    EXRIGHTPRICE = Column(DECIMAL(10, 2), doc="除权价格")
    UNDERWRITEDMETHODSID = Column(String(12), doc="承销方式ID")
    UNDERWRITEDMETHODS = Column(String(12), doc="承销方式")
    TARGETINVESTORS = Column(String(400), doc="配售对象")
    TARGETINVESTORS_EN = Column(String(1000), doc="配售对象_英")
    PARVALUE = Column(DECIMAL(10, 2), doc="每股面值")
    CURRENCYCODE = Column(String(12), doc="货币编码")
    PRICE = Column(DECIMAL(10, 4), doc="配售价格")
    PLACINGRATIO = Column(DECIMAL(12, 6), doc="配股比例")
    EXPENSE = Column(DECIMAL(20, 2), doc="实际发行总费用")
    SUBSCRIPTIONNONCURRENCY = Column(DECIMAL(20, 2), doc="非货币资金认购金额")
    RAISEFUND = Column(DECIMAL(20, 2), doc="实际募集资金净额")
    FEEPERSHARE = Column(DECIMAL(10, 4), doc="每股发行费用")
    EPS = Column(DECIMAL(10, 4), doc="发行后每股收益")
    EQUITYPERSHARESBEFORE = Column(DECIMAL(10, 4), doc="发行前每股净资产")
    EQUITYPERSHARESAFTER = Column(DECIMAL(10, 4), doc="发行后每股净资产")
    INVESTPROJECT = Column(String(4000), doc="募集资金用途")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class stk_eq_rs_plan(Base):

    __tablename__ = 'stk_eq_rs_plan'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    DIRECTORATEDECISION = Column(String(1000), doc="董事会预案内容")
    SHAREHOLDERSDECISION = Column(String(600), doc="股东大会预案内容")
    DIRECTORATEALLOTMENTRATIO = Column(DECIMAL(10, 4), doc="配股比率董")
    SHAREHOLDERSALLOTMENTRATIO = Column(DECIMAL(10, 4), doc="配股比率股")
    PARVALUE = Column(DECIMAL(10, 4), doc="每股面值")
    REFERENCESHARES = Column(DECIMAL(20, 0), doc="配股基数")
    REFERENCEDATE = Column(DateTime, doc="配股基准日")
    PRICEMODEID = Column(String(40), doc="发行定价方式ID")
    PRICEMODE = Column(String(40), doc="发行定价方式")
    ALLOTMENTSHARES = Column(DECIMAL(20, 0), doc="预计配股数量")
    RAISENETFUND = Column(DECIMAL(20, 2), doc="预计募集资金净额")
    RAISEFUND = Column(DECIMAL(20, 2), doc="预计募集资金总额")
    PRICECEILING = Column(DECIMAL(10, 2), doc="预计配股价格上限")
    PRICEFLOOR = Column(DECIMAL(10, 2), doc="预计配股价格下限")
    DESCRIPTION = Column(String(600), doc="变更说明")
    PASSDATE = Column(DateTime, doc="获准日期")
    PROJECTACTUALIZEID = Column(String(20), doc="方案进度ID")
    PROJECTACTUALIZE = Column(String(20), doc="方案进度")
    DECLAREDATE2 = Column(DateTime, doc="配股说明书公告日期")
    COMMENTS = Column(String(600), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_eq_rs_result(Base):

    __tablename__ = 'stk_eq_rs_result'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    SHORTNAME1 = Column(String(40), doc="公众配售简称")
    SHORTNAME1_EN = Column(String(100), doc="公众配售简称_英")
    PLACINGCODE1 = Column(String(16), doc="公众配售代码")
    SHORTNAME2 = Column(String(40), doc="其他配售简称")
    SHORTNAME2_EN = Column(String(100), doc="其他配售简称_英")
    PLACINGCODE2 = Column(String(16), doc="其他配售代码")
    DECLAREDATE = Column(DateTime, doc="配股说明书公告日期")
    RIGHTOFFERINGDECLAREDATE = Column(DateTime, doc="配股发行结果公告日")
    AVAILABLESHARES = Column(DECIMAL(20, 0), doc="可配售总股份")
    PLACINGSHARES = Column(DECIMAL(20, 0), doc="实际配售总股份数")
    PLACINGSHARESLIMITED = Column(DECIMAL(20, 0), doc="限售股股东有效认购股份数")
    PLACINGSHARESUNLIMITED = Column(DECIMAL(20, 0), doc="无限售股股东有效认购股份数")
    UNDERWRITINGBALANCESHARES = Column(DECIMAL(20, 0), doc="承销余额")
    PLACINGSHARESMAJORHOLDERS = Column(DECIMAL(20, 0), doc="大股东认购数量")
    PURCHASESHARES = Column(DECIMAL(20, 2), doc="有效认购资金总额")
    SUBSCRIPTIONSTATESHARESID = Column(String(40), doc="国家股认购方式ID")
    SUBSCRIPTIONSTATESHARES = Column(String(40), doc="国家股认购方式")
    SUBSCRIPTIONSTATELEGALENTITYID = Column(String(40), doc="国有法人股认购方式ID")
    SUBSCRIPTIONSTATELEGALENTITY = Column(String(40), doc="国有法人股认购方式")
    SUBSCRIPTIONLEGALENTITYID = Column(String(40), doc="法人股认购方式ID")
    SUBSCRIPTIONLEGALENTITY = Column(String(40), doc="法人股认购方式")
    SUBSCRIPTIONMAJORHOLDERSID = Column(String(40), doc="大股东认购方式ID")
    SUBSCRIPTIONMAJORHOLDERS = Column(String(40), doc="大股东认购方式")
    SUCCESSFULSIGN = Column(String(2), doc="发行成功标志")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)
    ACTPLACINGRATIO = Column(DECIMAL(12, 6), doc="实际配股比例")


class stk_eq_seo_plan(Base):

    __tablename__ = 'stk_eq_seo_plan'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    NEWISSUETYPEID = Column(String(12), doc="增发类别ID")
    NEWISSUETYPE = Column(String(40), doc="增发类别")
    PARVALUE = Column(DECIMAL(10, 2), doc="每股面值")
    CURRENCYCODE = Column(String(12), doc="货币编码")
    ISSUESIZE = Column(DECIMAL(20, 0), doc="总发行规模")
    ISSUESHARESPRIVATE = Column(DECIMAL(20, 0), doc="定向募集股份数")
    ISSUESHARESPUBLIC = Column(DECIMAL(20, 0), doc="公开发行数量")
    OBJECT = Column(String(2000), doc="发行对象")
    PRICEMODEID = Column(String(40), doc="发行定价方式ID")
    PRICEMODE = Column(String(40), doc="发行定价方式")
    RAISEFUND = Column(DECIMAL(20, 2), doc="预计募集资金总额")
    RAISENETFUND = Column(DECIMAL(20, 2), doc="预计募集资金净额")
    PRICECEILING = Column(DECIMAL(10, 2), doc="预计增发价格上限")
    PRICEFLOOR = Column(DECIMAL(10, 2), doc="预计增发价格下限")
    REFORMATIONSIGN = Column(String(2), doc="是否涉及重大资产重组")
    PASSDATE = Column(DateTime, doc="获准日期")
    PROJECTACTUALIZEID = Column(String(20), doc="方案进度ID")
    PROJECTACTUALIZE = Column(String(20), doc="方案进度")
    COMMENTS = Column(String(600), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_eq_seo_private(Base):

    __tablename__ = 'stk_eq_seo_private'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    REGISTERDATE = Column(DateTime, doc="股权登记托管日")
    CHANGEDATE = Column(DateTime, doc="股份变动日")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    UNDERWRITEDMETHODSID = Column(String(12), doc="承销方式ID")
    UNDERWRITEDMETHODS = Column(String(20), doc="承销方式")
    CURRENCYCODE = Column(String(12), doc="货币编码")
    PRICE = Column(DECIMAL(8, 2), doc="发行价格")
    OBJECT = Column(String(4000), doc="发行对象")
    ISSUESHARES = Column(DECIMAL(20, 0), doc="实际发行总股数")
    RAISEFUND = Column(DECIMAL(20, 2), doc="实际募集资金总额")
    EXPENSE = Column(DECIMAL(20, 2), doc="实际发行总费用")
    FEEPERSHARE = Column(DECIMAL(10, 4), doc="每股发行费用")
    RAISENETFUND = Column(DECIMAL(20, 2), doc="实际募集资金净额")
    PE1 = Column(DECIMAL(10, 4), doc="加权发行市盈率")
    PE2 = Column(DECIMAL(10, 4), doc="摊薄发行市盈率")
    PB = Column(DECIMAL(10, 4), doc="摊薄发行市净率")
    EPS = Column(DECIMAL(10, 4), doc="发行后每股收益")
    EQUITYPERSHAREBEFORE = Column(DECIMAL(10, 4), doc="发行前每股净资产")
    EQUITYPERSHAREAFTER = Column(DECIMAL(10, 4), doc="发行后每股净资产")
    COMMENTS = Column(String(1000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_eq_seo_publicinfo(Base):

    __tablename__ = 'stk_eq_seo_publicinfo'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    DECLAREDATE = Column(DateTime, doc="招股意向书公告日期")
    SIGNDATE = Column(DateTime, doc="招股意向书签署日")
    ISSUEMODEID = Column(String(100), doc="发行方式ID")
    ISSUEMODE = Column(String(100), doc="发行方式")
    UNDERWRITEDMETHODSID = Column(String(12), doc="承销方式ID")
    UNDERWRITEDMETHODS = Column(String(12), doc="承销方式")
    ISEXRIGHT = Column(String(2), doc="是否除权")
    REGISTERDATE = Column(DateTime, doc="股权登记日")
    EXRIGHTDATE = Column(DateTime, doc="除权基准日")
    UNDERWRITEDSTARTDATE = Column(DateTime, doc="承销开始日")
    UNDERWRITEDENDDATE = Column(DateTime, doc="承销截止日")
    PUBLICATIONS1 = Column(String(200), doc="增发招股意向书发表刊物")
    PUBLICATIONS1_EN = Column(String(400), doc="增发招股意向书发表刊物_英")
    WEBSITE = Column(String(200), doc="增发招股意向书发布网站")
    PUBLICATIONS2 = Column(String(200), doc="增发上市公告发表刊物")
    PUBLICATIONS2_EN = Column(String(400), doc="增发上市公告发表刊物_英")
    SUSPENSIONRESUMPTIONDATE = Column(String(4000), doc="承销期间的停牌、复牌时间")
    ISSUESTARTDATE = Column(DateTime, doc="增发开始日")
    ISSUEENDDATE = Column(DateTime, doc="增发截止日")
    ONLINESTARTDATE = Column(DateTime, doc="网上申购开始日")
    ONLINEENDDATE = Column(DateTime, doc="网上申购截止日")
    INQUIRYPRICESTARTDATE = Column(DateTime, doc="网下询价配售开始日")
    INQUIRYPRICEENDDATE = Column(DateTime, doc="网下询价配售结束日")
    PLACEMENTSTARTDATE = Column(DateTime, doc="配售开始日")
    PLACEMENTENDDATE = Column(DateTime, doc="配售截止日")
    ROADSHOWSTARTDATE = Column(DateTime, doc="路演开始日期")
    ROADSHOWENDDATE = Column(DateTime, doc="路演截止日期")
    OTHERISSUEDATE = Column(DateTime, doc="其他发行日期")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    LISTEDDECLAREDATE = Column(DateTime, doc="上市公告书发表日期")
    PRICE = Column(DECIMAL(10, 2), doc="发行价格")
    CURRENCYCODE = Column(String(12), doc="货币编码")
    ISSUESHARES = Column(DECIMAL(20, 0), doc="实际增发总股数")
    ISSUESHARESPRIVATE = Column(DECIMAL(20, 0), doc="实际非公开发行总股数")
    ISSUESHARESPUBLIC = Column(DECIMAL(20, 0), doc="实际公开发行总股数")
    PE1 = Column(DECIMAL(10, 4), doc="加权发行市盈率")
    PE2 = Column(DECIMAL(10, 4), doc="摊薄发行市盈率")
    PB = Column(DECIMAL(10, 4), doc="发行市净率")
    EPS = Column(DECIMAL(10, 4), doc="发行后每股收益")
    EQUITYPERSHAREBEFORE = Column(DECIMAL(10, 4), doc="发行前每股净资产")
    EQUITYPERSHAREAFTER = Column(DECIMAL(10, 4), doc="发行后每股净资产")
    EXPENSE = Column(DECIMAL(20, 2), doc="实际发行总费用")
    EXPENSEPERSHARE = Column(DECIMAL(10, 4), doc="每股发行费用")
    RAISEFUND = Column(DECIMAL(20, 2), doc="实际募集资金总额")
    RAISENETFUND = Column(DECIMAL(20, 2), doc="实际募集资金净额")
    INVESTPROJECT = Column(String(4000), doc="募集资金用途")
    STAFFNUMBER = Column(INTEGER, doc="公司职工总人数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class stk_eq_seo_publicresult(Base):

    __tablename__ = 'stk_eq_seo_publicresult'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EVENTID = Column(String(40), doc="权益融资事件ID")
    SECURITYTYPEID = Column(String(12), doc="股票种类ID")
    SECURITYTYPE = Column(String(12), doc="股票种类")
    SEO1DECLAREDATE = Column(DateTime, doc="招股意向书公告日期")
    SEO2DECLAREDATE = Column(DateTime, doc="中签率公告日期")
    SUBSCRIPTIONCODE1 = Column(String(20), doc="申购代码1")
    SHORTNAME1 = Column(String(20), doc="申购简称1")
    SHORTNAME1_EN = Column(String(100), doc="申购简称1_英")
    SUBSCRIPTIONCODE2 = Column(String(20), doc="申购代码2")
    SHORTNAME2 = Column(String(20), doc="申购简称2")
    SHORTNAME2_EN = Column(String(100), doc="申购简称2_英")
    SHARESUNLIMITED = Column(DECIMAL(20, 0), doc="无流通限制及锁定安排的股份数")
    SHARESOLDER = Column(DECIMAL(20, 0), doc="原股东优先配售数量")
    SHARESOLDERTOISSUE = Column(DECIMAL(10, 4), doc="原股东配售占总发行量的比例")
    PURCHASESHARESOLDER = Column(DECIMAL(20, 0), doc="原股东有效申购股数")
    PURCHASEHOUSEHOLDERSOLDER = Column(BIGINT, doc="原股东有效申购户数")
    PLACINGOLDER = Column(DECIMAL(12, 6), doc="原股东配售比例")
    ONLINEISSUE = Column(DECIMAL(20, 0), doc="网上发行数量")
    ONLINEISSUETOTOTALISSUE = Column(DECIMAL(10, 4), doc="网上发行占发行总量的比例")
    ONLINEPURCHASEHOUSEHOLDERS = Column(BIGINT, doc="网上有效申购户数")
    ONLINEPURCHASESHARES = Column(DECIMAL(20, 0), doc="网上有效申购股数")
    ONLINESUCCESSRATE = Column(DECIMAL(12, 6), doc="网上发行中签率")
    ONLINEOVERSUBSCRIPTIONRATIO = Column(DECIMAL(10, 4), doc="网上超额认购倍数")
    OFFLINEISSUE = Column(DECIMAL(20, 0), doc="网下配售数量")
    OFFLINEISSUETOTOTALISSUE = Column(DECIMAL(10, 4), doc="网下配售占发行总量的比例")
    OFFLINEPURCHASEHOUSEHOLDERS = Column(BIGINT, doc="网下有效申购户数")
    OFFLINEPURCHASESHARES = Column(DECIMAL(20, 0), doc="网下有效申购股数")
    OFFLINESUCCESSRATE = Column(DECIMAL(12, 6), doc="网下配售比例")
    OFFLINEOVERSUBSCRIPTIONRATIO = Column(DECIMAL(10, 4), doc="网下配售超额认购倍数")
    UNDERWRITINGBALANCESHARES = Column(DECIMAL(20, 0), doc="承销余额")
    CALLBACKSIGN = Column(String(2), doc="回拨机制适用性")
    CALLBACKTYPEID = Column(String(100), doc="回拨方式ID")
    CALLBACKTYPE = Column(String(200), doc="回拨方式")
    CALLBACKSHARES = Column(DECIMAL(20, 0), doc="回拨数量")
    PURCHASESHARES = Column(DECIMAL(20, 0), doc="总有效申购股数")
    PURCHASEHOUSEHOLDERS = Column(BIGINT, doc="总有效申购户数")
    OVERSUBSCRIPTIONRATIO = Column(DECIMAL(10, 4), doc="总超额认购倍数")
    SUCCESSRATE = Column(DECIMAL(12, 6), doc="总中签率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATETIME_EN = Column(DateTime)


class stk_eventlist(Base):

    __tablename__ = 'stk_eventlist'

    SYMBOL = Column(String(20), doc="证券代码")
    EVENTTYPECODE = Column(String(12), doc="事件类型编码")
    EVENTTYPE = Column(String(100), doc="事件类型")
    SCHEDULECODE = Column(String(12), doc="方案进度编码")
    SCHEDULE = Column(String(100), doc="方案进度")
    SCHEDULEDATE = Column(DateTime, doc="进度日期")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_balance(Base):

    __tablename__ = 'stk_fin_balance'

    INSTITUTIONID = Column(DECIMAL(20, 0))
    ENDDATE = Column(DateTime)
    STATETYPECODE = Column(String(12))
    SYMBOL = Column(String(12))
    INDUSTRYMARK = Column(BIGINT)
    EVENTID = Column(String(40))
    A001101 = Column(DECIMAL(20, 2))
    A0D110110 = Column(DECIMAL(20, 2))
    A0B1103 = Column(DECIMAL(20, 2))
    A0D1102 = Column(DECIMAL(20, 2))
    A0D110210 = Column(DECIMAL(20, 2))
    A0B1105 = Column(DECIMAL(20, 2))
    A0B1104 = Column(DECIMAL(20, 2))
    A0F1106 = Column(DECIMAL(20, 2))
    A001107 = Column(DECIMAL(20, 2))
    A0F1108 = Column(DECIMAL(20, 2))
    A001109 = Column(DECIMAL(20, 2))
    A0F1122 = Column(DECIMAL(20, 2))
    A001110 = Column(DECIMAL(20, 2))
    A001111 = Column(DECIMAL(20, 2))
    A001112 = Column(DECIMAL(20, 2))
    A001121 = Column(DECIMAL(20, 2))
    A001119 = Column(DECIMAL(20, 2))
    A001120 = Column(DECIMAL(20, 2))
    A0I1113 = Column(DECIMAL(20, 2))
    A0I1114 = Column(DECIMAL(20, 2))
    A0I1115 = Column(DECIMAL(20, 2))
    A0I1116 = Column(DECIMAL(20, 2))
    A0I111610 = Column(DECIMAL(20, 2))
    A0I111620 = Column(DECIMAL(20, 2))
    A0I111630 = Column(DECIMAL(20, 2))
    A0I111640 = Column(DECIMAL(20, 2))
    A001123 = Column(DECIMAL(20, 2))
    A001124 = Column(DECIMAL(20, 2))
    A001125 = Column(DECIMAL(20, 2))
    A0011 = Column(DECIMAL(20, 2))
    A0B1201 = Column(DECIMAL(20, 2))
    A0I1224 = Column(DECIMAL(20, 2))
    A0D1126 = Column(DECIMAL(20, 2))
    A0I1225 = Column(DECIMAL(20, 2))
    A001202 = Column(DECIMAL(20, 2))
    A001203 = Column(DECIMAL(20, 2))
    A001206 = Column(DECIMAL(20, 2))
    A001207 = Column(DECIMAL(20, 2))
    A001204 = Column(DECIMAL(20, 2))
    A001205 = Column(DECIMAL(20, 2))
    A0I1209 = Column(DECIMAL(20, 2))
    A001211 = Column(DECIMAL(20, 2))
    A001212 = Column(DECIMAL(20, 2))
    A001213 = Column(DECIMAL(20, 2))
    A001214 = Column(DECIMAL(20, 2))
    A001215 = Column(DECIMAL(20, 2))
    A001216 = Column(DECIMAL(20, 2))
    A001217 = Column(DECIMAL(20, 2))
    A001218 = Column(DECIMAL(20, 2))
    A0D121810 = Column(DECIMAL(20, 2))
    A001219 = Column(DECIMAL(20, 2))
    A001220 = Column(DECIMAL(20, 2))
    A001221 = Column(DECIMAL(20, 2))
    A0I1210 = Column(DECIMAL(20, 2))
    A0F1224 = Column(DECIMAL(20, 2))
    A001222 = Column(DECIMAL(20, 2))
    A001223 = Column(DECIMAL(20, 2))
    A0012 = Column(DECIMAL(20, 2))
    A0F13 = Column(DECIMAL(20, 2))
    A001 = Column(DECIMAL(20, 2))
    A0B2102 = Column(DECIMAL(20, 2))
    A0F2104 = Column(DECIMAL(20, 2))
    A0B2103 = Column(DECIMAL(20, 2))
    A0B210310 = Column(DECIMAL(20, 2))
    A0B210320 = Column(DECIMAL(20, 2))
    A002101 = Column(DECIMAL(20, 2))
    A0D210110 = Column(DECIMAL(20, 2))
    A002105 = Column(DECIMAL(20, 2))
    A0F2106 = Column(DECIMAL(20, 2))
    A0F2110 = Column(DECIMAL(20, 2))
    A0D2122 = Column(DECIMAL(20, 2))
    A0D2123 = Column(DECIMAL(20, 2))
    A002107 = Column(DECIMAL(20, 2))
    A002108 = Column(DECIMAL(20, 2))
    A002109 = Column(DECIMAL(20, 2))
    A0I2124 = Column(DECIMAL(20, 2))
    A0I2111 = Column(DECIMAL(20, 2))
    A0I2121 = Column(DECIMAL(20, 2))
    A002112 = Column(DECIMAL(20, 2))
    A002113 = Column(DECIMAL(20, 2))
    A002114 = Column(DECIMAL(20, 2))
    A002115 = Column(DECIMAL(20, 2))
    A0I2116 = Column(DECIMAL(20, 2))
    A0I2117 = Column(DECIMAL(20, 2))
    A0I2118 = Column(DECIMAL(20, 2))
    A0I2119 = Column(DECIMAL(20, 2))
    A0I211910 = Column(DECIMAL(20, 2))
    A0I211920 = Column(DECIMAL(20, 2))
    A0I211930 = Column(DECIMAL(20, 2))
    A0I211940 = Column(DECIMAL(20, 2))
    A002120 = Column(DECIMAL(20, 2))
    A002125 = Column(DECIMAL(20, 2))
    A002126 = Column(DECIMAL(20, 2))
    A0021 = Column(DECIMAL(20, 2))
    A002201 = Column(DECIMAL(20, 2))
    A002203 = Column(DECIMAL(20, 2))
    A002204 = Column(DECIMAL(20, 2))
    A002205 = Column(DECIMAL(20, 2))
    A002206 = Column(DECIMAL(20, 2))
    A002207 = Column(DECIMAL(20, 2))
    A0D2202 = Column(DECIMAL(20, 2))
    A0F2210 = Column(DECIMAL(20, 2))
    A002208 = Column(DECIMAL(20, 2))
    A002209 = Column(DECIMAL(20, 2))
    A0022 = Column(DECIMAL(20, 2))
    A0F23 = Column(DECIMAL(20, 2))
    A002 = Column(DECIMAL(20, 2))
    A003101 = Column(DECIMAL(20, 2))
    A003102 = Column(DECIMAL(20, 2))
    A003110 = Column(DECIMAL(20, 2))
    A003103 = Column(DECIMAL(20, 2))
    A003105 = Column(DECIMAL(20, 2))
    A003106 = Column(DECIMAL(20, 2))
    A003107 = Column(DECIMAL(20, 2))
    A0F3104 = Column(DECIMAL(20, 2))
    A0F3108 = Column(DECIMAL(20, 2))
    A003109 = Column(DECIMAL(20, 2))
    A0031 = Column(DECIMAL(20, 2))
    A0032 = Column(DECIMAL(20, 2))
    A003 = Column(DECIMAL(20, 2))
    A004 = Column(DECIMAL(20, 2))
    UPDATEID = Column(BIGINT, primary_key=True)
    REPORTTYPEID = Column(SMALLINT)
    A002127 = Column(DECIMAL(20, 2), doc="递延收益-流动负债")
    A002210 = Column(DECIMAL(20, 2), doc="递延收益-非流动负债")
    A003112 = Column(DECIMAL(20, 2), doc="其他权益工具")
    A00311210 = Column(DECIMAL(20, 2), doc="其中：优先股")
    A00311220 = Column(DECIMAL(20, 2), doc="其中：永续债")
    A00311230 = Column(DECIMAL(20, 2), doc="其中：其他")
    A003111 = Column(DECIMAL(20, 2), doc="其他综合收益")
    A001127 = Column(DECIMAL(20, 2), doc="应收款项融资")
    A001128 = Column(DECIMAL(20, 2), doc="合同资产")
    A001226 = Column(DECIMAL(20, 2), doc="债权投资")
    A001227 = Column(DECIMAL(20, 2), doc="其他债权投资")
    A001228 = Column(DECIMAL(20, 2), doc="其他权益工具投资")
    A001229 = Column(DECIMAL(20, 2), doc="其他非流动金融资产")
    A002128 = Column(DECIMAL(20, 2), doc="合同负债")


class stk_fin_cashflow(Base):

    __tablename__ = 'stk_fin_cashflow'

    INSTITUTIONID = Column(DECIMAL(20, 0))
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    STATETYPECODE = Column(String(12))
    SYMBOL = Column(String(12))
    INDUSTRYMARK = Column(BIGINT)
    EVENTID = Column(String(40))
    C001001 = Column(DECIMAL(20, 2))
    C0B1002 = Column(DECIMAL(20, 2))
    C0F1023 = Column(DECIMAL(20, 2))
    C0B1003 = Column(DECIMAL(20, 2))
    C0B1004 = Column(DECIMAL(20, 2))
    C0I1005 = Column(DECIMAL(20, 2))
    C0I1006 = Column(DECIMAL(20, 2))
    C0I1007 = Column(DECIMAL(20, 2))
    C0D1008 = Column(DECIMAL(20, 2))
    C0D1010 = Column(DECIMAL(20, 2))
    C0D1011 = Column(DECIMAL(20, 2))
    C0F1024 = Column(DECIMAL(20, 2))
    C0F1025 = Column(DECIMAL(20, 2))
    C0F1009 = Column(DECIMAL(20, 2))
    C001012 = Column(DECIMAL(20, 2))
    C001013 = Column(DECIMAL(20, 2))
    C0011 = Column(DECIMAL(20, 2))
    C001014 = Column(DECIMAL(20, 2))
    C0B1015 = Column(DECIMAL(20, 2))
    C0F1026 = Column(DECIMAL(20, 2))
    C0B1016 = Column(DECIMAL(20, 2))
    C0I1017 = Column(DECIMAL(20, 2))
    C0F1027 = Column(DECIMAL(20, 2))
    C0F1028 = Column(DECIMAL(20, 2))
    C0F1029 = Column(DECIMAL(20, 2))
    C0F1030 = Column(DECIMAL(20, 2))
    C0F1031 = Column(DECIMAL(20, 2))
    C0F1032 = Column(DECIMAL(20, 2))
    C0F1018 = Column(DECIMAL(20, 2))
    C0I1019 = Column(DECIMAL(20, 2))
    C001020 = Column(DECIMAL(20, 2))
    C001021 = Column(DECIMAL(20, 2))
    C001022 = Column(DECIMAL(20, 2))
    C0012 = Column(DECIMAL(20, 2))
    C001 = Column(DECIMAL(20, 2))
    C002001 = Column(DECIMAL(20, 2))
    C002002 = Column(DECIMAL(20, 2))
    C002004 = Column(DECIMAL(20, 2))
    C002003 = Column(DECIMAL(20, 2))
    C002005 = Column(DECIMAL(20, 2))
    C0021 = Column(DECIMAL(20, 2))
    C002007 = Column(DECIMAL(20, 2))
    C0I2008 = Column(DECIMAL(20, 2))
    C002009 = Column(DECIMAL(20, 2))
    C002006 = Column(DECIMAL(20, 2))
    C002010 = Column(DECIMAL(20, 2))
    C0022 = Column(DECIMAL(20, 2))
    C002 = Column(DECIMAL(20, 2))
    C003008 = Column(DECIMAL(20, 2), doc="发行证券收到的现金")
    C00300810 = Column(DECIMAL(20, 2), doc="吸收投资收到的现金")
    C0030081010 = Column(DECIMAL(20, 2))
    C003002 = Column(DECIMAL(20, 2))
    C00300820 = Column(DECIMAL(20, 2))
    C003004 = Column(DECIMAL(20, 2))
    C0031 = Column(DECIMAL(20, 2))
    C003005 = Column(DECIMAL(20, 2))
    C003006 = Column(DECIMAL(20, 2))
    C00300610 = Column(DECIMAL(20, 2))
    C003007 = Column(DECIMAL(20, 2))
    C0032 = Column(DECIMAL(20, 2))
    C003 = Column(DECIMAL(20, 2))
    C004 = Column(DECIMAL(20, 2))
    C007 = Column(DECIMAL(20, 2))
    C005 = Column(DECIMAL(20, 2))
    C008 = Column(DECIMAL(20, 2))
    C006 = Column(DECIMAL(20, 2))
    UPDATEID = Column(BIGINT, primary_key=True)
    REPORTTYPEID = Column(SMALLINT)


class stk_fin_cashflowindex(Base):

    __tablename__ = 'stk_fin_cashflowindex'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    NCFTONETPROFIT = Column(DECIMAL(20, 6), doc="净利润现金净含量")
    NCFTONETPROFITTTM = Column(DECIMAL(20, 6), doc="净利润现金净含量TTM")
    OPERATINGINCOMEINCASHRATIOA = Column(DECIMAL(20, 6), doc="营收入现金含量")
    OPERATINGINCOMEINCASHRATIOTTMA = Column(DECIMAL(20, 6), doc="营收入现金含量TTM")
    OPERATINGINCOMEINCASHRATIOB = Column(DECIMAL(20, 6), doc="营业收入现金净含量")
    OPERATINGINCOMEINCASHRATIOTTMB = Column(DECIMAL(20, 6), doc="营业收入现金净含量TTM")
    NCFTOOPERATINGPROFIT = Column(DECIMAL(20, 6), doc="营业利润现金净含量")
    NCFTOOPERATINGPROFITTTM = Column(DECIMAL(20, 6), doc="营业利润现金净含量TTM")
    NCFTOTOTALPROFIT = Column(DECIMAL(20, 6), doc="现金与利润总额比")
    OPERATINGCASHINFLOW = Column(DECIMAL(20, 6), doc="经营活动现金流入")
    OPERATINGCASHINFLOWTTM = Column(DECIMAL(20, 6), doc="经营活动现金流入TTM")
    OPERATINGINCOMEINCASH = Column(DECIMAL(20, 6), doc="销售商品提供劳务等收到的现金")
    OPERATINGINCOMEINCASHTTM = Column(DECIMAL(20, 6), doc="销售商品提供劳务等收到的现金TTM")
    OPERATINGCASHOUTFLOW = Column(DECIMAL(20, 6), doc="经营活动现金流出")
    OPERATINGCASHOUTFLOWTTM = Column(DECIMAL(20, 6), doc="经营活动现金流出TTM")
    PURCHASEINCASH = Column(DECIMAL(20, 6), doc="购买商品接受劳务支付的现金")
    PURCHASEINCASHTTM = Column(DECIMAL(20, 6), doc="购买商品接受劳务支付的现金TTM")
    WAGEINCASH = Column(DECIMAL(20, 6), doc="支付给职工以及为职工支付的现金")
    WAGEINCASHTTM = Column(DECIMAL(20, 6), doc="支付给职工以及为职工支付的现金TTM")
    OPERATINGNCF = Column(DECIMAL(20, 6), doc="经营活动现金净流量")
    OPERATINGNCFTTM = Column(DECIMAL(20, 6), doc="经营活动现金净流量TTM")
    INVESTINGNCF = Column(DECIMAL(20, 6), doc="投资活动现金净流量")
    INVESTINGNCFTTM = Column(DECIMAL(20, 6), doc="投资活动现金净流量TTM")
    FINANCINGNCF = Column(DECIMAL(20, 6), doc="筹资活动现金净流量")
    FINANCINGTTM = Column(DECIMAL(20, 6), doc="筹资活动现金净流量TTM")
    DEBTEEFINANCINGNCF = Column(DECIMAL(20, 6), doc="筹资活动债权人现金净流量")
    DEBTEEFINANCINGNCFTTM = Column(DECIMAL(20, 6), doc="筹资活动债权人现金净流量TTM")
    SHAREHOLDERFINANCINGNCF = Column(DECIMAL(20, 6), doc="筹资活动股东现金净流量")
    SHAREHOLDERFINANCINGNCFTTM = Column(DECIMAL(20, 6), doc="筹资活动股东现金净流量TTM")
    CASHINCREASE = Column(DECIMAL(20, 6), doc="现金及等价物净增加额")
    CASHINCREASETTM = Column(DECIMAL(20, 6), doc="现金及等价物净增加额TTM")
    DA = Column(DECIMAL(20, 6), doc="折旧摊销")
    DATTM = Column(DECIMAL(20, 6), doc="折旧摊销TTM")
    COMPANYCFA = Column(DECIMAL(20, 6), doc="公司现金流1")
    COMPANYCFB = Column(DECIMAL(20, 6), doc="公司现金流2")
    COMPANYCFTTMA = Column(DECIMAL(20, 6), doc="公司现金流TTM1")
    COMPANYCFTTMB = Column(DECIMAL(20, 6), doc="公司现金流TTM2")
    EQUITYCFA = Column(DECIMAL(20, 6), doc="股权现金流1")
    EQUITYCFB = Column(DECIMAL(20, 6), doc="股权现金流2")
    EQUITYCFTTMA = Column(DECIMAL(20, 6), doc="股权现金流TTM1")
    EQUITYCFTTMB = Column(DECIMAL(20, 6), doc="股权现金流TTM2")
    COMPANYCF = Column(DECIMAL(20, 6), doc="公司自由现金流（原有）")
    EQUITYCF = Column(DECIMAL(20, 6), doc="股权自由现金流（原有）")
    CASHRECOVERYRATIO = Column(DECIMAL(20, 6), doc="全部现金回收率")
    OPERATINGNCFTOPROFITRATIO = Column(DECIMAL(20, 6), doc="营运指数")
    LONGTERMINVESTCFTODA = Column(DECIMAL(20, 6), doc="资本支出与折旧摊销比")
    OPERATINGNCFTOMAINCASHNEEDEDA = Column(DECIMAL(20, 6), doc="现金适合比率")
    CASHREINVESTMENTRATIO = Column(DECIMAL(20, 6), doc="现金再投资比率")
    OPERATINGNCFTOMAINCASHNEEDEDB = Column(DECIMAL(20, 6), doc="现金满足投资比率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_cashflowindrect(Base):

    __tablename__ = 'stk_fin_cashflowindrect'

    INSTITUTIONID = Column(DECIMAL(20, 0))
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    STATETYPECODE = Column(String(12))
    SYMBOL = Column(String(12))
    INDUSTRYMARK = Column(BIGINT)
    EVENTID = Column(String(40))
    D000101 = Column(DECIMAL(20, 2))
    D000117 = Column(DECIMAL(20, 2))
    D000102 = Column(DECIMAL(20, 2))
    D000103 = Column(DECIMAL(20, 2))
    D000104 = Column(DECIMAL(20, 2))
    D000105 = Column(DECIMAL(20, 2))
    D000106 = Column(DECIMAL(20, 2))
    D000107 = Column(DECIMAL(20, 2))
    D000108 = Column(DECIMAL(20, 2))
    D000109 = Column(DECIMAL(20, 2))
    D000110 = Column(DECIMAL(20, 2))
    D000111 = Column(DECIMAL(20, 2))
    D000112 = Column(DECIMAL(20, 2))
    D000113 = Column(DECIMAL(20, 2))
    D000114 = Column(DECIMAL(20, 2))
    D000115 = Column(DECIMAL(20, 2))
    D000116 = Column(DECIMAL(20, 2))
    D0001 = Column(DECIMAL(20, 2))
    D000201 = Column(DECIMAL(20, 2))
    D000202 = Column(DECIMAL(20, 2))
    D000203 = Column(DECIMAL(20, 2))
    D000204 = Column(DECIMAL(20, 2))
    D000205 = Column(DECIMAL(20, 2))
    D000206 = Column(DECIMAL(20, 2))
    D000207 = Column(DECIMAL(20, 2))
    D0002 = Column(DECIMAL(20, 2))
    UPDATEID = Column(BIGINT, primary_key=True)
    REPORTTYPEID = Column(SMALLINT)
    D000118 = Column(DECIMAL(20, 2), doc="信用减值损失")


class stk_fin_cashflowindrectttm(Base):

    __tablename__ = 'stk_fin_cashflowindrectttm'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    SYMBOL = Column(String(12), doc="股票代码")
    INDUSTRYMARK = Column(BIGINT, doc="行业标识")
    NETPROFIT = Column(DECIMAL(20, 2), doc="净利润")
    UNRECOGNIZEDINVESTMENTLOSSES = Column(DECIMAL(20, 2), doc="未确认的投资损失")
    IMPAIRMENTOFASSETS = Column(DECIMAL(20, 2), doc="资产减值准备")
    DEPRECIATION = Column(DECIMAL(20, 2), doc="固定资产折旧、油气资产折耗、生产性生物资产折旧")
    AMORTIZATIONOFINTANGIBLEASSETS = Column(DECIMAL(20, 2), doc="无形资产摊销")
    AMORTIZATIONOFDEFERREDEXPENSES = Column(DECIMAL(20, 2), doc="长期待摊费用摊销")
    DISPOSALOFLONGTERMASSETS = Column(DECIMAL(20, 2), doc="处置固定资产、无形资产和其他长期资产的损失(收益以“－”号填列）")
    DISPOSALOFFIXEDASSETS = Column(DECIMAL(20, 2), doc="固定资产报废损失(收益以“－”号填列）")
    FAIRVALUECHANGE = Column(DECIMAL(20, 2), doc="公允价值变动损失(收益以“－”号填列）")
    FINANCEEXPENSE = Column(DECIMAL(20, 2), doc="财务费用(收益以“－”号填列）")
    INVESTINGLOSS = Column(DECIMAL(20, 2), doc="投资损失(收益以“－”号填列）")
    DEFERREDTAXASSETCHANGE = Column(DECIMAL(20, 2), doc="递延所得税资产减少（增加以“－”号填列）")
    DEFERREDTAXLIABILITYCHANGE = Column(DECIMAL(20, 2), doc="递延所得税负债增加（减少以“－”号填列）")
    INVENTORYCHANGE = Column(DECIMAL(20, 2), doc="存货的减少（增加以“－”号填列）")
    RECEIVABLECHANGE = Column(DECIMAL(20, 2), doc="经营性应收项目的减少（增加以“－”号填列）")
    PAYABLECHANGE = Column(DECIMAL(20, 2), doc="经营性应付项目的增加（减少以“－”号填列）")
    OTHER = Column(DECIMAL(20, 2), doc="其他")
    OPERATINGNETCASHFLOW = Column(DECIMAL(20, 2), doc="经营活动产生的现金流量净额")
    CONVERSIONOFDEBTTOCAPITAL = Column(DECIMAL(20, 2), doc="债务转为资本")
    CONVERTIBLEBONDINONEYEAR = Column(DECIMAL(20, 2), doc="一年内到期的可转换公司债券")
    FINANCELEASE = Column(DECIMAL(20, 2), doc="融资租赁固定资产")
    ENDCASH = Column(DECIMAL(20, 2), doc="现金的期末余额")
    BEGINCASH = Column(DECIMAL(20, 2), doc="现金的期初余额")
    ENDCASHEQUIVALENT = Column(DECIMAL(20, 2), doc="现金等价物的期末余额")
    BEGINCASHEQUIVALENT = Column(DECIMAL(20, 2), doc="现金等价物的期初余额")
    CASHEQUIVALENTCHANGE = Column(DECIMAL(20, 2), doc="现金及现金等价物净增加额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_cashflowttm(Base):

    __tablename__ = 'stk_fin_cashflowttm'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    SYMBOL = Column(String(12), doc="股票代码")
    INDUSTRYMARK = Column(BIGINT, doc="行业标识")
    SELLINGCASHINFLOW = Column(DECIMAL(20, 2), doc="销售商品、提供劳务收到的现金")
    CUSTOMERDEPOSITINCREASE = Column(DECIMAL(20, 2), doc="客户存款和同业存放款项净增加额")
    DEPOSITEINCENTRALBANKREDUCE = Column(DECIMAL(20, 2), doc="存放央行和同业款项净减少额")
    BORROWFROMCENTRALBANKINCREASE = Column(DECIMAL(20, 2), doc="向中央银行借款净增加额")
    BORROWFROMOTHERINCREASE = Column(DECIMAL(20, 2), doc="向其他金融机构拆入资金净增加额")
    PREMIUMSRECEIVED = Column(DECIMAL(20, 2), doc="收到原保险合同保费取得的现金")
    REINSURANCEBUSINESSCASHINFLOW = Column(DECIMAL(20, 2), doc="收到再保险业务现金净额")
    POLICYHOLDERSDEPOSITINCREASE = Column(DECIMAL(20, 2), doc="保户储金及投资款净增加额")
    DISPOSALOFTRADINGFINANCIAL = Column(DECIMAL(20, 2), doc="处置交易性金融资产净增加额")
    LOANSFROMOTHERBANKSINCREASE = Column(DECIMAL(20, 2), doc="拆入资金净增加额")
    REPURCHASEBUSINESSINCREASE = Column(DECIMAL(20, 2), doc="回购业务资金净增加额")
    INTERBANKLOANSREDUCTION = Column(DECIMAL(20, 2), doc="拆出资金净减少额")
    BUYINGBACKTHESALEREDUCTION = Column(DECIMAL(20, 2), doc="买入返售款项净减少额")
    INTERESTFEERECEIVED = Column(DECIMAL(20, 2), doc="收取利息、手续费及佣金的现金")
    TAXREFUNDRECEIVED = Column(DECIMAL(20, 2), doc="收到的税费返还")
    OTHEROPERATINGCASHINFLOW = Column(DECIMAL(20, 2), doc="收到的其他与经营活动有关的现金")
    OPERATINGCASHINFLOW = Column(DECIMAL(20, 2), doc="经营活动现金流入小计")
    PAIDFORCOMMODITYOUTFLOW = Column(DECIMAL(20, 2), doc="购买商品、接受劳务支付的现金")
    LOANTOCUSTOMERINCREASE = Column(DECIMAL(20, 2), doc="客户贷款及垫款净增加额")
    BORROWFROMCENTRALBANKREDUCTION = Column(DECIMAL(20, 2), doc="向中央银行借款净减少额")
    DEPOSITEINCENTRALBANKINCREASE = Column(DECIMAL(20, 2), doc="存放中央银行和同业款项净增加额")
    CLAIMSPAID = Column(DECIMAL(20, 2), doc="支付原保险合同赔付款项的现金")
    REINSURANCEBUSINESSPAID = Column(DECIMAL(20, 2), doc="支付再保业务现金净额")
    POLICYHOLDERDEPOSITREDUCTION = Column(DECIMAL(20, 2), doc="保户储金及投资款净减少额")
    INTERBANKLOANSINCREASE = Column(DECIMAL(20, 2), doc="拆出资金净增加额")
    BUYINGBACKTHESALEINCREASE = Column(DECIMAL(20, 2), doc="买入返售款项净增加额")
    LOANSFROMOTHERBANKSREDUCTION = Column(DECIMAL(20, 2), doc="拆入资金净减少额")
    SOLDFORREPURCHASEREDUCTION = Column(DECIMAL(20, 2), doc="卖出回购款项净减少额")
    INTERESTFEEPAID = Column(DECIMAL(20, 2), doc="支付利息、手续费及佣金的现金")
    POLICYHOLDERDIVIDENDPAID = Column(DECIMAL(20, 2), doc="支付保单红利的现金")
    PAIDTOEMPLOYEE = Column(DECIMAL(20, 2), doc="支付给职工以及为职工支付的现金")
    TAXEANDFEEPAID = Column(DECIMAL(20, 2), doc="支付的各项税费")
    OTHEROPERATINGCASHOUTFLOW = Column(DECIMAL(20, 2), doc="支付其他与经营活动有关的现金")
    OPERATINGCASHOUTFLOW = Column(DECIMAL(20, 2), doc="经营活动现金流出小计")
    OPERATINGNETCASHFLOW = Column(DECIMAL(20, 2), doc="经营活动产生的现金流量净额")
    INVESTMENTWITHDRAWAL = Column(DECIMAL(20, 2), doc="收回投资收到的现金")
    INVESTMENTINCOME = Column(DECIMAL(20, 2), doc="取得投资收益收到的现金")
    DISPOSALOFSUBSIDIARIES = Column(DECIMAL(20, 2), doc="处置子公司及其他营业单位收到的现金净额")
    DISPOSALOFLONGTERMASSETS = Column(DECIMAL(20, 2), doc="处置固定资产、无形资产和其他长期资产收回的现金净额")
    OTHERINVESTCASHINFLOW = Column(DECIMAL(20, 2), doc="收到的其他与投资活动有关的现金")
    INVESTINGCASHINFLOW = Column(DECIMAL(20, 2), doc="投资活动产生的现金流入小计")
    PAIDFORINVESTMENTS = Column(DECIMAL(20, 2), doc="投资支付的现金")
    PLEDGEDLOANSINCREASE = Column(DECIMAL(20, 2), doc="质押贷款净增加额")
    PAIDFORSUBSIDIARIES = Column(DECIMAL(20, 2), doc="取得子公司及其他营业单位支付的现金净额")
    PAIDFORLONGTERMASSETS = Column(DECIMAL(20, 2), doc="购建固定资产、无形资产和其他长期资产支付的现金")
    OTHERINVESTINGCASHOUTFLOW = Column(DECIMAL(20, 2), doc="支付其他与投资活动有关的现金")
    INVESTINGCASHOUTFLOW = Column(DECIMAL(20, 2), doc="投资活动产生的现金流出小计")
    INVESTINGNETCASHFLOW = Column(DECIMAL(20, 2), doc="投资活动产生的现金流量净额")
    CASHFROMINVESTMENT = Column(DECIMAL(20, 2), doc="发行证券收到的现金")
    CASHFROMEQUITY = Column(DECIMAL(20, 2), doc="吸收投资收到的现金")
    CASHINFLOWFROMMINORITY = Column(DECIMAL(20, 2), doc="其中：子公司吸收少数股东投资收到的现金")
    CASHINFLOWFROMBORROWING = Column(DECIMAL(20, 2), doc="取得借款收到的现金")
    CASHINFLOWFROMISSUINGBOND = Column(DECIMAL(20, 2), doc="发行债券收到的现金")
    CASHINFLOWFROMOTHERFIANCING = Column(DECIMAL(20, 2), doc="收到其他与筹资活动有关的现金")
    CASHINFLOWFROMFIANCING = Column(DECIMAL(20, 2), doc="筹资活动现金流入小计")
    REPAYMENTOFDEBT = Column(DECIMAL(20, 2), doc="偿还债务支付的现金")
    DIVIDENDINTERESTPAID = Column(DECIMAL(20, 2), doc="分配股利、利润或偿付利息支付的现金")
    DIVIDENDTOMINORITY = Column(DECIMAL(20, 2), doc="其中：子公司支付给少数股东的股利、利润")
    OTHERFINACINGCASHOUTFLOW = Column(DECIMAL(20, 2), doc="支付其他与筹资活动有关的现金")
    FINACINGCASHOUTFLOW = Column(DECIMAL(20, 2), doc="筹资活动现金流出小计")
    FINACINGNETCASHFLOW = Column(DECIMAL(20, 2), doc="筹资活动产生的现金流量净额")
    EXCHANGERATE = Column(DECIMAL(20, 2), doc="汇率变动对现金及现金等价物的影响")
    OTHEREFFECT = Column(DECIMAL(20, 2), doc="其他对现金的影响")
    CASHEQUIVALENTCHANGE = Column(DECIMAL(20, 2), doc="现金及现金等价物净增加额")
    BEGINCASHEQUIVALENT = Column(DECIMAL(20, 2), doc="期初现金及现金等价物余额")
    ENDCASHEQUIVALENT = Column(DECIMAL(20, 2), doc="期末现金及现金等价物余额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_construct(Base):

    __tablename__ = 'stk_fin_construct'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    CURRENTASSETRATIO = Column(DECIMAL(20, 6), doc="流动资产比率")
    CASHRATIO = Column(DECIMAL(20, 6), doc="现金资产比率")
    RECEIVABLERATIO = Column(DECIMAL(20, 6), doc="应收类资产比率")
    WORKINGCAPITALTOCURRENT = Column(DECIMAL(20, 6), doc="营运资金对流动资产比率")
    WORKINGCAPITALRATIO = Column(DECIMAL(20, 6), doc="营运资金比率")
    WORKINGCAPITALTOEQUITY = Column(DECIMAL(20, 6), doc="营运资金对净资产比率")
    NONCURRENTASSETRATIO = Column(DECIMAL(20, 6), doc="非流动资产比率")
    FIXEDASSETRATIO = Column(DECIMAL(20, 6), doc="固定资产比率")
    INTANGIBLEASSETRATIO = Column(DECIMAL(20, 6), doc="无形资产比率")
    TANGIBLEASSETRATIO = Column(DECIMAL(20, 6), doc="有形资产比率")
    EQUITYRATIO = Column(DECIMAL(20, 6), doc="所有者权益比率")
    RETAINEDEARNINGRATIO = Column(DECIMAL(20, 6), doc="留存收益资产比")
    LONGTERMASSETAPTNESSRATIO = Column(DECIMAL(20, 6), doc="长期资产适合率")
    EQUITYTOFIXEDASSETRATIO = Column(DECIMAL(20, 6), doc="股东权益对固定资产比率")
    CURRENTLIABILITYRATIO = Column(DECIMAL(20, 6), doc="流动负债比率")
    OPERATINGLIABILITYRATIO = Column(DECIMAL(20, 6), doc="经营负债比率")
    FINANCIALLIABILITYRATIO = Column(DECIMAL(20, 6), doc="金融负债比率")
    NONCURRENTLIABILITYRATIO = Column(DECIMAL(20, 6), doc="非流动负债比率")
    PARENTEQUITYRATIO = Column(DECIMAL(20, 6), doc="母公司所有者权益占比")
    MINORITYEQUITYRATIO = Column(DECIMAL(20, 6), doc="少数股东权益占比")
    MAINBUSINESSPROFITRATIO = Column(DECIMAL(20, 6), doc="主营业务利润占比")
    FINANCIALBUSINESSPROFITRATIO = Column(DECIMAL(20, 6), doc="金融活动利润占比")
    OPERATINGPROFITRATIO = Column(DECIMAL(20, 6), doc="营业利润占比")
    NONOPERATINGPROFITRATIO = Column(DECIMAL(20, 6), doc="营业外收入占比")
    TURNOVERTAXRATE = Column(DECIMAL(20, 6), doc="流转税率")
    CONSOLIDATEDTAXRATEA = Column(DECIMAL(20, 6), doc="综合税率A")
    CONSOLIDATEDTAXRATEB = Column(DECIMAL(20, 6), doc="综合税率B")
    INCOMETAXRATE = Column(DECIMAL(20, 6), doc="所得税率")
    PARENTPROFITRATIO = Column(DECIMAL(20, 6), doc="归属于母公司净利润占比")
    MINORITYPROFITRATIO = Column(DECIMAL(20, 6), doc="少数股东损益净利润占比")
    COMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="净利润综合收益占比")
    OTHERCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="其他综合收益占比")
    PARENTCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="归属于母公司综合收益占比")
    MINORITYCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="归属于少数股东综合收益占比")
    PARENTEQUITYTOINVESTRATIO = Column(DECIMAL(20, 6), doc="母公司所有者权益与投入资本比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_debtpay(Base):

    __tablename__ = 'stk_fin_debtpay'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    CURRENTRATIO = Column(DECIMAL(20, 6), doc="流动比率")
    QUICKRATIO = Column(DECIMAL(20, 6), doc="速动比率")
    CONSERVATIVEQUICKRATIO = Column(DECIMAL(20, 6), doc="保守速动比率")
    CASHRATIO = Column(DECIMAL(20, 6), doc="现金比率")
    WORKINGCAPITALTOLIABILITY = Column(DECIMAL(20, 6), doc="营运资金与借款比")
    WORKINGCAPITAL = Column(DECIMAL(20, 6), doc="营运资金")
    INTERESTCOVERAGERATIOA = Column(DECIMAL(20, 6), doc="利息保障倍数A")
    INTERESTCOVERAGERATIOB = Column(DECIMAL(20, 6), doc="利息保障倍数B")
    CURRENTLIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="经营活动产生的现金流量净额／流动负债")
    INTERESTCOVERAGERATIOC = Column(DECIMAL(20, 6), doc="现金流利息保障倍数")
    MATURINGLIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="现金流到期债务保障倍数")
    ASSETLIABILITYRATIO = Column(DECIMAL(20, 6), doc="资产负债率")
    LONGTERMLIABILITYTOASSET = Column(DECIMAL(20, 6), doc="长期借款与总资产比")
    LIABILITYTOTANGIBLEASSET = Column(DECIMAL(20, 6), doc="有形资产负债率")
    INTERESLIABILITYTOTANGIB = Column(DECIMAL(20, 6), doc="有形资产带息债务比")
    EQUITYMULTIPLIER = Column(DECIMAL(20, 6), doc="权益乘数")
    DEBTEQUITYRATIO = Column(DECIMAL(20, 6), doc="产权比率")
    EQUITYTODEBTRATIO = Column(DECIMAL(20, 6), doc="权益对负债比率")
    LONGTERMASSETLIABILITYRATIO = Column(DECIMAL(20, 6), doc="长期资本负债率")
    LONGTERMLIABILITYTOEQUITY = Column(DECIMAL(20, 6), doc="长期负债权益比率")
    LONGTERMLIABILITYTOWORKING = Column(DECIMAL(20, 6), doc="长期债务与营运资金比率")
    EBITDATOLIABILITY = Column(DECIMAL(20, 6), doc="息税折旧摊销前利润／负债合计")
    LIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="经营活动产生的现金流量净额／负债合计")
    INTERESLIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="经营活动产生的现金流量净额／带息债务")
    LIABILITYTOMARKETVALUE = Column(DECIMAL(20, 6), doc="负债与权益市价比率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_development(Base):

    __tablename__ = 'stk_fin_development'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    EQUITYAPPRECIATIONRATIOA = Column(DECIMAL(20, 6), doc="资本保值增值率A")
    EQUITYAPPRECIATIONRATIOB = Column(DECIMAL(20, 6), doc="资本保值增值率B")
    PARENTEQUITYAPPRECIATIONRATIO = Column(DECIMAL(20, 6), doc="母公司资本保值增值率")
    EQUITYGROWTHRATIOA = Column(DECIMAL(20, 6), doc="资本积累率A")
    EQUITYGROWTHRATIOB = Column(DECIMAL(20, 6), doc="资本积累率B")
    PARENTEQUITYGROWTHRATIO = Column(DECIMAL(20, 6), doc="母公司资本积累率")
    FIXEDASSETSGROWTHA = Column(DECIMAL(20, 6), doc="固定资产增长率A")
    FIXEDASSETSGROWTHB = Column(DECIMAL(20, 6), doc="固定资产增长率B")
    ASSETSGROWTHA = Column(DECIMAL(20, 6), doc="总资产增长率A")
    ASSETSGROWTHB = Column(DECIMAL(20, 6), doc="总资产增长率B")
    ROEGROWTHA = Column(DECIMAL(20, 6), doc="净资产收益率增长率A")
    ROEGROWTHB = Column(DECIMAL(20, 6), doc="净资产收益率增长率B")
    EPSGROWTHA = Column(DECIMAL(20, 6), doc="基本每股收益增长率A")
    EPSGROWTHB = Column(DECIMAL(20, 6), doc="基本每股收益增长率B")
    DILUTEDEPSGROWTHA = Column(DECIMAL(20, 6), doc="稀释每股收益增长率A")
    DILUTEDEPSGROWTHB = Column(DECIMAL(20, 6), doc="稀释每股收益增长率B")
    NETPROFITGROWTHA = Column(DECIMAL(20, 6), doc="净利润增长率A")
    NETPROFITGROWTHB = Column(DECIMAL(20, 6), doc="净利润增长率B")
    TOTALPROFITGROWTHA = Column(DECIMAL(20, 6), doc="利润总额增长率A")
    TOTALPROFITGROWTHB = Column(DECIMAL(20, 6), doc="利润总额增长率B")
    OPERATINGPROFITGROWTHA = Column(DECIMAL(20, 6), doc="营业利润增长率A")
    OPERATINGPROFITGROWTHB = Column(DECIMAL(20, 6), doc="营业利润增长率B")
    PARENTPROFITGROWTH = Column(DECIMAL(20, 6), doc="归属于母公司净利润增长率")
    COMPREHENSIVEGROWTH = Column(DECIMAL(20, 6), doc="综合收益增长率")
    PARENTCOMPREHENSIVEGROWTH = Column(DECIMAL(20, 6), doc="归属于母公司综合收益增长率")
    OPERATINGREVENUEGROWTHA = Column(DECIMAL(20, 6), doc="营业收入增长率A")
    OPERATINGREVENUEGROWTHB = Column(DECIMAL(20, 6), doc="营业收入增长率B")
    TOTALREVENUEGROWTHA = Column(DECIMAL(20, 6), doc="营业总收入增长率")
    TOTALREVENUEGROWTHB = Column(DECIMAL(20, 6), doc="营业总成本增长率")
    SALESEXPENSEGROWTH = Column(DECIMAL(20, 6), doc="销售费用增长率")
    MANAGEMENTEXPENSEGROWTH = Column(DECIMAL(20, 6), doc="管理费用增长率")
    ACCRUALS = Column(DECIMAL(20, 6), doc="应计项目")
    OPERATINGNCFPERSHAREGROWTHA = Column(DECIMAL(20, 6), doc="每股经营活动产生的净流量增长率A")
    OPERATINGNCFPERSHAREGROWTHB = Column(DECIMAL(20, 6), doc="每股经营活动产生的净流量增长率B")
    OPERATINGNCFGROWTHA = Column(DECIMAL(20, 6), doc="经营活动产生的净流量增长率A")
    OPERATINGNCFGROWTHB = Column(DECIMAL(20, 6), doc="经营活动产生的净流量增长率B")
    INVESTINGNCFGROWTHA = Column(DECIMAL(20, 6), doc="投资活动产生的现金流量增长率A")
    INVESTINGNCFGROWTHB = Column(DECIMAL(20, 6), doc="投资活动产生的现金流量增长率B")
    FINANCINGNCFGROWTHA = Column(DECIMAL(20, 6), doc="筹资活动产生的现金流量增长率A")
    FINANCINGNCFGROWTHB = Column(DECIMAL(20, 6), doc="筹资活动产生的现金流量增长率B")
    SUSTAINABLEGROWTHRATE = Column(DECIMAL(20, 6), doc="可持续增长率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    EQUITYGROWTHA = Column(DECIMAL(20, 6), doc="所有者权益增长率A ")
    EQUITYGROWTHB = Column(DECIMAL(20, 6), doc="所有者权益增长率B")
    EQUITYGROWTHC = Column(DECIMAL(20, 6), doc="所有者权益增长率C")
    NAVGROWTHA = Column(DECIMAL(20, 6), doc="每股净资产增长率A")
    NAVGROWTHB = Column(DECIMAL(20, 6), doc="每股净资产增长率B")
    NAVGROWTHC = Column(DECIMAL(20, 6), doc="每股净资产增长率C")
    ROEGROWTHC = Column(DECIMAL(20, 6), doc="净资产收益率增长率C")
    NETPROFITGROWTHC = Column(DECIMAL(20, 6), doc="净利润增长率C")
    OPERATINGREVENUEGROWTHC = Column(DECIMAL(20, 6), doc="营业收入增长率C")
    ASSETSGROWTHC = Column(DECIMAL(20, 6), doc="总资产增长率C")
    TOTALPROFITGROWTHC = Column(DECIMAL(20, 6), doc="利润总额增长率C")
    FIXEDASSETSGROWTHC = Column(DECIMAL(20, 6), doc="固定资产增长率C")
    EPSGROWTHC = Column(DECIMAL(20, 6), doc="基本每股收益增长率C")
    OPERATINGPROFITGROWTHC = Column(DECIMAL(20, 6), doc="营业利润增长率C")
    SUSTAINABLEGROWTHRATEB = Column(DECIMAL(20, 6), doc="可持续增长率2")
    EQUITYGROWTHRATIOC = Column(DECIMAL(20, 6), doc="资本积累率C")


class stk_fin_dividistrib(Base):

    __tablename__ = 'stk_fin_dividistrib'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    DIVIDENDSBTPERSHARE = Column(DECIMAL(20, 6), doc="每股税前现金股利")
    DIVIDENDSATPERSHARE = Column(DECIMAL(20, 6), doc="每股税后现金股利")
    DISTRIBUTIONRATE = Column(DECIMAL(20, 6), doc="股利分配率")
    CHANGEINVALUE = Column(DECIMAL(20, 6), doc="每股股利变动值")
    CHANGERATIO = Column(DECIMAL(20, 6), doc="每股股利变动比率")
    DIVIDENDCOVERAGERATIOA = Column(DECIMAL(20, 6), doc="现金股利保障倍数")
    DIVIDENDCOVERAGERATIOB = Column(DECIMAL(20, 6), doc="股利倍数")
    PROFITRETENTIONRATE = Column(DECIMAL(20, 6), doc="收益留存率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    DISTRIBUTIONRATEB = Column(DECIMAL(20, 6), doc="股利分配率2")
    DIVIDENDCOVERAGERATIOC = Column(DECIMAL(20, 6), doc="现金股利保障倍数2")
    DIVIDENDCOVERAGERATIOD = Column(DECIMAL(20, 6), doc="股利倍数2")
    PROFITRETENTIONRATEB = Column(DECIMAL(20, 6), doc="收益留存率2")


class stk_fin_earnpower(Base):

    __tablename__ = 'stk_fin_earnpower'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    ROA1A = Column(DECIMAL(20, 6), doc="资产报酬率A")
    ROA1B = Column(DECIMAL(20, 6), doc="资产报酬率B")
    ROA1C = Column(DECIMAL(20, 6), doc="资产报酬率C")
    ROA1TTM = Column(DECIMAL(20, 6), doc="资产报酬率TTM")
    ROA2A = Column(DECIMAL(20, 6), doc="总资产净利润率（ROA）A")
    ROA2B = Column(DECIMAL(20, 6), doc="总资产净利润率（ROA）B")
    ROA2C = Column(DECIMAL(20, 6), doc="总资产净利润率（ROA）C")
    ROA2TTM = Column(DECIMAL(20, 6), doc="总资产净利润率（ROA）TTM")
    NETPROFITTOCURRENTASSETA = Column(DECIMAL(20, 6), doc="流动资产净利润率A")
    NETPROFITTOCURRENTASSETB = Column(DECIMAL(20, 6), doc="流动资产净利润率B")
    NETPROFITTOCURRENTASSETC = Column(DECIMAL(20, 6), doc="流动资产净利润率C")
    NETPROFITTOCURRENTASSETTTM = Column(DECIMAL(20, 6), doc="流动资产净利润率TTM")
    NETPROFITTOFIXEDASSETA = Column(DECIMAL(20, 6), doc="固定资产净利润率A")
    NETPROFITTOFIXEDASSETB = Column(DECIMAL(20, 6), doc="固定资产净利润率B")
    NETPROFITTOFIXEDASSETC = Column(DECIMAL(20, 6), doc="固定资产净利润率C")
    NETPROFITTOFIXEDASSETTTM = Column(DECIMAL(20, 6), doc="固定资产净利润率TTM")
    ROEA = Column(DECIMAL(20, 6), doc="净资产收益率A")
    ROEB = Column(DECIMAL(20, 6), doc="净资产收益率B")
    ROEC = Column(DECIMAL(20, 6), doc="净资产收益率C")
    ROETTM = Column(DECIMAL(20, 6), doc="净资产收益率TTM")
    EBIT = Column(DECIMAL(20, 6), doc="息税前利润")
    EBITTTM = Column(DECIMAL(20, 6), doc="息税前利润TTM")
    EBTAT = Column(DECIMAL(20, 6), doc="息前税后利润")
    EBITDA = Column(DECIMAL(20, 6), doc="息税折旧摊销前收入")
    EBITDATTM = Column(DECIMAL(20, 6), doc="息税折旧摊销前收入TTM")
    NETPROFITTOTOTAL = Column(DECIMAL(20, 6), doc="净利润与利润总额比")
    NETPROFITTOEBIT = Column(DECIMAL(20, 6), doc="利润总额与息税前利润相比")
    EBITTOASSET = Column(DECIMAL(20, 6), doc="息税前利润与资产总额比")
    RETURNONINVESTEDCAPITAL = Column(DECIMAL(20, 6), doc="投入资本回报率")
    RETURNONLONGTERMINVESTED = Column(DECIMAL(20, 6), doc="长期资本收益率")
    OPERATINGMARGINRATIO = Column(DECIMAL(20, 6), doc="营业毛利率")
    OPERATINGMARGINRATIOTTM = Column(DECIMAL(20, 6), doc="营业毛利率TTM")
    OPERATINGCOSTRATIO = Column(DECIMAL(20, 6), doc="营业成本率")
    OPERATINGCOSTRATIOTTM = Column(DECIMAL(20, 6), doc="营业成本率TTM")
    OPERATINGPROFITOREVENUE = Column(DECIMAL(20, 6), doc="营业利润率")
    OPERATINGPROFITOREVENUETTM = Column(DECIMAL(20, 6), doc="营业利润率TTM")
    OPERATINGNETPROFITOREVENUE = Column(DECIMAL(20, 6), doc="营业净利率")
    OPERATINGNETPROFITOREVENUETTM = Column(DECIMAL(20, 6), doc="营业净利率TTM")
    GROSSCOSTRATIO = Column(DECIMAL(20, 6), doc="总营业成本率")
    GROSSCOSTRATIOTTM = Column(DECIMAL(20, 6), doc="总营业成本率TTM")
    SALESEXPENSERATE = Column(DECIMAL(20, 6), doc="销售费用率")
    SALESEXPENSERATETTM = Column(DECIMAL(20, 6), doc="销售费用率TTM")
    MANAGEMENTEXPENSERATE = Column(DECIMAL(20, 6), doc="管理费用率")
    MANAGEMENTEXPENSERATETTM = Column(DECIMAL(20, 6), doc="管理费用率TTM")
    FINANCIALEXPENSERATE = Column(DECIMAL(20, 6), doc="财务费用率")
    FINANCIALEXPENSERATETTM = Column(DECIMAL(20, 6), doc="财务费用率TTM")
    PERIODEXPENSERATE = Column(DECIMAL(20, 6), doc="销售期间费用率")
    PERIODEXPENSERATETTM = Column(DECIMAL(20, 6), doc="销售期间费用率TTM")
    PROFITTOCOST = Column(DECIMAL(20, 6), doc="成本费用利润率")
    PROFITTOCOSTTTM = Column(DECIMAL(20, 6), doc="成本费用利润率TTM")
    IMPAIRMENTLOSSTOREVENUE = Column(DECIMAL(20, 6), doc="资产减值损失／营业收入")
    IMPAIRMENTLOSSTOREVENUETTM = Column(DECIMAL(20, 6), doc="资产减值损失／营业收入TTM")
    EBITDATOREVENUE = Column(DECIMAL(20, 6), doc="息税折旧摊销前营业利润率")
    EBITDATOREVENUETTM = Column(DECIMAL(20, 6), doc="息税折旧摊销前利润率TTM")
    EBITTOREVENUE = Column(DECIMAL(20, 6), doc="息税前营业利润率")
    EBITTOREVENUETTM = Column(DECIMAL(20, 6), doc="息税前营业利润率TTM")
    NCFTONETPROFIT = Column(DECIMAL(20, 6), doc="净利润现金净含量")
    NCFTONETPROFITTTM = Column(DECIMAL(20, 6), doc="净利润现金净含量TTM")
    OPERATINGINCOMEINCASHRATIOA = Column(DECIMAL(20, 6), doc="营收入现金含量")
    OPERATINGINCOMEINCASHRATIOTTMA = Column(DECIMAL(20, 6), doc="营收入现金含量TTM")
    OPERATINGINCOMEINCASHRATIOB = Column(DECIMAL(20, 6), doc="营业收入现金净含量")
    OPERATINGINCOMEINCASHRATIOTTMB = Column(DECIMAL(20, 6), doc="营业收入现金净含量TTM")
    NCFTOOPERATINGPROFIT = Column(DECIMAL(20, 6), doc="营业利润现金净含量")
    NCFTOOPERATINGPROFITTTM = Column(DECIMAL(20, 6), doc="营业利润现金净含量TTM")
    NCFTOTOTALPROFIT = Column(DECIMAL(20, 6), doc="现金与利润总额比")
    NCFTOTOTALPROFITTTM = Column(DECIMAL(20, 6), doc="现金与利润总额比TTM")
    ROEPARENTA = Column(DECIMAL(20, 6), doc="归属于母公司净资产收益率A")
    ROEPARENTB = Column(DECIMAL(20, 6), doc="归属于母公司净资产收益率B")
    ROEPARENTC = Column(DECIMAL(20, 6), doc="归属于母公司净资产收益率C")
    ROEPARENTTTM = Column(DECIMAL(20, 6), doc="归属于母公司净资产收益率TTM")
    ROEPARENTCOMPREHENSIVEA = Column(DECIMAL(20, 6), doc="归属于母公司综合收益率A")
    ROEPARENTCOMPREHENSIVEB = Column(DECIMAL(20, 6), doc="归属于母公司综合收益率B")
    ROEPARENTCOMPREHENSIVEC = Column(DECIMAL(20, 6), doc="归属于母公司综合收益率C")
    ROEPARENTCOMPREHENSIVETTM = Column(DECIMAL(20, 6), doc="归属于母公司综合收益率TTM")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    RETURNONINVESTMENT = Column(DECIMAL(20, 6), doc="投资收益率")


class stk_fin_financialindexq(Base):

    __tablename__ = 'stk_fin_financialindexq'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    EPS = Column(DECIMAL(20, 6), doc="每股收益")
    EPSGROWTH = Column(DECIMAL(20, 6), doc="每股收益同比增长率")
    PARENTEPS = Column(DECIMAL(20, 6), doc="归属于母公司每股收益")
    PARENTEPSGROWTH = Column(DECIMAL(20, 6), doc="归属于母公司每股收益同比增长率")
    FINANCIALEXPENSERATEA = Column(DECIMAL(20, 6), doc="财务费用率A")
    FINANCIALEXPENSERATEB = Column(DECIMAL(20, 6), doc="财务费用率B")
    MANAGEMENTEXPENSERATEA = Column(DECIMAL(20, 6), doc="管理费用率A")
    MANAGEMENTEXPENSERATEB = Column(DECIMAL(20, 6), doc="管理费用率B")
    SALESEXPENSERATEA = Column(DECIMAL(20, 6), doc="销售费用率A")
    SALESEXPENSERATEB = Column(DECIMAL(20, 6), doc="销售费用率B")
    BUSINESSEXPENSERATEA = Column(DECIMAL(20, 6), doc="业务及管理费用率A")
    BUSINESSEXPENSERATEB = Column(DECIMAL(20, 6), doc="业务及管理费用率B")
    BUSINESSTAXRATIOA = Column(DECIMAL(20, 6), doc="营业税金率A")
    BUSINESSTAXRATIOB = Column(DECIMAL(20, 6), doc="营业税金率B")
    PERIODEXPENSERATEA = Column(DECIMAL(20, 6), doc="期间费用率A")
    PERIODEXPENSERATEB = Column(DECIMAL(20, 6), doc="期间费用率B")
    NETPROFITOREVENUEA = Column(DECIMAL(20, 6), doc="营业净利率A")
    NETPROFITOREVENUEB = Column(DECIMAL(20, 6), doc="营业净利率B")
    OPERATINGCOSTRATIO = Column(DECIMAL(20, 6), doc="营业成本率")
    GROSSCOSTRATIO = Column(DECIMAL(20, 6), doc="总营业成本率")
    OPERATINGPROFITOREVENUEA = Column(DECIMAL(20, 6), doc="营业利润率A")
    OPERATINGPROFITOREVENUEB = Column(DECIMAL(20, 6), doc="营业利润率B")
    PROFITTOCOST = Column(DECIMAL(20, 6), doc="成本费用利润率")
    OPERATENETINCOME = Column(DECIMAL(20, 6), doc="经营活动净收益")
    OPERATENETINCOMETOTOTALPROFIT = Column(DECIMAL(20, 6), doc="经营活动净收益/利润总额")
    VALUECHANGENETINCOME = Column(DECIMAL(20, 6), doc="价值变动净收益")
    VALUECHANGENETINCOMETOPROFIT = Column(DECIMAL(20, 6), doc="金融活动利润占比")
    GROSSPROFITMARGIN = Column(DECIMAL(20, 6), doc="销售毛利率")
    OPERATENETINCOMETOREVENUE = Column(DECIMAL(20, 6), doc="经营活动净收益/营业总收入")
    NETPROFITRECURRING = Column(DECIMAL(20, 6), doc="扣除非经常损益后的净利润")
    NETPROFITRECURRINGTONETPROFIT = Column(DECIMAL(20, 6), doc="扣除非经常损益后的净利润/净利润")
    PROFITPARENTRECURRING = Column(DECIMAL(20, 6), doc="归属于上市公司股东的扣除非经常性损益的净利润")
    TOTALREVENUEGROWTHA = Column(DECIMAL(20, 6), doc="营业总收入环比增长率")
    TOTALREVENUEGROWTHB = Column(DECIMAL(20, 6), doc="营业总收入同比增长率")
    OPERATINGREVENUEGROWTHA = Column(DECIMAL(20, 6), doc="营业收入环比增长率")
    OPERATINGREVENUEGROWTHB = Column(DECIMAL(20, 6), doc="营业收入同比增长率")
    OPERATINGPROFITGROWTHA = Column(DECIMAL(20, 6), doc="营业利润环比增长率")
    OPERATINGPROFITGROWTHB = Column(DECIMAL(20, 6), doc="营业利润同比增长率")
    TOTALPROFITGROWTHA = Column(DECIMAL(20, 6), doc="利润总额环比增长率")
    TOTALPROFITGROWTHB = Column(DECIMAL(20, 6), doc="利润总额同比增长率")
    TOTALOPERATINGCOSTGROWTHA = Column(DECIMAL(20, 6), doc="营业总成本环比增长率")
    TOTALOPERATINGCOSTGROWTHB = Column(DECIMAL(20, 6), doc="营业总成本同比增长率")
    PARENTPROFITGROWTHA = Column(DECIMAL(20, 6), doc="归属于母公司净利润环比增长率")
    PARENTPROFITGROWTHB = Column(DECIMAL(20, 6), doc="归属于母公司净利润同比增长率")
    NETPROFITGROWTHA = Column(DECIMAL(20, 6), doc="净利润环比增长率")
    NETPROFITGROWTHB = Column(DECIMAL(20, 6), doc="净利润同比增长率")
    NONOPERATINGPROFITRATIO = Column(DECIMAL(20, 6), doc="营业外收入占比")
    NETPROFITTOTOTAL = Column(DECIMAL(20, 6), doc="净利润与利润总额比")
    COMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="净利润综合收益占比")
    PARENTCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="归属于母公司综合收益占比")
    MINORITYCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="归属于少数股东综合收益占比")
    OTHERCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="其他综合收益占比")
    MINORITYPROFITRATIO = Column(DECIMAL(20, 6), doc="少数股东损益净利润占比")
    PARENTPROFITRATIO = Column(DECIMAL(20, 6), doc="归属于母公司净利润占比")
    NCFTONETPROFIT = Column(DECIMAL(20, 6), doc="净利润现金净含量")
    OPERATINGINCOMEINCASHRATIO = Column(DECIMAL(20, 6), doc="营业总收入现金净含量")
    NCFTOOPERATINGPROFIT = Column(DECIMAL(20, 6), doc="营业利润现金净含量")
    NCFTOTOTALPROFIT = Column(DECIMAL(20, 6), doc="现金与利润总额比")
    OPERATINGINCOMEINCASHRATIOA = Column(DECIMAL(20, 6), doc="营收入现金含量")
    NCFTOOPERATENETINCOME = Column(DECIMAL(20, 6), doc="现金与经营活动净收益比")
    ROE = Column(DECIMAL(20, 6), doc="净资产收益率")
    ROEGROWTHA = Column(DECIMAL(20, 6), doc="净资产收益率环比增长率")
    ROEGROWTHB = Column(DECIMAL(20, 6), doc="净资产收益率同比增长率")
    ROERECURRING = Column(DECIMAL(20, 6), doc="扣除非经常性损益后净资产收益率")
    ROA = Column(DECIMAL(20, 6), doc="总资产净利率")
    IMPAIRMENTTOOPERATINGPROFIT = Column(DECIMAL(20, 6), doc="资产减值损失/营业利润")
    OPERATINGNCFTOCASHEQUI = Column(DECIMAL(20, 6), doc="经营活动产生的现金流量净额占比")
    FINACINGNCFTOCASHEQUI = Column(DECIMAL(20, 6), doc="筹资活动产生的现金流量净额占比")
    INVESTINGNCFTOCASHEQUI = Column(DECIMAL(20, 6), doc="投资活动产生的现金流量净额占比")
    OPERATINGNCFGROWTHA = Column(DECIMAL(20, 6), doc="经营活动产生的现金流量环比增长率")
    OPERATINGNCFGROWTHB = Column(DECIMAL(20, 6), doc="经营活动产生的现金流量同比增长率")
    INVESTINGNCFGROWTHA = Column(DECIMAL(20, 6), doc="投资活动产生的现金流量环比增长率")
    INVESTINGNCFGROWTHB = Column(DECIMAL(20, 6), doc="投资活动产生的现金流量同比增长率")
    FINANCINGNCFGROWTHA = Column(DECIMAL(20, 6), doc="筹资活动产生的现金流量环比增长率")
    FINANCINGNCFGROWTHB = Column(DECIMAL(20, 6), doc="筹资活动产生的现金流量同比增长率")
    CASHEQUIVALENTCHANGEGROWTHA = Column(DECIMAL(20, 6), doc="现金净流量环比增长率")
    CASHEQUIVALENTCHANGEGROWTHB = Column(DECIMAL(20, 6), doc="现金净流量同比增长率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_forecfin(Base):

    __tablename__ = 'stk_fin_forecfin'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    SOURCE = Column(SMALLINT, doc="业绩来源")
    ENDDATE = Column(DateTime, doc="业绩报告期")
    DECLAREDATE = Column(DateTime, doc="预告日期")
    CHANGENUMBER = Column(SMALLINT, doc="业绩预告发布次数")
    PERFORMANCETYPE = Column(String(40), doc="业绩预告类型")
    PROFITPARENTFLOOR = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润（下限）")
    PROFITPARENTCEILING = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润（上限）")
    PROFITPARENTLAST = Column(DECIMAL(20, 2), doc="去年同期归属于母公司所有者的净利润")
    PROFITPARENTCHANGERATIOFLOOR = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润变动幅度（下限）%")
    PROFITPARENTCHANGERATIOCEILING = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润变动幅度（上限）%")
    PROFITFLOOR = Column(DECIMAL(20, 2), doc="预告净利润（下限）")
    PROFITCEILING = Column(DECIMAL(20, 2), doc="预告净利润（上限）")
    PROFITLAST = Column(DECIMAL(20, 2), doc="去年同期净利润")
    PROFITCHANGERATIOFLOOR = Column(DECIMAL(20, 2), doc="预告净利润变动幅度（下限）%")
    PROFITCHANGERATIOCEILING = Column(DECIMAL(20, 2), doc="预告净利润变动幅度（上限）%")
    EPSFLOOR = Column(DECIMAL(20, 4), doc="预告每股收益（下限）")
    EPSCEILING = Column(DECIMAL(20, 4), doc="预告每股收益（上限）")
    EPSLAST = Column(DECIMAL(20, 4), doc="去年同期每股收益")
    EPSCHANGERATIOFLOOR = Column(DECIMAL(20, 4), doc="预告每股收益变动幅度（下限）%")
    EPSCHANGERATIOCEILING = Column(DECIMAL(20, 4), doc="预告每股收益变动幅度（上限）%")
    AUDITSTATUS = Column(String(2), doc="预审计情况")
    CHANGEREASON = Column(LONGTEXT, doc="业绩变动原因")
    MODIFYREASON = Column(LONGTEXT, doc="业绩修正原因")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_forecfinnew(Base):

    __tablename__ = 'stk_fin_forecfinnew'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    SOURCE = Column(SMALLINT, doc="业绩来源")
    ENDDATE = Column(DateTime, primary_key=True, doc="业绩报告期")
    DECLAREDATE = Column(DateTime, doc="预告日期")
    PERFORMANCETYPEID = Column(String(40), doc="业绩预告类型编码")
    PERFORMANCETYPE = Column(String(40), doc="业绩预告类型")
    PROFITPARENTFLOOR = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润（下限）")
    PROFITPARENTCEILING = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润（上限）")
    PROFITPARENTLAST = Column(DECIMAL(20, 2), doc="去年同期归属于母公司所有者的净利润")
    PROFITPARENTCHANGERATIOFLOOR = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润变动幅度（下限）%")
    PROFITPARENTCHANGERATIOCEILING = Column(DECIMAL(20, 2), doc="预告归属于母公司所有者的净利润变动幅度（上限）%")
    PROFITFLOOR = Column(DECIMAL(20, 2), doc="预告净利润（下限）")
    PROFITCEILING = Column(DECIMAL(20, 2), doc="预告净利润（上限）")
    PROFITLAST = Column(DECIMAL(20, 2), doc="去年同期净利润")
    PROFITCHANGERATIOFLOOR = Column(DECIMAL(20, 2), doc="预告净利润变动幅度（下限）%")
    PROFITCHANGERATIOCEILING = Column(DECIMAL(20, 2), doc="预告净利润变动幅度（上限）%")
    EPSFLOOR = Column(DECIMAL(20, 4), doc="预告每股收益（下限）")
    EPSCEILING = Column(DECIMAL(20, 4), doc="预告每股收益（上限）")
    EPSLAST = Column(DECIMAL(20, 4), doc="去年同期每股收益")
    EPSCHANGERATIOFLOOR = Column(DECIMAL(20, 4), doc="预告每股收益变动幅度（下限）%")
    EPSCHANGERATIOCEILING = Column(DECIMAL(20, 4), doc="预告每股收益变动幅度（上限）%")
    AUDITSTATUS = Column(String(2), doc="预审计情况")
    CHANGEREASON = Column(LONGTEXT, doc="业绩变动原因")
    MODIFYREASON = Column(LONGTEXT, doc="业绩修正原因")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_fin_income(Base):

    __tablename__ = 'stk_fin_income'

    INSTITUTIONID = Column(DECIMAL(20, 0))
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    STATETYPECODE = Column(String(12))
    SYMBOL = Column(String(12))
    INDUSTRYMARK = Column(BIGINT)
    EVENTID = Column(String(40))
    B0011 = Column(DECIMAL(20, 2))
    B001101 = Column(DECIMAL(20, 2))
    BBD1102 = Column(DECIMAL(20, 2))
    BBD110210 = Column(DECIMAL(20, 2))
    BBD110220 = Column(DECIMAL(20, 2))
    B0D1104 = Column(DECIMAL(20, 2))
    B0D110410 = Column(DECIMAL(20, 2))
    B0D110420 = Column(DECIMAL(20, 2))
    B0D110430 = Column(DECIMAL(20, 2))
    B0D110440 = Column(DECIMAL(20, 2))
    B0D110450 = Column(DECIMAL(20, 2))
    B0I1103 = Column(DECIMAL(20, 2))
    B0I110310 = Column(DECIMAL(20, 2))
    B0I11031010 = Column(DECIMAL(20, 2))
    B0I110320 = Column(DECIMAL(20, 2))
    B0I110330 = Column(DECIMAL(20, 2))
    B0F1105 = Column(DECIMAL(20, 2))
    B0012 = Column(DECIMAL(20, 2))
    B001201 = Column(DECIMAL(20, 2))
    B0I1202 = Column(DECIMAL(20, 2))
    B0I1203 = Column(DECIMAL(20, 2))
    B0I120310 = Column(DECIMAL(20, 2))
    B0I120320 = Column(DECIMAL(20, 2))
    B0I1204 = Column(DECIMAL(20, 2))
    B0I120410 = Column(DECIMAL(20, 2))
    B0I120420 = Column(DECIMAL(20, 2))
    B0I1205 = Column(DECIMAL(20, 2))
    B0I1206 = Column(DECIMAL(20, 2))
    B0I1214 = Column(DECIMAL(20, 2))
    B001207 = Column(DECIMAL(20, 2))
    B0F1208 = Column(DECIMAL(20, 2))
    B0I1215 = Column(DECIMAL(20, 2))
    B001209 = Column(DECIMAL(20, 2))
    B001210 = Column(DECIMAL(20, 2))
    B001211 = Column(DECIMAL(20, 2))
    B001212 = Column(DECIMAL(20, 2))
    B0F1213 = Column(DECIMAL(20, 2))
    B001302 = Column(DECIMAL(20, 2))
    B00130210 = Column(DECIMAL(20, 2))
    B001301 = Column(DECIMAL(20, 2))
    B001303 = Column(DECIMAL(20, 2))
    B001304 = Column(DECIMAL(20, 2))
    B0013 = Column(DECIMAL(20, 2))
    B0014 = Column(DECIMAL(20, 2))
    B0015 = Column(DECIMAL(20, 2))
    B00150010 = Column(DECIMAL(20, 2))
    B001 = Column(DECIMAL(20, 2))
    B0021 = Column(DECIMAL(20, 2))
    B0022 = Column(DECIMAL(20, 2))
    B0023 = Column(DECIMAL(20, 2))
    B002 = Column(DECIMAL(20, 2))
    B0024 = Column(DECIMAL(20, 2))
    B0025 = Column(DECIMAL(20, 2))
    B003 = Column(DECIMAL(20, 4))
    B004 = Column(DECIMAL(20, 4))
    B005 = Column(DECIMAL(20, 2))
    B006 = Column(DECIMAL(20, 2))
    B0061 = Column(DECIMAL(20, 2))
    B0062 = Column(DECIMAL(20, 2))
    UPDATEID = Column(BIGINT, primary_key=True)
    REPORTTYPEID = Column(SMALLINT)
    B00140010 = Column(DECIMAL(20, 2), doc="其中：非流动资产处置利得")
    B00150020 = Column(DECIMAL(20, 2), doc="其中：非流动资产处置损失")
    B001216 = Column(DECIMAL(20, 2), doc="研发费用")
    B00121110 = Column(DECIMAL(20, 2), doc="其中：利息费用(财务费用)")
    B00121120 = Column(DECIMAL(20, 2), doc="其中：利息收入(财务费用)")
    B001305 = Column(DECIMAL(20, 2), doc="其他收益")
    B00130220 = Column(DECIMAL(20, 2), doc="其中：以摊余成本计量的金融资产终止确认收益")
    B001306 = Column(DECIMAL(20, 2), doc="净敞口套期收益")
    B001307 = Column(DECIMAL(20, 2), doc="信用减值损失")
    B001308 = Column(DECIMAL(20, 2), doc="资产处置收益")
    B0026 = Column(DECIMAL(20, 2), doc="归属于母公司其他权益工具持有者的净利润")
    B0063 = Column(DECIMAL(20, 2), doc="归属于母公司其他权益工具持有者的综合收益总额")


class stk_fin_incomettm(Base):

    __tablename__ = 'stk_fin_incomettm'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    SYMBOL = Column(String(12), doc="股票代码")
    INDUSTRYMARK = Column(BIGINT, doc="行业标识")
    TOTALREVENUE = Column(DECIMAL(20, 2), doc="营业总收入")
    REVENUE = Column(DECIMAL(20, 2), doc="营业收入")
    NETINTERESTINCOME = Column(DECIMAL(20, 2), doc="利息净收入")
    INTERESTINCOME = Column(DECIMAL(20, 2), doc="利息收入")
    INTERESTEXPENSE = Column(DECIMAL(20, 2), doc="利息支出")
    NETCOMMISSIONINCOME = Column(DECIMAL(20, 2), doc="手续费及佣金净收入")
    SECURITYTRADINGAGENCY = Column(DECIMAL(20, 2), doc="其中：代理买卖证券业务净收入")
    SECURITYUNDERWRITINGBUSINESS = Column(DECIMAL(20, 2), doc="其中:证券承销业务净收入")
    ASSETMANAGEMENTBUSINESS = Column(DECIMAL(20, 2), doc="其中：受托客户资产管理业务净收入")
    COMMISSIONINCOME = Column(DECIMAL(20, 2), doc="手续费及佣金收入")
    COMMISSIONEXPENSE = Column(DECIMAL(20, 2), doc="手续费及佣金支出")
    NETEARNEDPREMIUM = Column(DECIMAL(20, 2), doc="已赚保费")
    INSURANCEBUSINESSINCOME = Column(DECIMAL(20, 2), doc="保险业务收入")
    REINSURANCEPREMIUMINCOME = Column(DECIMAL(20, 2), doc="其中：分保费收入")
    REINSUREREXPENSE = Column(DECIMAL(20, 2), doc="减：分出保费")
    UNEARNEDPREMIUMRESERVE = Column(DECIMAL(20, 2), doc="减：提取未到期责任准备金")
    OTHEROPERATINGREVENUE = Column(DECIMAL(20, 2), doc="其他业务收入")
    TOTALOPERATINGCOST = Column(DECIMAL(20, 2), doc="营业总成本")
    OPERATINGCOST = Column(DECIMAL(20, 2), doc="营业成本")
    CASHSURRENDER = Column(DECIMAL(20, 2), doc="退保金")
    NETCLAIMEXPENSE = Column(DECIMAL(20, 2), doc="赔付支出净额")
    CLAIMEXPENSE = Column(DECIMAL(20, 2), doc="赔付支出")
    CLAIMEXPENSERECOVERABLE = Column(DECIMAL(20, 2), doc="减：摊回赔付支出")
    NETINSURANCERESERVE = Column(DECIMAL(20, 2), doc="提取保险责任准备金净额")
    INSURANCERESERVE = Column(DECIMAL(20, 2), doc="提取保险责任准备金")
    INSURANCERESERVERECOVERABLE = Column(DECIMAL(20, 2), doc="减：摊回保险责任准备金")
    POLICYHOLDERDIVIDEND = Column(DECIMAL(20, 2), doc="保单红利支出")
    REINSURANCEEXPENSE = Column(DECIMAL(20, 2), doc="分保费用")
    INSURANCECOMMISSIONEXPENSE = Column(DECIMAL(20, 2), doc="保险业务手续费及佣金支出")
    BUSINESSTAXANDSURCHARGE = Column(DECIMAL(20, 2), doc="营业税金及附加")
    BUSINESSANDMANAGEMENTEXPENSE = Column(DECIMAL(20, 2), doc="业务及管理费")
    REINSUREREXPENSERECOVERABLE = Column(DECIMAL(20, 2), doc="减：摊回分保费用")
    SELLINGEXPENSES = Column(DECIMAL(20, 2), doc="销售费用")
    MANAGEMENTEXPENSE = Column(DECIMAL(20, 2), doc="管理费用")
    FINANCEEXPENSE = Column(DECIMAL(20, 2), doc="财务费用")
    ASSETIMPAIRMENTLOSS = Column(DECIMAL(20, 2), doc="资产减值损失")
    OTHEROPERATINGEXPENSE = Column(DECIMAL(20, 2), doc="其他业务成本")
    INVESTMENTINCOME = Column(DECIMAL(20, 2), doc="投资收益")
    JOINTVENTUREINVESTMENTINCOME = Column(DECIMAL(20, 2), doc="其中：对联营企业和合营企业的投资收益")
    FAIRVALUECHANGE = Column(DECIMAL(20, 2), doc="公允价值变动收益")
    EXCHANGEGAINS = Column(DECIMAL(20, 2), doc="汇兑收益")
    OTHEROPERATINGPROFIT = Column(DECIMAL(20, 2), doc="其他业务利润")
    OPERATINGPROFIT = Column(DECIMAL(20, 2), doc="营业利润")
    NONOPERATINGINCOME = Column(DECIMAL(20, 2), doc="营业外收入")
    NONOPERATINGEXPENSES = Column(DECIMAL(20, 2), doc="营业外支出")
    DISPOSALOFNONCURRENTASSETS = Column(DECIMAL(20, 2), doc="其中：非流动资产处置净损益")
    TOTALPROFIT = Column(DECIMAL(20, 2), doc="利润总额")
    INCOMETAX = Column(DECIMAL(20, 2), doc="所得税费用")
    UNRECOGNIZEDINVESTMENTLOSSES = Column(DECIMAL(20, 2), doc="未确认的投资损失")
    OTHERPROFIT = Column(DECIMAL(20, 2), doc="影响净利润的其他项目")
    NETPROFIT = Column(DECIMAL(20, 2), doc="净利润")
    PARENTNETPROFIT = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润")
    MINORITYINTEREST = Column(DECIMAL(20, 2), doc="少数股东损益")
    EPS = Column(DECIMAL(20, 2), doc="基本每股收益")
    DILUTEDEPS = Column(DECIMAL(20, 2), doc="稀释每股收益")
    OTHERCOMPREHENSIVEINCOME = Column(DECIMAL(20, 2), doc="其他综合收益(损失)")
    COMPREHENSIVEINCOME = Column(DECIMAL(20, 2), doc="综合收益总额")
    PARENTCOMPREHENSIVEINCOME = Column(DECIMAL(20, 2), doc="归属于母公司所有者的综合收益总额")
    MINORITYCOMPREHENSIVEINCOME = Column(DECIMAL(20, 2), doc="归属于少数股东的综合收益总额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_ipodiscloseindex(Base):

    __tablename__ = 'stk_fin_ipodiscloseindex'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, primary_key=True, doc="会计期间")
    PROFITPARENTRECURRING = Column(DECIMAL(20, 2), doc="归属于上市公司股东的扣除非经常性损益的净利润")
    NONRECURRING = Column(DECIMAL(20, 2), doc="非经常性损益")
    EPSCHANGERATIO = Column(DECIMAL(20, 4), doc="基本每股收益本年比上年增减")
    EPSRECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的基本每股收益")
    DILUTEDEPSCHANGERATIO = Column(DECIMAL(20, 4), doc="稀释每股收益本年比上年增减")
    DILUTEDEPSRECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的稀释每股收益")
    ROE = Column(DECIMAL(20, 4), doc="加权平均净资产收益率")
    ROERECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的加权平均净资产收益率")
    OPERATECASHFLOWPERSHARE = Column(DECIMAL(20, 2), doc="每股经营活动产生的现金流量净额")
    NAVPARENT = Column(DECIMAL(20, 2), doc="归属于上市公司股东的每股净资产")
    DEBTTOASSETRATIO = Column(DECIMAL(20, 4), doc="资产负债率")
    DEBTTOASSETRATIOPARENT = Column(DECIMAL(20, 4), doc="母公司资产负债率")
    CURRENTRATIO = Column(DECIMAL(20, 2), doc="流动比率")
    QUICKRATIO = Column(DECIMAL(20, 2), doc="速动比率")
    RECEIVABLESTURNOVER = Column(DECIMAL(20, 4), doc="应收账款周转率")
    INVENTORYTURNOVER = Column(DECIMAL(20, 4), doc="存货周转率")
    EBITDA = Column(DECIMAL(20, 2), doc="息税折旧摊销前利润 ")
    INTERESTCOVERAGERATIO = Column(DECIMAL(20, 2), doc="利息保障倍数")
    INTANGIBLETOEQUITY = Column(DECIMAL(20, 4), doc="无形资产（扣除土地使用权）占净资产比例")
    ASSETTURNOVER = Column(DECIMAL(20, 4), doc="总资产周转率")
    NETCASHFLOWPERSHARE = Column(DECIMAL(20, 2), doc="每股净现金流量")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_fin_lcdiscloseindex(Base):

    __tablename__ = 'stk_fin_lcdiscloseindex'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, primary_key=True, doc="会计期间")
    PROFITPARENTRECURRING = Column(DECIMAL(20, 2), doc="归属于上市公司股东的扣除非经常性损益的净利润")
    NONRECURRING = Column(DECIMAL(20, 2), doc="非经常性损益")
    EPSCHANGERATIO = Column(DECIMAL(20, 4), doc="基本每股收益本年比上年增减")
    EPSRECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的基本每股收益")
    DILUTEDEPSCHANGERATIO = Column(DECIMAL(20, 4), doc="稀释每股收益本年比上年增减")
    DILUTEDEPSRECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的稀释每股收益")
    ROE = Column(DECIMAL(20, 4), doc="加权平均净资产收益率")
    ROERECURRING = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的加权平均净资产收益率")
    OPERATECASHFLOWPERSHARE = Column(DECIMAL(20, 4), doc="每股经营活动产生的现金流量净额")
    NAVPARENT = Column(DECIMAL(20, 4), doc="归属于上市公司股东的每股净资产")
    DEBTTOASSETRATIO = Column(DECIMAL(20, 4), doc="资产负债率")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_fin_operate(Base):

    __tablename__ = 'stk_fin_operate'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    RECEIVABLESTOINCOME = Column(DECIMAL(20, 6), doc="应收账款与收入比")
    RECEIVABLETURNOVERA = Column(DECIMAL(20, 6), doc="应收账款周转率A")
    RECEIVABLETURNOVERB = Column(DECIMAL(20, 6), doc="应收账款周转率B")
    RECEIVABLETURNOVERC = Column(DECIMAL(20, 6), doc="应收账款周转率C")
    RECEIVABLETURNOVERD = Column(DECIMAL(20, 6), doc="应收账款周转率D")
    RECEIVABLETURNOVERTTM = Column(DECIMAL(20, 6), doc="应收账款周转率TTM")
    RECEIVABLETURNOVERDAYSA = Column(DECIMAL(20, 6), doc="应收账款周转天数A")
    RECEIVABLETURNOVERDAYSB = Column(DECIMAL(20, 6), doc="应收账款周转天数B")
    RECEIVABLETURNOVERDAYSC = Column(DECIMAL(20, 6), doc="应收账款周转天数C")
    RECEIVABLETURNOVERDAYSTTM = Column(DECIMAL(20, 6), doc="应收账款周转天数TTM")
    INVENTORYTOINCOME = Column(DECIMAL(20, 6), doc="存货与收入比")
    INVENTORYTURNOVERA = Column(DECIMAL(20, 6), doc="存货周转率A")
    INVENTORYTURNOVERB = Column(DECIMAL(20, 6), doc="存货周转率B")
    INVENTORYTURNOVERC = Column(DECIMAL(20, 6), doc="存货周转率C")
    INVENTORYTURNOVERD = Column(DECIMAL(20, 6), doc="存货周转率D")
    INVENTORYTURNOVERTTM = Column(DECIMAL(20, 6), doc="存货周转率TTM")
    INVENTORYTURNOVERDAYSA = Column(DECIMAL(20, 6), doc="存货周转天数A")
    INVENTORYTURNOVERDAYSB = Column(DECIMAL(20, 6), doc="存货周转天数B")
    INVENTORYTURNOVERDAYSC = Column(DECIMAL(20, 6), doc="存货周转天数C")
    INVENTORYTURNOVERDAYSTTM = Column(DECIMAL(20, 6), doc="存货周转天数TTM")
    OPERATINGCYCLEA = Column(DECIMAL(20, 6), doc="营业周期A")
    OPERATINGCYCLEB = Column(DECIMAL(20, 6), doc="营业周期B")
    OPERATINGCYCLEC = Column(DECIMAL(20, 6), doc="营业周期C")
    OPERATINGCYCLETTM = Column(DECIMAL(20, 6), doc="营业周期TTM")
    PAYABLETURNOVERA = Column(DECIMAL(20, 6), doc="应付账款周转率A")
    PAYABLETURNOVERB = Column(DECIMAL(20, 6), doc="应付账款周转率B")
    PAYABLETURNOVERC = Column(DECIMAL(20, 6), doc="应付账款周转率C")
    PAYABLETURNOVERD = Column(DECIMAL(20, 6), doc="应付账款周转率D")
    PAYABLETURNOVERTTM = Column(DECIMAL(20, 6), doc="应付账款周转率TTM")
    WORKINGCAPITALTURNOVERA = Column(DECIMAL(20, 6), doc="营运资金（资本）周转率A")
    WORKINGCAPITALTURNOVERB = Column(DECIMAL(20, 6), doc="营运资金（资本）周转率B")
    WORKINGCAPITALTURNOVERC = Column(DECIMAL(20, 6), doc="营运资金（资本）周转率C")
    WORKINGCAPITALTURNOVERD = Column(DECIMAL(20, 6), doc="营运资金（资本）周转率D")
    WORKINGCAPITALTURNOVERTTM = Column(DECIMAL(20, 6), doc="营运资金（资本）周转率TTM")
    CASHEQUIVALENTSTURNOVERA = Column(DECIMAL(20, 6), doc="现金及现金等价物周转率A")
    CASHEQUIVALENTTURNOVERB = Column(DECIMAL(20, 6), doc="现金及现金等价物周转率B")
    CASHEQUIVALENTTURNOVERC = Column(DECIMAL(20, 6), doc="现金及现金等价物周转率C")
    CASHEQUIVALENTTURNOVERD = Column(DECIMAL(20, 6), doc="现金及现金等价物周转率D")
    CASHEQUIVALENTTURNOVERTTM = Column(DECIMAL(20, 6), doc="现金及现金等价物周转率TTM")
    CURRENTASSETTOINCOME = Column(DECIMAL(20, 6), doc="流动资产与收入比")
    CURRENTASSETTURNOVERA = Column(DECIMAL(20, 6), doc="流动资产周转率A")
    CURRENTASSETTURNOVERB = Column(DECIMAL(20, 6), doc="流动资产周转率B")
    CURRENTASSETTURNOVERC = Column(DECIMAL(20, 6), doc="流动资产周转率C")
    CURRENTASSETTURNOVERD = Column(DECIMAL(20, 6), doc="流动资产周转率D")
    CURRENTASSETTURNOVERTTM = Column(DECIMAL(20, 6), doc="流动资产周转率TTM")
    FIXEDASSETTOINCOME = Column(DECIMAL(20, 6), doc="固定资产与收入比")
    FIXEDASSETTURNOVERA = Column(DECIMAL(20, 6), doc="固定资产周转率A")
    FIXEDASSETTURNOVERB = Column(DECIMAL(20, 6), doc="固定资产周转率B")
    FIXEDASSETTURNOVERC = Column(DECIMAL(20, 6), doc="固定资产周转率C")
    FIXEDASSETTURNOVERD = Column(DECIMAL(20, 6), doc="固定资产周转率D")
    FIXEDASSETTURNOVERTTM = Column(DECIMAL(20, 6), doc="固定资产周转率TTM")
    NONCURRENTASSETTURNOVERA = Column(DECIMAL(20, 6), doc="非流动资产周转率A")
    NONCURRENTASSETTURNOVERB = Column(DECIMAL(20, 6), doc="非流动资产周转率B")
    NONCURRENTASSETTURNOVERC = Column(DECIMAL(20, 6), doc="非流动资产周转率C")
    NONCURRENTASSETTURNOVERD = Column(DECIMAL(20, 6), doc="非流动资产周转率D")
    NONCURRENTASSETTURNOVERTTM = Column(DECIMAL(20, 6), doc="非流动资产周转率TTM")
    CAPITALINTENSITY = Column(DECIMAL(20, 6), doc="资本密集度")
    ASSETTURNOVERA = Column(DECIMAL(20, 6), doc="总资产周转率A")
    ASSETTURNOVERB = Column(DECIMAL(20, 6), doc="总资产周转率B")
    ASSETTURNOVERC = Column(DECIMAL(20, 6), doc="总资产周转率C")
    ASSETTURNOVERD = Column(DECIMAL(20, 6), doc="总资产周转率D")
    ASSETTURNOVERTTM = Column(DECIMAL(20, 6), doc="总资产周转率TTM")
    EEQUITYTURNOVERA = Column(DECIMAL(20, 6), doc="股东权益周转率A")
    EEQUITYTURNOVERB = Column(DECIMAL(20, 6), doc="股东权益周转率B")
    EEQUITYTURNOVERC = Column(DECIMAL(20, 6), doc="股东权益周转率C")
    EEQUITYTURNOVERD = Column(DECIMAL(20, 6), doc="股东权益周转率D")
    EEQUITYTURNOVERTTM = Column(DECIMAL(20, 6), doc="股东权益周转率TTM")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_pershare(Base):

    __tablename__ = 'stk_fin_pershare'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    EPS = Column(DECIMAL(20, 6), doc="基本每股收益")
    DILUTEDEPS = Column(DECIMAL(20, 6), doc="稀释每股收益")
    EPSA = Column(DECIMAL(20, 6), doc="每股收益1")
    EPSTTMA = Column(DECIMAL(20, 6), doc="每股收益TTM1")
    EPSB = Column(DECIMAL(20, 6), doc="每股收益2")
    EPSTTMB = Column(DECIMAL(20, 6), doc="每股收益TTM2")
    EPSC = Column(DECIMAL(20, 6), doc="每股收益3")
    EPSTTMC = Column(DECIMAL(20, 6), doc="每股收益TTM3")
    EPSD = Column(DECIMAL(20, 6), doc="每股收益4")
    EPSTTMD = Column(DECIMAL(20, 6), doc="每股收益TTM4")
    COMPREHENSIVEEPSA = Column(DECIMAL(20, 6), doc="每股综合收益1")
    COMPREHENSIVEEPSTTMA = Column(DECIMAL(20, 6), doc="每股综合收益TTM1")
    COMPREHENSIVEEPSB = Column(DECIMAL(20, 6), doc="每股综合收益2")
    COMPREHENSIVEEPSTTMB = Column(DECIMAL(20, 6), doc="每股综合收益TTM2")
    PARENTEPSA = Column(DECIMAL(20, 6), doc="归属于母公司每股收益")
    PARENTEPSTTMA = Column(DECIMAL(20, 6), doc="归属于母公司每股收益TTM")
    PARENTEPSB = Column(DECIMAL(20, 6), doc="归属于母公司每股综合收益")
    PARENTEPSTTMB = Column(DECIMAL(20, 6), doc="归属于公司每股综合收益TTM")
    TOTALREVENUEPERSHARE = Column(DECIMAL(20, 6), doc="每股营业总收入")
    TOTALREVENUEPERSHARETTM = Column(DECIMAL(20, 6), doc="每股营业总收入TTM")
    REVENUEPERSHARE = Column(DECIMAL(20, 6), doc="每股营业收入")
    REVENUEPERSHARETTM = Column(DECIMAL(20, 6), doc="每股营业收入TTM")
    EBITPERSHARE = Column(DECIMAL(20, 6), doc="息税前每股收益")
    EBITPERSHARETTM = Column(DECIMAL(20, 6), doc="息税前每股收益TTM")
    EBITDAPERSHARE = Column(DECIMAL(20, 6), doc="息税折旧摊销前每股收益")
    EBITDAPERSHARETTM = Column(DECIMAL(20, 6), doc="息税折旧摊销前每股收益TTM")
    OPERATINGPROFITPERSHARE = Column(DECIMAL(20, 6), doc="每股营业利润")
    OPERATINGPROFITPERSHARETTM = Column(DECIMAL(20, 6), doc="每股营业利润TTM")
    NAV = Column(DECIMAL(20, 6), doc="每股净资产")
    TANGIBLEASSETPERSHARE = Column(DECIMAL(20, 6), doc="每股有形资产")
    LIABILITYPERSHARE = Column(DECIMAL(20, 6), doc="每股负债")
    CAPITALSURPLUSPERSHARE = Column(DECIMAL(20, 6), doc="每股资本公积")
    SURPLUSRESERVEPERSHARE = Column(DECIMAL(20, 6), doc="每股盈余公积")
    UNDISTRIBUTEDPROFITPERSHARE = Column(DECIMAL(20, 6), doc="每股未分配利润")
    RETAINEDEARNINGPERSHARE = Column(DECIMAL(20, 6), doc="每股留存收益")
    PARENTNAV = Column(DECIMAL(20, 6), doc="归属于母公司每股净资产")
    OPERATINGNCFPERSHARE = Column(DECIMAL(20, 6), doc="每股经营活动产生的现金流量净额")
    OPERATINGNCFPERSHARETTM = Column(DECIMAL(20, 6), doc="每股经营活动产生的现金流量净额TTM")
    INVESTINGNCFPERSHARE = Column(DECIMAL(20, 6), doc="每股投资活动现金净流量")
    INVESTINGNCFPERSHARETTM = Column(DECIMAL(20, 6), doc="每股投资活动现金净流量TTM")
    FINANCINGNCFPERSHARE = Column(DECIMAL(20, 6), doc="每股筹资活动现金净流量")
    FINANCINGNCFPERSHARETTM = Column(DECIMAL(20, 6), doc="每股筹资活动现金净流量TTM")
    COMPANYNCFPERSHAREA = Column(DECIMAL(20, 6), doc="每股企业自由现金流量")
    COMPANYNCFPERSHARETTMA = Column(DECIMAL(20, 6), doc="每股企业自由现金流量TTM")
    EQUITYNCFPERSHAREA = Column(DECIMAL(20, 6), doc="每股股东自由现金流量")
    EQUITYNCFPERSHARETTMA = Column(DECIMAL(20, 6), doc="每股股东自由现金流量TTM")
    DAPERSHARE = Column(DECIMAL(20, 6), doc="每股折旧和摊销")
    DAPERSHARETTM = Column(DECIMAL(20, 6), doc="每股折旧和摊销TTM")
    COMPANYNCFPERSHARE = Column(DECIMAL(20, 6), doc="每股企业自由现金流（原有）")
    EQUITYNCFPERSHARE = Column(DECIMAL(20, 6), doc="每股股权自由现金流（原有）")
    CASHINCREASEPERSHAREA = Column(DECIMAL(20, 6), doc="每股现金净流量1")
    CASHINCREASEPERSHARETTMA = Column(DECIMAL(20, 6), doc="每股现金净流量TTM1")
    CASHINCREASEPERSHAREB = Column(DECIMAL(20, 6), doc="每股现金净流量2")
    CASHINCREASEPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股现金净流量TTM2")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    PARENTEPSC = Column(DECIMAL(20, 6), doc="归属于母公司每股收益2")
    PARENTEPSTTMC = Column(DECIMAL(20, 6), doc="归属于母公司每股收益TTM2")
    PARENTEPSD = Column(DECIMAL(20, 6), doc="归属于母公司每股综合收益2")
    PARENTEPSTTMD = Column(DECIMAL(20, 6), doc="归属于公司每股综合收益TTM2")
    TOTALREVENUEPERSHAREB = Column(DECIMAL(20, 6), doc="每股营业总收入2")
    TOTALREVENUEPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股营业总收入TTM2")
    REVENUEPERSHAREB = Column(DECIMAL(20, 6), doc="每股营业收入2")
    REVENUEPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股营业收入TTM2")
    EBITPERSHAREB = Column(DECIMAL(20, 6), doc="息税前每股收益2")
    EBITPERSHARETTMB = Column(DECIMAL(20, 6), doc="息税前每股收益TTM2")
    EBITDAPERSHAREB = Column(DECIMAL(20, 6), doc="息税折旧摊销前每股收益2")
    EBITDAPERSHARETTMB = Column(DECIMAL(20, 6), doc="息税折旧摊销前每股收益TTM2")
    OPERATINGPROFITPERSHAREB = Column(DECIMAL(20, 6), doc="每股营业利润2")
    OPERATINGPROFITPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股营业利润TTM2")
    NAVB = Column(DECIMAL(20, 6), doc="每股净资产2")
    TANGIBLEASSETPERSHAREB = Column(DECIMAL(20, 6), doc="每股有形资产2")
    LIABILITYPERSHAREB = Column(DECIMAL(20, 6), doc="每股负债2")
    CAPITALSURPLUSPERSHAREB = Column(DECIMAL(20, 6), doc="每股资本公积2")
    SURPLUSRESERVEPERSHAREB = Column(DECIMAL(20, 6), doc="每股盈余公积2")
    UNDISTRIBUTEDPROFITPERSHAREB = Column(DECIMAL(20, 6), doc="每股未分配利润2")
    RETAINEDEARNINGPERSHAREB = Column(DECIMAL(20, 6), doc="每股留存收益2")
    PARENTNAVB = Column(DECIMAL(20, 6), doc="归属于母公司每股净资产2")
    OPERATINGNCFPERSHAREB = Column(DECIMAL(20, 6), doc="每股经营活动产生的现金流量净额2")
    OPERATINGNCFPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股经营活动产生的现金流量净额TTM2")
    INVESTINGNCFPERSHAREB = Column(DECIMAL(20, 6), doc="每股投资活动现金净流量2")
    INVESTINGNCFPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股投资活动现金净流量TTM2")
    FINANCINGNCFPERSHAREB = Column(DECIMAL(20, 6), doc="每股筹资活动现金净流量2")
    FINANCINGNCFPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股筹资活动现金净流量TTM2")
    COMPANYNCFPERSHAREB = Column(DECIMAL(20, 6), doc="每股企业自由现金流量2")
    COMPANYNCFPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股企业自由现金流量TTM2")
    EQUITYNCFPERSHAREB = Column(DECIMAL(20, 6), doc="每股股东自由现金流量2")
    EQUITYNCFPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股股东自由现金流量TTM2")
    DAPERSHAREB = Column(DECIMAL(20, 6), doc="每股折旧和摊销2")
    DAPERSHARETTMB = Column(DECIMAL(20, 6), doc="每股折旧和摊销TTM2")
    COMPANYNCFPERSHAREC = Column(DECIMAL(20, 6), doc="每股企业自由现金流量3")
    EQUITYNCFPERSHAREC = Column(DECIMAL(20, 6), doc="每股股权自由现金流量3")


class stk_fin_quitrafin(Base):

    __tablename__ = 'stk_fin_quitrafin'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="业绩报告期")
    DECLAREDATE = Column(DateTime, doc="业绩快报披露日")
    CHANGENUMBER = Column(SMALLINT, doc="业绩快报发布次数")
    GROSSREVENUE = Column(DECIMAL(20, 2), doc="营业总收入")
    GROSSREVENUELAST = Column(DECIMAL(20, 2), doc="去年同期营业总收入")
    GROSSREVENUECHANGERATIO = Column(DECIMAL(20, 2), doc="营业总收入变动幅度%")
    OPERATEPROFIT = Column(DECIMAL(20, 2), doc="营业利润")
    OPERATEPROFITLAST = Column(DECIMAL(20, 2), doc="去年同期营业利润")
    OPERATEPROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="营业利润变动幅度%")
    TOTALPROFIT = Column(DECIMAL(20, 2), doc="利润总额")
    TOTALPROFITLAST = Column(DECIMAL(20, 2), doc="去年同期利润总额")
    TOTALPROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="利润总额变动幅度%")
    PROFITPARENT = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润")
    PROFITPARENTLAST = Column(DECIMAL(20, 2), doc="去年同期归属于母公司所有者的净利润")
    PROFITPARENTCHANGERATIO = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润变动幅度%")
    PROFIT = Column(DECIMAL(20, 2), doc="净利润")
    PROFITLAST = Column(DECIMAL(20, 2), doc="去年同期净利润")
    PROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="净利润变动幅度%")
    EPS = Column(DECIMAL(20, 4), doc="每股收益")
    EPSLAST = Column(DECIMAL(20, 4), doc="去年同期每股收益")
    EPSCHANGERATIO = Column(DECIMAL(20, 4), doc="每股收益变动幅度%")
    ROE = Column(DECIMAL(20, 4), doc="净资产收益率")
    ROELAST = Column(DECIMAL(20, 4), doc="去年同期净资产收益率")
    ROECHANGERATIO = Column(DECIMAL(20, 4), doc="净资产收益率变动幅度%")
    ASSET = Column(DECIMAL(20, 2), doc="总资产")
    STARTDATEASSET = Column(DECIMAL(20, 2), doc="本报告期期初总资产")
    ASSETCHANGERATIO = Column(DECIMAL(20, 2), doc="总资产变动幅度%")
    EQUITYPARENT = Column(DECIMAL(20, 2), doc="归属于母公司所有者权益")
    STARTDATEEQUITYPARENT = Column(DECIMAL(20, 2), doc="本报告期期初归属于母公司所有者权益")
    EQUITYPARENTCHANGERATIO = Column(DECIMAL(20, 2), doc="归属于母公司所有者权益变动幅度%")
    EQUITY = Column(DECIMAL(20, 2), doc="所有者权益")
    STARTDATEEQUITY = Column(DECIMAL(20, 2), doc="本报告期期初所有者权益")
    EQUITYCHANGERATIO = Column(DECIMAL(20, 2), doc="所有者权益变动幅度%")
    NAVPSPARENT = Column(DECIMAL(20, 4), doc="归属于母公司每股净资产")
    STARTDATENAVPSPARENT = Column(DECIMAL(20, 4), doc="本报告期期初归属于母公司每股净资产")
    NAVPSPARENTCHANGERATIO = Column(DECIMAL(20, 4), doc="归属于母公司每股净资产变动幅度%")
    NAVPS = Column(DECIMAL(20, 4), doc="每股净资产")
    STARTDATENAVPS = Column(DECIMAL(20, 4), doc="本报告期期初每股净资产")
    NAVPSCHANGERATIO = Column(DECIMAL(20, 4), doc="每股净资产变动幅度%")
    MODIFYREASON = Column(LONGTEXT, doc="业绩修正原因")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_quitrafinnew(Base):

    __tablename__ = 'stk_fin_quitrafinnew'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, primary_key=True, doc="业绩报告期")
    DECLAREDATE = Column(DateTime, doc="业绩快报披露日")
    GROSSREVENUE = Column(DECIMAL(20, 2), doc="营业总收入")
    GROSSREVENUELAST = Column(DECIMAL(20, 2), doc="去年同期营业总收入")
    GROSSREVENUECHANGERATIO = Column(DECIMAL(20, 2), doc="营业总收入变动幅度%")
    OPERATEPROFIT = Column(DECIMAL(20, 2), doc="营业利润")
    OPERATEPROFITLAST = Column(DECIMAL(20, 2), doc="去年同期营业利润")
    OPERATEPROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="营业利润变动幅度%")
    TOTALPROFIT = Column(DECIMAL(20, 2), doc="利润总额")
    TOTALPROFITLAST = Column(DECIMAL(20, 2), doc="去年同期利润总额")
    TOTALPROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="利润总额变动幅度%")
    PROFITPARENT = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润")
    PROFITPARENTLAST = Column(DECIMAL(20, 2), doc="去年同期归属于母公司所有者的净利润")
    PROFITPARENTCHANGERATIO = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润变动幅度%")
    PROFIT = Column(DECIMAL(20, 2), doc="净利润")
    PROFITLAST = Column(DECIMAL(20, 2), doc="去年同期净利润")
    PROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="净利润变动幅度%")
    EPS = Column(DECIMAL(20, 4), doc="每股收益")
    EPSLAST = Column(DECIMAL(20, 4), doc="去年同期每股收益")
    EPSCHANGERATIO = Column(DECIMAL(20, 4), doc="每股收益变动幅度%")
    ROE = Column(DECIMAL(20, 4), doc="净资产收益率")
    ROELAST = Column(DECIMAL(20, 4), doc="去年同期净资产收益率")
    ROECHANGERATIO = Column(DECIMAL(20, 4), doc="净资产收益率变动幅度%")
    ASSET = Column(DECIMAL(20, 2), doc="总资产")
    STARTDATEASSET = Column(DECIMAL(20, 2), doc="本报告期期初总资产")
    ASSETCHANGERATIO = Column(DECIMAL(20, 2), doc="总资产变动幅度%")
    EQUITYPARENT = Column(DECIMAL(20, 2), doc="归属于母公司所有者权益")
    STARTDATEEQUITYPARENT = Column(DECIMAL(20, 2), doc="本报告期期初归属于母公司所有者权益")
    EQUITYPARENTCHANGERATIO = Column(DECIMAL(20, 2), doc="归属于母公司所有者权益变动幅度%")
    EQUITY = Column(DECIMAL(20, 2), doc="所有者权益")
    STARTDATEEQUITY = Column(DECIMAL(20, 2), doc="本报告期期初所有者权益")
    EQUITYCHANGERATIO = Column(DECIMAL(20, 2), doc="所有者权益变动幅度%")
    NAVPSPARENT = Column(DECIMAL(20, 4), doc="归属于母公司每股净资产")
    STARTDATENAVPSPARENT = Column(DECIMAL(20, 4), doc="本报告期期初归属于母公司每股净资产")
    NAVPSPARENTCHANGERATIO = Column(DECIMAL(20, 4), doc="归属于母公司每股净资产变动幅度%")
    NAVPS = Column(DECIMAL(20, 4), doc="每股净资产")
    STARTDATENAVPS = Column(DECIMAL(20, 4), doc="本报告期期初每股净资产")
    NAVPSCHANGERATIO = Column(DECIMAL(20, 4), doc="每股净资产变动幅度%")
    MODIFYREASON = Column(LONGTEXT, doc="业绩修正原因")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_fin_quitrasimfin(Base):

    __tablename__ = 'stk_fin_quitrasimfin'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID ")
    SYMBOL = Column(String(12), doc="股票代码 ")
    ENDDATE = Column(DateTime, doc="业绩报告期")
    DECLAREDATE = Column(DateTime, doc="业绩快报披露日")
    GROSSREVENUE = Column(DECIMAL(20, 2), doc="营业总收入")
    GROSSREVENUELAST = Column(DECIMAL(20, 2), doc="去年同期营业总收入")
    GROSSREVENUECHANGERATIO = Column(DECIMAL(20, 2), doc="营业总收入变动幅度%")
    OPERATEPROFIT = Column(DECIMAL(20, 2), doc="营业利润")
    OPERATEPROFITLAST = Column(DECIMAL(20, 2), doc="去年同期营业利润")
    OPERATEPROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="营业利润变动幅度%")
    TOTALPROFIT = Column(DECIMAL(20, 2), doc="利润总额")
    TOTALPROFITLAST = Column(DECIMAL(20, 2), doc="去年同期利润总额")
    TOTALPROFITCHANGERATIO = Column(DECIMAL(20, 2), doc="利润总额变动幅度%")
    PROFITPARENT = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润")
    PROFITPARENTLAST = Column(DECIMAL(20, 2), doc="去年同期归属于母公司所有者的净利润")
    PROFITPARENTCHANGERATIO = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润变动幅度%")
    EPS = Column(DECIMAL(20, 4), doc="每股收益")
    EPSLAST = Column(DECIMAL(20, 4), doc="去年同期每股收益")
    ROE = Column(DECIMAL(20, 4), doc="净资产收益率")
    ROELAST = Column(DECIMAL(20, 4), doc="去年同期净资产收益率")
    ASSET = Column(DECIMAL(20, 2), doc="总资产")
    STARTDATEASSET = Column(DECIMAL(20, 2), doc="本报告期期初总资产")
    ASSETCHANGERATIO = Column(DECIMAL(20, 2), doc="总资产变动幅度%")
    EQUITY = Column(DECIMAL(20, 2), doc="所有者权益")
    STARTDATEEQUITY = Column(DECIMAL(20, 2), doc="本报告期期初所有者权益")
    EQUITYCHANGERATIO = Column(DECIMAL(20, 2), doc="所有者权益变动幅度%")
    ABSTRACT = Column(LONGTEXT, doc="业绩简要说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_relativevalue(Base):

    __tablename__ = 'stk_fin_relativevalue'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="股票代码")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    PE1A = Column(DECIMAL(20, 6), doc="市盈率1")
    PE1B = Column(DECIMAL(20, 6), doc="市盈率2")
    PE1TTM = Column(DECIMAL(20, 6), doc="市盈率TTM")
    PSA = Column(DECIMAL(20, 6), doc="市销率1")
    PSB = Column(DECIMAL(20, 6), doc="市销率2")
    PSTTM = Column(DECIMAL(20, 6), doc="市销率TTM")
    PCFA = Column(DECIMAL(20, 6), doc="市现率1")
    PCFB = Column(DECIMAL(20, 6), doc="市现率2")
    PCFTTM = Column(DECIMAL(20, 6), doc="市现率TTM")
    PBVA = Column(DECIMAL(20, 6), doc="市净率")
    PRICETOTANGIBLEASSET = Column(DECIMAL(20, 6), doc="市值有形资产比")
    PE2A = Column(DECIMAL(20, 6), doc="市盈率母公司1")
    PE2B = Column(DECIMAL(20, 6), doc="市盈率母公司2")
    PE2TTM = Column(DECIMAL(20, 6), doc="市盈率母公司TTM")
    PBVB = Column(DECIMAL(20, 6), doc="市净率母公司")
    MARKETVALUEA = Column(DECIMAL(20, 6), doc="市值A")
    MARKETVALUEB = Column(DECIMAL(20, 6), doc="市值B")
    TOBINQA = Column(DECIMAL(20, 6), doc="托宾Q值A")
    TOBINQB = Column(DECIMAL(20, 6), doc="托宾Q值B")
    TOBINQC = Column(DECIMAL(20, 6), doc="托宾Q值C")
    TOBINQD = Column(DECIMAL(20, 6), doc="托宾Q值D")
    NETASSETTOMARKETVALUEA = Column(DECIMAL(20, 6), doc="账面市值比A")
    NETASSETTOMARKETVALUEB = Column(DECIMAL(20, 6), doc="账面市值比B")
    PRICETODIVIDEND = Column(DECIMAL(20, 6), doc="本利比")
    RETURNA = Column(DECIMAL(20, 6), doc="普通股获利率A")
    RETURNB = Column(DECIMAL(20, 6), doc="普通股获利率B")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    EVTOEBITDA = Column(DECIMAL(20, 6), doc="企业价值倍数")
    EVTOEBITDATTM = Column(DECIMAL(20, 6), doc="企业价值倍数TTM")
    PE1C = Column(DECIMAL(20, 6), doc="市盈率3")
    PE1D = Column(DECIMAL(20, 6), doc="市盈率4")
    PE1TTMB = Column(DECIMAL(20, 6), doc="市盈率TTM2")
    PSC = Column(DECIMAL(20, 6), doc="市销率3")
    PSD = Column(DECIMAL(20, 6), doc="市销率4")
    PSTTMB = Column(DECIMAL(20, 6), doc="市销率TTM2")
    PCFC = Column(DECIMAL(20, 6), doc="市现率3")
    PCFD = Column(DECIMAL(20, 6), doc="市现率4")
    PCFTTMB = Column(DECIMAL(20, 6), doc="市现率TTM2")
    PBVC = Column(DECIMAL(20, 6), doc="市净率2")
    PRICETOTANGIBLEASSETB = Column(DECIMAL(20, 6), doc="市值有形资产比2")
    PE2C = Column(DECIMAL(20, 6), doc="市盈率母公司3")
    PE2D = Column(DECIMAL(20, 6), doc="市盈率母公司4")
    PE2TTMB = Column(DECIMAL(20, 6), doc="市盈率母公司TTM2")
    PBVD = Column(DECIMAL(20, 6), doc="市净率母公司2")
    MARKETVALUEC = Column(DECIMAL(20, 6), doc="市值C")
    TOBINQE = Column(DECIMAL(20, 6), doc="托宾Q值E")
    TOBINQF = Column(DECIMAL(20, 6), doc="托宾Q值F")
    NETASSETTOMARKETVALUEC = Column(DECIMAL(20, 6), doc="账面市值比C")


class stk_fin_relforcdate(Base):

    __tablename__ = 'stk_fin_relforcdate'

    LISTEDCOID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ACCOUPERI = Column(DateTime, primary_key=True, doc="会计期间")
    EVENTID = Column(String(40), doc="事件ID")
    FIRRELFORCDATE = Column(DateTime, doc="首次预约披露日期")
    FIRCHGRELFORCDATE = Column(DateTime, doc="第一次变更后的预约披露日期")
    SECCHGRELFORCDATE = Column(DateTime, doc="第二次变更后的预约披露日期")
    THRCHGRELFORCDATE = Column(DateTime, doc="第三次变更后的预约披露日期")
    ACTRELDATE = Column(DateTime, doc="实际批露日期")
    ACTRELWEEKDAY = Column(String(2), doc="实际批露星期")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_fin_risk(Base):

    __tablename__ = 'stk_fin_risk'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    STARTDATE = Column(DateTime, doc="开始日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATETYPECODE = Column(String(12), doc="报表类型编码")
    DFL = Column(DECIMAL(20, 6), doc="财务杠杆")
    DOL = Column(DECIMAL(20, 6), doc="经营杠杆")
    DTL = Column(DECIMAL(20, 6), doc="综合杠杆")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_fin_simforecfin(Base):

    __tablename__ = 'stk_fin_simforecfin'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="业绩报告期")
    DECLAREDATE = Column(DateTime, doc="预告日期")
    FIRSTDECLAREDATE = Column(DateTime, doc="首次预告日期")
    CHANGENUMBER = Column(SMALLINT, doc="预告次数")
    PERFORMANCETYPE = Column(String(40), doc="业绩预告类型")
    PROFITCHANGERATIOCEILING = Column(DECIMAL(20, 2), doc="预告净利润最大变动幅度")
    ABSTRACT = Column(LONGTEXT, doc="业绩预告摘要")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_forecast(Base):

    __tablename__ = 'stk_forecast'

    REPORTID = Column(DECIMAL(20, 0), doc="研究报告ID")
    SYMBOL = Column(String(20), doc="股票代码")
    REPORTDATE = Column(DateTime, doc="报告日")
    ANALYST = Column(String(200), doc="分析师")
    INSTITUTIONNAME = Column(String(200), doc="研究机构")
    FORECASTYEAR = Column(DateTime, doc="预测年度")
    FEPS = Column(DECIMAL(20, 4), doc="每股收益")
    FPE = Column(DECIMAL(24, 6), doc="市盈率")
    FNETPRO = Column(DECIMAL(20, 2), doc="净利润")
    FEBIT = Column(DECIMAL(20, 2), doc="息税前收入")
    FEBITDA = Column(DECIMAL(20, 2), doc="扣除息、税、折旧及摊销前收入")
    FTURNOVER = Column(DECIMAL(20, 2), doc="主营业务收入")
    FCFPS = Column(DECIMAL(20, 2), doc="每股经营现金流")
    FBM = Column(DECIMAL(12, 4), doc="账面市值比")
    FBPS = Column(DECIMAL(12, 2), doc="每股净资产")
    FROA = Column(DECIMAL(12, 4), doc="总资产收益率")
    FROE = Column(DECIMAL(12, 4), doc="净资产收益率")
    FPB = Column(DECIMAL(24, 6), doc="市净率")
    FTOTALASSETSTURNOVER = Column(DECIMAL(12, 4), doc="总资产周转率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_guarantee_main(Base):

    __tablename__ = 'stk_guarantee_main'

    GUARANTEEID = Column(DECIMAL(20, 0), doc="担保事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    GUARANTEEINSTITUTIONID = Column(String(600), doc="被担保人机构ID")
    GUARANTEENAME = Column(String(1000), doc="被担保人名称")
    RELATETOGUARANTEE = Column(String(1000), doc="被担保人与上市公司关系")
    RELATETOGUARANTEEID = Column(String(400), doc="被担保人与上市公司关系ID")
    ISLISTINGCORPORATION = Column(String(4), doc="被担保人是否上市")
    CREDITORTYPEID = Column(String(200), doc="债权人类型ID")
    CREDITORTYPE = Column(String(200), doc="债权人类型")
    CREDITORID = Column(String(600), doc="债权人ID")
    CREDITORNAME = Column(String(1000), doc="债权人名称")
    CREDITORTOGUARANTEE = Column(String(1000), doc="债权人与被担保人关系")
    CREDITORTOGUARANTEEID = Column(String(400), doc="债权人与被担保人关系ID")
    RELATETOCREDITOR = Column(String(1000), doc="债权人与上市公司关系")
    RELATETOCREDITORID = Column(String(400), doc="债权人与上市公司关系ID")
    LOANWAY = Column(String(20), doc="借款形式")
    LOANWAYID = Column(String(20), doc="借款形式ID")
    LOANAMOUNT = Column(DECIMAL(20, 6), doc="借款金额")
    SIGNDATE = Column(DateTime, doc="担保协议签署日")
    STARTDATE = Column(DateTime, doc="担保起始日")
    ENDDATE = Column(DateTime, doc="担保终止日")
    GUARANTEETERM = Column(DECIMAL(10, 2), doc="担保期限")
    APPROVALSTATUS = Column(String(100), doc="审批状态")
    APPROVALSTATUSID = Column(String(100), doc="审批状态ID")
    APPROVALDATE = Column(DateTime, doc="审批日期")
    GUARANTEETYPE = Column(String(100), doc="担保方式")
    GUARANTEETYPEID = Column(String(100), doc="担保方式ID")
    GUARANTEEAMOUNT = Column(DECIMAL(20, 6), doc="担保金额")
    TERMDESCRIPTION = Column(String(400), doc="协议期限描述")
    PLEDGENAME = Column(String(1000), doc="质押物名称")
    PLEDGEUSEFOR = Column(String(1000), doc="质押物用途")
    BOOKVALUE = Column(DECIMAL(20, 6), doc="质押物账面价值")
    MARKETVALUE = Column(DECIMAL(20, 6), doc="质押物公允价值")
    PROPORTION = Column(DECIMAL(12, 4), doc="上市公司担保占被担保金额比例")
    GUARANTEENATURE = Column(String(200), doc="担保性质")
    GUARANTEENATUREID = Column(String(20), doc="担保性质ID")
    ISSTRAIGHTGUARANTEE = Column(String(20), doc="是否直接担保")
    SIGNSTATUS = Column(String(20), doc="签约状态")
    SIGNSTATUSID = Column(String(20), doc="签约状态ID")
    ISFULFIL = Column(String(20), doc="被担保人履约情况")
    ISIMPLEMENTATION = Column(String(20), doc="上市公司担保实施情况")
    ISIMPLEMENTATIONID = Column(String(20), doc="上市公司担保实施情况ID")
    ISILLEGAL = Column(String(2), doc="担保事项是否违规")
    ILLEGALEXPLAIN = Column(String(1000), doc="违规情况说明")
    ACCUMULATIVETOTAL = Column(DECIMAL(20, 6), doc="累计担保总额")
    TOTALTONETASSETS = Column(DECIMAL(18, 4), doc="上市公司累计担保占净资产比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    SOURCE = Column(String(12), doc="数据来源")
    RANK = Column(SMALLINT, doc="序号")


class stk_guarantee_son(Base):

    __tablename__ = 'stk_guarantee_son'

    GUARANTEEID = Column(DECIMAL(20, 0), doc="担保事件ID")
    GUARANTORNAME = Column(String(1000), doc="担保人名称")
    GUARANTORID = Column(String(600), doc="担保人ID")
    GUARANTORTYPEID = Column(String(200), doc="担保人类型ID")
    GUARANTORTYPE = Column(String(200), doc="担保人类型")
    GUARANTORTOGUARANTEE = Column(String(1000), doc="担保人与被担保人关系")
    GUARANTORTOGUARANTEEID = Column(String(400), doc="担保人与被担保人关系ID")
    RELATETOGUARANTOR = Column(String(1000), doc="担保人与上市公司关系")
    RELATETOGUARANTORID = Column(String(400), doc="担保人与上市公司关系ID")
    GUARANTEETYPE = Column(String(100), doc="担保方式")
    GUARANTEETYPEID = Column(String(100), doc="担保方式ID")
    GUARANTEEAMOUNT = Column(DECIMAL(20, 6), doc="担保金额")
    GUARANTEEAMOUNTTOTOTAL = Column(DECIMAL(12, 4), doc="占担保总额比例")
    BOOKVALUE = Column(DECIMAL(20, 6), doc="质押物账面价值")
    MARKETVALUE = Column(DECIMAL(20, 6), doc="质押物公允价值")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    RANK = Column(SMALLINT, doc="序号")


class stk_guarantee_statistics(Base):

    __tablename__ = 'stk_guarantee_statistics'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    REPORTSOURCE = Column(String(12), doc="公告来源")
    CURRENCYCODE = Column(String(12), doc="币种编码")
    GUARANTEEQUOTA = Column(DECIMAL(20, 6), doc="担保额度")
    QUOTATOOUTSIDE = Column(DECIMAL(20, 6), doc="对外担保额度（不含子公司）")
    QUOTATOSUBSIDIARY = Column(DECIMAL(20, 6), doc="对子公司担保额度")
    ACTUALGUARANTEEAMOUNT = Column(DECIMAL(20, 6), doc="担保发生额")
    ACTUALGUARANTEETOOUTSIDE = Column(DECIMAL(20, 6), doc="对外担保发生额（不含子公司）")
    ACTUALGUARANTEETOSUBSIDIARY = Column(DECIMAL(20, 6), doc="对子公司的担保发生额")
    ACCUMULATIVETOTALAMOUNT = Column(DECIMAL(20, 6), doc="担保总额")
    ACCUMULATIVETOOUTSIDE = Column(DECIMAL(20, 6), doc="对外担保余额（不含子公司）")
    ACCUMULATIVETOSUBSIDIARY = Column(DECIMAL(20, 6), doc="对子公司担保余额")
    GUARANTEETOTALTONETASSETS = Column(DECIMAL(18, 4), doc="担保总额占净资产的比例")
    GUARANTEETOSHAREHOLDER = Column(DECIMAL(20, 6), doc="为股东、实际控制人及其关联方提供担保的金额")
    GUARANTEETOHIGHDEBTRATIOCO = Column(DECIMAL(20, 6), doc="直接或间接为资产负债率超过 70％的被担保对象提供的债务担保金额")
    EXCEED50NETASSETSAMOUNT = Column(DECIMAL(20, 6), doc="担保总额超过净资产50％部分的金额")
    OVERDUEAMOUNT = Column(DECIMAL(20, 6), doc="逾期担保数额累计")
    ILLEGALAMOUNT = Column(DECIMAL(20, 6), doc="违规担保数额累计")
    LIABILITYEXPLAIN = Column(String(4000), doc="未到期担保可能承担连带清偿责任说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_controlchart(Base):

    __tablename__ = 'stk_holder_controlchart'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    ENDDATE = Column(DateTime, primary_key=True, doc="截止日期")
    CONTROLLINGRELATIONCHART = Column(LargeBinary(16777216), doc="控股关系图")
    FILETTYE = Column(String(20), doc="文件类型")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_holder_controller(Base):

    __tablename__ = 'stk_holder_controller'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    ENDDATE = Column(DateTime, doc="截止日期")
    JUDGMENTSTANDARD = Column(String(2), doc="判断标准")
    DIRECTCONTROLLER = Column(String(400), doc="直接控股股东名称")
    DIRECTCONTROLLERNATUREID = Column(String(60), doc="直接控股股东股份性质编码")
    DIRECTCONTROLLERNATURE = Column(String(100), doc="直接控股股东股份性质")
    SHAREHOLDINGRATIO = Column(DECIMAL(20, 4), doc="直接控股股东持股比例")
    SHARES = Column(DECIMAL(20, 2), doc="直接控股股东持股数量")
    ACTUALCONTROLLER = Column(String(240), doc="实际控制人名称")
    ACTUALCONTROLLERNATUREID = Column(String(200), doc="实际控制人性质编码")
    ACTUALCONTROLLERNATURE = Column(String(400), doc="实际控制人性质")
    ACTUALCONTROLLERSHARESNATUREID = Column(String(60), doc="实际控制人股份性质编码")
    ACTUALCONTROLLERSHARESNATURE = Column(String(100), doc="实际控制人股份性质")
    ACTUALCONTROLLERBACKGROUND = Column(String(4000), doc="实际控制人背景")
    OWNERSHIPRATIO = Column(DECIMAL(20, 4), doc="实际控制人拥有上市公司所有权比例")
    CONTROLRATIO = Column(DECIMAL(20, 4), doc="实际控制人拥有上市公司控制权比例")
    SEPARATIONDEGREE = Column(DECIMAL(20, 4), doc="两权分离度")
    COMMENTS = Column(LONGTEXT, doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    SHAREHOLDERID = Column(String(200), doc="股东ID")


class stk_holder_detail(Base):

    __tablename__ = 'stk_holder_detail'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(10), doc="股票代码")
    ENDDATE = Column(DateTime, doc="截止日期")
    SYSTEMATICSID = Column(String(12), doc="机构分类编码")
    SYSTEMATICS = Column(String(100), doc="机构分类")
    SHAREHOLDERID = Column(DECIMAL(30, 0), doc="持股机构ID")
    FUNDID = Column(DECIMAL(30, 0), doc="股东ID对应的基金ID")
    SHAREHOLDERNAME = Column(String(600), doc="持股机构")
    CATEGORYCODE = Column(String(12), doc="股东类别编码")
    HOLDSHARES = Column(DECIMAL(20, 2), doc="持股数量")
    HOLDPROPORTION = Column(DECIMAL(20, 6), doc="持股比例")
    PRICE = Column(DECIMAL(10, 4), doc="股票价格")
    LASTENDDATE = Column(DateTime, doc="上期统计截止日期")
    LASTSHAREHOLDERID = Column(DECIMAL(30, 0), doc="上期持股机构ID")
    LASTHOLDSHARES = Column(DECIMAL(20, 2), doc="上期持股数量")
    LASTHOLDPROPORTION = Column(DECIMAL(20, 6), doc="上期持股比例")
    LASTPRICE = Column(DECIMAL(10, 4), doc="上期股票价格")
    RIGHTSRATIO = Column(DECIMAL(10, 6), doc="期间送转增配股比例")
    STATUS = Column(String(2), doc="增减维持标识")
    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    SOURCE = Column(String(2), doc="数据来源")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_equitynatureall(Base):

    __tablename__ = 'stk_holder_equitynatureall'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(300), doc="证券简称")
    SHORTNAME_EN = Column(String(600), doc="证券简称_en")
    REGISTERADDRESS = Column(String(1200), doc="注册地址")
    OFFICEADDRESS = Column(String(1200), doc="办公地址")
    ENDDATE = Column(DateTime, doc="截止日期")
    JUDGMENTSTANDARD = Column(String(1), doc="判断标准")
    LARGESTHOLDER = Column(String(1200), doc="第一大控股股东")
    LARGESTHOLDERRATE = Column(DECIMAL(20, 4), doc="第一大股东持股比率")
    LARGESTHOLDERNATURE = Column(String(600), doc="第一大股东股东性质")
    LARGESTCATEGORYID = Column(String(150), doc="第一大股东股东类别编码")
    LARGESTCATEGORY = Column(String(600), doc="第一大股东股东类别")
    LARGESTSHARESNATUREID = Column(String(150), doc="第一大股东拥有上市公司股份性质编码")
    LARGESTSHARESNATURE = Column(String(600), doc="第一大股东拥有上市公司股份性质")
    TOPTENHOLDERSRATE = Column(DECIMAL(20, 4), doc="前十大股东持股比例")
    CONTROLLER = Column(String(1800), doc="实际控制人名称")
    CONTROLLERNATUREID = Column(String(900), doc="实际控制人性质编码")
    CONTROLLERNATURE = Column(String(3000), doc="实际控制人性质")
    CONTROLLERSHARESNATUREID = Column(String(900), doc="实际控制人拥有上市公司股份性质编码")
    CONTROLLERSHARESNATURE = Column(String(3000), doc="实际控制人拥有上市公司股份性质")
    CONTROLPROPORTION = Column(DECIMAL(20, 4), doc="实际控制人拥有上市公司控制权比例")
    OWNERSHIPPROPORTION = Column(DECIMAL(20, 4), doc="实际控制人拥有上市公司所有权比例")
    CONTROLLERSEPERATION = Column(DECIMAL(20, 4), doc="两权分离率")
    EQUITYNATUREID = Column(String(30), doc="股权性质编码")
    EQUITYNATURE = Column(String(60), doc="股权性质")
    HIERARCHYID = Column(String(30), doc="层级判断编码")
    HIERARCHY = Column(String(120), doc="层级判断")
    FOUNDER = Column(String(1200), doc="创始人")
    ORIGINATOR = Column(String(4000), doc="发起人")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_incrordesr(Base):

    __tablename__ = 'stk_holder_incrordesr'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(10), doc="股票代码")
    ENDDATE = Column(DateTime, doc="截止日期")
    STATUS = Column(String(2), doc="增减维持标识")
    HOLDERNUMBER = Column(SMALLINT, doc="机构持股家数")
    SHARES = Column(DECIMAL(20, 2), doc="机构持股数量")
    PROPORTION = Column(DECIMAL(20, 6), doc="机构持股比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_number(Base):

    __tablename__ = 'stk_holder_number'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    SHAREHOLDERS = Column(DECIMAL(20, 0), doc="股东总数")
    ASHAREHOLDERS = Column(DECIMAL(20, 0), doc="A股股东户数")
    BSHAREHOLDERS = Column(DECIMAL(20, 0), doc="B股东户数")
    HSHAREHOLDERS = Column(DECIMAL(20, 0), doc="H股东户数")
    NONFLOATINGSHAREHOLDERS = Column(DECIMAL(20, 0), doc="未流通股东户数")
    FLOATINGSHAREHOLDERS = Column(DECIMAL(20, 0), doc="已流通股东户数")
    COMMENTS = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_pledge(Base):

    __tablename__ = 'stk_holder_pledge'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    SHAREHOLDERID = Column(DECIMAL(20, 0), doc="股东ID")
    FULLNAME = Column(String(200), doc="股东名称")
    PLEDGEFREEZINGCUSTODYNUMBER = Column(DECIMAL(20, 2), doc="质押、冻结或托管总数")
    PLEDGENUMBER = Column(DECIMAL(20, 2), doc="其中：质押数量")
    FREEZINGNUMBER = Column(DECIMAL(20, 2), doc="其中：冻结数量")
    CUSTODYNUMBER = Column(DECIMAL(20, 2), doc="其中：托管股份")
    COMMENTS = Column(LONGTEXT, doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_relation(Base):

    __tablename__ = 'stk_holder_relation'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    ENDDATE = Column(DateTime, doc="截止日期")
    RELATIONSHIPID = Column(String(40), doc="关系类型")
    RELATIONSHIP = Column(String(200))
    FULLNAME1 = Column(String(200), doc="关系人1名称")
    FULLNAME1ISSHAREHOLDER = Column(String(2), doc="关系人1是否该上市公司股东")
    FULLNAME2 = Column(String(200), doc="关系人2名称")
    FULLNAME2ISSHAREHOLDER = Column(String(2), doc="关系人2是否该上市公司股东")
    SHAREHOLDINGRATIO = Column(DECIMAL(20, 4), doc="持有比例")
    SPECIALEXPLANATION = Column(String(4000), doc="特殊说明")
    RELATIONDETAILED = Column(String(400), doc="关系详情")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_holder_systematics(Base):

    __tablename__ = 'stk_holder_systematics'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, primary_key=True, doc="截止日期")
    FUNDHOLDSHARES = Column(DECIMAL(20, 2), doc="基金持股数量")
    FUNDHOLDPROPORTION = Column(DECIMAL(10, 4), doc="基金持股比例")
    QFIIHOLDSHARES = Column(DECIMAL(20, 2), doc="合格境外投资者持股数量")
    QFIIHOLDPROPORTION = Column(DECIMAL(10, 4), doc="合格境外投资者持股比例")
    BROKERHOLDSHARES = Column(DECIMAL(20, 2), doc="券商持股数量")
    BROKERHOLDPROPORTION = Column(DECIMAL(10, 4), doc="券商持股比例")
    INSURANCEHOLDSHARES = Column(DECIMAL(20, 2), doc="保险持股数量")
    INSURANCEHOLDPROPORTION = Column(DECIMAL(10, 4), doc="保险持股比例")
    SECURITYFUNDHOLDSHARES = Column(DECIMAL(20, 2), doc="社保基金持股数量")
    SECURITYFUNDHOLDPROPORTION = Column(DECIMAL(10, 4), doc="社保基金持股比例")
    ENTRUSTHOLDSHARES = Column(DECIMAL(20, 2), doc="信托持股数量")
    ENTRUSTHOLDPROPORTION = Column(DECIMAL(10, 4), doc="信托持股比例")
    FINANCEHOLDSHARES = Column(DECIMAL(20, 2), doc="财务持股数量")
    FINANCEHOLDPROPORTION = Column(DECIMAL(10, 4), doc="财务持股比例")
    BANKHOLDSHARES = Column(DECIMAL(20, 2), doc="银行持股数量")
    BANKHOLDPROPORTION = Column(DECIMAL(10, 4), doc="银行持股比例")
    NONFINANCEHOLDSHARES = Column(DECIMAL(20, 2), doc="非金融类上市公司持股数量")
    NONFINANCEHOLDPROPORTION = Column(DECIMAL(10, 4), doc="非金融类上市公司持股比例")
    UPDATEID = Column(BIGINT, doc="数据ID")
    OTHERHOLDSHARES = Column(DECIMAL(20, 2), doc="其他机构持股数量")
    OTHERHOLDPROPORTION = Column(DECIMAL(10, 4), doc="其他机构持股比例")


class stk_holder_top10(Base):

    __tablename__ = 'stk_holder_top10'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    SHAREHOLDERID = Column(DECIMAL(20, 0), doc="股东ID")
    FULLNAME = Column(String(200), doc="股东名称")
    SHAREHOLDERTYPEID = Column(String(12), doc="股东类型编码")
    SHAREHOLDERTYPE = Column(String(100), doc="股东类型")
    SHARES = Column(DECIMAL(20, 2), doc="持股数量")
    CHANGEREASONID = Column(String(12), doc="变动原因编码")
    CHANGEREASON = Column(String(100), doc="变动原因")
    IFPLEDGEFREEZINGCUSTODY = Column(String(2), doc="股份是否质押、冻结或托管")
    PERCENTAGEHOLDING = Column(DECIMAL(20, 4), doc="持股比例")
    SHARESNATUREID = Column(String(60), doc="股份性质编码")
    SHARESNATURE = Column(String(100), doc="股份性质")
    RANK = Column(INTEGER, doc="持股排名")
    COMMENTS = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CHANGETYPE = Column(String(2), doc="变动方向")
    CHANGENUM = Column(DECIMAL(20, 4), doc="变动数量")
    CHANGEPERCENTAGE = Column(DECIMAL(20, 4), doc="变动比例")
    CHANGENUMPERCENTAGE = Column(DECIMAL(20, 4), doc="变动数量占总股本比例")
    CHANGESTARTDATE = Column(DateTime, doc="变动起始日期")
    SHAREHOLDERNATURE = Column(String(40), doc="股东性质")
    UNCRICULATIONSHARES = Column(DECIMAL(20, 2), doc="未流通股份数量")


class stk_holder_top10floating(Base):

    __tablename__ = 'stk_holder_top10floating'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="截止日期")
    SHAREHOLDERID = Column(DECIMAL(20, 0), doc="股东ID")
    FULLNAME = Column(String(600), doc="股东名称")
    SHAREHOLDERTYPEID = Column(String(12), doc="股东类型编码")
    SHAREHOLDERTYPE = Column(String(100), doc="股东类型")
    SHARES = Column(DECIMAL(20, 2), doc="持股数量")
    SHAREHOLDINGRATIO = Column(DECIMAL(20, 4), doc="持股比例")
    SHARESNATUREID = Column(String(60), doc="股份性质编码")
    SHARESNATURE = Column(String(100), doc="股份性质")
    RANK = Column(INTEGER, doc="持股排名")
    COMMENTS = Column(String(4000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CHANGETYPE = Column(String(2), doc="变动方向")
    CHANGENUM = Column(DECIMAL(20, 4), doc="变动数量")
    CHANGEPERCENTAGE = Column(DECIMAL(20, 4), doc="变动比例")
    CHANGENUMPERCENTAGE = Column(DECIMAL(20, 4), doc="变动数量占总股本比例")
    CHANGESTARTDATE = Column(DateTime, doc="变动起始日期")


class stk_indfi_basis(Base):

    __tablename__ = 'stk_indfi_basis'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    STATETYPECODE = Column(String(1), doc="期初/期末值标识")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    CASH = Column(DECIMAL(30, 6), doc="行业货币资金")
    TRADABLEASSET = Column(DECIMAL(30, 6), doc="行业交易性金融资产")
    DERIVATIVEASSET = Column(DECIMAL(30, 6), doc="行业衍生金融资产")
    INVESTMENT = Column(DECIMAL(30, 6), doc="行业短期投资净额")
    BILLRECEIVABLE = Column(DECIMAL(30, 6), doc="行业应收票据净额")
    NETRECEIVABLE = Column(DECIMAL(30, 6), doc="行业应收账款净额")
    NETINVENTORY = Column(DECIMAL(30, 6), doc="行业存货净额")
    TOTALCURRENTASSETS = Column(DECIMAL(30, 6), doc="行业流动资产合计")
    AVSFA = Column(DECIMAL(30, 6), doc="行业可供出售金融资产净额")
    HELDMATURITYINVESTMENT = Column(DECIMAL(30, 6), doc="行业持有至到期投资净额")
    NLEINVST = Column(DECIMAL(30, 6), doc="行业长期股权投资净额")
    NETFIXASSET = Column(DECIMAL(30, 6), doc="行业固定资产净额")
    INTANGIBLEASSETS = Column(DECIMAL(30, 6), doc="行业无形资产净额")
    NGDWL = Column(DECIMAL(30, 6), doc="行业商誉净额")
    TOTNCAST = Column(DECIMAL(30, 6), doc="行业非流动资产合计")
    TOTALASSETS = Column(DECIMAL(30, 6), doc="行业资产总计")
    SHORTTERMLOAN = Column(DECIMAL(30, 6), doc="行业短期借款")
    TRADABLEDEBT = Column(DECIMAL(30, 6), doc="行业交易性金融负债")
    DERFINANCIALLIABILITY = Column(DECIMAL(30, 6), doc="行业衍生金融负债")
    NOTESPAYABLE = Column(DECIMAL(30, 6), doc="行业应付票据")
    ACCOUNTSPAYABLE = Column(DECIMAL(30, 6), doc="行业应付账款")
    NCLDOY = Column(DECIMAL(30, 6), doc="行业一年内到期的非流动负债")
    TOTALCURRENTLIABILITIES = Column(DECIMAL(30, 6), doc="行业流动负债合计")
    LONGTERMLOANS = Column(DECIMAL(30, 6), doc="行业长期借款")
    LONGTERMLIABILITY = Column(DECIMAL(30, 6), doc="行业长期负债合计")
    TOTNCL = Column(DECIMAL(30, 6), doc="行业非流动负债合计")
    TOTALLIABILITIES = Column(DECIMAL(30, 6), doc="行业负债合计")
    PAIDINCAPITAL = Column(DECIMAL(30, 6), doc="行业实收资本")
    SURPLUSRESERVES = Column(DECIMAL(30, 6), doc="行业盈余公积")
    UNDISTRIBUTEDPROFITS = Column(DECIMAL(30, 6), doc="行业未分配利润")
    TOTALEQUITY = Column(DECIMAL(30, 6), doc="行业所有者权益合计")
    TOTALREVENUE = Column(DECIMAL(30, 6), doc="行业营业总收入")
    BUSINESSREVENUE = Column(DECIMAL(30, 6), doc="行业营业收入")
    TOTALOPERATINGCOST = Column(DECIMAL(30, 6), doc="行业营业总成本")
    OPERATINGCOST = Column(DECIMAL(30, 6), doc="行业营业成本")
    SELLINGEXPENSES = Column(DECIMAL(30, 6), doc="行业销售费用")
    MANAGEMENTEXPENSE = Column(DECIMAL(30, 6), doc="行业管理费用")
    FINANCEEXPENSEA = Column(DECIMAL(30, 6), doc="行业财务费用A")
    FAIRVALUEGAINS = Column(DECIMAL(30, 6), doc="行业公允价值变动收益")
    INCOMEINVESTMENT = Column(DECIMAL(30, 6), doc="行业投资收益")
    EXCHANGEGAINS = Column(DECIMAL(30, 6), doc="行业汇兑收益")
    OPERATINGPROFIT = Column(DECIMAL(30, 6), doc="行业营业利润")
    NONOPERATINGINCOME = Column(DECIMAL(30, 6), doc="行业营业外收入")
    NONOPERATINGEXPENSES = Column(DECIMAL(30, 6), doc="行业营业外支出")
    TOTALPROFIT = Column(DECIMAL(30, 6), doc="行业利润总额")
    INCOMETAX = Column(DECIMAL(30, 6), doc="行业所得税费用")
    NETPROFIT = Column(DECIMAL(30, 6), doc="行业净利润")
    OTHERCOMPREHENSIVEINCOME = Column(DECIMAL(30, 6), doc="行业其他综合收益")
    COMPREHENSIVEINCOME = Column(DECIMAL(30, 6), doc="行业综合收益总额")
    OPERATINGNETCASHFLOW = Column(DECIMAL(30, 6), doc="行业经营活动产生的现金流量净额")
    CASHEQUIVALENTCHANGE = Column(DECIMAL(30, 6), doc="行业现金及现金等价物净增加额")
    ENDCASHEQUIVALENT = Column(DECIMAL(30, 6), doc="行业期末现金及现金等价物余额")
    INVESTMENTINCOME = Column(DECIMAL(30, 6), doc="行业取得投资收益收到的现金")
    PAIDFORLONGTERMASSETS = Column(DECIMAL(30, 6), doc="行业购建固定资产、无形资产和其他长期资产支付的现金")
    DIVIDENDINTERESTPAID = Column(DECIMAL(30, 6), doc="行业分配股利、利润或偿付利息支付的现金")
    DEPRECIATION = Column(DECIMAL(30, 6), doc="行业固定资产折旧、油气资产折耗、生产性生物资产折旧")
    AMORINTA = Column(DECIMAL(30, 6), doc="行业无形资产摊销")
    AMORLPE = Column(DECIMAL(30, 6), doc="行业长期待摊费用摊销")
    FINANCEEXPENSEB = Column(DECIMAL(30, 6), doc="行业财务费用B")
    DEFERREDTAXASSETCHANGE = Column(DECIMAL(30, 6), doc="行业递延所得税资产减少")
    INCDEFFEREDTAXLIABILITY = Column(DECIMAL(30, 6), doc="行业递延所得税负债增加")
    DIVIDENDPERSHARE = Column(DECIMAL(30, 6), doc="行业每股派息税前")
    TOTALSHARES = Column(DECIMAL(30, 6), doc="行业最新股本/总股本")
    LONGTERMCAPITAL = Column(DECIMAL(30, 6), doc="行业长期资本额")
    TOTALTANGIBLEASSETS = Column(DECIMAL(30, 6), doc="行业有形资产总额")
    WORKINGCAPITAL = Column(DECIMAL(30, 6), doc="行业营运资金")
    EBIT = Column(DECIMAL(30, 6), doc="行业息税前利润")
    MARKETVALUEA = Column(DECIMAL(30, 6), doc="行业市值A")
    MARKETVALUEB = Column(DECIMAL(30, 6), doc="行业市值B")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_cashflow(Base):

    __tablename__ = 'stk_indfi_cashflow'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    NCFTONETPROFIT = Column(DECIMAL(20, 6), doc="行业净利润现金净含量")
    OPERATINGINCOMEINCASHRATIO = Column(DECIMAL(20, 6), doc="行业营业收入现金净含量")
    NCFTOOPERATINGPROFIT = Column(DECIMAL(20, 6), doc="行业营业利润现金净含量")
    CASHRECOVERYRATIO = Column(DECIMAL(20, 6), doc="行业全部现金回收率")
    OPERATINGNCFTOPROFITRATIO = Column(DECIMAL(20, 6), doc="行业营运指数")
    OPERATNCFTOMAINCASHNEEDED = Column(DECIMAL(20, 6), doc="行业现金满足投资比率")
    CASHFLOWRISK = Column(DECIMAL(20, 6), doc="行业现金流风险")
    MUTABLERATE = Column(DECIMAL(20, 6), doc="行业易变现率")
    NETRATIOTOSHORTTERM = Column(DECIMAL(20, 6), doc="行业短期融资净值结构比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_construct(Base):

    __tablename__ = 'stk_indfi_construct'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    CURRENTASSETRATIO = Column(DECIMAL(20, 6), doc="行业流动资产比率")
    CASHRATIO = Column(DECIMAL(20, 6), doc="行业现金资产比率")
    RECEIVABLERATIO = Column(DECIMAL(20, 6), doc="行业应收类资产比率")
    WORKINGCAPITALRATIO = Column(DECIMAL(20, 6), doc="行业营运资金比率")
    WORKINGCAPITALTOCURRENT = Column(DECIMAL(20, 6), doc="行业营运资金对净资产比率")
    NONCURRENTASSETRATIO = Column(DECIMAL(20, 6), doc="行业非流动资产比率")
    FIXEDASSETRATIO = Column(DECIMAL(20, 6), doc="行业固定资产比率")
    INTANGIBLEASSETRATIO = Column(DECIMAL(20, 6), doc="行业无形资产比率")
    TANGIBLEASSETRATIO = Column(DECIMAL(20, 6), doc="行业有形资产比率")
    EQUITYRATIO = Column(DECIMAL(20, 6), doc="行业所有者权益比率")
    RETAINEDEARNINGRATIO = Column(DECIMAL(20, 6), doc="行业留存收益与资产比")
    EQUITYTOFIXEDASSETRATIO = Column(DECIMAL(20, 6), doc="行业股东权益对固定资产比率")
    CURRENTLIABILITYRATIO = Column(DECIMAL(20, 6), doc="行业流动负债比率")
    OPERATINGLIABILITYRATIO = Column(DECIMAL(20, 6), doc="行业经营负债比率")
    FINANCIALLIABILITYRATIO = Column(DECIMAL(20, 6), doc="行业金融负债比率")
    NONCURRENTLIABILITYRATIO = Column(DECIMAL(20, 6), doc="行业非流动负债比率")
    MAINBUSINESSPROFITRATIO = Column(DECIMAL(20, 6), doc="行业主营业务利润占比")
    FINBUSINESSPROFITRATIO = Column(DECIMAL(20, 6), doc="行业金融活动利润占比")
    OPERATINGPROFITRATIO = Column(DECIMAL(20, 6), doc="行业营业利润占比")
    NONOPERATINGPROFITRATIO = Column(DECIMAL(20, 6), doc="行业营业外收入占比")
    COMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="行业净利润与综合收益比")
    OTHERCOMPREHENSIVERATIO = Column(DECIMAL(20, 6), doc="行业其他综合收益占比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_crn(Base):

    __tablename__ = 'stk_indfi_crn'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市，已经退市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    CR_4A = Column(DECIMAL(20, 6), doc="CR_4（主营业务收入）")
    CR_5A = Column(DECIMAL(20, 6), doc="CR_5（主营业务收入）")
    CR_8A = Column(DECIMAL(20, 6), doc="CR_8（主营业务收入）")
    CR_10A = Column(DECIMAL(20, 6), doc="CR_10（主营业务收入）")
    CR_20A = Column(DECIMAL(20, 6), doc="CR_20（主营业务收入）")
    CR_4B = Column(DECIMAL(20, 6), doc="CR_4（营业收入）")
    CR_5B = Column(DECIMAL(20, 6), doc="CR_5（营业收入）")
    CR_8B = Column(DECIMAL(20, 6), doc="CR_8（营业收入）")
    CR_10B = Column(DECIMAL(20, 6), doc="CR_10（营业收入）")
    CR_20B = Column(DECIMAL(20, 6), doc="CR_20（营业收入）")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_debtpay(Base):

    __tablename__ = 'stk_indfi_debtpay'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    CURRENTRATIO = Column(DECIMAL(20, 6), doc="行业流动比率")
    QUICKRATIO = Column(DECIMAL(20, 6), doc="行业速动比率")
    CONSERVATIVEQUICKRATIO = Column(DECIMAL(20, 6), doc="行业保守速动比率")
    CASHRATIO = Column(DECIMAL(20, 6), doc="行业现金比率")
    WORKINGCAPITALTOLIABILITY = Column(DECIMAL(20, 6), doc="行业营运资金与借款比")
    INTERESTCOVERAGERATIOA = Column(DECIMAL(20, 6), doc="行业利息保障倍数A")
    INTERESTCOVERAGERATIOB = Column(DECIMAL(20, 6), doc="行业利息保障倍数B")
    CURRENTLIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="行业经营活动产生的现金流量净额与流动负债比")
    INTERESTCOVERAGERATIOC = Column(DECIMAL(20, 6), doc="行业现金流利息保障倍数")
    ASSETLIABILITYRATIO = Column(DECIMAL(20, 6), doc="行业资产负债率")
    LONGTERMLIABILITYTOASSET = Column(DECIMAL(20, 6), doc="行业长期借款与总资产比")
    LIABILITYTOTANGIBLEASSET = Column(DECIMAL(20, 6), doc="行业有形资产负债率")
    INTERESLIABILITYTOTANGIB = Column(DECIMAL(20, 6), doc="行业有形资产与带息债务比")
    EQUITYMULTIPLIER = Column(DECIMAL(20, 6), doc="行业权益乘数")
    DEBTEQUITYRATIO = Column(DECIMAL(20, 6), doc="行业产权比率")
    EQUITYTODEBTRATIO = Column(DECIMAL(20, 6), doc="行业权益与负债比")
    LONGTERMCAPITALDEBTRATIO = Column(DECIMAL(20, 6), doc="行业长期资本负债率")
    LONGTERMLIABILITYTOEQUITY = Column(DECIMAL(20, 6), doc="行业长期负债与权益比")
    LIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="行业经营活动产生的现金流量净额与负债合计比")
    INTERESLIABILITYCOVERAGE = Column(DECIMAL(20, 6), doc="行业经营活动产生的现金流量净额与带息债务比")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_development(Base):

    __tablename__ = 'stk_indfi_development'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    EQUITYAPPRECIATIONRATIO = Column(DECIMAL(20, 6), doc="行业资本保值增值率")
    EQUITYGROWTHRATIO = Column(DECIMAL(20, 6), doc="行业资本积累率")
    FIXEDASSETSGROWTH = Column(DECIMAL(20, 6), doc="行业固定资产增长率")
    ASSETSGROWTH = Column(DECIMAL(20, 6), doc="行业总资产增长率")
    ROEGROWTH = Column(DECIMAL(20, 6), doc="行业净资产收益率增长率")
    NETPROFITGROWTH = Column(DECIMAL(20, 6), doc="行业净利润增长率")
    OPERATINGPROFITGROWTH = Column(DECIMAL(20, 6), doc="行业营业利润增长率")
    OPERATINGREVENUEGROWTH = Column(DECIMAL(20, 6), doc="行业营业收入增长率")
    TOTALREVENUEGROWTHA = Column(DECIMAL(20, 6), doc="行业营业总收入增长率")
    TOTALREVENUEGROWTHB = Column(DECIMAL(20, 6), doc="行业营业总成本增长率")
    SALESEXPENSEGROWTH = Column(DECIMAL(20, 6), doc="行业销售费用增长率")
    MANAGEMENTEXPENSEGROWTH = Column(DECIMAL(20, 6), doc="行业管理费用增长率")
    OPERATINGNCFPERSHAREGROWTH = Column(DECIMAL(20, 6), doc="行业每股经营活动产生的净流量增长率")
    SUSTAINABLEGROWTHRATEA = Column(DECIMAL(20, 6), doc="行业可持续增长率A")
    SUSTAINABLEGROWTHRATEB = Column(DECIMAL(20, 6), doc="行业可持续增长率B")
    EQUITYGROWTH = Column(DECIMAL(20, 6), doc="行业所有者权益增长率")
    NAVGROWTH = Column(DECIMAL(20, 6), doc="行业每股净资产增长率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_dividistrib(Base):

    __tablename__ = 'stk_indfi_dividistrib'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    DISTRIBUTIONRATE = Column(DECIMAL(20, 6), doc="行业股利分配率")
    PROFITRETENTIONRATE = Column(DECIMAL(20, 6), doc="行业收益留存率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_earnpower(Base):

    __tablename__ = 'stk_indfi_earnpower'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    ROA1A = Column(DECIMAL(20, 6), doc="行业资产报酬率A")
    ROA1B = Column(DECIMAL(20, 6), doc="行业资产报酬率B")
    ROA2A = Column(DECIMAL(20, 6), doc="行业总资产净利润率（ROA）A")
    ROA2B = Column(DECIMAL(20, 6), doc="行业总资产净利润率（ROA）B")
    ROEA = Column(DECIMAL(20, 6), doc="行业净资产收益率A")
    ROEB = Column(DECIMAL(20, 6), doc="行业净资产收益率B")
    NETPROFITTOTOTAL = Column(DECIMAL(20, 6), doc="行业净利润与利润总额比")
    EBITTOASSET = Column(DECIMAL(20, 6), doc="行业息税前利润与资产总额比")
    RETURNONINVESTEDCAPITAL = Column(DECIMAL(20, 6), doc="行业投入资本回报率")
    RETURNONLONGTERMINVESTED = Column(DECIMAL(20, 6), doc="行业长期资本收益率")
    OPERATINGMARGINRATIO = Column(DECIMAL(20, 6), doc="行业营业毛利率")
    OPERATINGCOSTRATIO = Column(DECIMAL(20, 6), doc="行业营业成本率")
    OPERATINGPROFITOREVENUE = Column(DECIMAL(20, 6), doc="行业营业利润率")
    OPERATINGNETPROFITOREVENUE = Column(DECIMAL(20, 6), doc="行业营业净利率")
    GROSSCOSTRATIO = Column(DECIMAL(20, 6), doc="行业总营业成本率")
    SALESEXPENSERATE = Column(DECIMAL(20, 6), doc="行业销售费用率")
    MANAGEMENTEXPENSERATE = Column(DECIMAL(20, 6), doc="行业管理费用率")
    FINANCIALEXPENSERATE = Column(DECIMAL(20, 6), doc="行业财务费用率")
    PERIODEXPENSERATE = Column(DECIMAL(20, 6), doc="行业销售期间费用率")
    PROFITTOCOST = Column(DECIMAL(20, 6), doc="行业成本费用利润率")
    EBITDATOREVENUE = Column(DECIMAL(20, 6), doc="行业息税折旧摊销前营业利润率")
    EBITTOREVENUE = Column(DECIMAL(20, 6), doc="行业息税前营业利润率")
    RETURNONINVESTMENT = Column(DECIMAL(20, 6), doc="行业投资收益率")
    PRICECOSTPROFIT = Column(DECIMAL(20, 6), doc="行业价格成本费用利润率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_hhi(Base):

    __tablename__ = 'stk_indfi_hhi'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市，已经退市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    HHI_A = Column(DECIMAL(20, 6), doc="HHI(A)")
    HHI_B = Column(DECIMAL(20, 6), doc="HHI(B)")
    HHI_C = Column(DECIMAL(20, 6), doc="HHI(C)")
    HHI_D = Column(DECIMAL(20, 6), doc="HHI(D)")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_indtrajectory(Base):

    __tablename__ = 'stk_indfi_indtrajectory'

    STOCKCODE = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    CROSSSYMBOL = Column(String(6), doc="AB股交叉码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_lernerindex(Base):

    __tablename__ = 'stk_indfi_lernerindex'

    STOCKCODE = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    STOCKLERNERINDEX = Column(DECIMAL(20, 6), doc="个股勒纳指数")
    INDUSTRYLERNERINDEX = Column(DECIMAL(20, 6), doc="行业勒纳指数")
    STATUS = Column(String(1), doc="交易状态")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_lpesv(Base):

    __tablename__ = 'stk_indfi_lpesv'

    INDUSTRYCODE = Column(String(200), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    STATISTICALCALIBRE = Column(String(1), doc="统计口径")
    SGNYEAR = Column(String(4), doc="发布年份")
    STANDARD = Column(String(1), doc="标准标识")
    ROE = Column(DECIMAL(20, 2), doc="净资产收益率")
    ROA = Column(DECIMAL(20, 2), doc="总资产报酬率")
    ROS = Column(DECIMAL(20, 2), doc="销售（营业）利润率")
    GROSSPROFITRATE = Column(DECIMAL(20, 2), doc="主营业务利润率")
    NCFTONETPROFIT = Column(DECIMAL(20, 2), doc="盈余现金保障倍数")
    PROFITTOCOST = Column(DECIMAL(20, 2), doc="成本费用利润率")
    RETURNONCAPITAL = Column(DECIMAL(20, 2), doc="资本收益率")
    ASSETTURNOVER = Column(DECIMAL(20, 2), doc="总资产周转率")
    RECEIVABLESTURNOVER = Column(DECIMAL(20, 2), doc="应收账款周转率")
    BADASSETSRATIOA = Column(DECIMAL(20, 2), doc="不良资产比率")
    CURRENTASSETTURNOVER = Column(DECIMAL(20, 2), doc="流动资产周转率")
    CASHTOASSET = Column(DECIMAL(20, 2), doc="资产现金回收率")
    DEBTTOASSETRATIO = Column(DECIMAL(20, 2), doc="资产负债率")
    INTERESTCOVERAGERATIO = Column(DECIMAL(20, 2), doc="已获利息倍数")
    QUICKRATIO = Column(DECIMAL(20, 2), doc="速动比率")
    CASHFLOWSRATIO = Column(DECIMAL(20, 2), doc="现金流动负债比率")
    DEBTRATIO = Column(DECIMAL(20, 2), doc="带息负债比率")
    CONTINGENTDEBTRATIO = Column(DECIMAL(20, 2), doc="或有负债比率")
    SALESGROWTHRATE = Column(DECIMAL(20, 2), doc="销售（营业）增长率")
    EQUITYAPPRECIATIONRATIO = Column(DECIMAL(20, 2), doc="资本保值增值率")
    SALESRATEGROWTHRATE = Column(DECIMAL(20, 2), doc="销售（营业）利率增长率")
    ASSETSGROWTH = Column(DECIMAL(20, 2), doc="总资产增长率")
    TR = Column(DECIMAL(20, 2), doc="技术投入比率")
    INVENTORYTURNOVER = Column(DECIMAL(20, 2), doc="存货周转率")
    AVERAGECAPITALGROWTHRATE3Y = Column(DECIMAL(20, 2), doc="三年资本平均增长率")
    AVERAGESALESGROWTHRATE3Y = Column(DECIMAL(20, 2), doc="三年销售平均增长率")
    BADASSETSRATIOB = Column(DECIMAL(20, 2), doc="不良资产比率（旧制度）")
    RECSTOCKTOCURRENTASSETS = Column(DECIMAL(20, 2), doc="两金占流动资产比重")
    COSTEXPENSERATIOSA = Column(DECIMAL(20, 2), doc="成本费用占主营营业收入比重")
    COSTEXPENSERATIOSB = Column(DECIMAL(20, 2), doc="成本费用占营业收入比重")
    EVA = Column(DECIMAL(20, 2), doc="经济增加值率")
    EBITDA = Column(DECIMAL(20, 2), doc="EBITDA率")
    PERIODCOSTTOMAININCOME = Column(DECIMAL(20, 2), doc="期间费用占主营营业收入的比率")
    EQUITYGROWTHRATIO = Column(DECIMAL(20, 2), doc="资本积累率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_npesv(Base):

    __tablename__ = 'stk_indfi_npesv'

    INDUSTRYCODE = Column(String(200), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    STATISTICALCALIBRE = Column(String(1), doc="统计口径")
    SGNYEAR = Column(String(4), doc="发布年份")
    STANDARD = Column(String(1), doc="标准标识")
    ROE = Column(DECIMAL(20, 2), doc="净资产收益率")
    ROA = Column(DECIMAL(20, 2), doc="总资产报酬率")
    ROS = Column(DECIMAL(20, 2), doc="销售（营业）利润率")
    GROSSPROFITRATE = Column(DECIMAL(20, 2), doc="主营业务利润率")
    NCFTONETPROFIT = Column(DECIMAL(20, 2), doc="盈余现金保障倍数")
    PROFITTOCOST = Column(DECIMAL(20, 2), doc="成本费用利润率")
    RETURNONCAPITAL = Column(DECIMAL(20, 2), doc="资本收益率")
    ASSETTURNOVER = Column(DECIMAL(20, 2), doc="总资产周转率")
    RECEIVABLESTURNOVER = Column(DECIMAL(20, 2), doc="应收账款周转率")
    BADASSETSRATIOA = Column(DECIMAL(20, 2), doc="不良资产比率")
    CURRENTASSETTURNOVER = Column(DECIMAL(20, 2), doc="流动资产周转率")
    CASHTOASSET = Column(DECIMAL(20, 2), doc="资产现金回收率")
    DEBTTOASSETRATIO = Column(DECIMAL(20, 2), doc="资产负债率")
    INTERESTCOVERAGERATIO = Column(DECIMAL(20, 2), doc="已获利息倍数")
    QUICKRATIO = Column(DECIMAL(20, 2), doc="速动比率")
    CASHFLOWSRATIO = Column(DECIMAL(20, 2), doc="现金流动负债比率")
    DEBTRATIO = Column(DECIMAL(20, 2), doc="带息负债比率")
    CONTINGENTDEBTRATIO = Column(DECIMAL(20, 2), doc="或有负债比率")
    SALESGROWTHRATE = Column(DECIMAL(20, 2), doc="销售（营业）增长率")
    EQUITYAPPRECIATIONRATIO = Column(DECIMAL(20, 2), doc="资本保值增值率")
    SALESRATEGROWTHRATE = Column(DECIMAL(20, 2), doc="销售（营业）利率增长率")
    ASSETSGROWTH = Column(DECIMAL(20, 2), doc="总资产增长率")
    TR = Column(DECIMAL(20, 2), doc="技术投入比率")
    INVENTORYTURNOVER = Column(DECIMAL(20, 2), doc="存货周转率")
    AVERAGECAPITALGROWTHRATE3Y = Column(DECIMAL(20, 2), doc="三年资本平均增长率")
    AVERAGESALESGROWTHRATE3Y = Column(DECIMAL(20, 2), doc="三年销售平均增长率")
    BADASSETSRATIOB = Column(DECIMAL(20, 2), doc="不良资产比率（旧制度）")
    RECSTOCKTOCURRENTASSETS = Column(DECIMAL(20, 2), doc="两金占流动资产比重")
    COSTEXPENSERATIOSA = Column(DECIMAL(20, 2), doc="成本费用占主营营业收入比重")
    COSTEXPENSERATIOSB = Column(DECIMAL(20, 2), doc="成本费用占营业收入比重")
    EVA = Column(DECIMAL(20, 2), doc="经济增加值率")
    EBITDA = Column(DECIMAL(20, 2), doc="EBITDA率")
    PERIODCOSTTOMAININCOME = Column(DECIMAL(20, 2), doc="期间费用占主营营业收入的比率")
    EQUITYGROWTHRATIO = Column(DECIMAL(20, 2), doc="资本积累率")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_operate(Base):

    __tablename__ = 'stk_indfi_operate'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    RECEIVABLESTOINCOME = Column(DECIMAL(20, 6), doc="行业应收账款与收入比")
    RECEIVABLETURNOVERA = Column(DECIMAL(20, 6), doc="行业应收账款周转率A")
    RECEIVABLETURNOVERB = Column(DECIMAL(20, 6), doc="行业应收账款周转率B")
    RECEIVABLETURNOVERDAYSA = Column(DECIMAL(20, 6), doc="行业应收账款周转天数A")
    RECEIVABLETURNOVERDAYSB = Column(DECIMAL(20, 6), doc="行业应收账款周转天数B")
    INVENTORYTOINCOME = Column(DECIMAL(20, 6), doc="行业存货与收入比")
    INVENTORYTURNOVERA = Column(DECIMAL(20, 6), doc="行业存货周转率A")
    INVENTORYTURNOVERB = Column(DECIMAL(20, 6), doc="行业存货周转率B")
    INVENTORYTURNOVERDAYSA = Column(DECIMAL(20, 6), doc="行业存货周转天数A")
    INVENTORYTURNOVERDAYSB = Column(DECIMAL(20, 6), doc="行业存货周转天数B")
    PAYABLETURNOVERA = Column(DECIMAL(20, 6), doc="行业应付账款周转率A")
    PAYABLETURNOVERB = Column(DECIMAL(20, 6), doc="行业应付账款周转率B")
    WORKINGCAPITALTURNOVERA = Column(DECIMAL(20, 6), doc="行业营运资金（资本）周转率A")
    WORKINGCAPITALTURNOVERB = Column(DECIMAL(20, 6), doc="行业营运资金（资本）周转率B")
    CASHEQUIVALENTSTURNOVERA = Column(DECIMAL(20, 6), doc="行业现金及现金等价物周转率A")
    CASHEQUIVALENTTURNOVERB = Column(DECIMAL(20, 6), doc="行业现金及现金等价物周转率B")
    CURRENTASSETTURNOVERA = Column(DECIMAL(20, 6), doc="行业流动资产周转率A")
    CURRENTASSETTURNOVERB = Column(DECIMAL(20, 6), doc="行业流动资产周转率B")
    FIXEDASSETTURNOVERA = Column(DECIMAL(20, 6), doc="行业固定资产周转率A")
    FIXEDASSETTURNOVERB = Column(DECIMAL(20, 6), doc="行业固定资产周转率B")
    NONCURRENTASSETTURNOVERA = Column(DECIMAL(20, 6), doc="行业非流动资产周转率A")
    NONCURRENTASSETTURNOVERB = Column(DECIMAL(20, 6), doc="行业非流动资产周转率B")
    ASSETTURNOVERA = Column(DECIMAL(20, 6), doc="行业总资产周转率A")
    ASSETTURNOVERB = Column(DECIMAL(20, 6), doc="行业总资产周转率B")
    EEQUITYTURNOVERA = Column(DECIMAL(20, 6), doc="行业股东权益周转率A")
    EEQUITYTURNOVERB = Column(DECIMAL(20, 6), doc="行业股东权益周转率B")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_pershare(Base):

    __tablename__ = 'stk_indfi_pershare'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    EPS = Column(DECIMAL(20, 6), doc="行业基本每股收益")
    DILUTEDEPS = Column(DECIMAL(20, 6), doc="行业稀释每股收益")
    EPSA = Column(DECIMAL(20, 6), doc="行业每股收益A")
    EPSB = Column(DECIMAL(20, 6), doc="行业每股收益B")
    EPSC = Column(DECIMAL(20, 6), doc="行业每股收益C")
    EPSD = Column(DECIMAL(20, 6), doc="行业每股收益D")
    COMPREHENSIVEEPSA = Column(DECIMAL(20, 6), doc="行业每股综合收益A")
    COMPREHENSIVEEPSB = Column(DECIMAL(20, 6), doc="行业每股综合收益B")
    TOTALREVENUEPERSHAREA = Column(DECIMAL(20, 6), doc="行业每股营业总收入A")
    TOTALREVENUEPERSHAREB = Column(DECIMAL(20, 6), doc="行业每股营业总收入B")
    REVENUEPERSHAREA = Column(DECIMAL(20, 6), doc="行业每股营业收入A")
    REVENUEPERSHAREB = Column(DECIMAL(20, 6), doc="行业每股营业收入B")
    EBITPERSHAREA = Column(DECIMAL(20, 6), doc="行业息税前每股收益A")
    EBITPERSHAREB = Column(DECIMAL(20, 6), doc="行业息税前每股收益B")
    EBITDAPERSHAREA = Column(DECIMAL(20, 6), doc="行业息税折旧摊销前每股收益A")
    EBITDAPERSHAREB = Column(DECIMAL(20, 6), doc="行业息税折旧摊销前每股收益B")
    OPERATINGPROFITPERSHAREA = Column(DECIMAL(20, 6), doc="行业每股营业利润A")
    OPERATINGPROFITPERSHAREB = Column(DECIMAL(20, 6), doc="行业每股营业利润B")
    NAVA = Column(DECIMAL(20, 6), doc="行业每股净资产A")
    NAVB = Column(DECIMAL(20, 6), doc="行业每股净资产B")
    TANGIBLEASSETPERSHAREA = Column(DECIMAL(20, 6), doc="行业每股有形资产A")
    TANGIBLEASSETPERSHAREB = Column(DECIMAL(20, 6), doc="行业每股有形资产B")
    LIABILITYPERSHAREA = Column(DECIMAL(20, 6), doc="行业每股负债A")
    LIABILITYPERSHAREB = Column(DECIMAL(20, 6), doc="行业每股负债B")
    UNDISTRIBUTEDPROFIT = Column(DECIMAL(20, 6), doc="行业每股未分配利润")
    OPERATINGNCFPERSHARE = Column(DECIMAL(20, 6), doc="行业每股经营活动产生的现金流量净额")
    CASHINCREASEPERSHAREA = Column(DECIMAL(20, 6), doc="行业每股现金净流量A")
    CASHINCREASEPERSHAREB = Column(DECIMAL(20, 6), doc="行业每股现金净流量B")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_relativevalue(Base):

    __tablename__ = 'stk_indfi_relativevalue'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    PE = Column(DECIMAL(20, 6), doc="行业市盈率")
    PS = Column(DECIMAL(20, 6), doc="行业市销率")
    PCF = Column(DECIMAL(20, 6), doc="行业市现率")
    PBV = Column(DECIMAL(20, 6), doc="行业市净率")
    TOBINQA = Column(DECIMAL(20, 6), doc="行业托宾Q值A")
    TOBINQB = Column(DECIMAL(20, 6), doc="行业托宾Q值B")
    TOBINQC = Column(DECIMAL(20, 6), doc="行业托宾Q值C")
    TOBINQD = Column(DECIMAL(20, 6), doc="行业托宾Q值D")
    NETASSETTOMARKETVALUEA = Column(DECIMAL(20, 6), doc="行业账面市值比A")
    NETASSETTOMARKETVALUEB = Column(DECIMAL(20, 6), doc="行业账面市值比B")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_indfi_risk(Base):

    __tablename__ = 'stk_indfi_risk'

    INDUSTRYCODE = Column(String(10), doc="行业代码")
    INDUSTRYNAME = Column(String(200), doc="行业名称")
    ENDDATE = Column(DateTime, doc="截止日期")
    MARKETTYPE = Column(String(2), doc="市场类型")
    MEANALGORITHM = Column(String(1), doc="均值算法")
    ST = Column(String(1), doc="是否剔除ST或*ST股")
    ISNEWORSUSPEND = Column(String(1), doc="是否剔除当年新上市或被暂停上市的公司")
    SAMPLENUMBER = Column(SMALLINT, doc="行业内公司总数")
    DFL = Column(DECIMAL(20, 6), doc="行业财务杠杆")
    DOL = Column(DECIMAL(20, 6), doc="行业经营杠杆")
    DTL = Column(DECIMAL(20, 6), doc="行业总杠杆")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_industryclass(Base):

    __tablename__ = 'stk_industryclass'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    INDUSTRYCLASSIFICATIONID = Column(String(40), doc="行业分类标准编码")
    CHANGEDATE = Column(DateTime, doc="变更日期")
    INDUSTRYCODE = Column(String(20), doc="行业代码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_institutionholderalias(Base):

    __tablename__ = 'stk_institutionholderalias'

    INSTITUTIONHOLDERID = Column(DECIMAL(30, 0), doc="GTA股东机构ID")
    ALIAS = Column(String(200), doc="机构别名")
    SHAREHOLDERTYPE = Column(String(100), doc="股东类型")
    SHAREHOLDERTYPECODE = Column(String(10), doc="股东类型编码")
    COMMENTS = Column(String(4000), doc="备注")
    ISSTANDARDFULLNAME = Column(String(2), doc="是否为标准名称")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_institutioninfo(Base):

    __tablename__ = 'stk_institutioninfo'

    INSTITUTIONID = Column(DECIMAL(20, 0))
    FULLNAME = Column(String(200))
    ENNAME = Column(String(400))
    SYMBOL = Column(String(20))
    OWNSHIPID = Column(String(12))
    ESTABLISHWAYID = Column(String(12))
    ESTABLISHDATE = Column(DateTime)
    IPODATE = Column(DateTime)
    EXCHANGECODE = Column(String(100))
    LEGALREPRESENTATIVE = Column(String(100))
    GENERALMANAGER = Column(String(100))
    SECRETARY = Column(String(100))
    SECRETARYTEL = Column(String(100))
    SECRETARYFAX = Column(String(100))
    SECRETARYEMAIL = Column(String(200))
    SECURITYCONSULTANT = Column(String(100))
    REGISTERCAPITAL = Column(BIGINT)
    CURRENCYCODE = Column(String(12))
    REGISTERADDRESS = Column(String(400))
    LATESTREGISTERDATE = Column(DateTime)
    OFFICEADDRESS = Column(String(400))
    ZIPCODE = Column(String(20))
    BUSINESSLICENSENUMBER = Column(String(100))
    TAXREGISTRYNO = Column(String(100))
    WEBSITE = Column(String(200))
    EMAIL = Column(String(200))
    DISCLOSEPAPER = Column(String(200))
    DISCLOSEWEBSITE = Column(String(200))
    REPORTPLACE = Column(String(200))
    CITYCODE = Column(String(12))
    PROVINCECODE = Column(String(12))
    REGIONCODE = Column(String(6))
    MAINBUSINESS = Column(String(2000))
    BUSINESSSCOPE = Column(String(4000))
    HISTORY = Column(String(4000))
    INDUSTRYCLASSIFICATIONID = Column(String(40))
    INDUSTRYCODE = Column(String(20))
    CHANGEDATE = Column(DateTime)
    UPDATEID = Column(BIGINT, primary_key=True)
    SHORTNAME = Column(String(80), doc="英文简称")
    ENSHORTNAME = Column(String(100))
    CORPESTABLISHEDDATE = Column(DateTime, doc="股份公司设立日期")
    SOCIALCREDITCODE = Column(String(20), doc="统一社会信用代码")


class stk_itemchange(Base):

    __tablename__ = 'stk_itemchange'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="机构ID")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(20), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    CHANGEDATE = Column(DateTime, doc="实施日期")
    CHANGEDITEM = Column(String(100), doc="变更属性")
    VALUEBEFORE = Column(String(1000), doc="变更前值")
    CODEBEFORE = Column(String(200), doc="变更前(编码|英文)")
    VALUEAFTER = Column(String(1000), doc="变更后值")
    CODEAFTER = Column(String(200), doc="变更后(编码|英文)")
    REASON = Column(String(200), doc="变更原因")
    REASONID = Column(String(100), doc="变更原因编码")
    STATEIDCHANGE = Column(String(100), doc="状态前后编码变动")
    COMMENTS = Column(LONGTEXT, doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_listedcoinfochg(Base):

    __tablename__ = 'stk_listedcoinfochg'

    LISTEDCOID = Column(DECIMAL(20, 0), doc="上市公司ID")
    ANNOUNCEMENTDATE = Column(DateTime, doc="公告日期")
    CHANGEDITEM = Column(String(100), doc="变更属性")
    EVENTTYPE = Column(String(40), doc="事件类型编码")
    VALUE_BEFORE = Column(String(4000), doc="变更前值")
    CODE_BEFORE = Column(String(4000), doc="变更前(编码|英文)")
    VALUE_AFTER = Column(String(4000), doc="变更后值")
    CODE_AFTER = Column(String(4000), doc="变更后(编码|英文)")
    IMPLEMENTDATE = Column(DateTime, doc="实施日期")
    DESCRIPVALUE_BEFORE = Column(String(100), doc="变更前属性描述")
    DESCRIPVALUE_AFTER = Column(String(100), doc="变更后属性描述")
    SYMBOL = Column(String(20), doc="证券代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    TRADINGSTATE = Column(String(20), doc="变更后简称状态标识")
    NOTE = Column(String(1000), doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_lock_shares(Base):

    __tablename__ = 'stk_lock_shares'

    SYMBOL = Column(String(20), doc="证券代码")
    ENDDATE = Column(DateTime, doc="截止日期")
    FULLNAME = Column(String(400), doc="股东名称")
    FULLNAME_EN = Column(String(1000), doc="股东英文名称")
    REASON = Column(String(200), doc="限售原因")
    REASONID = Column(String(60), doc="限售原因编码")
    BEGINNINGSHARES = Column(DECIMAL(20, 2), doc="期初持有数量")
    ADDSHARES = Column(DECIMAL(20, 2), doc="本期增加限售股数")
    LISTEDSHARES = Column(DECIMAL(20, 2), doc="本期解禁数量")
    LISTEDDATE = Column(DateTime, doc="本期解禁日期")
    ENDSHARES = Column(DECIMAL(20, 2), doc="期末持有限售股数")
    FIRSTLISTEDSHARES = Column(DECIMAL(20, 2), doc="期后第一批解禁数量")
    FIRSTLISTEDDATE = Column(DateTime, doc="期后第一批解禁日期")
    SECONDLISTEDSHARES = Column(DECIMAL(20, 2), doc="期后第二批解禁数量")
    SECONDLISTEDDATE = Column(DateTime, doc="期后第二批解禁日期")
    THIRDLISTEDSHARES = Column(DECIMAL(20, 2), doc="期后第三批解禁数量")
    THIRDLISTEDDATE = Column(DateTime, doc="期后第三批解禁日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0))
    UPDATETIME_EN = Column(DateTime)


class stk_lockshares_summary(Base):

    __tablename__ = 'stk_lockshares_summary'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    LISTEDDATE = Column(DateTime, primary_key=True, doc="解禁日期")
    HOLDERNUMBER = Column(BIGINT, doc="解禁股东家数")
    LISTEDSHARES = Column(DECIMAL(20, 4), doc="本期解禁流通股数")
    TOTALLOCKSHARES = Column(DECIMAL(20, 4), doc="总限售股数")
    PROPORTION1 = Column(DECIMAL(10, 4), doc="本期解禁流通股数占总限售股数比例")
    PROPORTION2 = Column(DECIMAL(10, 4), doc="占流通A股比例")
    PROPORTION3 = Column(DECIMAL(10, 4), doc="占总股本比例")
    REMAINEDLOCKSHARES = Column(DECIMAL(20, 4), doc="剩余限售股数量")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_ma_assetreplace(Base):

    __tablename__ = 'stk_ma_assetreplace'

    EVENTID = Column(DECIMAL(20, 0), primary_key=True, doc="事件ID")
    RANK = Column(BIGINT, primary_key=True, doc="序号")
    ASSETSSURRENDEREDPARTY = Column(String(1000), doc="资产置出方")
    SINSTITUTIONID = Column(DECIMAL(20, 0), doc="资产置出方机构ID")
    SCONCERTEDACTION = Column(SMALLINT, doc="资产置出方一致行动人标识")
    ASSETSRECEIVEDPARTY = Column(String(1000), doc="资产置入方")
    BINSTITUTIONID = Column(DECIMAL(20, 0), doc="资产置入方机构ID")
    RCONCERTEDACTION = Column(SMALLINT, doc="资产置入方一致行动人标识")
    SRECEIVINGPARTY = Column(String(1000), doc="置出资产承接方")
    RRECEIVINGPARTY = Column(String(1000), doc="置入资产承接方")
    SBOOKVALUE = Column(DECIMAL(20, 4), doc="置出资产账面价值")
    STRADINGPRICE = Column(DECIMAL(20, 4), doc="置出资产交易价格")
    RBOOKVALUE = Column(DECIMAL(20, 4), doc="置入资产账面价值")
    RTRADINGPRICE = Column(DECIMAL(20, 4), doc="置入资产交易价格")
    STRANSFERDATE = Column(DateTime, doc="置出资产过户日期")
    RTRANSFERDATE = Column(DateTime, doc="置入资产过户日期")
    SAPPRSREPTNO = Column(String(100), doc="置出资产披露文档号")
    RAPPRSREPTNO = Column(String(100), doc="置入资产披露文档号")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_ma_assetstopay(Base):

    __tablename__ = 'stk_ma_assetstopay'

    EVENTID = Column(DECIMAL(20, 0), primary_key=True, doc="事件ID")
    RANK = Column(BIGINT, primary_key=True, doc="序号")
    AMOUNT = Column(DECIMAL(20, 4), doc="支付金额")
    ASSETNAME = Column(String(400), doc="资产名称")
    OWNERSHIP = Column(String(200), doc="标的权属")
    EXPLANATION = Column(String(4000), doc="资产说明")
    BOOKVALUE = Column(DECIMAL(20, 4), doc="账面价值")
    EVALUATIONVALUE = Column(DECIMAL(20, 4), doc="评估价值")
    BASEDAY = Column(DateTime, doc="评估基准日")
    GUARANTEE = Column(String(100), doc="担保情况")
    OPERATION = Column(String(2000), doc="运营情况")
    AMOUNTTOBUYERTOTALASSETS = Column(DECIMAL(10, 4), doc="资产交易金额占买方比")
    AMOUNTTOSELLERTOTALASSETS = Column(DECIMAL(10, 4), doc="资产交易金额占卖方比")
    EVALUATIONINSTITUTION = Column(String(100), doc="评估机构")
    OTHERNOTES = Column(String(4000), doc="其他情况说明")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_ma_assettrans(Base):

    __tablename__ = 'stk_ma_assettrans'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    RANK = Column(BIGINT, doc="序号")
    SELLER = Column(String(1000), doc="资产转让方")
    SINSTITUTIONID = Column(DECIMAL(20, 0), doc="转让方机构ID")
    BUYER = Column(String(1000), doc="资产受让方")
    BINSTITUTIONID = Column(DECIMAL(20, 0), doc="受让方机构ID")
    VARIETY = Column(SMALLINT, doc="交易类型")
    TRADINGATTITUDE = Column(SMALLINT, doc="交易态度")
    BUYERCOMBINATIONORNOT = Column(SMALLINT, doc="是否买方组合")
    BUYERCONCERTEDACTION = Column(SMALLINT, doc="买方一致行动人标识")
    SELLERCOMBINATIONORNOT = Column(SMALLINT, doc="是否卖方组合")
    SELLERCONCERTEDACTION = Column(SMALLINT, doc="卖方一致行动人标识")
    CONTROLTRANSFERORNOT = Column(SMALLINT, doc="是否发生控制权转移")
    TRADINGTYPEID = Column(String(200), doc="交易方式编码")
    TRADINGTYPE = Column(String(200), doc="交易方式")
    TOUCHEDOFFERORNOT = Column(SMALLINT, doc="是否触及要约")
    OFFEREXEMPTIONORNOT = Column(SMALLINT, doc="是否豁免要约")
    TRANSFERDATE = Column(DateTime, doc="资产过户日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_ma_cashpayment(Base):

    __tablename__ = 'stk_ma_cashpayment'

    EVENTID = Column(DECIMAL(20, 0), primary_key=True, doc="事件ID")
    CASHAMOUNT = Column(DECIMAL(20, 4), doc="现金支付金额")
    DEBTAMOUNT = Column(DECIMAL(20, 4), doc="承担债务金额")
    PAYTYPE = Column(SMALLINT, doc="付款方式")
    FINANCETYPESID = Column(String(40), doc="融资方式编码")
    FINANCETYPES = Column(String(200), doc="融资方式")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_ma_cdr(Base):

    __tablename__ = 'stk_ma_cdr'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    RANK = Column(BIGINT, doc="序号")
    CREDITOR = Column(String(1000), doc="债权人名称")
    CREDITORINSTITUTIONID = Column(DECIMAL(20, 0), doc="债权人机构ID")
    DEBTOR = Column(String(1000), doc="债务人名称")
    DEBTORINSTITUTIONID = Column(DECIMAL(20, 0), doc="债务人机构ID")
    TOTALDEBT = Column(DECIMAL(20, 4), doc="整体债务金额")
    PROFIT = Column(DECIMAL(20, 4), doc="重组收益")
    DEBTRESTRUCTURINGTYPEID = Column(String(200), doc="债务重组方式编码")
    DEBTRESTRUCTURINGTYPE = Column(String(200), doc="债务重组方式")
    AMOUNTINVOLVED = Column(DECIMAL(20, 4), doc="重组涉及金额")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_ma_equitytransfer(Base):

    __tablename__ = 'stk_ma_equitytransfer'

    EVENTID = Column(DECIMAL(20, 0), primary_key=True, doc="事件ID")
    RANK = Column(BIGINT, primary_key=True, doc="序号")
    SELLER = Column(String(1000), doc="转让方")
    SINSTITUTIONID = Column(DECIMAL(20, 0), doc="转让方机构ID")
    BUYER = Column(String(1000), doc="受让方")
    BINSTITUTIONID = Column(DECIMAL(20, 0), doc="受让方机构ID")
    EQUITYNATUREBEFORE = Column(String(100), doc="变动前股权性质")
    EQUITYNATUREAFTER = Column(String(100), doc="变动后股权性质")
    PROPORTION = Column(DECIMAL(10, 4), doc="变动股权比例")
    CHANGETYPEID = Column(String(100), doc="变动方式编码")
    CHANGETYPE = Column(String(200), doc="变动方式")
    PRICE = Column(DECIMAL(10, 3), doc="每股转让价格")
    AMOUNT = Column(DECIMAL(20, 4), doc="转让总价")
    VOLUME = Column(BIGINT, doc="转让股数")
    PRICEUNITS = Column(String(200), doc="计价单位")
    MAINSCHANGEORNOT = Column(SMALLINT, doc="第一大股东变更与否")
    MARKETVALUE = Column(DECIMAL(20, 4), doc="交易时总市值")
    TOTALSHARE = Column(BIGINT, doc="交易时总股数")
    MAINSEQUITYRATIOB = Column(DECIMAL(10, 4), doc="变动前控股股东的持股比例")
    TSHARESRATIO = Column(DECIMAL(10, 4), doc="转让时的流通股比例")
    MAINSEQUITYRATIOA = Column(DECIMAL(10, 4), doc="变动后控股股东的持股比例")
    UPDATEID = Column(BIGINT, doc="数据ID")
    ISCHGACTUALCONTROLLER = Column(SMALLINT, doc="实际控制人是否变更")
    ACTUALCONTROLLERBEFORE = Column(String(200), doc="变动前实际控制人名称")
    ACTUALCONTROLLERAFTER = Column(String(200), doc="变动后实际控制人名称")


class stk_ma_merger(Base):

    __tablename__ = 'stk_ma_merger'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    RANK = Column(BIGINT, doc="序号")
    MERGERTYPEID = Column(String(100), doc="合并方式编码")
    MERGERTYPE = Column(String(200), doc="合并方式")
    COMBININGPARTY = Column(String(1000), doc="合并方")
    COMBININGINSTITUTIONID = Column(DECIMAL(20, 0), doc="合并方机构ID")
    COMBINEDPARTY = Column(String(1000), doc="被合并方")
    COMBINEDINSTITUTIONID = Column(DECIMAL(20, 0), doc="被合并方机构ID")
    CONCERTEDACTION = Column(SMALLINT, doc="被合并方一致行动人标识")
    SURVIVINGPARTY = Column(String(1000), doc="存续方")
    PROPORTION = Column(DECIMAL(10, 4), doc="吸收方相对被吸收方换股比例")
    COMBININGSTOCKPRICE = Column(DECIMAL(10, 3), doc="合并股票价格")
    COMBINEDSTOCKPRICE = Column(DECIMAL(10, 3), doc="被合并股票价格")
    LISTEDDATE = Column(DateTime, doc="新增股份上市日期")
    ISSUESHARES = Column(BIGINT, doc="本次换股增加股份数量")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_ma_otherparty(Base):

    __tablename__ = 'stk_ma_otherparty'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="机构ID")
    INSTITUTIONFULLNAME = Column(String(1000), doc="机构名称")
    RELATIONSHIP = Column(String(200), doc="与上市公司关系")
    RELATIONSHIPID = Column(String(100), doc="与上市公司关系编码")
    TRADINGPOSITION = Column(String(100), doc="交易地位")
    TRADINGPOSITIONID = Column(String(40), doc="交易地位编码")
    LISTINGSIGN = Column(String(4), doc="上市公司标识")
    SYMBOL = Column(String(20), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    COMPANYPROPERTY = Column(String(40), doc="企业性质")
    COMPANYPROPERTYID = Column(String(100), doc="企业性质编码")
    INDUSTRYNAME = Column(String(200), doc="证监会行业名称")
    INDUSTRYCODE = Column(String(40), doc="证监会行业代码")
    COUNTRYCODE = Column(String(40), doc="国别代码")
    REGISTEREDADDRESS = Column(String(400), doc="注册地址")
    OFFICEADDRESS = Column(String(400), doc="办公地址")
    OFFICEZIPCODE = Column(String(40), doc="办公地址邮编")
    TEL = Column(String(200), doc="联系电话")
    FAX = Column(String(200), doc="公司传真")
    WEBSITE = Column(String(200), doc="公司网址")
    EMAIL = Column(String(200), doc="电子邮箱")
    BUSINESSSCOPE = Column(String(4000), doc="经营范围")
    RANK = Column(BIGINT, doc="序号")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    UPDATEID1 = Column(BIGINT, doc="源表STK_MA_InvolvedParty.UPDATEID")
    UPDATEID2 = Column(BIGINT, doc="源表STK_MA_TradingMain.UPDATEID")


class stk_ma_participant(Base):

    __tablename__ = 'stk_ma_participant'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="机构ID")
    INSTITUTIONFULLNAME = Column(String(1000), doc="机构名称")
    RELATIONSHIP = Column(String(200), doc="与上市公司关系")
    RELATIONSHIPID = Column(String(100), doc="与上市公司关系编码")
    TRADINGPOSITION = Column(String(100), doc="交易地位")
    TRADINGPOSITIONID = Column(String(40), doc="交易地位编码")
    LISTINGSIGN = Column(String(4), doc="上市公司标识")
    SYMBOL = Column(String(20), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    COMPANYPROPERTYID = Column(String(40), doc="企业性质编码")
    COMPANYPROPERTY = Column(String(100), doc="企业性质")
    INDUSTRYNAME = Column(String(200), doc="证监会行业名称")
    INDUSTRYCODE = Column(String(40), doc="证监会行业代码")
    COUNTRYCODE = Column(String(40), doc="国别代码")
    REGISTEREDADDRESS = Column(String(400), doc="注册地址")
    REGISTEREDPROVINCE = Column(String(40), doc="注册地所在省")
    REGISTEREDCITY = Column(String(40), doc="注册地所在市")
    REGISTEREDZIPCODE = Column(String(40), doc="注册地邮政编码")
    OFFICEADDRESS = Column(String(400), doc="办公地址")
    OFFICEPROVINCE = Column(String(40), doc="办公地所在省")
    OFFICECITY = Column(String(40), doc="办公地所在市")
    OFFICEZIPCODE = Column(String(40), doc="办公地邮政编码")
    WEBSITE = Column(String(200), doc="国际互联网址")
    TEL = Column(String(200), doc="联系电话")
    FAX = Column(String(200), doc="公司传真")
    EMAIL = Column(String(200), doc="电子邮箱")
    BUSINESSSCOPE = Column(String(4000), doc="经营范围")
    ASSESSINSTITUTION = Column(String(200), doc="聘请资产评估机构")
    FINANCIALADVISER = Column(String(200), doc="聘请财务顾问")
    LAWFIRM = Column(String(400), doc="聘请律师事务所")
    ACCOUNTINGFIRM = Column(String(200), doc="聘请会计师事务所")
    RANK = Column(BIGINT, doc="序号")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_ma_stockpayment(Base):

    __tablename__ = 'stk_ma_stockpayment'

    EVENTID = Column(DECIMAL(20, 0), primary_key=True, doc="事件ID")
    AMOUNT = Column(DECIMAL(20, 4), doc="支付金额")
    PRICE = Column(DECIMAL(10, 3), doc="股票价格")
    VOLUME = Column(BIGINT, doc="发行数量")
    PROPORTION = Column(DECIMAL(10, 4), doc="买方相对卖方换股比例")
    SOURCEID = Column(String(40), doc="股票来源编码")
    SOURCE = Column(String(200), doc="股票来源")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_ma_tenderoffer(Base):

    __tablename__ = 'stk_ma_tenderoffer'

    EVENTID = Column(DECIMAL(20, 0), primary_key=True, doc="事件ID")
    ACQUIRER = Column(String(1000), doc="要约收购方")
    ACQUIRERINSTITUTIONID = Column(DECIMAL(20, 0), doc="要约收购方机构ID")
    BUYERCOMBINATIONORNOT = Column(SMALLINT, doc="是否买方组合")
    BUYERCONCERTEDACTION = Column(SMALLINT, doc="买方一致行动人标识")
    TRADINGATTITUDE = Column(SMALLINT, doc="交易态度")
    CONTROLTRANSFERORNOT = Column(SMALLINT, doc="是否发生控制权转移")
    TYPE = Column(SMALLINT, doc="要约类型")
    PREORDERTSHARESVOLUME = Column(BIGINT, doc="预购流通股数量")
    PREORDERTSHARESRATIO = Column(DECIMAL(10, 4), doc="预购流通股比例")
    TSHARESOFFERPRICE = Column(DECIMAL(10, 3), doc="流通股要约价")
    TSHARESBASEPRICE = Column(DECIMAL(10, 3), doc="流通股定价基准")
    PREORDERNONTSHARESVOLUME = Column(BIGINT, doc="预购非流通股数量")
    PREORDERNONTSHARESRATIO = Column(DECIMAL(10, 4), doc="预购非流通股比例")
    NONTSHARESOFFERPRICE = Column(DECIMAL(10, 3), doc="非流通股要约价")
    NONTSHARESBASEPRICE = Column(DECIMAL(10, 3), doc="非流通股定价基准")
    AIMTOTERMINATEORNOT = Column(SMALLINT, doc="是否以终止上市为目的")
    BETERMINATEDORNOT = Column(SMALLINT, doc="是否终止上市")
    CONTINUEDLISTINGORNOT = Column(SMALLINT, doc="是否有继续上市的安排")
    STARTDATE = Column(DateTime, doc="要约起始日期")
    EXPIRATIONDATE = Column(DateTime, doc="要约终止日期")
    COMPETITIVETENDEROFFER = Column(String(4), doc="有无竞争要约")
    PREACCEPTTSHARESVOLUME = Column(BIGINT, doc="预受流通股数量")
    PREACCEPTNONTSHARESVOLUME = Column(BIGINT, doc="预受非流通股数量")
    TSHARESVOLUME = Column(BIGINT, doc="成交流通股数量")
    TSHARESRATIO = Column(DECIMAL(10, 4), doc="成交流通股比例")
    NONTSHARESVOLUME = Column(BIGINT, doc="成交非流通股数量")
    NONTSHARESRATIO = Column(DECIMAL(10, 4), doc="成交非流通股比例")
    PAYTYPE = Column(SMALLINT, doc="付款方式")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_ma_tradingmain(Base):

    __tablename__ = 'stk_ma_tradingmain'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    FIRSTDECLAREDATE = Column(DateTime, doc="首次公告日期")
    FINISHDECLAREDATE = Column(DateTime, doc="完成公告日期")
    ISSUCCEED = Column(String(4), doc="交易是否成功")
    TRADINGPOSITIONID = Column(String(40), doc="上市公司交易地位编码")
    TRADINGPOSITION = Column(String(100), doc="上市公司交易地位")
    RESTRUCTURINGTYPE = Column(String(100), doc="重组类型")
    RESTRUCTURINGTYPEID = Column(String(100), doc="重组类型编码")
    UNDERLYINGTYPE = Column(String(100), doc="标的分类")
    UNDERLYINGTYPEID = Column(String(40), doc="标的分类编码")
    UNDERLYINGVALUE = Column(DECIMAL(20, 4), doc="卖方标的价值 屏蔽")
    EXPENSEVALUE = Column(DECIMAL(20, 4), doc="买方支出价值")
    RELEVANCESIGN = Column(String(4), doc="关联交易标识")
    MAJORRESTRUCTURINGSIGN = Column(String(4), doc="重大资产重组标识")
    ASSESSINSTITUTION = Column(String(400), doc="上市公司聘请的资产评估机构")
    FINANCIALADVISER = Column(String(400), doc="上市公司聘请的财务顾问")
    ACCOUNTINGFIRM = Column(String(400), doc="上市公司聘请的会计师事务所")
    LAWFIRM = Column(String(400), doc="上市公司聘请的律师事务所")
    OUTLINE = Column(LONGTEXT, doc="交易概述")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    LATESTDECLAREDATE = Column(DateTime, doc="最新公告日期")
    PAYTYPEID = Column(String(40), doc="支付方式编码")
    LATESTPROGRAMSCHEDULE = Column(String(40), doc="最新进度")
    LATESTPROGRAMSCHEDULEID = Column(String(10), doc="最新进度编码")
    MERGERTYPE = Column(String(40), doc="并购类型")
    MERGERTYPEID = Column(String(2), doc="并购类型编码")
    ISINTELPROMA = Column(String(2), doc="是否涉及知识产权并购")
    BUYER = Column(String(4000), doc="买方")
    SELLER = Column(String(4000), doc="卖方")
    UNDERLYING = Column(String(4000), doc="标的方")
    BOOKVALUE = Column(DECIMAL(20, 4), doc="标的账面价值")
    EVALUATIONVALUE = Column(DECIMAL(20, 4), doc="标的评估价值")
    EVALUATIONCHANGE = Column(DECIMAL(20, 4), doc="评估增值")
    EVALUATIONRATIO = Column(DECIMAL(20, 4), doc="评估增值率")
    EVALUATIONBASEDAY = Column(DateTime, doc="评估基准日")
    EVALUATIONMETHOD = Column(String(200), doc="评估方法")
    APPRSREPTNO = Column(String(100), doc="资产评估披露文档号")
    PAYTYPE = Column(String(100), doc="支付方式")
    SOURCETYPEID = Column(String(50), doc="资金来源编码")
    SOURCETYPE = Column(String(200), doc="资金来源")
    MAREGIONTYPEID = Column(String(10), doc="并购地区类型编码")
    MAREGIONTYPE = Column(String(100), doc="并购地区类型")
    CROSSPROVINCESIGN = Column(String(2), doc="跨省并购标识")
    CROSSCITYSIGN = Column(String(2), doc="跨市并购标识")


class stk_ma_tradingschedule(Base):

    __tablename__ = 'stk_ma_tradingschedule'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    SCHEDULEDATE = Column(DateTime, doc="进度日期")
    PROGRAMSCHEDULE = Column(String(100), doc="方案进度")
    PROGRAMSCHEDULEID = Column(String(100), doc="方案进度编码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    PROGRAMCONTENT = Column(LONGTEXT, doc="进度内容")
    RANK = Column(SMALLINT, doc="序号")


class stk_ma_underlying(Base):

    __tablename__ = 'stk_ma_underlying'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    RANK = Column(BIGINT, doc="序号")
    UNDERLYINGNAME = Column(String(1400), doc="标的物名称")
    SYMBOL = Column(String(20), doc="标的证券代码")
    OWNERSHIP = Column(String(1000), doc="标的权属")
    PROPERTYID = Column(String(40), doc="股份性质编码")
    PROPERTY = Column(String(200), doc="股份性质")
    NETASSETSPERSHARE = Column(DECIMAL(20, 4), doc="每股净资产")
    VOLUME = Column(BIGINT, doc="转让股数")
    PROPORTION = Column(DECIMAL(10, 4), doc="转让比例")
    BOOKVALUE = Column(DECIMAL(20, 4), doc="账面价值")
    EVALUATIONVALUE = Column(DECIMAL(20, 4), doc="评估价值")
    BASEDAY = Column(DateTime, doc="评估基准日")
    EXPLANATION = Column(String(4000), doc="标的物说明")
    GUARANTEEID = Column(String(40), doc="担保情况编码")
    GUARANTEE = Column(String(200), doc="担保情况")
    OPERATION = Column(String(2000), doc="运营情况")
    AMOUNTTOBUYERTOTALASSETS = Column(DECIMAL(10, 4), doc="资产交易金额占买方比")
    AMOUNTTOSELLERTOTALASSETS = Column(DECIMAL(10, 4), doc="资产交易金额占卖方比")
    OTHERNOTES = Column(String(4000), doc="其他情况说明")
    BEQUITYPROPORTIONBEFORE = Column(DECIMAL(10, 4), doc="买前股比")
    BSTATUSBEFOREID = Column(String(40), doc="买前地位编码")
    BSTATUSBEFORE = Column(String(200), doc="买前地位")
    BEQUITYPROPORTIONAFTER = Column(DECIMAL(10, 4), doc="买后股比")
    BSTATUSAFTERID = Column(String(40), doc="买后地位编码")
    BSTATUSAFTER = Column(String(200), doc="买后地位")
    SEQUITYPROPORTIONBEFORE = Column(DECIMAL(10, 4), doc="卖前股比")
    SSTATUSBEFOREID = Column(String(40), doc="卖前地位编码")
    SSTATUSBEFORE = Column(String(200), doc="卖前地位")
    SEQUITYPROPORTIONAFTER = Column(DECIMAL(10, 4), doc="卖后股比")
    SSTATUSAFTERID = Column(String(40), doc="卖后地位编码")
    SSTATUSAFTER = Column(String(200), doc="卖后地位")
    APPRSREPTNO = Column(String(100), doc="资产评估披露文档号")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    EVALUATIONCHANGE = Column(DECIMAL(20, 4), doc="评估增值")
    EVALUATIONRATIO = Column(DECIMAL(20, 4), doc="评估增值率")
    EVALUATIONMETHOD = Column(String(200), doc="评估方法")


class stk_mkt_adjustfactor(Base):

    __tablename__ = 'stk_mkt_adjustfactor'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    FWARDFACTOR = Column(DECIMAL(12, 6), doc="前复权因子")
    BWARDFACTOR = Column(DECIMAL(12, 6), doc="后复权因子")
    CUMULATEFWARDFACTOR = Column(DECIMAL(12, 6), doc="前累计复权因子")
    CUMULATEBWARDFACTOR = Column(DECIMAL(12, 6), doc="后累计复权因子")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_mkt_blocktrade(Base):

    __tablename__ = 'stk_mkt_blocktrade'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SERIALNUMBER = Column(SMALLINT, doc="交易序列号")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    SECURITYTYPEID = Column(String(12), doc="证券类型编码")
    SECURITYTYPE = Column(String(40), doc="证券类型")
    EXCHANGECODE = Column(String(40), doc="市场类型编码")
    EXCHANGETYPE = Column(String(60), doc="市场类型")
    PRICE = Column(DECIMAL(10, 3), doc="成交价")
    PRICEUNIT = Column(String(20), doc="成交价对应单位")
    VOLUME = Column(DECIMAL(22, 6), doc="成交量")
    VOLUMEUNIT = Column(String(20), doc="成交量对应单位")
    AMOUNT = Column(DECIMAL(26, 6), doc="成交额")
    AMOUNTUNIT = Column(String(20), doc="成交额对应单位")
    SELLER = Column(String(160), doc="卖方营业部名称")
    BUYER = Column(String(160), doc="买方营业部名称")
    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_mkt_capitalflow(Base):

    __tablename__ = 'stk_mkt_capitalflow'

    SECURITYID = Column(DECIMAL(20, 0))
    SYMBOL = Column(String(12))
    TRADINGDATE = Column(DateTime)
    MAINBUYAMOUNT = Column(DECIMAL(20, 2))
    MAINSELLAMOUNT = Column(DECIMAL(20, 2))
    INSBUYAMOUNT = Column(DECIMAL(20, 2))
    INSSELLAMOUNT = Column(DECIMAL(20, 2))
    BIGBUYAMOUNT = Column(DECIMAL(20, 2))
    BIGSELLAMOUNT = Column(DECIMAL(20, 2))
    MIDBUYAMOUNT = Column(DECIMAL(20, 2))
    MIDSELLAMOUNT = Column(DECIMAL(20, 2))
    SMALLBUYAMOUNT = Column(DECIMAL(20, 2))
    SMALLSELLAMOUNT = Column(DECIMAL(20, 2))
    MAINBUYVOLUME = Column(DECIMAL(20, 0))
    MAINSELLVOLUME = Column(DECIMAL(20, 0))
    INSBUYVOLUME = Column(DECIMAL(20, 0))
    INSSELLVOLUME = Column(DECIMAL(20, 0))
    BIGBUYVOLUME = Column(DECIMAL(20, 0))
    BIGSELLVOLUME = Column(DECIMAL(20, 0))
    MIDBUYVOLUME = Column(DECIMAL(20, 0))
    MIDSELLVOLUME = Column(DECIMAL(20, 0))
    SMALLBUYVOLUME = Column(DECIMAL(20, 0))
    SMALLSELLVOLUME = Column(DECIMAL(20, 0))
    MAININTBUYAMOUNT = Column(DECIMAL(20, 2))
    MAININTSELLAMOUNT = Column(DECIMAL(20, 2))
    INSINTBUYAMOUNT = Column(DECIMAL(20, 2))
    INSINTSELLAMOUNT = Column(DECIMAL(20, 2))
    BIGINTBUYAMOUNT = Column(DECIMAL(20, 2))
    BIGINTSELLAMOUNT = Column(DECIMAL(20, 2))
    MIDINTBUYAMOUNT = Column(DECIMAL(20, 2))
    MIDINTSELLAMOUNT = Column(DECIMAL(20, 2))
    SMALLINTBUYAMOUNT = Column(DECIMAL(20, 2))
    SMALLINTSELLAMOUNT = Column(DECIMAL(20, 2))
    MAININTBUYVOLUME = Column(DECIMAL(20, 0))
    MAININTSELLVOLUME = Column(DECIMAL(20, 0))
    INSINTBUYVOLUME = Column(DECIMAL(20, 0))
    INSINTSELLVOLUME = Column(DECIMAL(20, 0))
    BIGINTBUYVOLUME = Column(DECIMAL(20, 0))
    BIGINTSELLVOLUME = Column(DECIMAL(20, 0))
    MIDINTBUYVOLUME = Column(DECIMAL(20, 0))
    MIDINTSELLVOLUME = Column(DECIMAL(20, 0))
    SMALLINTBUYVOLUME = Column(DECIMAL(20, 0))
    SMALLINTSELLVOLUME = Column(DECIMAL(20, 0))
    TICKNUMBER = Column(DECIMAL(20, 0))
    MAINBUYORDER = Column(DECIMAL(20, 0))
    MAINSELLORDER = Column(DECIMAL(20, 0))
    INSBUYORDER = Column(DECIMAL(20, 0))
    INSSELLORDER = Column(DECIMAL(20, 0))
    BIGBUYORDER = Column(DECIMAL(20, 0))
    BIGSELLORDER = Column(DECIMAL(20, 0))
    MIDBUYORDER = Column(DECIMAL(20, 0))
    MIDSELLORDER = Column(DECIMAL(20, 0))
    SMALLBUYORDER = Column(DECIMAL(20, 0))
    SMALLSELLORDER = Column(DECIMAL(20, 0))
    MAINNETBUYVOLUME = Column(DECIMAL(20, 0))
    MAININTNETBUYVOLUME = Column(DECIMAL(20, 0))
    INSNETBUYVOLUME = Column(DECIMAL(20, 0))
    INSINTNETBUYVOLUME = Column(DECIMAL(20, 0))
    BIGNETBUYVOLUME = Column(DECIMAL(20, 0))
    BIGINTNETBUYVOLUME = Column(DECIMAL(20, 0))
    MIDNETBUYVOLUME = Column(DECIMAL(20, 0))
    MIDINTNETBUYVOLUME = Column(DECIMAL(20, 0))
    SMALLNETBUYVOLUME = Column(DECIMAL(20, 0))
    SMALLINTNETBUYVOLUME = Column(DECIMAL(20, 0))
    MAINNETBUYAMOUNT = Column(DECIMAL(20, 2))
    MAININTNETBUYAMOUNT = Column(DECIMAL(20, 2))
    INSNETBUYAMOUNT = Column(DECIMAL(20, 2))
    INSINTNETBUYAMOUNT = Column(DECIMAL(20, 2))
    BIGNETBUYAMOUNT = Column(DECIMAL(20, 2))
    BIGINTNETBUYAMOUNT = Column(DECIMAL(20, 2))
    MIDNETBUYAMOUNT = Column(DECIMAL(20, 2))
    MIDINTNETBUYAMOUNT = Column(DECIMAL(20, 2))
    SMALLNETBUYAMOUNT = Column(DECIMAL(20, 2))
    SMALLINTNETBUYAMOUNT = Column(DECIMAL(20, 2))
    NETVOLUME = Column(DECIMAL(20, 0))
    NETVOLUMERATIO = Column(DECIMAL(6, 4))
    OPENNETVOLUME = Column(DECIMAL(20, 0))
    OPENNETVOLUMERATIO = Column(DECIMAL(6, 4))
    CLOSENETVOLUME = Column(DECIMAL(20, 0))
    CLOSENETVOLUMERATIO = Column(DECIMAL(6, 4))
    NETAMOUNT = Column(DECIMAL(20, 2))
    NETAMOUNTRATIO = Column(DECIMAL(6, 4))
    OPENNETAMOUNT = Column(DECIMAL(20, 2))
    OPENNETAMOUNTRATIO = Column(DECIMAL(6, 4))
    CLOSENETAMOUNT = Column(DECIMAL(20, 2))
    CLOSENETAMOUNTRATIO = Column(DECIMAL(6, 4))
    COMMITBUYVOLUME = Column(DECIMAL(20, 0))
    COMMITSELLVOLUME = Column(DECIMAL(20, 0))
    VOLUMEFLOWRATIO = Column(DECIMAL(6, 4))
    OPENVOLUMEFLOWRATIO = Column(DECIMAL(6, 4))
    CLOSEVOLUMEFLOWRATIO = Column(DECIMAL(6, 4))
    AMOUNTFLOWRATIO = Column(DECIMAL(6, 4))
    OPENAMOUNTFLOWRATIO = Column(DECIMAL(6, 4))
    CLOSEAMOUNTFLOWRATIO = Column(DECIMAL(6, 4))
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_mkt_capitalflows(Base):

    __tablename__ = 'stk_mkt_capitalflows'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(12), doc="股票代码")
    EXCHANGECODE = Column(String(40), doc="市场代码")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    BUYORSELL = Column(String(2), doc="内外盘标识")
    M_SMALL = Column(DECIMAL(20, 3), doc="小单")
    M_MID = Column(DECIMAL(20, 3), doc="中单")
    M_BIG = Column(DECIMAL(20, 3), doc="大单")
    M_BIGGER = Column(DECIMAL(20, 3), doc="超大单")
    M_SUPER = Column(DECIMAL(20, 3), doc="巨额成交单")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_mkt_divident(Base):

    __tablename__ = 'stk_mkt_divident'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    EXDIVIDENDDATE = Column(DateTime, doc="除权除息日")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    SYMBOL = Column(String(12), doc="证券代码")
    RECORDDATE = Column(DateTime, doc="股权登记日")
    FINALTRADINGDATE = Column(DateTime, doc="最后交易日（B股）")
    PAYMENTDATE = Column(DateTime, doc="派息日")
    CURRENCYCODE = Column(String(40), doc="货币类型")
    ALLOTMENTPRICE = Column(DECIMAL(10, 4), doc="配股价格")
    ALLOTMENTPERSHARE = Column(DECIMAL(10, 6), doc="配股比例")
    DIVIDENTBT = Column(DECIMAL(10, 6), doc="每股分红（税前）")
    DIVIDENTAT = Column(DECIMAL(10, 6), doc="每股分红（税后）")
    BONUSRATIO = Column(DECIMAL(10, 6), doc="送股比例")
    CONVERSIONRATIO = Column(DECIMAL(10, 6), doc="转增比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class stk_mkt_dividentnew(Base):

    __tablename__ = 'stk_mkt_dividentnew'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    EXDIVIDENDDATE = Column(DateTime, primary_key=True, doc="除权除息日")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    SYMBOL = Column(String(12), doc="证券代码")
    RECORDDATE = Column(DateTime, doc="股权登记日")
    FINALTRADINGDATE = Column(DateTime, doc="最后交易日(B股)")
    PAYMENTDATE = Column(DateTime, doc="派息日期")
    CURRENCYCODE = Column(String(40), doc="货币类型")
    ALLOTMENTPRICE = Column(DECIMAL(12, 6), doc="配股价格")
    ALLOTMENTPERSHARE = Column(DECIMAL(12, 6), doc="配股比例")
    DIVIDENTBT = Column(DECIMAL(12, 6), doc="每股分红(税前)")
    DIVIDENTAT = Column(DECIMAL(12, 6), doc="每股分红(税后)")
    BONUSRATIO = Column(DECIMAL(12, 6), doc="送股比例")
    SPLITRATIO = Column(DECIMAL(12, 6), doc="拆分比例")
    UPDATEID = Column(BIGINT, doc="数据ID")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class stk_mkt_exchangerate(Base):

    __tablename__ = 'stk_mkt_exchangerate'

    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    WEEKDAY = Column(SMALLINT, doc="星期")
    CNYTOUSD = Column(DECIMAL(10, 4), doc="人民币对美元")
    HKDTOCNY = Column(DECIMAL(10, 4), doc="人民币对港元")
    HKDTOUSD = Column(DECIMAL(10, 4), doc="港元对美元")
    CROSSHKDTOCNY = Column(DECIMAL(10, 4), doc="人民币对港元换算后")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_mkt_nightcale(Base):

    __tablename__ = 'stk_mkt_nightcale'

    CALENDARDATE = Column(DateTime, doc="日历日期")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    ISOPEN = Column(String(2), doc="开市与否")
    WEEKDAY = Column(SMALLINT, doc="星期")
    SECURITYTYPE = Column(String(100), doc="证券品种")
    TRADINGTYPE = Column(String(100), doc="交易品种")
    VARIETYID = Column(DECIMAL(20, 0), doc="品种ID")
    ISNIGHTTRADING = Column(SMALLINT, doc="夜盘标识")
    NIGHTTRADINGSTARTTIMEA = Column(String(100), doc="夜盘交易夜晚开始时间")
    NIGHTTRADINGENDTIMEA = Column(String(100), doc="夜盘交易夜晚结束时间")
    NIGHTTRADINGDATEA = Column(DateTime, doc="夜盘夜晚交易所属业务日期")
    NIGHTTRADINGSTARTTIMEB = Column(String(100), doc="夜盘交易白天开始时间")
    NIGHTTRADINGENDTIMEB = Column(String(100), doc="夜盘交易白天结束时间")
    NIGHTTRADINGDATEB = Column(DateTime, doc="夜盘白天交易所属业务日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_mkt_quotation(Base):

    __tablename__ = 'stk_mkt_quotation'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    SHORTNAME = Column(String(20), doc="股票简称")
    FILLING = Column(String(20), doc="填充标识")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘(交易所)")
    OPENPRICE = Column(DECIMAL(10, 3), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="最低价")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 0), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    STATECODE = Column(String(40), doc="交易状态编码")
    AVGPRICE = Column(DECIMAL(10, 3), doc="均价")
    CHANGE = Column(DECIMAL(10, 3), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 5), doc="涨跌幅")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TURNOVERRATE1 = Column(DECIMAL(10, 5), doc="换手率")
    TURNOVERRATE2 = Column(DECIMAL(10, 5), doc="换手率（基准.自由流通股本）")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="总市值")
    CIRCULATEDMARKETVALUE = Column(DECIMAL(20, 2), doc="流通市值")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="振幅")
    RELATIVEIPOCHANGE = Column(DECIMAL(10, 3), doc="相对发行价涨跌")
    RELATIVEIPOCHANGERATIO = Column(DECIMAL(10, 5), doc="相对发行价涨跌幅")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    MINTICKSIZE = Column(DECIMAL(16, 4), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 3), doc="跌停价格")
    LIMITUP = Column(DECIMAL(10, 3), doc="涨停价")
    ACIRCULATEDSHARE = Column(DECIMAL(20, 2), doc="流通A股股本")
    BCIRCULATEDSHARE = Column(DECIMAL(20, 2), doc="流通B股股本")
    AVALUE = Column(DECIMAL(20, 2), doc="流通A股市值")
    BVALUE = Column(DECIMAL(20, 2), doc="流通B股市值")
    LIMITSTATUS = Column(SMALLINT, doc="涨跌停状态")
    AFTERHOURSVOLUME = Column(BIGINT, doc="盘后成交量")
    AFTERHOURSAMOUNT = Column(DECIMAL(20, 0), doc="盘后成交金额")


class stk_mkt_quotationlatest(Base):

    __tablename__ = 'stk_mkt_quotationlatest'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    SHORTNAME = Column(String(20), doc="股票简称")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘(交易所)")
    OPENPRICE = Column(DECIMAL(10, 3), doc="开盘价")
    CLOSEPRICE = Column(DECIMAL(10, 3), doc="收盘价")
    HIGHPRICE = Column(DECIMAL(10, 3), doc="最高价")
    LOWPRICE = Column(DECIMAL(10, 3), doc="最低价")
    VOLUME = Column(BIGINT, doc="成交量")
    AMOUNT = Column(DECIMAL(20, 0), doc="成交金额")
    LATESTCLOSEPRICE = Column(DECIMAL(10, 3), doc="前收盘价")
    LATESTTRADINGDATE = Column(DateTime, doc="前交易日期")
    DISTANCE = Column(INTEGER, doc="距前交易日天数")
    STATECODE = Column(String(40), doc="交易状态编码")
    AVGPRICE = Column(DECIMAL(10, 3), doc="均价")
    CHANGE = Column(DECIMAL(10, 3), doc="涨跌")
    CHANGERATIO = Column(DECIMAL(10, 5), doc="涨跌幅")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TURNOVERRATE1 = Column(DECIMAL(10, 5), doc="换手率")
    TURNOVERRATE2 = Column(DECIMAL(10, 5), doc="换手率（基准.自由流通股本）")
    MARKETVALUE = Column(DECIMAL(20, 2), doc="总市值")
    CIRCULATEDMARKETVALUE = Column(DECIMAL(20, 2), doc="流通市值")
    AMPLITUDE = Column(DECIMAL(16, 6), doc="振幅")
    RELATIVEIPOCHANGE = Column(DECIMAL(10, 3), doc="相对发行价涨跌")
    RELATIVEIPOCHANGERATIO = Column(DECIMAL(10, 5), doc="相对发行价涨跌幅")
    UPDATEID = Column(BIGINT, doc="数据ID")
    MINTICKSIZE = Column(DECIMAL(10, 2), doc="价格档位")
    LIMITDOWN = Column(DECIMAL(10, 3), doc="跌停价格")
    LIMITUP = Column(DECIMAL(10, 3), doc="涨停价")
    ACIRCULATEDSHARE = Column(DECIMAL(20, 2), doc="流通A股股本")
    BCIRCULATEDSHARE = Column(DECIMAL(20, 2), doc="流通B股股本")
    AVALUE = Column(DECIMAL(20, 2), doc="流通A股市值")
    BVALUE = Column(DECIMAL(20, 2), doc="流通B股市值")
    LIMITSTATUS = Column(SMALLINT, doc="涨跌停状态")
    AFTERHOURSVOLUME = Column(BIGINT, doc="盘后成交量")
    AFTERHOURSAMOUNT = Column(DECIMAL(20, 0), doc="盘后成交金额")


class stk_mkt_repricefactor(Base):

    __tablename__ = 'stk_mkt_repricefactor'

    SECURITYID = Column(DECIMAL(20, 0), primary_key=True, doc="证券ID")
    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), doc="证券代码")
    FWARDFACTOR1 = Column(DECIMAL(12, 6), doc="前复权因子")
    CUMULATEFWARDFACTOR1 = Column(DECIMAL(12, 6), doc="前累计复权因子")
    EXDIVIDENDFWARDFACTOR1 = Column(DECIMAL(12, 6), doc="不考虑现金分红的前复权因子")
    EXDIVIDENDCUMULATEFFACTOR1 = Column(DECIMAL(12, 6), doc="不考虑现金分红的前累计复权因子")
    FWARDFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑拆分、股改的前复权因子")
    CUMULATEFWARDFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑拆分、股改的前累计复权因子")
    EXDIVIDENDFWARDFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑现金分红、拆分、股改的前复权因子")
    EXDIVIDENDCUMULATEFFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑现金分红、拆分、股改的前累计复权因子")
    BWARDFACTOR1 = Column(DECIMAL(12, 6), doc="后复权因子")
    CUMULATEBWARDFACTOR1 = Column(DECIMAL(12, 6), doc="后累计复权因子")
    EXDIVIDENDBWARDFACTOR1 = Column(DECIMAL(12, 6), doc="不考虑现金分红的后复权因子")
    EXDIVIDENDCUMULATEBFACTOR1 = Column(DECIMAL(12, 6), doc="不考虑现金分红的后累计复权因子")
    BWARDFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑拆分、股改的后复权因子")
    CUMULATEBWARDFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑拆分、股改的后累计复权因子")
    EXDIVIDENDBWARDFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑现金分红、拆分、股改的后复权因子")
    EXDIVIDENDCUMULATEBFACTOR2 = Column(DECIMAL(12, 6), doc="不考虑现金分红、拆分、股改的后累计复权因子")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_notes_accountingpolicy(Base):

    __tablename__ = 'stk_notes_accountingpolicy'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    ITEMID = Column(String(400), doc="项目编码")
    ITEMEXPLANATION = Column(LONGTEXT, doc="项目说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_adminexpense(Base):

    __tablename__ = 'stk_notes_adminexpense'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_afsfinassect(Base):

    __tablename__ = 'stk_notes_afsfinassect'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    ITEM_EN = Column(String(1000), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_ap(Base):

    __tablename__ = 'stk_notes_ap'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    AGE = Column(String(200), doc="账龄")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    BEGINNINGPROPORTION = Column(DECIMAL(20, 4), doc="期初比例")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    ENDINGPROPORTION = Column(DECIMAL(20, 4), doc="期末比例")
    REASONSCHANGES = Column(LONGTEXT, doc="变动原因")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_apsd(Base):

    __tablename__ = 'stk_notes_apsd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    VESTINGPERIOD = Column(SMALLINT, doc="期间归属")
    SPECIALDISCLOSEREASONS = Column(String(1000), doc="特别披露原因")
    ITEM = Column(String(400), doc="单位或项目名称")
    DATEOCCURRENCE = Column(String(400), doc="发生日期")
    ARREARSAGING = Column(String(400), doc="欠款帐龄")
    MONEY = Column(DECIMAL(20, 4), doc="金额")
    PROPORTIONOFTOTALAP = Column(DECIMAL(20, 4), doc="占应付帐款总额的比例")
    RELATIONSHIPWITHCOMPANY = Column(String(200), doc="与本公司关系")
    PAYMENTINSTRUCTIONS = Column(LONGTEXT, doc="款项说明")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    RANK = Column(SMALLINT, doc="排名")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_ar(Base):

    __tablename__ = 'stk_notes_ar'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    ITEM = Column(String(400), doc="项目名称")
    AGE = Column(String(200), doc="账龄")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    BEGINNINGPROPORTION = Column(DECIMAL(20, 4), doc="期初比例")
    BEGINNINGBADDEBTPROVISION = Column(DECIMAL(20, 4), doc="期初坏账准备金额")
    BEGINNINGBADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="期初坏账准备计提比例")
    BEGINNINGNETVALUE = Column(DECIMAL(20, 4), doc="期初净额")
    BADDEBTPROVISIONINCREASE = Column(DECIMAL(20, 4), doc="坏账准备本期增加")
    BADDEBTPROVISIONREDUCE = Column(DECIMAL(20, 4), doc="坏账准备本期减少")
    BADDEBTPROVISIONREVERSAL = Column(DECIMAL(20, 4), doc="其中：坏账准备本期转回")
    BADDEBTPROVISIONWRITEOFF = Column(DECIMAL(20, 4), doc="其中：坏账准备本期冲销")
    BADDEBTPROVISIONOTHER = Column(DECIMAL(20, 4), doc="其中：其他")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    ENDINGPROPORTION = Column(DECIMAL(20, 4), doc="期末比例")
    ENDINGBADDEBTPROVISION = Column(DECIMAL(20, 4), doc="期末坏账准备金额")
    ENDINGBADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="期末坏账准备计提比例")
    ENDINGNETVALUE = Column(DECIMAL(20, 4), doc="期末净额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_arsd(Base):

    __tablename__ = 'stk_notes_arsd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    VESTINGPERIOD = Column(SMALLINT, doc="期间归属")
    SPECIALDISCLOSEREASONS = Column(String(1000), doc="特别披露原因")
    ITEM = Column(String(600), doc="单位或项目名称")
    AGEORDATE = Column(String(400), doc="欠款帐龄或日期")
    MONEY = Column(DECIMAL(20, 4), doc="金额")
    PROPORTIONOFTOTALAR = Column(DECIMAL(20, 4), doc="占应收账款总额的比例")
    BADDEBTPROVISION = Column(DECIMAL(20, 4), doc="坏账准备金额")
    BADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="坏账准备计提比例")
    RELATIONSHIPWITHCOMPANY = Column(String(200), doc="与本公司关系")
    REASONFORPROVISION = Column(LONGTEXT, doc="计提理由")
    PAYMENTINSTRUCTIONS = Column(LONGTEXT, doc="款项说明")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    RANK = Column(SMALLINT, doc="排名")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_assetimpairment(Base):

    __tablename__ = 'stk_notes_assetimpairment'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(200), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    CURRENTPROVISION = Column(DECIMAL(20, 4), doc="本期增加额-本期计提额")
    ADDOTHER = Column(DECIMAL(20, 4), doc="本期增加额-其他")
    CURRENTREVERSAL = Column(DECIMAL(20, 4), doc="本期减少额-转回数")
    CURRENTRESELLER = Column(DECIMAL(20, 4), doc="本期减少额-转销数")
    LOWEROTHER = Column(DECIMAL(20, 4), doc="本期减少额-其他")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_basiccontent(Base):

    __tablename__ = 'stk_notes_basiccontent'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    GENERALSITUATION = Column(LONGTEXT, doc="公司基本情况")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_billrandp(Base):

    __tablename__ = 'stk_notes_billrandp'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    TYPEOFNOTECODE = Column(String(20), doc="票据种类编码")
    TYPEOFNOTE = Column(String(400), doc="票据种类")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_billrandpspecial(Base):

    __tablename__ = 'stk_notes_billrandpspecial'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    SPECIALDISCLOSEREASONS = Column(String(2000), doc="特别披露原因")
    COMPANY = Column(String(1000), doc="出票单位")
    DATEOFISSUE = Column(String(40), doc="出票日期")
    EXPIRATIONDATE = Column(String(40), doc="到期日")
    TYPEOFNOTECODE = Column(String(20), doc="票据种类编码")
    TYPEOFNOTE = Column(String(400), doc="票据种类")
    POSITIONVALUE = Column(DECIMAL(20, 2), doc="金额")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_bondspayable(Base):

    __tablename__ = 'stk_notes_bondspayable'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    RANK = Column(BIGINT, doc="序号")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    SPECIES = Column(String(1000), doc="种类")
    DEADLINE = Column(String(200), doc="期限")
    ISSUEDATE = Column(String(200), doc="发行日期")
    MATURITYDATE = Column(String(200), doc="到期日")
    COUPONRATE = Column(DECIMAL(20, 4), doc="票面利率")
    PARVALUETOTAL = Column(DECIMAL(20, 4), doc="面值总额")
    ISSUEAMOUNT = Column(DECIMAL(20, 4), doc="发行金额")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初余额")
    INCREASEDURINGYEAR = Column(DECIMAL(20, 4), doc="本期增加额")
    DECREASEDURINGYEAR = Column(DECIMAL(20, 4), doc="本期减少额")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="期末余额")
    BEGINNINGINTERESTPAYABLE = Column(DECIMAL(20, 4), doc="期初应付利息")
    CURRENTACCRUEDINTEREST = Column(DECIMAL(20, 4), doc="本期应计利息")
    CURRENTINTERESTPAID = Column(DECIMAL(20, 4), doc="本期已付利息")
    ENDINGINTERESTPAYABLE = Column(DECIMAL(20, 4), doc="期末应付利息")
    CURRENCY = Column(String(12), doc="币种")
    SPAREA = Column(String(400), doc="备用1")
    SPAREANUM = Column(DECIMAL(20, 4), doc="备用1（NUM）")
    SPAREB = Column(String(400), doc="备用2")
    SPAREBNUM = Column(DECIMAL(20, 4), doc="备用2（NUM）")
    SPAREC = Column(String(400), doc="备用3")
    SPARECCHA = Column(String(400), doc="备用3（CHA）")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_businesstaxappend(Base):

    __tablename__ = 'stk_notes_businesstaxappend'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    TAXTYPE = Column(String(200), doc="税种")
    TAXBASIS = Column(String(400), doc="计税基础")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_capitalreserve(Base):

    __tablename__ = 'stk_notes_capitalreserve'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 2), doc="本期增加数")
    CURRENTDECREASE = Column(DECIMAL(20, 2), doc="本期减少数")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_capitalstock(Base):

    __tablename__ = 'stk_notes_capitalstock'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ARECIRCULATION = Column(SMALLINT, doc="是否流通")
    STOCKTYPEDETAILS = Column(String(1000), doc="股票种类明细")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    CONVERSIONCONVERTIBLEBONDS = Column(DECIMAL(20, 4), doc="可转债转股")
    PLACEMENT = Column(DECIMAL(20, 4), doc="配股")
    BONUS = Column(DECIMAL(20, 4), doc="送股")
    ADDITIONAL = Column(DECIMAL(20, 4), doc="增发")
    CONVERSED = Column(DECIMAL(20, 4), doc="转增")
    OTHERCHANGES = Column(DECIMAL(20, 4), doc="其他变动")
    SUBTOTAL = Column(DECIMAL(20, 4), doc="变动金额（小计）")
    ADJUSTMENTSHAREREFORM = Column(DECIMAL(20, 4), doc="股改调整")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    VERIFICATIONINSTRUCTIONS = Column(String(4000), doc="验资说明")
    CURRENCY = Column(String(12), doc="币种")
    SPAREA = Column(String(400), doc="备用1")
    SPAREANUM = Column(DECIMAL(20, 4), doc="备用1（NUM）")
    SPAREB = Column(String(400), doc="备用2")
    SPAREBNUM = Column(DECIMAL(20, 4), doc="备用2（NUM）")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_cbd(Base):

    __tablename__ = 'stk_notes_cbd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    ITEM = Column(String(400), doc="项目名称")
    AGE = Column(String(200), doc="账龄")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    BEGINNINGPROPORTION = Column(DECIMAL(20, 4), doc="期初比例")
    BEGINNINGBADDEBTPROVISION = Column(DECIMAL(20, 4), doc="期初坏账准备金额")
    BEGINNINGBADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="期初坏账准备计提比例")
    BEGINNINGNETVALUE = Column(DECIMAL(20, 4), doc="期初净额")
    BADDEBTPROVISIONINCREASE = Column(DECIMAL(20, 4), doc="坏账准备本期增加")
    BADDEBTPROVISIONREDUCE = Column(DECIMAL(20, 4), doc="坏账准备本期减少")
    BADDEBTPROVISIONREVERSAL = Column(DECIMAL(20, 4), doc="其中：坏账准备本期转回")
    BADDEBTPROVISIONWRITEOFF = Column(DECIMAL(20, 4), doc="其中：坏账准备本期冲销")
    BADDEBTPROVISIONOTHER = Column(DECIMAL(20, 4), doc="其中：其他")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    ENDINGPROPORTION = Column(DECIMAL(20, 4), doc="期末比例")
    ENDINGBADDEBTPROVISION = Column(DECIMAL(20, 4), doc="期末坏账准备金额")
    ENDINGBADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="期末坏账准备计提比例")
    ENDINGNETVALUE = Column(DECIMAL(20, 4), doc="期末净额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_cbdsd(Base):

    __tablename__ = 'stk_notes_cbdsd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    VESTINGPERIOD = Column(SMALLINT, doc="期间归属")
    SPECIALDISCLOSEREASONS = Column(String(1000), doc="特别披露原因")
    ITEM = Column(String(400), doc="单位或项目名称")
    AGEORDATE = Column(String(400), doc="欠款帐龄或日期")
    MONEY = Column(DECIMAL(20, 4), doc="金额")
    PROPORTIONOFTOTALCBD = Column(DECIMAL(20, 4), doc="占预付款项总额的比例")
    BADDEBTPROVISION = Column(DECIMAL(20, 4), doc="坏账准备金额")
    BADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="坏账准备计提比例")
    RELATIONSHIPWITHCOMPANY = Column(String(200), doc="与本公司关系")
    REASONFORPROVISION = Column(LONGTEXT, doc="计提理由")
    PAYMENTINSTRUCTIONS = Column(LONGTEXT, doc="款项说明")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    RANK = Column(SMALLINT, doc="排名")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_cip(Base):

    __tablename__ = 'stk_notes_cip'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGBOOKBALANCE = Column(DECIMAL(20, 2), doc="期初账面余额")
    BEGINNINGIMPAIRMENTPROVISION = Column(DECIMAL(20, 2), doc="期初减值准备")
    BEGINNINGBOOKVALUE = Column(DECIMAL(20, 2), doc="期初账面价值")
    ENDINGBOOKBALANCE = Column(DECIMAL(20, 2), doc="期末账面余额")
    ENDINGIMPAIRMENTPROVISION = Column(DECIMAL(20, 2), doc="期末减值准备")
    ENDINGBOOKVALUE = Column(DECIMAL(20, 2), doc="期末账面价值")
    IMPAIRMENTPROVISIONINCREASE = Column(DECIMAL(20, 2), doc="本期增加减值准备")
    IMPAIRMENTPROVISIONDECREASE = Column(DECIMAL(20, 2), doc="本期减少减值准备")
    CURRENCYCODE = Column(String(12), doc="币种")
    REASONSINSTRUCTIONS = Column(String(1000), doc="减值准备计提原因")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_cipchange(Base):

    __tablename__ = 'stk_notes_cipchange'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BUDGETAMOUNT = Column(DECIMAL(20, 2), doc="预算数")
    BEGINNINGBALANCE = Column(DECIMAL(20, 2), doc="期初余额")
    NEWSUBSIDIARY = Column(DECIMAL(20, 2), doc="新增子公司转入数")
    CURRENTINCREASE = Column(DECIMAL(20, 2), doc="本期增加金额")
    INTOFIXEDASSETS = Column(DECIMAL(20, 2), doc="本期转入固定资产金额")
    INTOINTANGIBLEASSETS = Column(DECIMAL(20, 2), doc="本期转入无形资产金额")
    INTODEFERREDASSETS = Column(DECIMAL(20, 2), doc="本期转入长期待摊费用")
    OTHERDECREASE = Column(DECIMAL(20, 2), doc="本期其他减少金额")
    ENDINGBALANCE = Column(DECIMAL(20, 2), doc="期末余额")
    TOTALINPUTTOBUDGET = Column(DECIMAL(20, 2), doc="工程累计投入占预算比例")
    WORKINGSCHEDULE = Column(DECIMAL(20, 2), doc="工程进度")
    TOTALCAPITALIZINGINTEREST = Column(DECIMAL(20, 2), doc="利息资本化累计金额")
    CURRENTCAPITALIZINGINTEREST = Column(DECIMAL(20, 2), doc="其中：本期利息资本化金额")
    CAPITALIZINGINTERESTRATE = Column(DECIMAL(20, 2), doc="本期利息资本化率")
    CURRENCYCODE = Column(String(12), doc="币种")
    CAPITALSOURCE = Column(String(1000), doc="资金来源")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_deferredincometax(Base):

    __tablename__ = 'stk_notes_deferredincometax'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    DEFERREDINCOMETAXTYPE = Column(SMALLINT, doc="递延所得税类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    ITEM = Column(String(200), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    PICTUREEXPLANATION = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_devexpense(Base):

    __tablename__ = 'stk_notes_devexpense'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 4), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 4), doc="本期增加数")
    CURRENTDECREASE = Column(DECIMAL(20, 4), doc="本期减少数")
    PROFITORLOSS = Column(DECIMAL(20, 4), doc="其中：计入当期损益")
    CONFIRMINTANGIBLEASSETS = Column(DECIMAL(20, 4), doc="其中：确认为无形资产")
    ENDINGVALUE = Column(DECIMAL(20, 4), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_dividendpayable(Base):

    __tablename__ = 'stk_notes_dividendpayable'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_dr(Base):

    __tablename__ = 'stk_notes_dr'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    AGE = Column(String(200), doc="账龄")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    BEGINNINGPROPORTION = Column(DECIMAL(20, 4), doc="期初比例")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    ENDINGPROPORTION = Column(DECIMAL(20, 4), doc="期末比例")
    REASONSCHANGES = Column(LONGTEXT, doc="变动原因")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_drsd(Base):

    __tablename__ = 'stk_notes_drsd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    VESTINGPERIOD = Column(SMALLINT, doc="期间归属")
    SPECIALDISCLOSEREASONS = Column(String(1000), doc="特别披露原因")
    ITEM = Column(String(400), doc="单位或项目名称")
    DATEOCCURRENCE = Column(String(400), doc="发生日期")
    ARREARSAGING = Column(String(400), doc="欠款帐龄")
    MONEY = Column(DECIMAL(20, 4), doc="金额")
    PROPORTIONOFTOTALDR = Column(DECIMAL(20, 4), doc="占预收账款总额的比例")
    RELATIONSHIPWITHCOMPANY = Column(String(200), doc="与本公司关系")
    PAYMENTINSTRUCTIONS = Column(LONGTEXT, doc="款项说明")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    RANK = Column(SMALLINT, doc="排名")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_equityinvest(Base):

    __tablename__ = 'stk_notes_equityinvest'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    LONGTERMINVESTMENTPROJECTS = Column(String(1000), doc="长期投资项目")
    ACCOUNTINGMETHODS = Column(String(100), doc="核算方法")
    INVESTMENTCOST = Column(DECIMAL(20, 4), doc="投资成本")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    CHANGESVALUE = Column(DECIMAL(20, 4), doc="增减变动")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    SHAREHOLDINGSCALE = Column(String(100), doc="持股比例")
    VOTESCALE = Column(String(100), doc="表决权比例")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    PICTUREEXPLANATION = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_equityinvestcoinfo(Base):

    __tablename__ = 'stk_notes_equityinvestcoinfo'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    COMPANYNAME = Column(String(1000), doc="被投资单位名称")
    REGISTEREDCAPITAL = Column(DECIMAL(20, 4), doc="注册资本")
    REGISTEREDCAPITALCURRENCY = Column(String(12), doc="注册资本币种")
    YEARTOTALASSETS = Column(DECIMAL(20, 4), doc="本年资产总额")
    YEARTOTALLIABILITIES = Column(DECIMAL(20, 4), doc="本年负债总额")
    YEARTOTALOPERATINGINCOME = Column(DECIMAL(20, 4), doc="本年营业收入总额")
    PROFITFORTHEYEAR = Column(DECIMAL(20, 4), doc="本年净利润")
    CURRENCY = Column(String(12), doc="币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_fairvalueb(Base):

    __tablename__ = 'stk_notes_fairvalueb'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="分类")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初数")
    CURRENTFAIRVALUECHANGE = Column(DECIMAL(20, 2), doc="本期公允价值变动损益")
    FAIRVALUECHANGEINEQUITY = Column(DECIMAL(20, 2), doc="计入权益的累计公允价值变动")
    CURRENTIMPAIRMENT = Column(DECIMAL(20, 2), doc="本期计提的减值")
    CURRENTPURCHASE = Column(DECIMAL(20, 2), doc="本期购买金额")
    SALESSALES = Column(DECIMAL(20, 2), doc="本期出售金额")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末数")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    OTHERCHANGES = Column(DECIMAL(20, 2), doc="其他变动")


class stk_notes_financecosts(Base):

    __tablename__ = 'stk_notes_financecosts'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(SMALLINT, doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_fixedassect(Base):

    __tablename__ = 'stk_notes_fixedassect'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORYID = Column(String(200), doc="类别编码")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 4), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 4), doc="本期增加数")
    SUBSIDIARIESINCREASE = Column(DECIMAL(20, 4), doc="其中：增加子公司")
    PURCHASESINCREASE = Column(DECIMAL(20, 4), doc="其中：购置增加")
    CIPTRANSFER = Column(DECIMAL(20, 4), doc="其中：在建工程转入")
    OTHERSINCREASE = Column(DECIMAL(20, 4), doc="其中：其他")
    CURRENTDECREASE = Column(DECIMAL(20, 4), doc="本期减少数")
    SUBSIDIARIESDECREASE = Column(DECIMAL(20, 4), doc="其中：减少子公司")
    DISPOSALOFFIXEDASSETS = Column(DECIMAL(20, 4), doc="其中：固定资产清理")
    OTHERSDECREASE = Column(DECIMAL(20, 4), doc="其中：其他")
    ENDINGVALUE = Column(DECIMAL(20, 4), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    IMAGEREMARK = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_goodwill(Base):

    __tablename__ = 'stk_notes_goodwill'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    COMPANYNAMEORITEM = Column(String(1000), doc="单位名称或事项")
    BEGINNINGBALANCE = Column(DECIMAL(20, 2), doc="期初余额")
    CURRENTINCREASE = Column(DECIMAL(20, 2), doc="本期增加")
    MERGEINCREASE = Column(DECIMAL(20, 2), doc="其中：企业合并形成的增加")
    OTHERINCREASE = Column(DECIMAL(20, 2), doc="其中：其他增加")
    CURRENTDECREASE = Column(DECIMAL(20, 2), doc="本期减少")
    DISPOSEDECREASE = Column(DECIMAL(20, 2), doc="其中：处置形成的减少")
    OTHERDECREASE = Column(DECIMAL(20, 2), doc="其中：其他减少")
    ENDINGBALANCE = Column(DECIMAL(20, 2), doc="期末余额")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    CATEGORY = Column(SMALLINT, doc="科目类别")
    OTHER = Column(DECIMAL(20, 2), doc="其他")


class stk_notes_govgrants(Base):

    __tablename__ = 'stk_notes_govgrants'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(600), doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    ISDAILY = Column(SMALLINT, doc="是否与日常活动相关")


class stk_notes_impjntfin(Base):

    __tablename__ = 'stk_notes_impjntfin'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    ENDDATE = Column(DateTime, doc="年度区间")
    SGNRGN = Column(String(10), doc="区域标识")
    RALATEDPARTYID = Column(DECIMAL(20, 0), doc="关联公司ID")
    RALATEDPARTY = Column(String(200), doc="关联公司名称")
    RELATIONSHIPCODE = Column(String(6), doc="与上市公司关系编码")
    RELATIONSHIP = Column(String(100), doc="与上市公司关系")
    CURRENTASSETS = Column(DECIMAL(20, 2), doc="流动资产")
    NONCURRENTASSETS = Column(DECIMAL(20, 2), doc="非流动资产")
    TOTALASSETS = Column(DECIMAL(20, 2), doc="资产总计")
    CURRENTLIABILITY = Column(DECIMAL(20, 2), doc="流动负债")
    NONCURRENTLIABILITY = Column(DECIMAL(20, 2), doc="非流动负债")
    TOTALLIABILITY = Column(DECIMAL(20, 2), doc="负债总计")
    EQUITYPARENT = Column(DECIMAL(20, 2), doc="归属于母公司股东权益")
    NETASSETSBYSHARES = Column(DECIMAL(20, 2), doc="按持股比例计算的净资产份额")
    ADJUSTMENTS = Column(DECIMAL(20, 2), doc="调整事项")
    GOODWILL = Column(DECIMAL(20, 2), doc="其中：商誉")
    INTTRDUNRPROF = Column(DECIMAL(20, 2), doc="其中：内部交易未实现利润")
    OTHER = Column(DECIMAL(20, 2), doc="其中：其他（公允价值差额）")
    EQINVBOOKVALUE = Column(DECIMAL(20, 2), doc="权益投资的账面价值")
    EQINVFAIRVALUE = Column(DECIMAL(20, 2), doc="存在公开报价的联营/合营企业权益投资的公允价值")
    OPERATINGEVENUE = Column(DECIMAL(20, 2), doc="营业收入")
    NETPROFIT = Column(DECIMAL(20, 2), doc="净利润")
    DISCOPERNETPROFIT = Column(DECIMAL(20, 2), doc="终止经营的净利润")
    OTHERCOMPREHENSIVEINCOME = Column(DECIMAL(20, 2), doc="其他综合收益")
    COMPREHENSIVEINCOME = Column(DECIMAL(20, 2), doc="综合收益总额")
    RECEIVEDDIVIDEND = Column(DECIMAL(20, 2), doc="本年度收到的来自联营/合营企业的股利")
    CURRENCY = Column(String(1000), doc="币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_interestpayable(Base):

    __tablename__ = 'stk_notes_interestpayable'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 2), doc="本期增加数")
    CURRENTDECREASE = Column(DECIMAL(20, 2), doc="本期减少数")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_invassect(Base):

    __tablename__ = 'stk_notes_invassect'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORYID = Column(String(200), doc="类别编码")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 4), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 4), doc="本期增加数")
    CURRENTDECREASE = Column(DECIMAL(20, 4), doc="本期减少数")
    OTHERCHANGE = Column(DECIMAL(20, 4), doc="其他变动")
    ENDINGVALUE = Column(DECIMAL(20, 4), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    IMAGEREMARK = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_inventories(Base):

    __tablename__ = 'stk_notes_inventories'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGBOOKBALANCE = Column(DECIMAL(20, 2), doc="期初账面余额")
    BEGINNINGPROVISION = Column(DECIMAL(20, 2), doc="期初跌价准备")
    BEGINNINGBOOKVALUE = Column(DECIMAL(20, 2), doc="期初账面价值")
    PROVISIONINCREASE = Column(DECIMAL(20, 2), doc="跌价准备本期增加")
    PROVISIONREDUCE = Column(DECIMAL(20, 2), doc="跌价准备本期减少")
    REVERSEDPROVISION = Column(DECIMAL(20, 2), doc="其中：跌价准备本期转回")
    WRITEOFFPROVISION = Column(DECIMAL(20, 2), doc="其中：跌价准备本期冲销")
    OTHERPROVISIONREDUCE = Column(DECIMAL(20, 2), doc="其中：跌价准备本期其他减少")
    ENDINGBOOKBALANCE = Column(DECIMAL(20, 2), doc="期末账面余额")
    ENDINGPROVISION = Column(DECIMAL(20, 2), doc="期末跌价准备")
    ENDINGBOOKVALUE = Column(DECIMAL(20, 2), doc="期末账面价值")
    RPROVISIONTOENDBALANCE = Column(DECIMAL(20, 2), doc="本期转回金额占该项存货期末余额比例")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    IMAGEREMARK = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_investmentinc(Base):

    __tablename__ = 'stk_notes_investmentinc'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="投资收益明细项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_invexit(Base):

    __tablename__ = 'stk_notes_invexit'

    SYMBOL = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    ENDDATE = Column(DateTime, doc="统计截止时间")
    RALATEDPARTY = Column(String(200), doc="子公司名称")
    SGNRGN = Column(String(10), doc="地区")
    ESTABLISHDATE = Column(String(10), doc="注册成立时间")
    EXITMODE = Column(String(10), doc="退出方式")
    DISPOSALDATE = Column(String(10), doc="处置时间")
    DISPOSALPRICE = Column(DECIMAL(20, 2), doc="处置价款")
    DISPOSALEQUITY = Column(DECIMAL(10, 2), doc="股权处置比例")
    CURRENCY = Column(String(100), doc="币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class stk_notes_longtermloan(Base):

    __tablename__ = 'stk_notes_longtermloan'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_longtermprepaidfee(Base):

    __tablename__ = 'stk_notes_longtermprepaidfee'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(200), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    INCREASEDURINGYEAR = Column(DECIMAL(20, 4), doc="本年增加 ")
    DECREASEDURINGYEAR = Column(DECIMAL(20, 4), doc="本年减少 ")
    AMORTIZATIONYEAR = Column(DECIMAL(20, 4), doc="其中：本年摊销 ")
    DECREASEDUEOTHER = Column(DECIMAL(20, 4), doc="其中：其他 ")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    PICTUREEXPLANATION = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    EXPLANATION = Column(String(4000), doc="说明")


class stk_notes_machabalance(Base):

    __tablename__ = 'stk_notes_machabalance'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="分类")
    ITEM = Column(String(400), doc="项目")
    AMOUNT = Column(DECIMAL(20, 2), doc="金额")
    AMOUNTTOTOTALASSETS = Column(DECIMAL(20, 2), doc="占总资产比重")
    PROPORTIONCHANGE = Column(DECIMAL(20, 2), doc="比重增减")
    CURRENCYCODE = Column(String(12), doc="币种")
    CHANGEINSTRUCTIONS = Column(String(1000), doc="重大变动说明")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_monetaryfunds(Base):

    __tablename__ = 'stk_notes_monetaryfunds'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    ITEM_EN = Column(String(1000), doc="项目")
    LOCALCURRENCY = Column(String(12), doc="本位币币种")
    FOREIGNCURRENCY = Column(String(12), doc="外币币种")
    BEGINNINGFOREIGNAMOUNT = Column(DECIMAL(20, 2), doc="期初外币金额")
    BEGINNINGEXCHANGERATE = Column(String(40), doc="期初汇率")
    BEGINNINGLOCALCURAMOUNT = Column(DECIMAL(20, 2), doc="期初折合本位币金额")
    ENDINGFOREIGNAMOUNT = Column(DECIMAL(20, 2), doc="期末外币金额")
    ENDINGEXCHANGERATE = Column(String(40), doc="期末汇率")
    ENDINGLOCALCURAMOUNT = Column(DECIMAL(20, 2), doc="期末折合本位币金额")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    IMAGEREMARK = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_nldoneyear(Base):

    __tablename__ = 'stk_notes_nldoneyear'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_nomtaxrate(Base):

    __tablename__ = 'stk_notes_nomtaxrate'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    ITEMID = Column(String(200), doc="项目编码")
    TAXRATE = Column(String(200), doc="税率")
    TAXEXPLANATION = Column(String(4000), doc="税项说明")
    REMARK = Column(LONGTEXT, doc="备注")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_nonbusexp(Base):

    __tablename__ = 'stk_notes_nonbusexp'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_nonbusinc(Base):

    __tablename__ = 'stk_notes_nonbusinc'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_nonrecurring(Base):

    __tablename__ = 'stk_notes_nonrecurring'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    POSITIONVALUE = Column(DECIMAL(20, 2), doc="金额")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_oar(Base):

    __tablename__ = 'stk_notes_oar'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    ITEM = Column(String(400), doc="项目名称")
    AGE = Column(String(200), doc="账龄")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    BEGINNINGPROPORTION = Column(DECIMAL(20, 4), doc="期初比例")
    BEGINNINGBADDEBTPROVISION = Column(DECIMAL(20, 4), doc="期初坏账准备金额")
    BEGINNINGBADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="期初坏账准备计提比例")
    BEGINNINGNETVALUE = Column(DECIMAL(20, 4), doc="期初净额")
    BADDEBTPROVISIONINCREASE = Column(DECIMAL(20, 4), doc="坏账准备本期增加")
    BADDEBTPROVISIONREDUCE = Column(DECIMAL(20, 4), doc="坏账准备本期减少")
    BADDEBTPROVISIONREVERSAL = Column(DECIMAL(20, 4), doc="其中：坏账准备本期转回")
    BADDEBTPROVISIONWRITEOFF = Column(DECIMAL(20, 4), doc="其中：坏账准备本期冲销")
    BADDEBTPROVISIONOTHER = Column(DECIMAL(20, 4), doc="其中：其他")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    ENDINGPROPORTION = Column(DECIMAL(20, 4), doc="期末比例")
    ENDINGBADDEBTPROVISION = Column(DECIMAL(20, 4), doc="期末坏账准备金额")
    ENDINGBADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="期末坏账准备计提比例")
    ENDINGNETVALUE = Column(DECIMAL(20, 4), doc="期末净额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_oarsd(Base):

    __tablename__ = 'stk_notes_oarsd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    VESTINGPERIOD = Column(SMALLINT, doc="期间归属")
    SPECIALDISCLOSEREASONS = Column(String(1000), doc="特别披露原因")
    ITEM = Column(String(400), doc="单位或项目名称")
    AGEORDATE = Column(String(400), doc="欠款帐龄或日期")
    MONEY = Column(DECIMAL(20, 4), doc="金额")
    PROPORTIONOFTOTALOAR = Column(DECIMAL(20, 4), doc="占其他应收款总额的比例")
    BADDEBTPROVISION = Column(DECIMAL(20, 4), doc="坏账准备金额")
    BADDEBTPROVISIONRATIO = Column(DECIMAL(20, 4), doc="坏账准备计提比例")
    RELATIONSHIPWITHCOMPANY = Column(String(200), doc="与本公司关系")
    REASONFORPROVISION = Column(LONGTEXT, doc="计提理由")
    PAYMENTINSTRUCTIONS = Column(LONGTEXT, doc="款项说明")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    RANK = Column(SMALLINT, doc="排名")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_ocassect(Base):

    __tablename__ = 'stk_notes_ocassect'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_op(Base):

    __tablename__ = 'stk_notes_op'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    AGE = Column(String(200), doc="账龄")
    BEGINNINGBALANCE = Column(DECIMAL(20, 4), doc="期初余额")
    BEGINNINGPROPORTION = Column(DECIMAL(20, 4), doc="期初比例")
    ENDINGBALANCE = Column(DECIMAL(20, 4), doc="期末余额")
    ENDINGPROPORTION = Column(DECIMAL(20, 4), doc="期末比例")
    REASONSCHANGES = Column(LONGTEXT, doc="变动原因")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_operateincomecosts(Base):

    __tablename__ = 'stk_notes_operateincomecosts'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORY = Column(SMALLINT, doc="类别")
    DISTRIBUTIONSTANDARD = Column(SMALLINT, doc="分布标准")
    ITEM = Column(String(200), doc="项目")
    CURRENCY = Column(String(12), doc="币种")
    EARNINGS = Column(DECIMAL(20, 4), doc="本期收入金额")
    EARNINGSPROPORTION = Column(DECIMAL(20, 4), doc="本期收入比例")
    COSTS = Column(DECIMAL(20, 4), doc="本期成本金额")
    GROSSMARGIN = Column(DECIMAL(20, 4), doc="本期毛利金额")
    GROSSMARGINRATE = Column(DECIMAL(20, 4), doc="本期毛利率")
    GROSSMARGINPROPORTION = Column(DECIMAL(20, 4), doc="本期毛利比例")
    PREVIOUSEARNINGS = Column(DECIMAL(20, 4), doc="上期收入金额")
    PREVIOUSEARNINGSPROPORTION = Column(DECIMAL(20, 4), doc="上期收入比例")
    PREVIOUSCOSTS = Column(DECIMAL(20, 4), doc="上期成本金额")
    PREVIOUSGROSSMARGIN = Column(DECIMAL(20, 4), doc="上期毛利金额")
    PREVIOUSGROSSMARGINRATE = Column(DECIMAL(20, 4), doc="上期毛利率")
    PREVIOUSGROSSMARGINPROPORTION = Column(DECIMAL(20, 4), doc="上期毛利比例")
    INCOMEGROWTHRATE = Column(DECIMAL(20, 4), doc="收入增长率")
    GROSSPROFITGROWTHRATE = Column(DECIMAL(20, 4), doc="毛利增长率")
    SPARE1 = Column(String(200), doc="备用1")
    SPARE1NUM = Column(DECIMAL(20, 4), doc="备用1（NUM）")
    SPARE2 = Column(String(200), doc="备用2")
    SPARE2NUM = Column(DECIMAL(20, 4), doc="备用2（NUM）")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    PICTUREEXPLANATION = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_opsd(Base):

    __tablename__ = 'stk_notes_opsd'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    VESTINGPERIOD = Column(SMALLINT, doc="期间归属")
    SPECIALDISCLOSEREASONS = Column(String(1000), doc="特别披露原因")
    ITEM = Column(String(400), doc="单位或项目名称")
    DATEOCCURRENCE = Column(String(400), doc="发生日期")
    ARREARSAGING = Column(String(400), doc="欠款帐龄")
    MONEY = Column(DECIMAL(20, 4), doc="金额")
    PROPORTIONOFTOTALOP = Column(DECIMAL(20, 4), doc="占其他应付款总额的比例")
    RELATIONSHIPWITHCOMPANY = Column(String(200), doc="与本公司关系")
    PAYMENTINSTRUCTIONS = Column(LONGTEXT, doc="款项说明")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    RANK = Column(SMALLINT, doc="排名")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_payrecbus(Base):

    __tablename__ = 'stk_notes_payrecbus'

    SYMBOL = Column(String(6), doc="证券代码")
    ENDDATE = Column(DateTime, doc="年度区间")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    SUBJECTAREACODE = Column(SMALLINT, doc="科目类别")
    ITEMCODE = Column(String(6), doc="项目编码")
    ITEM = Column(String(200), doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期发生额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期发生额")
    CURRENCY = Column(String(6), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")


class stk_notes_paysalary(Base):

    __tablename__ = 'stk_notes_paysalary'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    INCREASEDURINGYEAR = Column(DECIMAL(20, 4), doc="本年增加额")
    DECREASEDURINGYEAR = Column(DECIMAL(20, 4), doc="本年减少额")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_realestate(Base):

    __tablename__ = 'stk_notes_realestate'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    CATEGORYID = Column(String(200), doc="类别编码")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 4), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 4), doc="本期增加数")
    CURRENTDECREASE = Column(DECIMAL(20, 4), doc="本期减少数")
    ENDINGVALUE = Column(DECIMAL(20, 4), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    IMAGEREMARK = Column(LargeBinary(16777216), doc="图片说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_sellexpense(Base):

    __tablename__ = 'stk_notes_sellexpense'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    AMOUNT = Column(DECIMAL(20, 4), doc="本期金额")
    PREVIOUSAMOUNT = Column(DECIMAL(20, 4), doc="上期金额")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_shorttermloan(Base):

    __tablename__ = 'stk_notes_shorttermloan'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGYEARVALUE = Column(DECIMAL(20, 4), doc="年初数")
    ENDINGYEARVALUE = Column(DECIMAL(20, 4), doc="年末数")
    CURRENCY = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_subjoint(Base):

    __tablename__ = 'stk_notes_subjoint'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    ENDDATE = Column(DateTime, doc="年度区间")
    RALATEDPARTYID = Column(DECIMAL(20, 0), doc="关联公司ID")
    RALATEDPARTY = Column(String(200), doc="关联公司名称")
    RELATIONSHIPCODE = Column(String(6), doc="与上市公司关系编码")
    RELATIONSHIP = Column(String(100), doc="与上市公司关系")
    ESTABLISHDATE = Column(String(10), doc="注册成立时间")
    REGISTERCAPITAL = Column(DECIMAL(20, 2), doc="注册资本")
    BUSINESSSCOPE = Column(String(4000), doc="经营范围")
    REGISTERADDRESS = Column(String(400), doc="注册地")
    DIRECTHOLDINGRATIO = Column(DECIMAL(10, 2), doc="直接持股")
    INDIRECTHOLDINGRATIO = Column(DECIMAL(10, 2), doc="间接持股")
    TOTALASSETS = Column(DECIMAL(20, 2), doc="总资产")
    OPERATINGEVENUE = Column(DECIMAL(20, 2), doc="营业收入")
    NETPROFIT = Column(DECIMAL(20, 2), doc="净利润")
    PROFITPARENT = Column(DECIMAL(20, 2), doc="归属于母公司所有者的净利润")
    CURRENCY = Column(String(100), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    ESTABLISHWAY = Column(String(100), doc="设立方式")
    TOTALCOST = Column(DECIMAL(20, 2), doc="期末总投资额")
    ISEXIT = Column(String(10), doc="是否退出")
    SGNRGN = Column(String(10), doc="区域标识")
    CORPORATEINCOMETAX = Column(String(20), doc="关联公司企业所得税率")
    COUNTRYCODE3 = Column(String(3), doc="关联公司所在国别代码")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_surplusreserve(Base):

    __tablename__ = 'stk_notes_surplusreserve'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    CURRENTINCREASE = Column(DECIMAL(20, 2), doc="本期增加数")
    CURRENTDECREASE = Column(DECIMAL(20, 2), doc="本期减少数")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_taxpayable(Base):

    __tablename__ = 'stk_notes_taxpayable'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEMCODE = Column(String(20), doc="项目编码")
    ITEM = Column(String(400), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_topfivebp(Base):

    __tablename__ = 'stk_notes_topfivebp'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    INSTITUTIONRANK = Column(SMALLINT, doc="机构排名")
    BUSINESSINSTITUTIONID = Column(DECIMAL(20, 0), doc="业务往来机构ID")
    BUSINESSINSTITUTIONNAME = Column(String(200), doc="业务往来机构名称")
    BUSINESSRELATIONS = Column(SMALLINT, doc="业务关系")
    BUSINESSTYPE = Column(SMALLINT, doc="业务类型")
    POSITIONVALUE = Column(DECIMAL(20, 2), doc="金额")
    POSITIONVALUETOTOTALVALUE = Column(DECIMAL(20, 2), doc="占年度业务总额比例")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_tradfinassect(Base):

    __tablename__ = 'stk_notes_tradfinassect'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    ITEM = Column(String(400), doc="项目")
    ITEM_EN = Column(String(1000), doc="项目")
    BEGINNINGVALUE = Column(DECIMAL(20, 2), doc="期初值")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末值")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_notes_udp(Base):

    __tablename__ = 'stk_notes_udp'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    ENDDATE = Column(DateTime, doc="会计期间")
    SOURCE = Column(SMALLINT, doc="数据来源")
    STATETYPECODE = Column(SMALLINT, doc="报表类型")
    PREVIOUSENDINGVALUEASFOUND = Column(DECIMAL(20, 2), doc="调整前上期末未分配利润")
    TOTALADJUSTOFBEGINNINGVALUE = Column(DECIMAL(20, 2), doc="调整期初未分配利润合计数")
    BEGINNINGVALUEASLEFT = Column(DECIMAL(20, 2), doc="调整后期初未分配利润")
    CURRENTPARENTNETPROFIT = Column(DECIMAL(20, 2), doc="本期归属于母公司所有者的净利润")
    SURPLUSRESERVEREDUCELOSS = Column(DECIMAL(20, 2), doc="盈余公积弥补亏损")
    LONGTERMEQUITYINVESTMENTEFFECT = Column(DECIMAL(20, 2), doc="长期股权投资成本法改权益法的影响")
    EXCHANGEACCOUNTINGPOLICY = Column(DECIMAL(20, 2), doc="会计政策变更")
    OTHERINCREASE = Column(DECIMAL(20, 2), doc="其他增加")
    LEGALSURPLUS = Column(DECIMAL(20, 2), doc="提取法定盈余公积")
    DISCRETIONARYSURPLUS = Column(DECIMAL(20, 2), doc="提取任意盈余公积")
    GENERALRISKPREPARATION = Column(DECIMAL(20, 2), doc="提取一般风险准备")
    TRANSACTIONRISKPREPARATION = Column(DECIMAL(20, 2), doc="提取交易风险准备")
    ORDINARYDIVIDEND = Column(DECIMAL(20, 2), doc="应付普通股股利")
    ORDINARYDIVIDENDTOEQUITY = Column(DECIMAL(20, 2), doc="转作股本的普通股股利")
    OTHERDECREASE = Column(DECIMAL(20, 2), doc="其他减少")
    ENDINGVALUE = Column(DECIMAL(20, 2), doc="期末未分配利润")
    CURRENCYCODE = Column(String(12), doc="币种")
    EXPLANATION = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_originalholders(Base):

    __tablename__ = 'stk_originalholders'

    SYMBOL = Column(String(20), doc="证券代码")
    RANK = Column(INTEGER, primary_key=True, doc="股东序号")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    FULLNAME = Column(String(200), doc="股东名称")
    FULLNAME_EN = Column(String(1000), doc="股东英文名称")
    SHARES = Column(DECIMAL(20, 2), doc="持股数量")
    PERCENTAGEHOLDING = Column(DECIMAL(20, 4), doc="持股比例")
    LOCKTERM = Column(SMALLINT, doc="锁定期")
    STARTDATE = Column(DateTime, doc="锁定起始日")
    PLANLISTEDDATE = Column(DateTime, doc="计划上市交易日")
    LISTEDDATE = Column(DateTime, doc="实际上市交易日")
    LISTEDSHARES = Column(DECIMAL(20, 2), doc="实际解禁数量")
    COMMENTS = Column(String(1000), doc="备注")
    UPDATEID = Column(BIGINT, doc="数据ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True)
    UPDATETIME_EN = Column(DateTime)


class stk_personalholderalias(Base):

    __tablename__ = 'stk_personalholderalias'

    PERSONALHOLDERID = Column(DECIMAL(30, 0), doc="GTA股东人员ID")
    ALIAS = Column(String(200), primary_key=True, doc="人员别名")
    SHAREHOLDERTYPE = Column(String(100), doc="股东类型")
    SHAREHOLDERTYPECODE = Column(String(10), doc="股东类型编码")
    COMMENTS = Column(String(4000), doc="备注")
    ISSTANDARDFULLNAME = Column(String(2), doc="是否为标准名称")
    UPDATEID = Column(BIGINT, doc="数据ID")


class stk_pretrdinfo(Base):

    __tablename__ = 'stk_pretrdinfo'

    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), primary_key=True, doc="证券代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SHORTNAME = Column(String(100), doc="证券简称")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    INDUSTRYCODE = Column(String(40), doc="所属行业")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    PRECLOSE = Column(DECIMAL(8, 4), doc="前收盘价")
    EXDIVIDENDPRECLOSE = Column(DECIMAL(8, 4), doc="除权除息后的前收盘价")
    UPLIMIT = Column(DECIMAL(8, 4), doc="涨停价")
    DOWNLIMIT = Column(DECIMAL(8, 4), doc="跌停价")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    PRICESHIFTUNIT = Column(DECIMAL(8, 4), doc="价格档位")
    UPDATEID = Column(BIGINT, doc="数据ID")
    EPS = Column(DECIMAL(8, 4), doc="本年每股利润")
    ENDDATE = Column(DateTime, doc="截止日期")
    NAVPERSHARE = Column(DECIMAL(8, 4), doc="每股净资产")
    PARENTEPS = Column(DECIMAL(8, 4), doc="归属于母公司股东每股利润")


class stk_pretrdinfohistory(Base):

    __tablename__ = 'stk_pretrdinfohistory'

    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), primary_key=True, doc="证券代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SHORTNAME = Column(String(100), doc="证券简称")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    INDUSTRYCODE = Column(String(40), doc="所属行业")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    PRECLOSE = Column(DECIMAL(8, 4), doc="前收盘价")
    EXDIVIDENDPRECLOSE = Column(DECIMAL(8, 4), doc="除权除息后的前收盘价")
    UPLIMIT = Column(DECIMAL(8, 4), doc="涨停价")
    DOWNLIMIT = Column(DECIMAL(8, 4), doc="跌停价")
    STATUSID = Column(SMALLINT, doc="交易状态编码")
    PRICESHIFTUNIT = Column(DECIMAL(8, 4), doc="价格档位")
    UPDATEID = Column(BIGINT, doc="数据ID")
    EPS = Column(DECIMAL(8, 4), doc="本年每股利润")
    ENDDATE = Column(DateTime, doc="截止日期")
    NAVPERSHARE = Column(DECIMAL(8, 4), doc="每股净资产")
    PARENTEPS = Column(DECIMAL(8, 4), doc="归属于母公司股东每股利润")


class stk_relationship_background(Base):

    __tablename__ = 'stk_relationship_background'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    ENDDATE = Column(DateTime, doc="截止日期")
    FULLNAME = Column(String(200), doc="关系人名称")
    RELATIONSHIPID = Column(String(12), doc="与上市公司关系类型编码")
    RELATIONSHIP = Column(String(100), doc="与上市公司关系类型")
    NATUREID = Column(String(12), doc="关系人性质编码")
    NATURE = Column(String(100), doc="关系人性质")
    REGISTEREDADDRESS = Column(String(400), doc="注册地址")
    BUSINESSSCOPE = Column(String(4000), doc="经营范围")
    REGISTEREDCAPITAL = Column(DECIMAL(20, 2), doc="注册资本")
    SHAREHOLDERBACKGROUND = Column(String(4000), doc="股东背景")
    SPECIALEXPLANATION = Column(String(4000), doc="特殊说明")
    CURRENCYCODE = Column(String(12), doc="币种")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_rpt_ralatedparty(Base):

    __tablename__ = 'stk_rpt_ralatedparty'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    REPORTSOURCE = Column(String(40), doc="公告来源")
    ENDDATE = Column(DateTime, doc="统计截止日期")
    RALATEDPARTYID = Column(DECIMAL(20, 0), doc="关联方ID")
    RALATEDPARTY = Column(String(200), doc="关联方名称")
    OTHERPARTYSIGN = Column(String(20), doc="是否其他关联方")
    RELATIONID = Column(String(100), doc="关联关系分类ID")
    RELATION = Column(String(100), doc="关联关系分类")
    RELATIONSHIP = Column(String(100), doc="关联关系")
    ENTERPRISENATUREID = Column(String(100), doc="企业类型分类ID")
    ENTERPRISENATURE = Column(String(100), doc="企业类型分类")
    REGISTERCAPITAL = Column(DECIMAL(20, 2), doc="注册资本")
    CURRENCYCODE = Column(String(40), doc="货币编码")
    REGISTERADDRESS = Column(String(400), doc="注册地址")
    LEGALREPRESENTATIVE = Column(String(200), doc="法人代表")
    BUSINESSNATURE = Column(LONGTEXT, doc="业务性质")
    RESHAREHOLDINGRATIO = Column(DECIMAL(20, 2), doc="关联公司持股比例")
    REVOTERATIO = Column(DECIMAL(20, 2), doc="关联公司表决权比例")
    COSHAREHOLDINGRATIO = Column(DECIMAL(20, 2), doc="上市公司持股比例")
    COVOTERATIO = Column(DECIMAL(20, 2), doc="上市公司表决权比例")
    ORGANIZATIONCODE = Column(String(20), doc="组织机构代码")
    NOTE = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_rpt_transactions(Base):

    __tablename__ = 'stk_rpt_transactions'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    REPORTSOURCE = Column(String(40), doc="公告来源")
    ENDDATE = Column(DateTime, doc="统计截止日期")
    RALATEDPARTYID = Column(DECIMAL(20, 0), doc="关联方ID")
    RALATEDPARTY = Column(String(1000), doc="关联方名称")
    RELATIONID = Column(String(100), doc="关联关系分类ID")
    RELATION = Column(String(100), doc="关联关系分类")
    RELATIONSHIP = Column(String(1000), doc="关联关系")
    TRANSACTIONNATURE = Column(SMALLINT, doc="交易性质")
    TRANSACTIONDIRECTION = Column(String(100), doc="交易方向")
    TRANSACTIONKINDID = Column(String(100), doc="关联交易事项分类ID")
    TRANSACTIONKIND = Column(String(100), doc="关联交易事项分类")
    TRANSACTIONS = Column(String(100), doc="关联交易事项")
    TRANSACTIONRANK = Column(BIGINT, doc="交易序号")
    TRANSACTIONAMOUNT = Column(DECIMAL(20, 2), doc="交易金额")
    TRANSACTIONAMOUNTRATIO = Column(DECIMAL(10, 4), doc="交易金额占比")
    CURRENCYCODE = Column(String(40), doc="货币编码")
    CAPTIALEXPENSES = Column(DECIMAL(20, 2), doc="资金费用")
    INTERSETRATE = Column(String(100), doc="利率")
    ENDBANLANCE = Column(DECIMAL(20, 2), doc="期末余额")
    TRANSACTIONPRICE = Column(String(400), doc="交易价格")
    TRADINGDATE = Column(DateTime, doc="交易日期")
    TRANSACTIONLIMIT = Column(String(200), doc="交易期限")
    TRANSACTIONBANK = Column(String(200), doc="涉及银行")
    TRANSACTIONCONTENT = Column(String(800), doc="交易内容")
    PRICINGPRINCIPLEID = Column(String(100), doc="交易定价原则分类ID")
    PRICINGPRINCIPLE = Column(String(100), doc="交易定价原则分类")
    TRANSACTIONPRICING = Column(LONGTEXT, doc="交易定价原则")
    PROFITINFLUENCESIGN = Column(SMALLINT, doc="是否影响公司利润")
    PROFITINFLUENCE = Column(LONGTEXT, doc="交易对利润的影响")
    NOTE = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_rpt_transfer(Base):

    __tablename__ = 'stk_rpt_transfer'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(12), doc="股票代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    ENDDATE = Column(DateTime, doc="统计截止日期")
    RALATEDPARTYID = Column(DECIMAL(20, 0), doc="关联方ID")
    RALATEDPARTY = Column(String(600), doc="关联方名称")
    RELATIONID = Column(String(100), doc="关联关系分类ID")
    RELATION = Column(String(100), doc="关联关系分类")
    RELATIONSHIP = Column(String(600), doc="关联关系")
    ACCOUNTTITLEID = Column(String(100), doc="资金往来科目分类ID")
    ACCOUNTTITLE = Column(String(100), doc="资金往来科目分类")
    TRANSACTIONACCOUNT = Column(String(100), doc="资金往来科目")
    TRANSACTIONRANK = Column(BIGINT, doc="交易序号")
    BEGINNINGBANLANCE = Column(DECIMAL(20, 2), doc="年初余额")
    ENDBANLANCE = Column(DECIMAL(20, 2), doc="年末余额")
    ENDBANLANCERATIO = Column(DECIMAL(10, 4), doc="年末余额占比")
    CURRENCYCODE = Column(String(40), doc="货币编码")
    NOTE = Column(LONGTEXT, doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_shares_structure(Base):

    __tablename__ = 'stk_shares_structure'

    INSTITUTIONID = Column(DECIMAL(20, 0), primary_key=True, doc="上市公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    CHANGEDATE = Column(DateTime, primary_key=True, doc="变动日期")
    CHANGEREASON = Column(String(400), doc="变动原因")
    CHANGEREASONID = Column(String(400), doc="变动原因ID")
    EVENTID = Column(String(40), doc="事件ID")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    STATEOWNEDSHARES = Column(DECIMAL(20, 0), doc="国有股")
    STATESHARES = Column(DECIMAL(20, 0), doc="--国家股")
    SLS = Column(DECIMAL(20, 0), doc="--国有法人股")
    OTHERDOMESTICSHARES = Column(DECIMAL(20, 0), doc="其他内资股")
    SOCIALLEGALPERSONSHARES = Column(DECIMAL(20, 0), doc="--社会法人股")
    NATURALPERSONSHARES = Column(DECIMAL(20, 0), doc="--境内自然人持股")
    PROMOTERSHARES = Column(DECIMAL(20, 0), doc="发起人股份")
    EMPLOYEESHARES = Column(DECIMAL(20, 0), doc="内部职工股")
    EXECUTIVESSHARES = Column(DECIMAL(20, 0), doc="高管股")
    FOREIGNSHARES = Column(DECIMAL(20, 0), doc="外资持股")
    FOREIGNLEGALPERSONSHARES = Column(DECIMAL(20, 0), doc="--境外法人股")
    FOREIGNERSHARES = Column(DECIMAL(20, 0), doc="--境外自然人股")
    ALLOCATIONSHARES = Column(DECIMAL(20, 0), doc="募集法人股")
    STRATEGICINVESTORSHARES = Column(DECIMAL(20, 0), doc="--战略投资者配售股份")
    FUNDALLOCATIONSHARES = Column(DECIMAL(20, 0), doc="--基金配售股份")
    OTHERALLOCATIONSHARES = Column(DECIMAL(20, 0), doc="--一般法人配售股份")
    TRANSFERREDALOTTEDSHARES = Column(DECIMAL(20, 0), doc="转配股")
    PREFERREDSHARE = Column(DECIMAL(20, 0), doc="优先股")
    OTHERNEGOTIABLESHARES = Column(DECIMAL(20, 0), doc="其他非流通股")
    NONTRADABLESHARE = Column(DECIMAL(20, 0), doc="未流通股合计")
    OTHERLOCKSHARES = Column(DECIMAL(20, 0), doc="其他限售股")
    LOCKSHARESTOTAL = Column(DECIMAL(20, 0), doc="限售流通股合计")
    TRADABLESHARESA = Column(DECIMAL(20, 0), doc="流通A股")
    TRADABLEEXECUTIVESSHARES = Column(DECIMAL(20, 0), doc="--无限售高管股")
    TRADABLESHARESB = Column(DECIMAL(20, 0), doc="流通B股")
    TRADABLESHARESH = Column(DECIMAL(20, 0), doc="流通H股")
    OTHERTRADABLESHARES = Column(DECIMAL(20, 0), doc="其他流通股份")
    TRADESHARESTOTAL = Column(DECIMAL(20, 0), doc="流通股合计")
    TOTAL = Column(DECIMAL(20, 0), doc="总股本")
    COMMENTS = Column(String(800), doc="备注")
    UPDATEID = Column(BIGINT, doc="数据ID")
    ALLOCATIONLESHARES = Column(DECIMAL(20, 0), doc="配售法人股")


class stk_shares_structure_daily(Base):

    __tablename__ = 'stk_shares_structure_daily'

    INSTITUTIONID = Column(DECIMAL(20, 0), doc="上市公司ID")
    SYMBOL = Column(String(20), doc="证券代码")
    SHARESDATE = Column(DateTime, doc="股本日期")
    CHANGEDATE = Column(DateTime, doc="变动日期")
    CHANGEREASON = Column(String(400), doc="变动原因")
    CHANGEREASONID = Column(String(400), doc="变动原因ID")
    EVENTID = Column(String(40), doc="事件ID")
    STATEOWNEDSHARES = Column(DECIMAL(20, 0), doc="国有股")
    STATESHARES = Column(DECIMAL(20, 0), doc="--国家股")
    SLS = Column(DECIMAL(20, 0), doc="--国有法人股")
    OTHERDOMESTICSHARES = Column(DECIMAL(20, 0), doc="其他内资股")
    SOCIALLEGALPERSONSHARES = Column(DECIMAL(20, 0), doc="--社会法人股")
    NATURALPERSONSHARES = Column(DECIMAL(20, 0), doc="--境内自然人持股")
    PROMOTERSHARES = Column(DECIMAL(20, 0), doc="发起人股份")
    EMPLOYEESHARES = Column(DECIMAL(20, 0), doc="内部职工股")
    EXECUTIVESSHARES = Column(DECIMAL(20, 0), doc="高管股")
    FOREIGNSHARES = Column(DECIMAL(20, 0), doc="外资持股")
    FOREIGNLEGALPERSONSHARES = Column(DECIMAL(20, 0), doc="--境外法人股")
    FOREIGNERSHARES = Column(DECIMAL(20, 0), doc="--境外自然人股")
    ALLOCATIONSHARES = Column(DECIMAL(20, 0), doc="募集法人股")
    STRATEGICINVESTORSHARES = Column(DECIMAL(20, 0), doc="--战略投资者配售股份")
    FUNDALLOCATIONSHARES = Column(DECIMAL(20, 0), doc="--基金配售股份")
    OTHERALLOCATIONSHARES = Column(DECIMAL(20, 0), doc="--一般法人配售股份")
    TRANSFERREDALOTTEDSHARES = Column(DECIMAL(20, 0), doc="转配股")
    PREFERREDSHARE = Column(DECIMAL(20, 0), doc="优先股")
    OTHERNEGOTIABLESHARES = Column(DECIMAL(20, 0), doc="其他非流通股")
    NONTRADABLESHARE = Column(DECIMAL(20, 0), doc="未流通股合计")
    OTHERLOCKSHARES = Column(DECIMAL(20, 0), doc="其他限售股")
    LOCKSHARESTOTAL = Column(DECIMAL(20, 0), doc="限售流通股合计")
    TRADABLESHARESA = Column(DECIMAL(20, 0), doc="流通A股")
    TRADABLEEXECUTIVESSHARES = Column(DECIMAL(20, 0), doc="--无限售高管股")
    TRADABLESHARESB = Column(DECIMAL(20, 0), doc="流通B股")
    TRADABLESHARESH = Column(DECIMAL(20, 0), doc="流通H股")
    OTHERTRADABLESHARES = Column(DECIMAL(20, 0), doc="其他流通股份")
    TRADESHARESTOTAL = Column(DECIMAL(20, 0), doc="流通股合计")
    TOTAL = Column(DECIMAL(20, 0), doc="总股本")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    ALLOCATIONLESHARES = Column(DECIMAL(20, 0), doc="配售法人股")


class stk_sr_difference(Base):

    __tablename__ = 'stk_sr_difference'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    REPUNUMBER = Column(INTEGER, doc="回购次数")
    REPUAVERAGEPRICE = Column(DECIMAL(10, 4), doc="回购平均价格")
    ACTUALDAYS = Column(INTEGER, doc="实际回购天数")
    DAYSDIFFERENCE = Column(INTEGER, doc="回购天数差异")
    ACTUALAMOUNT = Column(DECIMAL(16, 2), doc="实际回购量")
    AMOUNTDIFFERENCE = Column(DECIMAL(16, 2), doc="回购量差异")
    ACTUALTOTAL = Column(DECIMAL(20, 4), doc="实际回购支出总额")
    ACTUALREPURATIO = Column(DECIMAL(10, 4), doc="实际回购支出总额占市值的比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_sr_equitychange(Base):

    __tablename__ = 'stk_sr_equitychange'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    CHANGEDECLAREDATE = Column(DateTime, doc="回购注销完成日期")
    SHARECLASSID = Column(String(6), doc="股份类别编码")
    SHARECLASS = Column(String(100), doc="股份类别名称")
    BEFORECHANGINGSHARES = Column(DECIMAL(16, 2), doc="本次变动前数量")
    BEFORECHANGINGRATIO = Column(DECIMAL(10, 4), doc="本次变动前比例")
    CHANGESVALUE = Column(DECIMAL(16, 2), doc="本次变动增减")
    AFTERCHANGINGSHARES = Column(DECIMAL(16, 2), doc="本次变动后数量")
    AFTERCHANGINGRATIO = Column(DECIMAL(10, 4), doc="本次变动后比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_sr_implement(Base):

    __tablename__ = 'stk_sr_implement'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    DECLAREDATE = Column(DateTime, doc="公告日期")
    TITLE = Column(String(200), doc="公告标题")
    STARTDATE = Column(DateTime, doc="回购开始日期")
    ENDDATE = Column(DateTime, doc="回购截至日期")
    REPUPARTY = Column(String(200), doc="股份回购方")
    BUYBACKPARTY = Column(String(1200), doc="股份被回购方")
    SHARES = Column(DECIMAL(16, 2), doc="回购股份数量")
    REPURATIO = Column(DECIMAL(10, 4), doc="占总股本的比例")
    HIGHPRICE = Column(DECIMAL(10, 4), doc="回购成交最高价")
    LOWPRICE = Column(DECIMAL(10, 4), doc="回购成交最低价")
    TOTAL = Column(DECIMAL(20, 4), doc="支付总金额")
    CUMULATESHARES = Column(DECIMAL(16, 2), doc="累计回购股份数量")
    CUMULATEREPURATIO = Column(DECIMAL(10, 4), doc="累计回购占总股本比例")
    CUMULATEHIGHPRICE = Column(DECIMAL(10, 4), doc="累计成交最高价")
    CUMULATELOWPRICE = Column(DECIMAL(10, 4), doc="累计成交最低价")
    CUMULATETOTAL = Column(DECIMAL(20, 4), doc="累计支付总金额")
    CURRENCY = Column(String(6), doc="币种")
    EXPLANATION = Column(String(4000), doc="说明")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_sr_indexm(Base):

    __tablename__ = 'stk_sr_indexm'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    ACTUALMONTH = Column(String(7), doc="实际发生回购月份")
    AMOUNTMONTH = Column(DECIMAL(16, 2), doc="当月回购的股份数量")
    RELATIVEPRICE = Column(DECIMAL(10, 4), doc="相对回购价格（回购前后一个月）")
    REPUSCALE = Column(DECIMAL(20, 4), doc="回购规模")
    REPUSCALERATIO = Column(DECIMAL(10, 4), doc="回购规模占市值的比例")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_sr_repumain(Base):

    __tablename__ = 'stk_sr_repumain'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    SHORTNAME = Column(String(100), doc="证券简称")
    INSTITUTIONNAME = Column(String(200), doc="公司全称")
    DECLAREDATE = Column(DateTime, doc="回购预案公告日期")
    FIRSTDECLAREDATE = Column(DateTime, doc="首次实施回购日期")
    FINISHDECLAREDATE = Column(DateTime, doc="回购完成日期")
    ISCOMPLETE = Column(String(1), doc="是否实施完成")
    REPUPURPOSE = Column(String(400), doc="回购目的")
    REPUTYPEID = Column(String(6), doc="回购方式编码")
    REPUTYPE = Column(String(40), doc="回购方式")
    REPUUSE = Column(String(400), doc="回购用途")
    PRICINGPRINCIPLE = Column(String(4000), doc="回购定价原则")
    SHARESPECIES = Column(String(40), doc="回购股份种类")
    REPUSOURCEID = Column(String(20), doc="回购资金来源编码")
    REPUSOURCE = Column(String(40), doc="回购资金来源")
    REPUSOURCEEXPLANATION = Column(String(400), doc="回购资金来源说明")
    SHARESCEILING = Column(DECIMAL(16, 2), doc="拟回购数量上限")
    SHARESFLOOR = Column(DECIMAL(16, 2), doc="拟回购数量下限")
    INTENDREPURATIO = Column(DECIMAL(10, 4), doc="拟回购股份占总股本的比例")
    REPUFUNDCEILING = Column(DECIMAL(20, 4), doc="拟用于回购的资金总额上限")
    REPUFUNDFLOOR = Column(DECIMAL(20, 4), doc="拟用于回购的资金总额下限")
    CURRENCY = Column(String(6), doc="币种")
    STARTDATE = Column(DateTime, doc="拟回购起始日期")
    ENDDATE = Column(DateTime, doc="拟回购终止日期")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    EXPLANATION = Column(LONGTEXT)


class stk_sr_schedule(Base):

    __tablename__ = 'stk_sr_schedule'

    EVENTID = Column(DECIMAL(20, 0), doc="事件ID")
    INSTITUTIONID = Column(DECIMAL(20, 0), doc="公司ID")
    SYMBOL = Column(String(6), doc="证券代码")
    SCHEDULEDATE = Column(DateTime, doc="进度日期")
    REPUSCHEDULEID = Column(String(6), doc="回购进度编码")
    REPUSCHEDULE = Column(String(100), doc="回购进度")
    CONTENT = Column(String(4000), doc="进度内容")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class stk_stockinfo(Base):

    __tablename__ = 'stk_stockinfo'

    SECURITYID = Column(DECIMAL(20, 0))
    SYMBOL = Column(String(20))
    INSTITUTIONID = Column(DECIMAL(20, 0))
    SHORTNAME = Column(String(100))
    PYSHORTNAME = Column(String(100))
    ENSHORTNAME = Column(String(400))
    ENNAME = Column(String(200))
    LISTEDDATE = Column(DateTime)
    DELISTEDDATE = Column(DateTime)
    IPOSHARES = Column(DECIMAL(20, 0))
    PARVALUE = Column(DECIMAL(20, 10))
    ISSUEPRICE = Column(DECIMAL(10, 4))
    CURRENCYCODE = Column(String(40))
    EXCHANGECODE = Column(String(40))
    BOARDID = Column(String(40))
    SHARETYPE = Column(String(6))
    ISIN = Column(String(40))
    STATUSID = Column(String(40))
    UPDATEID = Column(BIGINT, primary_key=True)
    FORMERNAME = Column(String(1000), doc="股票简称曾用名")
    CURRENCY = Column(String(40), doc="面值币种")
    GTASYMBOL = Column(String(100), doc="国泰安代码")


class stk_suspentioninfo(Base):

    __tablename__ = 'stk_suspentioninfo'

    SYMBOL = Column(String(20))
    SHORTNAME = Column(String(100))
    SUSPENTIONTYPECODE = Column(String(12))
    ANNOUNCEMENTDATE = Column(DateTime)
    SUSPENTIONDATE = Column(DateTime)
    SUSPENSTIONTIME = Column(String(12))
    RESUMPTIONDATE = Column(DateTime)
    RESUMPTIONTIME = Column(String(12))
    SUSPENTIONTERM = Column(DECIMAL(8, 2))
    REASONID = Column(String(100))
    REASON = Column(String(400))
    UPDATEID = Column(BIGINT, primary_key=True)


class stk_view_stockinfo(Base):

    __tablename__ = 'stk_view_stockinfo'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SHORTNAME = Column(String(100), doc="证券名称")
    SYMBOL = Column(String(12), doc="证券代码")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    INDUSTRYCODE = Column(String(40), doc="所属行业")
    TRADINGVOLUME = Column(DECIMAL(20, 0), doc="前5天总成交量")
    NAVPERSHARE = Column(DECIMAL(8, 4), doc="每股净资产")
    PRECLOSE = Column(DECIMAL(8, 4), doc="昨收盘价")
    LASTYEAREPS = Column(DECIMAL(8, 4), doc="上年每股利润")
    CURRENTEPS = Column(DECIMAL(8, 4), doc="本年每股利润")
    UPLIMIT = Column(DECIMAL(8, 4), doc="涨停价")
    DOWNLIMIT = Column(DECIMAL(8, 4), doc="跌停价")
    PRICESHIFTUNIT = Column(DECIMAL(8, 4), doc="价格档位")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    TRADINGDATE = Column(DateTime)
    CLOSE = Column(DECIMAL(8, 4))
    LASTENDDATE = Column(DateTime)
    EXDIVIDENDPRECLOSE = Column(DECIMAL(8, 4))
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5))
    ENDDATE = Column(DateTime)
    PARENTEPS = Column(DECIMAL(8, 4), doc="归属于母公司股东每股利润")


class stk_view_stockinfohistory(Base):

    __tablename__ = 'stk_view_stockinfohistory'

    TRADINGDATE = Column(DateTime, primary_key=True, doc="交易日期")
    SYMBOL = Column(String(12), primary_key=True, doc="证券代码")
    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SHORTNAME = Column(String(100), doc="证券名称")
    PYSHORTNAME = Column(String(100), doc="拼音简称")
    EXCHANGECODE = Column(String(40), doc="交易所编码")
    CIRCULATEDSHARE = Column(DECIMAL(20, 0), doc="流通股本")
    TOTALSHARE = Column(DECIMAL(20, 0), doc="总股本")
    INDUSTRYCODE = Column(String(40), doc="所属行业")
    PERMINTRADINGVOLUME = Column(DECIMAL(21, 5), doc="前5天平均每分钟成交量")
    TRADINGVOLUME = Column(DECIMAL(20, 0), doc="前5天总成交量")
    CLOSE = Column(DECIMAL(8, 4), doc="收盘价")
    PRECLOSE = Column(DECIMAL(8, 4), doc="昨收盘价")
    EXDIVIDENDPRECLOSE = Column(DECIMAL(8, 4), doc="除权除息后的昨收盘价")
    UPLIMIT = Column(DECIMAL(8, 4), doc="涨停价")
    DOWNLIMIT = Column(DECIMAL(8, 4), doc="跌停价")
    PRICESHIFTUNIT = Column(DECIMAL(8, 4), doc="价格档位")
    NAVPERSHARE = Column(DECIMAL(8, 4), doc="每股净资产")
    LASTYEAREPS = Column(DECIMAL(8, 4), doc="上年每股利润")
    CURRENTEPS = Column(DECIMAL(8, 4), doc="本年每股利润")
    LASTENDDATE = Column(DateTime, doc="上年每股利润指标所处会计期间的截止时间")
    ENDDATE = Column(DateTime, doc="本年每股利润指标所处会计期间的截止时间")
    UPDATEID = Column(BIGINT, doc="数据ID")
    PARENTEPS = Column(DECIMAL(8, 4), doc="归属于母公司股东每股利润")


class sz_securityinfo(Base):

    __tablename__ = 'sz_securityinfo'

    SYMBOL = Column(String(20), doc="证券代码")
    SYMBOLNAME = Column(String(100), doc="中文证券名称")
    UPDATEDATE = Column(DateTime, doc="记录更新日期")
    UPDATETIME1 = Column(String(12), doc="记录更新时间")
    NAMEPREFIX = Column(String(20), doc="证券简称前缀")
    SYMBOLNAME_EN = Column(String(100), doc="英文证券名称")
    UNDERLYINGSECURITYSYMBOL = Column(String(20), doc="基础证券代码")
    ISIN = Column(String(40), doc="ISIN代码")
    INDUSTRYCODE = Column(String(20), doc="行业代码")
    CURRENCYTYPE = Column(String(6), doc="货币种类")
    PARVALUE = Column(DECIMAL(7, 2), doc="每股面值")
    ISSUEVOLUME = Column(BIGINT, doc="发行数量")
    CIRCULATEDSHARE = Column(BIGINT, doc="流通股数")
    PERSHRPROFITLASTYEAR = Column(DECIMAL(9, 4), doc="上年每股利润")
    PERSHRPROFITCURRENTYEAR = Column(DECIMAL(9, 4), doc="本年每股利润")
    ACCUMULATIVENAV = Column(DECIMAL(9, 4), doc="基金份额累计净值")
    TRADINGFEERATE = Column(DECIMAL(7, 6), doc="经手费率")
    STAMPTAXRATE = Column(DECIMAL(7, 6), doc="印花税率")
    TRANSFERRINGFEERATE = Column(DECIMAL(7, 6), doc="过户费率")
    LISTEDDATE = Column(DateTime, doc="上市日期")
    INTERESTSTARTDATE = Column(DateTime, doc="债券起息日")
    EXPIRYDATE = Column(DateTime, doc="到期/交割日")
    TRADINGUNIT = Column(INTEGER, doc="交易单位")
    BUYPERSHARES = Column(DECIMAL(20, 0), doc="买数量单位")
    SELLPERSHARES = Column(DECIMAL(20, 0), doc="卖数量单位")
    SINGLEDESIGNATEVOLLIMIT = Column(BIGINT, doc="每笔委托限量")
    PRICESTALL = Column(DECIMAL(10, 3), doc="价格档位")
    CALLAUCTIONPRICELIMITPAR = Column(DECIMAL(10, 3), doc="集合竞价限价参数")
    CONTAUCTIONPRICELIMITPAR = Column(DECIMAL(10, 3), doc="连续竞价限价参数")
    PRICELIMITPARNATURE = Column(SMALLINT, doc="限价参数性质")
    RISECEILINGPRICE = Column(DECIMAL(10, 3), doc="涨幅上限价格")
    DECLINEFLOORPRICE = Column(DECIMAL(10, 3), doc="跌幅下限价格")
    BLOCKTRADINGPRICECEILING = Column(DECIMAL(10, 3), doc="大宗交易价格上限")
    BLOCKTRADINGPRICEFLOOR = Column(DECIMAL(10, 3), doc="大宗交易价格下限")
    CONVERSIONRATE = Column(DECIMAL(5, 2), doc="债券折合比例")
    GUARANTYDISCOUNTRATE = Column(DECIMAL(5, 2), doc="担保物折算率")
    FINANCING = Column(String(2), doc="融资标的标志")
    SECURITIESLENDING = Column(String(2), doc="融券标的标志")
    SAMPLESTOCKSIGN = Column(String(2), doc="成份股标志")
    MARKETMAKERSIGN = Column(String(2), doc="做市商标志")
    MARKETTYPE = Column(String(20), doc="市场种类")
    SYMBOLTYPE = Column(String(20), doc="证券类别")
    SYMBOLLEVEL = Column(String(2), doc="证券级别")
    PRODSTATUSID = Column(String(2), doc="产品状态标志")
    TRANSACTIONTYPE = Column(String(2), doc="交易类型")
    PRODTRADINGSTAGE = Column(String(2), doc="产品交易阶段")
    SUSPENDEDTRADINGSIGN = Column(String(2), doc="暂停交易标志")
    FINANCIALTRDSTATUS = Column(String(2), doc="融资交易状态")
    SECURITYCREDITTRDSTATUS = Column(String(2), doc="融券交易状态")
    SECURITYCREDITSELLLIMIT = Column(String(2), doc="融券卖出价格限制")
    NETWORKVOTINGSIGN = Column(String(2), doc="网络投票标志")
    OTHBUSINESSSTATUS = Column(String(16), doc="其他业务状态")
    RESERVEFIELD = Column(String(24), doc="备用字段")
    RESERVEFSIGN = Column(String(2), doc="备用标志")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class sz_securityinfohistory(Base):

    __tablename__ = 'sz_securityinfohistory'

    TRADINGDATE = Column(DateTime, doc="交易日期")
    SYMBOL = Column(String(10), doc="证券代码")
    SECURITYNAME = Column(String(100), doc="证劵名称")
    SYMBOLSOURCE = Column(String(10), doc="证券代码源")
    SECURITYEN = Column(String(100), doc="证券英文简称")
    ISIN = Column(String(20), doc="ISIN代码")
    SYMBOLUNDERLYING = Column(String(10), doc="基础证券代码")
    UNDERLYINGSECURITYIDSOURCE = Column(String(10), doc="基础证券代码源")
    SECURITYTYPE = Column(String(10), doc="证券类别代码")
    SECURITYSTATUSTAG = Column(String(20), doc="证券状态标识")
    PRECLOSEPRICE = Column(DECIMAL(10, 3), doc="昨收盘价")
    LISTINGDATE = Column(DateTime, doc="上市日期")
    CURRENCY = Column(String(3), doc="币种")
    PARVALUE = Column(DECIMAL(7, 2), doc="每股面值")
    ISSUEDVOLUME = Column(BIGINT, doc="总发行量")
    OUTSTANDINGSHARE = Column(BIGINT, doc="流通股数")
    INDUSTRYTYPE = Column(String(10), doc="行业种类")
    PREYEAREPS = Column(DECIMAL(9, 4), doc="上年每股利润")
    YEAREPS = Column(DECIMAL(9, 4), doc="本年每股利润")
    OFFERINGFLAG = Column(String(1), doc="收购（转股、行权）标志")
    NAV = Column(DECIMAL(9, 4), doc="基金T-1日累计净值")
    COUPONRATE = Column(DECIMAL(9, 4), doc="票面利率")
    ISSUEPRICE = Column(DECIMAL(9, 4), doc="贴现发行价")
    INTEREST = Column(DECIMAL(9, 4), doc="每百元应计利息")
    INTERESTACCRUALDATE = Column(DateTime, doc="起息日")
    MATURITYDATE = Column(DateTime, doc="到期交割日")
    CONVERSIONPRICE = Column(DECIMAL(9, 4), doc="行权价格")
    CONVERSIONRATIO = Column(DECIMAL(9, 4), doc="行权比例")
    CONVERSIONBEGINDATE = Column(DateTime, doc="行权开始日")
    CONVERSIONENDDATE = Column(DateTime, doc="行权结束日")
    CALLORPUT = Column(String(1), doc="认购认沽")
    WARRANTCLEARINGTYPE = Column(String(1), doc="权证结算方式")
    CLEARINGPRICE = Column(DECIMAL(9, 4), doc="结算价格")
    OPTIONTYPE = Column(String(1), doc="行权类型")
    ENDDATE = Column(DateTime, doc="最后交易日")
    EXPIRATIONDAYS = Column(String(10), doc="购回期限")
    DAYTRADING = Column(String(1), doc="回转交易标志")
    GAGEFLAG = Column(String(1), doc="保证金证券标志")
    GAGERATE = Column(DECIMAL(5, 2), doc="担保品折算率")
    CRDBUYUNDERLYING = Column(String(1), doc="融资标的标志")
    CRDSELLUNDERLYING = Column(String(1), doc="融券标的标志")
    CRDPRICECHECKTYPE = Column(String(1), doc="提价检查方式")
    PLEDGEFLAG = Column(String(1), doc="质押入库标志")
    CONTRACTMULTIPLIER = Column(DECIMAL(5, 2), doc="债券折合回购标准券比例")
    REGULARSHARE = Column(String(20), doc="对应回购标准券")
    QUALIFICATIONFLAG = Column(String(1), doc="投资者适当性管理标志")
    MARKETMAKERFLAG = Column(String(1), doc="做市商标志")
    ROUNDLOT = Column(INTEGER, doc="整手数")
    TICKSIZE = Column(DECIMAL(10, 3), doc="最小报价单位")
    BUYQTYUPPERLIMIT = Column(DECIMAL(15, 2), doc="买数量上限")
    SELLQTYUPPERLIMIT = Column(DECIMAL(15, 2), doc="卖数量上限")
    BUYVOLUMEUNIT = Column(DECIMAL(20, 0), doc="买数量单位")
    SELLVOLUMEUNIT = Column(DECIMAL(20, 0), doc="卖数量单位")
    LIMITUPRATEO = Column(DECIMAL(10, 3), doc="开盘集合竞价上涨幅度")
    LIMITDOWNRATEO = Column(DECIMAL(10, 3), doc="开盘集合竞价下跌幅度")
    LIMITUPABSOLUTEO = Column(DECIMAL(10, 3), doc="开盘集合竞价上涨限价")
    LIMITDOWNABSOLUTEO = Column(DECIMAL(10, 3), doc="开盘集合竞价下跌限价")
    AUCTIONUPDOWNRATEO = Column(DECIMAL(10, 3), doc="开盘集合竞价有效范围涨跌幅度")
    AUCTIONUPDOWNABSOLUTEO = Column(DECIMAL(10, 3), doc="开盘集合竞价有效范围涨跌价格")
    LIMITUPRATET = Column(DECIMAL(10, 3), doc="连续竞价上涨幅度")
    LIMITDOWNRATET = Column(DECIMAL(10, 3), doc="连续竞价下跌幅度")
    LIMITUPABSOLUTET = Column(DECIMAL(10, 3), doc="连续竞价上涨限价")
    LIMITDOWNABSOLUTET = Column(DECIMAL(10, 3), doc="连续竞价下跌限价")
    AUCTIONUPDOWNRATET = Column(DECIMAL(10, 3), doc="连续竞价有效范围涨跌幅度")
    AUCTIONUPDOWNABSOLUTET = Column(DECIMAL(10, 3), doc="连续竞价有效范围涨跌价格")
    LIMITUPRATEC = Column(DECIMAL(10, 3), doc="收盘集合竞价上涨幅度")
    LIMITDOWNRATEC = Column(DECIMAL(10, 3), doc="收盘集合竞价下跌幅度")
    LIMITUPABSOLUTEC = Column(DECIMAL(10, 3), doc="收盘集合竞价上涨限价")
    LIMITDOWNABSOLUTEC = Column(DECIMAL(10, 3), doc="收盘集合竞价下跌限价")
    AUCTIONUPDOWNRATEC = Column(DECIMAL(10, 3), doc="收盘集合竞价有效范围涨跌幅度")
    AUCTIONUPDOWNABSOLUTEC = Column(DECIMAL(10, 3), doc="收盘集合竞价有效范围涨跌价格")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")
    PRICEUPLIMIT = Column(DECIMAL(20, 4), doc="涨停价格")
    PRICEDOWNLIMIT = Column(DECIMAL(20, 4), doc="跌停价格")


class tbl_chn_bond_infochg(Base):

    __tablename__ = 'tbl_chn_bond_infochg'

    SECURITYID = Column(DECIMAL(20, 0), doc="证券ID")
    SYMBOL = Column(String(32), doc="证券代码")
    BONDID = Column(DECIMAL(20, 0), doc="债券主体ID")
    ANNOUNCEMENTDATE = Column(DateTime, doc="公告日期")
    CHANGEDITEM = Column(String(100), doc="变更属性")
    VALUE_BEFORE = Column(String(2000), doc="变更前值")
    CODE_BEFORE = Column(String(200), doc="变更前(编码|英文)")
    VALUE_AFTER = Column(String(2000), doc="变更后值")
    CODE_AFTER = Column(String(200), doc="变更后(编码|英文)")
    NOTE = Column(String(1000), doc="备注")
    IMPLEMENTDATE = Column(DateTime, doc="实施日期")
    EVENTTYPE = Column(String(40), doc="事件类型编码")
    DESCRIPVALUE_BEFORE = Column(String(100), doc="变更前属性描述")
    DESCRIPVALUE_AFTER = Column(String(100), doc="变更后属性描述")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class zz_bondcloseweight(Base):

    __tablename__ = 'zz_bondcloseweight'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(20), doc="指数代码")
    TRADINGDATE = Column(DateTime, doc="日期")
    SHHCODE = Column(String(20), doc="沪市代码")
    SHHSECURITYID = Column(DECIMAL(20, 0), doc="沪市证券ID")
    SHZCODE = Column(String(20), doc="深市代码")
    SHZSECURITYID = Column(DECIMAL(20, 0), doc="深市证券ID")
    INTERBANKCODE = Column(String(20), doc="银行间代码")
    INTERBANKSECURITYID = Column(DECIMAL(20, 0), doc="银行间证券ID")
    CONSTITUENTCODE = Column(String(40), doc="所在交易所交易代码")
    TRADINGCURRENCY = Column(String(6), doc="交易所使用的币种")
    EXCHANGERATE = Column(DECIMAL(9, 4), doc="交易货币对指数币种汇率")
    WEIGHT = Column(DECIMAL(10, 3), doc="权重")
    RESERVE = Column(String(20), doc="保留字段")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class zz_bondtermstructure(Base):

    __tablename__ = 'zz_bondtermstructure'

    CURVENAME = Column(String(160), doc="曲线名称")
    TRADINGDATE = Column(DateTime, doc="日期")
    TERM = Column(DECIMAL(10, 2), doc="年限")
    SPOTRATE = Column(DECIMAL(10, 4), doc="即期利率")
    HPRETURN = Column(DECIMAL(10, 4), doc="到期收益率")
    FORWARDRATE = Column(DECIMAL(10, 4), doc="远期利率")
    RESERVE = Column(String(20), doc="保留字段")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class zz_bondvaluation(Base):

    __tablename__ = 'zz_bondvaluation'

    TRADINGDATE = Column(DateTime, doc="日期")
    SHHCODE = Column(String(20), doc="沪市代码")
    SHHSECURITYID = Column(DECIMAL(20, 0), doc="沪市证券ID")
    SHZCODE = Column(String(20), doc="深市代码")
    SHZSECURITYID = Column(DECIMAL(20, 0), doc="深市证券ID")
    INTERBANKCODE = Column(String(20), doc="银行间代码")
    INTERBANKSECURITYID = Column(DECIMAL(20, 0), doc="银行间证券ID")
    CALCULAPRICE = Column(DECIMAL(10, 4), doc="计算价格")
    HPRETURN = Column(DECIMAL(10, 4), doc="计算收益率")
    ADJDURATION = Column(DECIMAL(10, 4), doc="修正久期")
    CONVEXITY = Column(DECIMAL(10, 4), doc="凸性")
    CLEANPRICE = Column(DECIMAL(10, 4), doc="净价")
    ACCRUEINTEREST = Column(DECIMAL(10, 4), doc="应计利息")
    RESERVE = Column(String(20), doc="保留字段")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


class zz_divisoradjustment(Base):

    __tablename__ = 'zz_divisoradjustment'

    SECURITYID = Column(DECIMAL(20, 0), doc="指数ID")
    SYMBOL = Column(String(30), doc="指数代码")
    EFFECTIVEDATE = Column(DateTime, doc="生效日期")
    CURRENTDIVISOR = Column(DECIMAL(24, 4), doc="原除数")
    NEWDIVISOR = Column(DECIMAL(24, 4), doc="调整后除数")
    UPDATEID = Column(BIGINT, primary_key=True, doc="数据ID")


csmar_class_dict = {
    'bond_agency': bond_agency,
    'bond_basiccredit': bond_basiccredit,
    'bond_basicinfo': bond_basicinfo,
    'bond_bondtype': bond_bondtype,
    'bond_bs': bond_bs,
    'bond_calpretrdinfo': bond_calpretrdinfo,
    'bond_cfdm': bond_cfdm,
    'bond_cfets_dquote_his_dq': bond_cfets_dquote_his_dq,
    'bond_cfets_pledgedrepo_hdq': bond_cfets_pledgedrepo_hdq,
    'bond_cfetsclosingyield': bond_cfetsclosingyield,
    'bond_cfetsvaluationindex': bond_cfetsvaluationindex,
    'bond_cfim': bond_cfim,
    'bond_conversion': bond_conversion,
    'bond_conversionrate': bond_conversionrate,
    'bond_convertinfo': bond_convertinfo,
    'bond_convertissue': bond_convertissue,
    'bond_convertprice': bond_convertprice,
    'bond_crmwinfo': bond_crmwinfo,
    'bond_currencyswapcurve': bond_currencyswapcurve,
    'bond_discloseindex': bond_discloseindex,
    'bond_fixreporate': bond_fixreporate,
    'bond_guarantorinfo': bond_guarantorinfo,
    'bond_guarantorrating': bond_guarantorrating,
    'bond_inbankod': bond_inbankod,
    'bond_info': bond_info,
    'bond_interestfloat': bond_interestfloat,
    'bond_is': bond_is,
    'bond_issuecost': bond_issuecost,
    'bond_issuer': bond_issuer,
    'bond_issueregiinfo': bond_issueregiinfo,
    'bond_lastquotationmonth': bond_lastquotationmonth,
    'bond_lastquotationweek': bond_lastquotationweek,
    'bond_lastquotationyear': bond_lastquotationyear,
    'bond_mkttrade': bond_mkttrade,
    'bond_nafmiipricntrlcrv': bond_nafmiipricntrlcrv,
    'bond_otc_quotationhis': bond_otc_quotationhis,
    'bond_otc_quotationoptimal': bond_otc_quotationoptimal,
    'bond_payment': bond_payment,
    'bond_pretrdinfo': bond_pretrdinfo,
    'bond_pretrdinfohistory': bond_pretrdinfohistory,
    'bond_quotation': bond_quotation,
    'bond_quotationderivative': bond_quotationderivative,
    'bond_quotationlatest': bond_quotationlatest,
    'bond_quotationmonth': bond_quotationmonth,
    'bond_quotations': bond_quotations,
    'bond_quotationweek': bond_quotationweek,
    'bond_quotationyear': bond_quotationyear,
    'bond_ratetype': bond_ratetype,
    'bond_rating': bond_rating,
    'bond_redemption': bond_redemption,
    'bond_repayterm': bond_repayterm,
    'bond_repototal': bond_repototal,
    'bond_repovariety': bond_repovariety,
    'bond_shcvaluation': bond_shcvaluation,
    'bond_shcyield': bond_shcyield,
    'bond_stagesredemption': bond_stagesredemption,
    'bond_suspentioninfo': bond_suspentioninfo,
    'bond_tenderissue': bond_tenderissue,
    'bond_tenderresult': bond_tenderresult,
    'bond_treasyield': bond_treasyield,
    'cmo_pretrdinfo': cmo_pretrdinfo,
    'cmo_pretrdinfohistory': cmo_pretrdinfohistory,
    'cost_riskfree': cost_riskfree,
    'ffut_calpretrdinfo': ffut_calpretrdinfo,
    'ffut_pretrdinfo': ffut_pretrdinfo,
    'ffut_pretrdinfohistory': ffut_pretrdinfohistory,
    'fund_allocation': fund_allocation,
    'fund_areaclass': fund_areaclass,
    'fund_bwardfactor': fund_bwardfactor,
    'fund_calpretrdinfo': fund_calpretrdinfo,
    'fund_classinfochange': fund_classinfochange,
    'fund_custodian': fund_custodian,
    'fund_daynav': fund_daynav,
    'fund_etfconstitsec': fund_etfconstitsec,
    'fund_etfpchasredemlis': fund_etfpchasredemlis,
    'fund_evl_dayahay': fund_evl_dayahay,
    'fund_evl_dayamth': fund_evl_dayamth,
    'fund_evl_dayasen': fund_evl_dayasen,
    'fund_evl_dayayear': fund_evl_dayayear,
    'fund_evl_daythryear': fund_evl_daythryear,
    'fund_evl_weekahay': fund_evl_weekahay,
    'fund_evl_weekayear': fund_evl_weekayear,
    'fund_evl_weekthryear': fund_evl_weekthryear,
    'fund_feeschange': fund_feeschange,
    'fund_fundcodeinfo': fund_fundcodeinfo,
    'fund_fundcompany': fund_fundcompany,
    'fund_funddividend': fund_funddividend,
    'fund_fundmanager': fund_fundmanager,
    'fund_fwardfactor': fund_fwardfactor,
    'fund_holderstructure': fund_holderstructure,
    'fund_indexreturn': fund_indexreturn,
    'fund_industrystockclass': fund_industrystockclass,
    'fund_jajxrate': fund_jajxrate,
    'fund_listing': fund_listing,
    'fund_mainpersonnel': fund_mainpersonnel,
    'fund_mkt_bwardquotation': fund_mkt_bwardquotation,
    'fund_mkt_fwardquotation': fund_mkt_fwardquotation,
    'fund_mkt_lastbwardquotem': fund_mkt_lastbwardquotem,
    'fund_mkt_lastbwardquotew': fund_mkt_lastbwardquotew,
    'fund_mkt_lastbwardquotey': fund_mkt_lastbwardquotey,
    'fund_mkt_lastfwardquotem': fund_mkt_lastfwardquotem,
    'fund_mkt_lastfwardquotew': fund_mkt_lastfwardquotew,
    'fund_mkt_lastfwardquotey': fund_mkt_lastfwardquotey,
    'fund_mkt_lastquotationmonth': fund_mkt_lastquotationmonth,
    'fund_mkt_lastquotationweek': fund_mkt_lastquotationweek,
    'fund_mkt_lastquotationyear': fund_mkt_lastquotationyear,
    'fund_mkt_quotation': fund_mkt_quotation,
    'fund_mkt_quotationlatest': fund_mkt_quotationlatest,
    'fund_mkt_quotationmonth': fund_mkt_quotationmonth,
    'fund_mkt_quotationweek': fund_mkt_quotationweek,
    'fund_mkt_quotationyear': fund_mkt_quotationyear,
    'fund_mktdayreturn': fund_mktdayreturn,
    'fund_mktmonthreturn': fund_mktmonthreturn,
    'fund_mktpf_pfm': fund_mktpf_pfm,
    'fund_mktpf_pfm_week': fund_mktpf_pfm_week,
    'fund_mktweekreturn': fund_mktweekreturn,
    'fund_mktyearreturn': fund_mktyearreturn,
    'fund_nav': fund_nav,
    'fund_nav_month': fund_nav_month,
    'fund_nav_pfm': fund_nav_pfm,
    'fund_nav_pfm_month': fund_nav_pfm_month,
    'fund_nav_pfm_week': fund_nav_pfm_week,
    'fund_nav_pfm_year': fund_nav_pfm_year,
    'fund_nav_week': fund_nav_week,
    'fund_nav_year': fund_nav_year,
    'fund_performance_compare': fund_performance_compare,
    'fund_performance_deviation': fund_performance_deviation,
    'fund_portfolio_abs': fund_portfolio_abs,
    'fund_portfolio_bondcredit': fund_portfolio_bondcredit,
    'fund_portfolio_bondvariety': fund_portfolio_bondvariety,
    'fund_portfolio_currency': fund_portfolio_currency,
    'fund_portfolio_stock': fund_portfolio_stock,
    'fund_pretrdinfo': fund_pretrdinfo,
    'fund_pretrdinfohistory': fund_pretrdinfohistory,
    'fund_promoter': fund_promoter,
    'fund_prospectuses': fund_prospectuses,
    'fund_ptf_bondspe': fund_ptf_bondspe,
    'fund_ptf_bsstock': fund_ptf_bsstock,
    'fund_ptf_bsstocktotal': fund_ptf_bsstocktotal,
    'fund_ptf_der': fund_ptf_der,
    'fund_ptf_fund': fund_ptf_fund,
    'fund_purchredchg': fund_purchredchg,
    'fund_quotation': fund_quotation,
    'fund_reportdate': fund_reportdate,
    'fund_resolution': fund_resolution,
    'fund_sharechange': fund_sharechange,
    'fund_shareholdercompany': fund_shareholdercompany,
    'fund_shsecrate': fund_shsecrate,
    'fund_stracontract': fund_stracontract,
    'fund_stractshare': fund_stractshare,
    'fund_strader': fund_strader,
    'fund_strainfo': fund_strainfo,
    'fund_stranav': fund_stranav,
    'fund_straquotation': fund_straquotation,
    'fund_strbder': fund_strbder,
    'fund_strbinfo': fund_strbinfo,
    'fund_strbnav': fund_strbnav,
    'fund_strbquotation': fund_strbquotation,
    'fund_strinfo': fund_strinfo,
    'fund_strmder': fund_strmder,
    'fund_strmnav': fund_strmnav,
    'fund_strmquotation': fund_strmquotation,
    'fund_strtrackamonth': fund_strtrackamonth,
    'fund_strtrackaweek': fund_strtrackaweek,
    'fund_strtrackbmonth': fund_strtrackbmonth,
    'fund_strtrackbweek': fund_strtrackbweek,
    'fund_tenholders': fund_tenholders,
    'fund_unitclassinfo': fund_unitclassinfo,
    'fut_calpretrdinfo': fut_calpretrdinfo,
    'fut_pretrdinfo': fut_pretrdinfo,
    'fut_pretrdinfohistory': fut_pretrdinfohistory,
    'idx_closeweight': idx_closeweight,
    'idx_closeweightfree': idx_closeweightfree,
    'idx_indexinfo': idx_indexinfo,
    'idx_mkt_lastquotationweek': idx_mkt_lastquotationweek,
    'idx_mkt_quotation': idx_mkt_quotation,
    'idx_samplechange': idx_samplechange,
    'idx_samplelatest': idx_samplelatest,
    'idx_weight': idx_weight,
    'idx_weightnextday': idx_weightnextday,
    'io_calpretrdinfo': io_calpretrdinfo,
    'io_pretrdinfo': io_pretrdinfo,
    'io_pretrdinfohistory': io_pretrdinfohistory,
    'mac_area_ampimonth': mac_area_ampimonth,
    'mac_area_ampiyear': mac_area_ampiyear,
    'mac_area_cpimonth': mac_area_cpimonth,
    'mac_area_cpiyear': mac_area_cpiyear,
    'mac_area_fixedassetsidx': mac_area_fixedassetsidx,
    'mac_area_fixedassetsidxyear': mac_area_fixedassetsidxyear,
    'mac_area_gdpquarter': mac_area_gdpquarter,
    'mac_area_gdpyear': mac_area_gdpyear,
    'mac_area_industrysalevalue': mac_area_industrysalevalue,
    'mac_area_industryvalueadd': mac_area_industryvalueadd,
    'mac_area_ppimonth': mac_area_ppimonth,
    'mac_area_ppiyear': mac_area_ppiyear,
    'mac_area_productoutputmonth': mac_area_productoutputmonth,
    'mac_area_productoutputyear': mac_area_productoutputyear,
    'mac_area_purchaseidxmonth': mac_area_purchaseidxmonth,
    'mac_area_purchaseidxyear': mac_area_purchaseidxyear,
    'mac_area_rpimonth': mac_area_rpimonth,
    'mac_area_rpiyear': mac_area_rpiyear,
    'mac_areagdp_expendyear': mac_areagdp_expendyear,
    'mac_areagdp_idx1978year': mac_areagdp_idx1978year,
    'mac_areagdp_idxyear': mac_areagdp_idxyear,
    'mac_areagdp_incomeyear': mac_areagdp_incomeyear,
    'mac_bondyieldsd': mac_bondyieldsd,
    'mac_fixedbaseidx': mac_fixedbaseidx,
    'mac_industry_financialyear': mac_industry_financialyear,
    'mac_industry_ppimonth': mac_industry_ppimonth,
    'mac_industry_ppiyear': mac_industry_ppiyear,
    'mac_industry_saleinventory': mac_industry_saleinventory,
    'mac_industry_valueadd': mac_industry_valueadd,
    'mac_industryvalueadd': mac_industryvalueadd,
    'mac_statsinfo_calendar': mac_statsinfo_calendar,
    'plate_bondchange': plate_bondchange,
    'plate_bondchangelatest': plate_bondchangelatest,
    'plate_bondsamplechange': plate_bondsamplechange,
    'plate_concept': plate_concept,
    'plate_fundchange': plate_fundchange,
    'plate_fundchangelatest': plate_fundchangelatest,
    'plate_fundsamplechange': plate_fundsamplechange,
    'plate_futurechange': plate_futurechange,
    'plate_futurechangelatest': plate_futurechangelatest,
    'plate_futuresamplechange': plate_futuresamplechange,
    'plate_indexchange': plate_indexchange,
    'plate_indexchangelatest': plate_indexchangelatest,
    'plate_indexsamplechange': plate_indexsamplechange,
    'plate_platetree': plate_platetree,
    'plate_platetree_state2': plate_platetree_state2,
    'plate_sochange': plate_sochange,
    'plate_sochangelatest': plate_sochangelatest,
    'plate_sosamplechange': plate_sosamplechange,
    'plate_stockchange': plate_stockchange,
    'plate_stockchangelatest': plate_stockchangelatest,
    'plate_stocksamplechange': plate_stocksamplechange,
    'pled_agrrepamt': pled_agrrepamt,
    'pled_agrrepdetl': pled_agrrepdetl,
    'pled_amtstat': pled_amtstat,
    'pled_ltvratio': pled_ltvratio,
    'pled_repbysecco': pled_repbysecco,
    'pled_sectrdvol': pled_sectrdvol,
    'pled_stkfrzdetl': pled_stkfrzdetl,
    'pled_stkratio': pled_stkratio,
    'pled_stktrdvol': pled_stktrdvol,
    'pled_trddetl': pled_trddetl,
    'pub_chnadmdivisioncode': pub_chnadmdivisioncode,
    'pub_codingschema': pub_codingschema,
    'pub_continuingcontract': pub_continuingcontract,
    'pub_eventtype': pub_eventtype,
    'pub_exchangeinfo': pub_exchangeinfo,
    'pub_indclassifysets': pub_indclassifysets,
    'pub_indclassifyversion': pub_indclassifyversion,
    'pub_institutionidchange': pub_institutionidchange,
    'pub_institutioninfo': pub_institutioninfo,
    'pub_isocontrycode': pub_isocontrycode,
    'pub_isocurrencycode': pub_isocurrencycode,
    'pub_mainconcontract': pub_mainconcontract,
    'pub_maincontract': pub_maincontract,
    'pub_personnelinfo': pub_personnelinfo,
    'pub_pretradinginfo': pub_pretradinginfo,
    'pub_securityconstant': pub_securityconstant,
    'pub_securityinfo': pub_securityinfo,
    'sh_securityinfo': sh_securityinfo,
    'smt_collateral': smt_collateral,
    'smt_collaterald': smt_collaterald,
    'smt_traded': smt_traded,
    'smt_tradesumd': smt_tradesumd,
    'smt_underlyingsd': smt_underlyingsd,
    'so_calpretrdinfo': so_calpretrdinfo,
    'so_pretrdinfo': so_pretrdinfo,
    'so_pretrdinfohistory': so_pretrdinfohistory,
    'stk_af_analystrank': stk_af_analystrank,
    'stk_af_forecast': stk_af_forecast,
    'stk_af_ratingchange': stk_af_ratingchange,
    'stk_af_ratingstatistic': stk_af_ratingstatistic,
    'stk_af_targetvalue': stk_af_targetvalue,
    'stk_calendard': stk_calendard,
    'stk_dividend': stk_dividend,
    'stk_eq_ipo_coinfo': stk_eq_ipo_coinfo,
    'stk_eq_ipo_employeeinfo': stk_eq_ipo_employeeinfo,
    'stk_eq_ipo_info': stk_eq_ipo_info,
    'stk_eq_ipo_ipocg': stk_eq_ipo_ipocg,
    'stk_eq_ipo_marketexhibit': stk_eq_ipo_marketexhibit,
    'stk_eq_ipo_overallot': stk_eq_ipo_overallot,
    'stk_eq_ipo_result': stk_eq_ipo_result,
    'stk_eq_rs_info': stk_eq_rs_info,
    'stk_eq_rs_plan': stk_eq_rs_plan,
    'stk_eq_rs_result': stk_eq_rs_result,
    'stk_eq_seo_plan': stk_eq_seo_plan,
    'stk_eq_seo_private': stk_eq_seo_private,
    'stk_eq_seo_publicinfo': stk_eq_seo_publicinfo,
    'stk_eq_seo_publicresult': stk_eq_seo_publicresult,
    'stk_eventlist': stk_eventlist,
    'stk_fin_balance': stk_fin_balance,
    'stk_fin_cashflow': stk_fin_cashflow,
    'stk_fin_cashflowindex': stk_fin_cashflowindex,
    'stk_fin_cashflowindrect': stk_fin_cashflowindrect,
    'stk_fin_cashflowindrectttm': stk_fin_cashflowindrectttm,
    'stk_fin_cashflowttm': stk_fin_cashflowttm,
    'stk_fin_construct': stk_fin_construct,
    'stk_fin_debtpay': stk_fin_debtpay,
    'stk_fin_development': stk_fin_development,
    'stk_fin_dividistrib': stk_fin_dividistrib,
    'stk_fin_earnpower': stk_fin_earnpower,
    'stk_fin_financialindexq': stk_fin_financialindexq,
    'stk_fin_forecfin': stk_fin_forecfin,
    'stk_fin_forecfinnew': stk_fin_forecfinnew,
    'stk_fin_income': stk_fin_income,
    'stk_fin_incomettm': stk_fin_incomettm,
    'stk_fin_ipodiscloseindex': stk_fin_ipodiscloseindex,
    'stk_fin_lcdiscloseindex': stk_fin_lcdiscloseindex,
    'stk_fin_operate': stk_fin_operate,
    'stk_fin_pershare': stk_fin_pershare,
    'stk_fin_quitrafin': stk_fin_quitrafin,
    'stk_fin_quitrafinnew': stk_fin_quitrafinnew,
    'stk_fin_quitrasimfin': stk_fin_quitrasimfin,
    'stk_fin_relativevalue': stk_fin_relativevalue,
    'stk_fin_relforcdate': stk_fin_relforcdate,
    'stk_fin_risk': stk_fin_risk,
    'stk_fin_simforecfin': stk_fin_simforecfin,
    'stk_forecast': stk_forecast,
    'stk_guarantee_main': stk_guarantee_main,
    'stk_guarantee_son': stk_guarantee_son,
    'stk_guarantee_statistics': stk_guarantee_statistics,
    'stk_holder_controlchart': stk_holder_controlchart,
    'stk_holder_controller': stk_holder_controller,
    'stk_holder_detail': stk_holder_detail,
    'stk_holder_equitynatureall': stk_holder_equitynatureall,
    'stk_holder_incrordesr': stk_holder_incrordesr,
    'stk_holder_number': stk_holder_number,
    'stk_holder_pledge': stk_holder_pledge,
    'stk_holder_relation': stk_holder_relation,
    'stk_holder_systematics': stk_holder_systematics,
    'stk_holder_top10': stk_holder_top10,
    'stk_holder_top10floating': stk_holder_top10floating,
    'stk_indfi_basis': stk_indfi_basis,
    'stk_indfi_cashflow': stk_indfi_cashflow,
    'stk_indfi_construct': stk_indfi_construct,
    'stk_indfi_crn': stk_indfi_crn,
    'stk_indfi_debtpay': stk_indfi_debtpay,
    'stk_indfi_development': stk_indfi_development,
    'stk_indfi_dividistrib': stk_indfi_dividistrib,
    'stk_indfi_earnpower': stk_indfi_earnpower,
    'stk_indfi_hhi': stk_indfi_hhi,
    'stk_indfi_indtrajectory': stk_indfi_indtrajectory,
    'stk_indfi_lernerindex': stk_indfi_lernerindex,
    'stk_indfi_lpesv': stk_indfi_lpesv,
    'stk_indfi_npesv': stk_indfi_npesv,
    'stk_indfi_operate': stk_indfi_operate,
    'stk_indfi_pershare': stk_indfi_pershare,
    'stk_indfi_relativevalue': stk_indfi_relativevalue,
    'stk_indfi_risk': stk_indfi_risk,
    'stk_industryclass': stk_industryclass,
    'stk_institutionholderalias': stk_institutionholderalias,
    'stk_institutioninfo': stk_institutioninfo,
    'stk_itemchange': stk_itemchange,
    'stk_listedcoinfochg': stk_listedcoinfochg,
    'stk_lock_shares': stk_lock_shares,
    'stk_lockshares_summary': stk_lockshares_summary,
    'stk_ma_assetreplace': stk_ma_assetreplace,
    'stk_ma_assetstopay': stk_ma_assetstopay,
    'stk_ma_assettrans': stk_ma_assettrans,
    'stk_ma_cashpayment': stk_ma_cashpayment,
    'stk_ma_cdr': stk_ma_cdr,
    'stk_ma_equitytransfer': stk_ma_equitytransfer,
    'stk_ma_merger': stk_ma_merger,
    'stk_ma_otherparty': stk_ma_otherparty,
    'stk_ma_participant': stk_ma_participant,
    'stk_ma_stockpayment': stk_ma_stockpayment,
    'stk_ma_tenderoffer': stk_ma_tenderoffer,
    'stk_ma_tradingmain': stk_ma_tradingmain,
    'stk_ma_tradingschedule': stk_ma_tradingschedule,
    'stk_ma_underlying': stk_ma_underlying,
    'stk_mkt_adjustfactor': stk_mkt_adjustfactor,
    'stk_mkt_blocktrade': stk_mkt_blocktrade,
    'stk_mkt_capitalflow': stk_mkt_capitalflow,
    'stk_mkt_capitalflows': stk_mkt_capitalflows,
    'stk_mkt_divident': stk_mkt_divident,
    'stk_mkt_dividentnew': stk_mkt_dividentnew,
    'stk_mkt_exchangerate': stk_mkt_exchangerate,
    'stk_mkt_nightcale': stk_mkt_nightcale,
    'stk_mkt_quotation': stk_mkt_quotation,
    'stk_mkt_quotationlatest': stk_mkt_quotationlatest,
    'stk_mkt_repricefactor': stk_mkt_repricefactor,
    'stk_notes_accountingpolicy': stk_notes_accountingpolicy,
    'stk_notes_adminexpense': stk_notes_adminexpense,
    'stk_notes_afsfinassect': stk_notes_afsfinassect,
    'stk_notes_ap': stk_notes_ap,
    'stk_notes_apsd': stk_notes_apsd,
    'stk_notes_ar': stk_notes_ar,
    'stk_notes_arsd': stk_notes_arsd,
    'stk_notes_assetimpairment': stk_notes_assetimpairment,
    'stk_notes_basiccontent': stk_notes_basiccontent,
    'stk_notes_billrandp': stk_notes_billrandp,
    'stk_notes_billrandpspecial': stk_notes_billrandpspecial,
    'stk_notes_bondspayable': stk_notes_bondspayable,
    'stk_notes_businesstaxappend': stk_notes_businesstaxappend,
    'stk_notes_capitalreserve': stk_notes_capitalreserve,
    'stk_notes_capitalstock': stk_notes_capitalstock,
    'stk_notes_cbd': stk_notes_cbd,
    'stk_notes_cbdsd': stk_notes_cbdsd,
    'stk_notes_cip': stk_notes_cip,
    'stk_notes_cipchange': stk_notes_cipchange,
    'stk_notes_deferredincometax': stk_notes_deferredincometax,
    'stk_notes_devexpense': stk_notes_devexpense,
    'stk_notes_dividendpayable': stk_notes_dividendpayable,
    'stk_notes_dr': stk_notes_dr,
    'stk_notes_drsd': stk_notes_drsd,
    'stk_notes_equityinvest': stk_notes_equityinvest,
    'stk_notes_equityinvestcoinfo': stk_notes_equityinvestcoinfo,
    'stk_notes_fairvalueb': stk_notes_fairvalueb,
    'stk_notes_financecosts': stk_notes_financecosts,
    'stk_notes_fixedassect': stk_notes_fixedassect,
    'stk_notes_goodwill': stk_notes_goodwill,
    'stk_notes_govgrants': stk_notes_govgrants,
    'stk_notes_impjntfin': stk_notes_impjntfin,
    'stk_notes_interestpayable': stk_notes_interestpayable,
    'stk_notes_invassect': stk_notes_invassect,
    'stk_notes_inventories': stk_notes_inventories,
    'stk_notes_investmentinc': stk_notes_investmentinc,
    'stk_notes_invexit': stk_notes_invexit,
    'stk_notes_longtermloan': stk_notes_longtermloan,
    'stk_notes_longtermprepaidfee': stk_notes_longtermprepaidfee,
    'stk_notes_machabalance': stk_notes_machabalance,
    'stk_notes_monetaryfunds': stk_notes_monetaryfunds,
    'stk_notes_nldoneyear': stk_notes_nldoneyear,
    'stk_notes_nomtaxrate': stk_notes_nomtaxrate,
    'stk_notes_nonbusexp': stk_notes_nonbusexp,
    'stk_notes_nonbusinc': stk_notes_nonbusinc,
    'stk_notes_nonrecurring': stk_notes_nonrecurring,
    'stk_notes_oar': stk_notes_oar,
    'stk_notes_oarsd': stk_notes_oarsd,
    'stk_notes_ocassect': stk_notes_ocassect,
    'stk_notes_op': stk_notes_op,
    'stk_notes_operateincomecosts': stk_notes_operateincomecosts,
    'stk_notes_opsd': stk_notes_opsd,
    'stk_notes_payrecbus': stk_notes_payrecbus,
    'stk_notes_paysalary': stk_notes_paysalary,
    'stk_notes_realestate': stk_notes_realestate,
    'stk_notes_sellexpense': stk_notes_sellexpense,
    'stk_notes_shorttermloan': stk_notes_shorttermloan,
    'stk_notes_subjoint': stk_notes_subjoint,
    'stk_notes_surplusreserve': stk_notes_surplusreserve,
    'stk_notes_taxpayable': stk_notes_taxpayable,
    'stk_notes_topfivebp': stk_notes_topfivebp,
    'stk_notes_tradfinassect': stk_notes_tradfinassect,
    'stk_notes_udp': stk_notes_udp,
    'stk_originalholders': stk_originalholders,
    'stk_personalholderalias': stk_personalholderalias,
    'stk_pretrdinfo': stk_pretrdinfo,
    'stk_pretrdinfohistory': stk_pretrdinfohistory,
    'stk_relationship_background': stk_relationship_background,
    'stk_rpt_ralatedparty': stk_rpt_ralatedparty,
    'stk_rpt_transactions': stk_rpt_transactions,
    'stk_rpt_transfer': stk_rpt_transfer,
    'stk_shares_structure': stk_shares_structure,
    'stk_shares_structure_daily': stk_shares_structure_daily,
    'stk_sr_difference': stk_sr_difference,
    'stk_sr_equitychange': stk_sr_equitychange,
    'stk_sr_implement': stk_sr_implement,
    'stk_sr_indexm': stk_sr_indexm,
    'stk_sr_repumain': stk_sr_repumain,
    'stk_sr_schedule': stk_sr_schedule,
    'stk_stockinfo': stk_stockinfo,
    'stk_suspentioninfo': stk_suspentioninfo,
    'stk_view_stockinfo': stk_view_stockinfo,
    'stk_view_stockinfohistory': stk_view_stockinfohistory,
    'sz_securityinfo': sz_securityinfo,
    'sz_securityinfohistory': sz_securityinfohistory,
    'tbl_chn_bond_infochg': tbl_chn_bond_infochg,
    'zz_bondcloseweight': zz_bondcloseweight,
    'zz_bondtermstructure': zz_bondtermstructure,
    'zz_bondvaluation': zz_bondvaluation,
    'zz_divisoradjustment': zz_divisoradjustment,
}
