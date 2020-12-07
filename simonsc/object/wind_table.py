from sqlalchemy import Column, String, DECIMAL, DateTime, BIGINT, SMALLINT, INTEGER, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
wind_tables = ['AEQUFROPLEINFOREPPEREND', 'AINDEXCSI500WEIGHT', 'AINDEXDESCRIPTION', 'AINDEXEODPRICES', 'AINDEXFINANCIALDERIVATIVE', 'AINDEXHS300CLOSEWEIGHT', 'AINDEXHS300WEIGHT', 'AINDEXINDUSTRIESEODCITICS', 'AINDEXMEMBERS', 'AINDEXMEMBERSCITICS', 'AINDEXMEMBERSCITICS2', 'AINDEXMEMBERSCITICS2ZL', 'AINDEXMEMBERSCITICS3', 'AINDEXMEMBERSCITICSZL', 'ASAREPLANTRADE', 'ASHAREACCOUNTSPAYABLE', 'ASHAREADMINISTRATION', 'ASHAREANNFINANCIALINDICATOR', 'ASHAREAUDITOPINION', 'ASHAREBALANCESHEET', 'ASHAREBANKINDICATOR', 'ASHAREBEGUARANTEED', 'ASHARECALENDAR', 'ASHARECAPITALIZATION', 'ASHARECAPITALOPERATION', 'ASHARECASHFLOW', 'ASHARECIRCULATINGHOLDERS', 'ASHARECOCAPITALOPERATION', 'ASHARECOMPANYHOLDSHARES', 'ASHARECONCEPTUALPLATE', 'ASHARECREDITORRIGHTS', 'ASHARECUSTOMER', 'ASHAREDEFENDANT', 'ASHAREDESCRIPTION', 'ASHAREDIRECTOR', 'ASHAREDIVIDEND', 'ASHAREEARNINGEST', 'ASHAREEODPRICES', 'ASHAREEQUFROINFO', 'ASHAREEQUITYPLEDGEINFO', 'ASHAREEQUITYRELATIONSHIPS', 'ASHAREESOPDESCRIPTION', 'ASHAREESOPTRADINGINFO', 'ASHAREFINANCIALDERIVATIVE', 'ASHAREFINANCIALINDICATOR', 'ASHAREFLOATHOLDER', 'ASHAREFREEFLOAT', 'ASHAREGROUP', 'ASHAREGROUPINFORMATION', 'ASHAREGUARANTEERELATIONSHIP', 'ASHAREGUARANTEESTATISTICS', 'ASHAREHOLDER', 'ASHAREHOLDERNUMBER', 'ASHAREHOLDING', 'ASHAREIBROKERINDICATOR', 'ASHAREILLEGALITY', 'ASHAREINCDESCRIPTION', 'ASHAREINCEXECQTYPRI', 'ASHAREINCEXERCISEPCT', 'ASHAREINCEXERCISEPCTZL', 'ASHAREINCOME', 'ASHAREINCQUANTITYDETAILS', 'ASHAREINCQUANTITYPRICE', 'ASHAREINDUSRATING', 'ASHAREINDUSTRIESCLASSCITICS', 'ASHAREINDUSTRIESCLASSCITICSZL', 'ASHAREINDUSTRIESCODE', 'ASHAREINSIDEHOLDER', 'ASHAREINSIDERTRADE', 'ASHAREINSTHOLDERDERDATA', 'ASHAREINSURANCEINDICATOR', 'ASHAREINTENSITYTREND', 'ASHAREINTENSITYTRENDADJ', 'ASHAREINVESTMENTPEVC', 'ASHAREIPOPRICINGFORECAST', 'ASHARELONGLOAN', 'ASHAREMAJORHOLDERPLANHOLD', 'ASHAREMAJORHOLDERPLANHOLDZL', 'ASHAREMANAGEMENT', 'ASHAREMANAGEMENTHOLDREWARD', 'ASHAREMARGINSUBJECT', 'ASHAREMARGINTRADE', 'ASHAREMARGINTRADESUM', 'ASHAREMECHANISMOWNERSHIP', 'ASHAREMERGERSUBJECT', 'ASHAREMJRHOLDERTRADE', 'ASHAREPEVCINVESTMENT', 'ASHAREPLAINTIFF', 'ASHAREPLEDGEPROPORTION', 'ASHAREPLEDGETRADE', 'ASHAREPREVIOUSENNAME', 'ASHAREPRODUCT', 'ASHAREPROFITEXPRESS', 'ASHAREPROFITNOTICE', 'ASHAREPROSECUTION', 'ASHARERECEIVABLES', 'ASHAREREGINV', 'ASHARERELATEDPARTYDEBT', 'ASHARERIGHTISSUE', 'ASHARESELLSUBJECT', 'ASHAREST', 'ASHARESTAFF', 'ASHARESTAFFSTRUCTURE', 'ASHARESTIBHOLDERVOTE', 'ASHARESTOCKRATING', 'ASHARESUPERVISOR', 'ASHARESUPPLIER', 'ASHARETRADINGSUSPENSION', 'ASHARETYPECODE', 'CFUNDBANKACCOUNT', 'CFUNDCHANGEWINDCODE', 'CFUNDCODEANDSNAME', 'CFUNDCOMPANYPREVIOUSNAME', 'CFUNDFACTIONALSTYLE', 'CFUNDHOLDRESTRICTEDCIRCULATION', 'CFUNDINDEXMEMBERS', 'CFUNDINDEXTABLE', 'CFUNDINDUSTRIESCODE', 'CFUNDINTRODUCTION', 'CFUNDMANAGEMENT', 'CFUNDPCHREDM', 'CFUNDPORTFOLIOCHANGES', 'CFUNDPREVIOUSNAME', 'CFUNDRALATEDSECURITIESCODE', 'CFUNDRATESENSITIVE', 'CFUNDSTYLECOEFFICIENT', 'CFUNDSTYLETHRESHOLD', 'CFUNDTACODE', 'CFUNDTYPECODE', 'CFUNDWINDCUSTOMCODE', 'CFUNDWINDINDEXCOMPONENT', 'CFUNDWINDINDEXMEMBERS', 'CHANGEWINDCODE', 'CHINACLOSEDFUNDEODPRICE', 'CHINAFEEDERFUND', 'CHINAGRADINGFUND', 'CHINAMFMPERFORMANCE', 'CHINAMFPERFORMANCE', 'CHINAMUTUALFUNDASSETPORTFOLIO', 'CHINAMUTUALFUNDBENCHMARK', 'CHINAMUTUALFUNDBENCHMARKEOD', 'CHINAMUTUALFUNDBONDPORTFOLIO', 'CHINAMUTUALFUNDDESCRIPTION', 'CHINAMUTUALFUNDFLOATSHARE', 'CHINAMUTUALFUNDINDPORTFOLIO', 'CHINAMUTUALFUNDMANAGER', 'CHINAMUTUALFUNDNAV', 'CHINAMUTUALFUNDPCHREDM', 'CHINAMUTUALFUNDPOSESTIMATION', 'CHINAMUTUALFUNDREPNAVPER', 'CHINAMUTUALFUNDSEATTRADING', 'CHINAMUTUALFUNDSECTOR', 'CHINAMUTUALFUNDSHARE', 'CHINAMUTUALFUNDSTOCKPORTFOLIO', 'CHINAMUTUALFUNDSUSPENDPCHREDM', 'CHINAMUTUALFUNDTRACKINGINDEX', 'CLOSEDFUNDPCHREDM', 'CMFAIPINFO', 'CMFCODEANDSNAME', 'CMFCONSEPTION', 'CMFDESCCHANGE', 'CMFFAIRVALUECHANGEPROFIT', 'CMFFIXEDINVESTMENTRATE', 'CMFHOLDER', 'CMFHOLDERSTRUCTURE', 'CMFHOLDINGRATIOANOMALY', 'CMFINDEXDESCRIPTION', 'CMFINDEXEOD', 'CMFINDUSTRYPLATE', 'CMFIOPVNAV', 'CMFNAVOPERATIONRECORD', 'CMFOTHERPORTFOLIO', 'CMFPREFERENTIALFEE', 'CMFPROPORTIONOFINVEOBJ', 'CMFRISKLEVEL', 'CMFSECCLASS', 'CMFSELLINGAGENTS', 'CMFSUBREDFEE', 'CMFTHEMECONCEPT', 'CMFTRADINGSUSPENSION', 'CMFUNDOPERATEPERIOD', 'CMMFPORTFOLIOPTM', 'CMMQUARTERLYDATA', 'CMONEYMARKETDAILYFINCOME', 'CMONEYMARKETFINCOME', 'CMONEYMARKETFSCARRYOVERM', 'CODEANDSNAME', 'COMPANYPREVIOUSNAME', 'COMPINTRODUCTION', 'COMPORGANIZATIONCODE', 'COUNTRYANDAREACODE', 'COUNTRYANDAREACODEZL', 'CPFUNDDESCRIPTION', 'CURRENCYCODE', 'ETFPCHREDM', 'FINANCIALQUALIFICATION', 'FINDEXPERFORMANCE', 'FUNDCREDITRECORD', 'GLOBALMARKETTRADINGTIME', 'GLOBALWORKINGDAY', 'INDEXCONTRASTSECTOR', 'LOFDESCRIPTION', 'LOFPCHREDM', 'RALATEDSECURITIESCODE', 'SHSCCHANNELHOLDINGS', 'SHSCDAILYSTATISTICS', 'WINDCUSTOMCODE', 'WIND_PDUPDATE_LOG']
Base = declarative_base()
metadata = Base.metadata


class AEQUFROPLEINFOREPPEREND(Base):

    __tablename__ = 'AEQUFROPLEINFOREPPEREND'

    CRNCY_CODE = Column(DECIMAL(20, 4), doc="质押冻结比例(%)")
    F_NAV_ACCUMULATED = Column(String(200), doc="股东名称")
    F_NAV_ADJFACTOR = Column(DECIMAL(20, 4), doc="持股数量(股)")
    F_NAV_ADJUSTED = Column(String(400), doc="备注")
    F_NAV_DIVACCUMULATED = Column(DECIMAL(20, 4), doc="质押或冻结数量(股)")
    F_NAV_UNIT = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICE_DATE = Column(String(8), doc="报告期")
    S_FRO_SHARES = Column(DECIMAL(20, 4), doc="冻结股份数量")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PLEDGE_SHARES = Column(DECIMAL(20, 4), doc="质押股份数量")


class AINDEXCSI500WEIGHT(Base):

    __tablename__ = 'AINDEXCSI500WEIGHT'

    CLOSEVALUE = Column(DECIMAL(20, 4), doc="收盘")
    EXCHANGE = Column(String(20), doc="交易所")
    FREE_SHR_RATIO = Column(DECIMAL(20, 4), doc="自由流通比例(%)(归档后)")
    INDEXNAME = Column(String(40), doc="指数名称")
    INDEXNAME_ENG = Column(String(100), doc="指数英文名称")
    MV_CALCULATION = Column(DECIMAL(20, 2), doc="计算用市值")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPEN_ADJUSTED = Column(DECIMAL(20, 4), doc="调整后开盘参考价")
    OPMODE = Column(String(1))
    S_CON_WINDCODE = Column(String(40), doc="Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SHR_CALCULATION = Column(DECIMAL(20, 2), doc="计算用股本(股)")
    TOT_MV = Column(DECIMAL(20, 2), doc="总市值")
    TOT_SHR = Column(DECIMAL(20, 2), doc="总股本(股)")
    TRADE_DT = Column(String(10), doc="生效日期")
    WEIGHT = Column(DECIMAL(20, 4), doc="权重(%)")
    WEIGHTFACTOR = Column(DECIMAL(20, 8), doc="权重因子")


class AINDEXDESCRIPTION(Base):

    __tablename__ = 'AINDEXDESCRIPTION'

    CHANGE_HISTORY = Column(String(100), doc="变更历史")
    EXPIRE_DATE = Column(String(8), doc="终止发布日期")
    INCOME_PROCESSING_METHOD = Column(String(20), doc="收益处理方式")
    INDEX_INTRO = Column(LONGTEXT, doc="指数简介")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CODE = Column(String(40), doc="交易代码")
    S_INFO_COMPNAME = Column(String(100), doc="指数名称")
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所")
    S_INFO_INDEX_BASEPER = Column(String(8), doc="基期")
    S_INFO_INDEX_BASEPT = Column(DECIMAL(20, 4), doc="基点")
    S_INFO_INDEX_WEIGHTSRULE = Column(String(10), doc="加权方式")
    S_INFO_INDEXCODE = Column(DECIMAL(9, 0), doc="指数类别代码")
    S_INFO_INDEXSTYLE = Column(String(40), doc="指数风格")
    S_INFO_INDEXTYPE = Column(String(40), doc="指数类别")
    S_INFO_LISTDATE = Column(String(8), doc="发布日期")
    S_INFO_NAME = Column(String(50), doc="证券简称")
    S_INFO_PINYIN = Column(String(40), doc="简称拼音")
    S_INFO_PUBLISHER = Column(String(100), doc="发布方")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    WEIGHT_TYPE = Column(DECIMAL(9, 0), doc="权重类型")
    WEIGHT_TYPE_NAME = Column(String(100), doc="权重类型名称")


class AINDEXEODPRICES(Base):

    __tablename__ = 'AINDEXEODPRICES'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_AMOUNT = Column(DECIMAL(20, 4), doc="成交金额(千元)")
    S_DQ_CHANGE = Column(DECIMAL(20, 4), doc="涨跌(点)")
    S_DQ_CLOSE = Column(DECIMAL(20, 4), doc="收盘价(点)")
    S_DQ_HIGH = Column(DECIMAL(20, 4), doc="最高价(点)")
    S_DQ_LOW = Column(DECIMAL(20, 4), doc="最低价(点)")
    S_DQ_OPEN = Column(DECIMAL(20, 4), doc="开盘价(点)")
    S_DQ_PCTCHANGE = Column(DECIMAL(20, 4), doc="涨跌幅(%)")
    S_DQ_PRECLOSE = Column(DECIMAL(20, 4), doc="昨收盘价(点)")
    S_DQ_VOLUME = Column(DECIMAL(20, 4), doc="成交量(手)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(10), doc="证券ID")
    TRADE_DT = Column(String(8), doc="交易日期")


class AINDEXFINANCIALDERIVATIVE(Base):

    __tablename__ = 'AINDEXFINANCIALDERIVATIVE'

    ACCOUNTS_GROWTH_RATE = Column(DECIMAL(20, 4), doc="应收账款比年初增速")
    ACCT_PAYABLE = Column(DECIMAL(20, 4), doc="应付账款合计")
    ACCT_RCV = Column(DECIMAL(20, 4), doc="应收账款合计")
    ADV_FROM_CUST = Column(DECIMAL(20, 4), doc="预收账款合计")
    ASSET_TURNOVER = Column(DECIMAL(20, 4), doc="资产周转率")
    ASSETS_GROWTH_RATE = Column(DECIMAL(20, 4), doc="总资产比年初增速")
    ASSETS_LIABILITIES = Column(DECIMAL(20, 4), doc="资产负债率")
    BONDS_PAYABLE = Column(DECIMAL(20, 4), doc="应付债券合计")
    CAP_RSRV = Column(DECIMAL(20, 4), doc="资本公积金合计")
    CASH_CASH_EQU_END_PERIOD = Column(DECIMAL(20, 4), doc="期末现金合计")
    CASH_PAID_INVEST = Column(DECIMAL(20, 4), doc="投资支付的现金合计")
    CASH_PAID_INVEST_TOT = Column(DECIMAL(20, 4), doc="投资现金流出合计")
    CASH_PAY_ACQ_CONST_FIOLTA = Column(DECIMAL(20, 4), doc="购建固定无形和长期资产支付的现金合计")
    CASH_PAY_BEH_EMPL = Column(DECIMAL(20, 4), doc="支付给职工以及为职工支付的现金合计")
    CASH_PAY_DIST_DPCP_INT_EXP = Column(DECIMAL(20, 4), doc="分配股利偿付利息支付的现金合计")
    CASH_PAY_GOODS_PURCH_SERV_REC = Column(DECIMAL(20, 4), doc="购买商品支付的现金合计")
    CASH_PREPAY_AMT_BORR = Column(DECIMAL(20, 4), doc="偿付债务支付的现金合计")
    CASH_RECP_BORROW = Column(DECIMAL(20, 4), doc="取得借款收到的现金合计")
    CASH_RECP_CAP_CONTRIB = Column(DECIMAL(20, 4), doc="吸收投资收到的现金合计")
    CASHFLOW_INCOME_RATIO = Column(DECIMAL(20, 4), doc="现金流收入比")
    CONST_IN_PROG = Column(DECIMAL(20, 4), doc="在建工程合计")
    EMPL_BEN_PAYABLE = Column(DECIMAL(20, 4), doc="应付职工薪酬合计")
    FIN_EXP_TOT = Column(DECIMAL(20, 4), doc="财务费用合计")
    FINANCIAL_LEVERAGE = Column(DECIMAL(20, 4), doc="财务杠杆")
    FIX_ASSETS = Column(DECIMAL(20, 4), doc="固定资产合计")
    GERL_ADMIN_EXP_TOT = Column(DECIMAL(20, 4), doc="管理费用合计")
    GROSS_MARGIN_INC_LESS_CHAIN = Column(DECIMAL(20, 4), doc="单季度:毛利率环比增减")
    GROSS_MARGIN_INC_LESS_QUA = Column(DECIMAL(20, 4), doc="单季度:毛利率同比增减")
    GROSS_PROFIT_MARGIN = Column(DECIMAL(20, 4), doc="毛利率")
    GROSSPROFIT_MARGIN_INC_LESS = Column(DECIMAL(20, 4), doc="毛利率同比增减")
    IMPAIR_LOSS_ASSETS_TOT = Column(DECIMAL(20, 4), doc="资产减值损失合计")
    INC_TAX_TOT = Column(DECIMAL(20, 4), doc="所得税合计")
    INGREDIENT_NUM = Column(DECIMAL(20, 0), doc="成分股数量")
    INVEST_REAL_ESTATE = Column(DECIMAL(20, 4), doc="投资性房地产合计")
    LONG_TERM_EQY_INVEST = Column(DECIMAL(20, 4), doc="长期股权投资合计")
    LOSS_INGREDIENT_NUM = Column(DECIMAL(20, 0), doc="亏损成分股数量")
    LT_BORROW = Column(DECIMAL(20, 4), doc="长期借款合计")
    MONETARY_CAP = Column(DECIMAL(20, 4), doc="货币资金合计")
    NET_AFTER_DED_NR_LP_CORRECT = Column(DECIMAL(20, 4), doc="扣非归属净利润合计")
    NET_ASSET_TURNOVER = Column(DECIMAL(20, 4), doc="净资产周转率")
    NET_ASSETS_GROWTH_RATE = Column(DECIMAL(20, 4), doc="净资产比年初增速")
    NET_BUSINESS_CYCLE = Column(DECIMAL(20, 4), doc="净营业周期")
    NET_CASH_FLOWS_FNC_TOT = Column(DECIMAL(20, 4), doc="筹资活动净流量合计")
    NET_CASH_FLOWS_INV_TOT = Column(DECIMAL(20, 4), doc="投资活动净流量合计")
    NET_CASH_RECP_DISP_FIOLTA = Column(DECIMAL(20, 4), doc="处置固定资产等收回的现金合计")
    NET_CASHFLOW_PROFIT = Column(DECIMAL(20, 4), doc="现金流净利润比")
    NET_GAIN_CHG_FV_TOT = Column(DECIMAL(20, 4), doc="公允价值变动净收益合计")
    NET_INCR_CASH_CASH_EQU_TOT = Column(DECIMAL(20, 4), doc="现金及现金等价物净增加额合计")
    NET_INCR_CASH_CASH_EQU_TTM = Column(DECIMAL(20, 4), doc="现金及现金等价物净增加额(TTM)")
    NET_INVEST_INC_TOT = Column(DECIMAL(20, 4), doc="投资净收益合计")
    NET_PRO_RATE_INC_LESS_CHAIN = Column(DECIMAL(20, 4), doc="单季度:净利润率环比增减")
    NET_PRO_RATE_INC_LESS_QUA = Column(DECIMAL(20, 4), doc="单季度:净利润率同比增减")
    NET_PRO_RATE_INC_LESS_TTM = Column(DECIMAL(20, 4), doc="净利率同比增减(TTM)")
    NET_PRO_RATE_INCREASE_LESS = Column(DECIMAL(20, 4), doc="净利润率同比增减")
    NET_PROFIT_GROWTH_RATE = Column(DECIMAL(20, 4), doc="净利润同比增速")
    NET_PROFIT_GROWTH_RATE_CHAIN = Column(DECIMAL(20, 4), doc="单季度:净利润环比增速")
    NET_PROFIT_GROWTH_RATE_QUA = Column(DECIMAL(20, 4), doc="单季度:净利润同比增速")
    NET_PROFIT_GROWTH_RATE_TTM = Column(DECIMAL(20, 4), doc="净利润同比增速(TTM)")
    NET_PROFIT_INCL_MIN_INT_INC = Column(DECIMAL(20, 4), doc="净利润(含少数股东权益)合计")
    NET_PROFIT_RATE = Column(DECIMAL(20, 4), doc="净利润率")
    NET_PROFIT_RATE_QUA = Column(DECIMAL(20, 4), doc="单季度:净利润率")
    NET_PROFIT_RATE_TTM = Column(DECIMAL(20, 4), doc="净利润率(TTM)")
    NET_PROFIT_TOT = Column(DECIMAL(20, 4), doc="净利润合计")
    NET_PROFIT_TTM = Column(DECIMAL(20, 4), doc="净利润(TTM)")
    NON_CUR_LIAB_DUE_WITHIN_1Y = Column(DECIMAL(20, 4), doc="一年内到期的非流动负债合计")
    NON_OPER_EXP_TOT = Column(DECIMAL(20, 4), doc="营业外支出合计")
    NON_OPER_REV_TOT = Column(DECIMAL(20, 4), doc="营业外收入合计")
    NOTES_PAYABLE = Column(DECIMAL(20, 4), doc="应付票据合计")
    NOTES_RCV = Column(DECIMAL(20, 4), doc="应收票据合计")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPER_COST_TOT = Column(DECIMAL(20, 4), doc="营业成本合计")
    OPER_PROFIT_TOT = Column(DECIMAL(20, 4), doc="营业利润合计")
    OPER_REV = Column(DECIMAL(20, 4), doc="营业收入合计")
    OPER_REV_GROWTH_RATE = Column(DECIMAL(20, 4), doc="营业收入同比增速")
    OPER_REV_GROWTH_RATE_CHAIN = Column(DECIMAL(20, 4), doc="单季度:营业收入环比增速")
    OPER_REV_GROWTH_RATE_QUA = Column(DECIMAL(20, 4), doc="单季度:营业收入同比增速")
    OPER_REV_GROWTH_RATE_TTM = Column(DECIMAL(20, 4), doc="营业收入同比增速(TTM)")
    OPER_REV_TTM = Column(DECIMAL(20, 4), doc="营业收入(TTM)")
    OPMODE = Column(String(1))
    OWNERS_EQUITY = Column(DECIMAL(20, 4), doc="所有者权益合计")
    PAID_UP_CAPITAL = Column(DECIMAL(20, 4), doc="实收资本合计")
    PERIOD_EXPENSE_INC_LESS = Column(DECIMAL(20, 4), doc="期间费用率同比增减")
    PERIOD_EXPENSE_INC_LESS_CHAIN = Column(DECIMAL(20, 4), doc="单季度:?期间费用率环比增减")
    PERIOD_EXPENSE_INC_LESS_QUA = Column(DECIMAL(20, 4), doc="单季度:?期间费用率同比增减")
    PERIOD_EXPENSE_RATE = Column(DECIMAL(20, 4), doc="期间费用率")
    PERIOD_EXPENSE_RATE_QUA = Column(DECIMAL(20, 4), doc="单季度:期间费用率")
    PREPAY = Column(DECIMAL(20, 4), doc="预付款项合计")
    PROC_ISSUE_BONDS = Column(DECIMAL(20, 4), doc="发行债券收到的现金合计")
    PROFIT_RATE_QUA = Column(DECIMAL(20, 4), doc="单季度:毛利率")
    REPORT_PERIOD = Column(String(12), doc="报告期")
    REPORT_TYPE_CODE = Column(DECIMAL(9, 0), doc="报表类型代码")
    ROA = Column(DECIMAL(20, 4), doc="ROA")
    ROA_INCREASE_LESS = Column(DECIMAL(20, 4), doc="ROA同比增减")
    ROA_INCREASE_LESS_CHAIN = Column(DECIMAL(20, 4), doc="单季度:ROA环比增减")
    ROA_INCREASE_LESS_QUA = Column(DECIMAL(20, 4), doc="单季度:ROA同比增减")
    ROA_INCREASE_LESS_TTM = Column(DECIMAL(20, 4), doc="ROA同比增减(TTM)")
    ROA_QUA = Column(DECIMAL(20, 4), doc="单季度:ROA")
    ROA_TTM = Column(DECIMAL(20, 4), doc="ROA(TTM)")
    ROE = Column(DECIMAL(20, 4), doc="ROE")
    ROE_INCREASE_LESS = Column(DECIMAL(20, 4), doc="ROE同比增减")
    ROE_INCREASE_LESS_CHAIN = Column(DECIMAL(20, 4), doc="单季度:ROE环比增减")
    ROE_INCREASE_LESS_QUA = Column(DECIMAL(20, 4), doc="单季度:ROE同比增减")
    ROE_INCREASE_LESS_TTM = Column(DECIMAL(20, 4), doc="ROE同比增减(TTM)")
    ROE_QUA = Column(DECIMAL(20, 4), doc="单季度:ROE")
    ROE_TTM = Column(DECIMAL(20, 4), doc="ROE(TTM)")
    S_FA_ARTURNDAYS = Column(DECIMAL(20, 4), doc="应收账款周转天数")
    S_FA_CURRENT = Column(DECIMAL(20, 4), doc="流动比率")
    S_FA_EXTRAORDINARY = Column(DECIMAL(20, 4), doc="非经常性损益合计")
    S_FA_INVTURNDAYS = Column(DECIMAL(20, 4), doc="存货周转天数")
    S_FA_QUICK = Column(DECIMAL(20, 4), doc="速动比率")
    S_FA_SALESCASHINTOOR = Column(DECIMAL(20, 4), doc="销售商品提供劳务收到的现金合计")
    S_INFO_WINDCODE = Column(String(60), doc="指数Wind代码")
    S_VAL_PCF_OCF = Column(DECIMAL(20, 4), doc="经营现金流合计")
    S_VAL_PCF_OCF_CHAIN = Column(DECIMAL(20, 4), doc="单季度:经营现金流环比增速")
    S_VAL_PCF_OCF_GROWTH_RATE = Column(DECIMAL(20, 4), doc="经营现金流同比增速")
    S_VAL_PCF_OCF_GROWTH_RATE_TTM = Column(DECIMAL(20, 4), doc="经营现金流同比增速(TTM)")
    S_VAL_PCF_OCF_QUA = Column(DECIMAL(20, 4), doc="单季度:经营现金流同比增速")
    S_VAL_PCF_OCF_TTM = Column(DECIMAL(20, 4), doc="经营现金流(TTM)")
    SALES_EXPENSE_RATE = Column(DECIMAL(20, 4), doc="销售费用率")
    SALES_EXPENSE_RATE_QUA = Column(DECIMAL(20, 4), doc="单季度:销售费用率")
    SELLING_DIST_EXP_TOT = Column(DECIMAL(20, 4), doc="销售费用合计")
    ST_BORROW = Column(DECIMAL(20, 4), doc="短期借款合计")
    STOCK_RATIO_GROWTH_RATE = Column(DECIMAL(20, 4), doc="存货比年初增速")
    STOT_CASH_INFLOWS_FNC_TOT = Column(DECIMAL(20, 4), doc="筹资活动现金流入合计")
    STOT_CASH_INFLOWS_INV_TOT = Column(DECIMAL(20, 4), doc="投资活动现金流入合计")
    STOT_CASH_INFLOWS_OPER_TOT = Column(DECIMAL(20, 4), doc="经营活动现金流入合计")
    STOT_CASH_OUTFLOWS_FNC_TOT = Column(DECIMAL(20, 4), doc="筹资活动现金流出合计")
    STOT_CASH_OUTFLOWS_OPER_TOT = Column(DECIMAL(20, 4), doc="经营活动现金流出合计")
    TOT_CUR_ASSETS = Column(DECIMAL(20, 4), doc="流动资产合计")
    TOT_CUR_LIAB = Column(DECIMAL(20, 4), doc="流动负债合计")
    TOT_NON_CUR_ASSETS = Column(DECIMAL(20, 4), doc="非流动资产合计")
    TOT_NON_CUR_LIAB = Column(DECIMAL(20, 4), doc="非流动负债合计")
    TOT_PROFIT = Column(DECIMAL(20, 4), doc="利润总额合计")
    TOTAL_ACCOUNTS_RECEIVABLE = Column(DECIMAL(20, 4), doc="应收账款合计")
    TOTAL_ASSETS = Column(DECIMAL(20, 4), doc="总资产合计")
    TOTAL_INVENTORY = Column(DECIMAL(20, 4), doc="存货合计")
    TOTAL_NET_ASSETS = Column(DECIMAL(20, 4), doc="净资产合计")
    UNDISTRIBUTED_PROFIT = Column(DECIMAL(20, 4), doc="未分配利润合计")


class AINDEXHS300CLOSEWEIGHT(Base):

    __tablename__ = 'AINDEXHS300CLOSEWEIGHT'

    I_WEIGHT = Column(DECIMAL(20, 4), doc="权重")
    I_WEIGHT_11 = Column(DECIMAL(20, 2), doc="总股本(股)")
    I_WEIGHT_12 = Column(String(2), doc="自由流通比例(%)(归档后)")
    I_WEIGHT_14 = Column(DECIMAL(20, 8), doc="权重因子")
    I_WEIGHT_15 = Column(DECIMAL(20, 4), doc="收盘")
    I_WEIGHT_16 = Column(String(2), doc="调整后开盘参考价")
    I_WEIGHT_17 = Column(DECIMAL(20, 2), doc="总市值")
    I_WEIGHT_18 = Column(DECIMAL(20, 2), doc="计算用市值")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_WINDCODE = Column(String(40), doc="成份股Wind代码")
    S_IN_INDEX = Column(DECIMAL(20, 2), doc="计算用股本(股)")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")
    TRADE_DT = Column(String(10), doc="交易日期")


class AINDEXHS300WEIGHT(Base):

    __tablename__ = 'AINDEXHS300WEIGHT'

    I_WEIGHT = Column(DECIMAL(20, 4), doc="权重")
    I_WEIGHT_11 = Column(DECIMAL(20, 2), doc="总股本(股)")
    I_WEIGHT_12 = Column(DECIMAL(20, 4), doc="自由流通比例(%)(归档后)")
    I_WEIGHT_14 = Column(DECIMAL(20, 8), doc="权重因子")
    I_WEIGHT_15 = Column(DECIMAL(20, 4), doc="收盘")
    I_WEIGHT_16 = Column(DECIMAL(20, 4), doc="调整后开盘参考价")
    I_WEIGHT_17 = Column(DECIMAL(20, 2), doc="总市值")
    I_WEIGHT_18 = Column(DECIMAL(20, 2), doc="计算用市值")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_WINDCODE = Column(String(60), doc="成份股Wind代码")
    S_IN_INDEX = Column(DECIMAL(20, 2), doc="计算用股本(股)")
    S_INFO_WINDCODE = Column(String(60), doc="指数Wind代码")
    TRADE_DT = Column(String(12), doc="交易日期")


class AINDEXINDUSTRIESEODCITICS(Base):

    __tablename__ = 'AINDEXINDUSTRIESEODCITICS'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_AMOUNT = Column(DECIMAL(20, 4), doc="成交金额(千元)")
    S_DQ_CHANGE = Column(DECIMAL(20, 4), doc="涨跌(点)")
    S_DQ_CLOSE = Column(DECIMAL(20, 4), doc="收盘价(点)")
    S_DQ_HIGH = Column(DECIMAL(20, 4), doc="最高价(点)")
    S_DQ_LOW = Column(DECIMAL(20, 4), doc="最低价(点)")
    S_DQ_OPEN = Column(DECIMAL(20, 4), doc="开盘价(点)")
    S_DQ_PCTCHANGE = Column(DECIMAL(20, 4), doc="涨跌幅(%)")
    S_DQ_PRECLOSE = Column(DECIMAL(20, 4), doc="昨收盘价(点)")
    S_DQ_VOLUME = Column(DECIMAL(20, 4), doc="成交量(手)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")


class AINDEXMEMBERS(Base):

    __tablename__ = 'AINDEXMEMBERS'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="成份股Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")


class AINDEXMEMBERSCITICS(Base):

    __tablename__ = 'AINDEXMEMBERSCITICS'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="成份股Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")


class AINDEXMEMBERSCITICS2(Base):

    __tablename__ = 'AINDEXMEMBERSCITICS2'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class AINDEXMEMBERSCITICS2ZL(Base):

    __tablename__ = 'AINDEXMEMBERSCITICS2ZL'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class AINDEXMEMBERSCITICS3(Base):

    __tablename__ = 'AINDEXMEMBERSCITICS3'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class AINDEXMEMBERSCITICSZL(Base):

    __tablename__ = 'AINDEXMEMBERSCITICSZL'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="成份股Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")


class ASAREPLANTRADE(Base):

    __tablename__ = 'ASAREPLANTRADE'

    ANN_DT = Column(String(8), doc="首次披露公告日")
    ANN_DT_NEW = Column(String(8), doc="最新公告日")
    CHANGE_END_DATE = Column(String(8), doc="变动截止日期")
    CHANGE_START_DATE = Column(String(8), doc="变动起始日期")
    HOLD_NUMBER = Column(DECIMAL(20, 4), doc="持有证券数量(股/张)")
    HOLD_PROPORTION = Column(DECIMAL(20, 4), doc="持股数量占比(%)")
    HOLD_RESTRICTED_STOCK = Column(DECIMAL(20, 4), doc="持有限售股数量(股)")
    HOLD_UNLIMITED_SALE_SHARES = Column(DECIMAL(20, 4), doc="持有无限售股数量(股)")
    HOLDER_ID = Column(String(10), doc="持有方id")
    HOLDER_NAME = Column(String(100), doc="持有方名称")
    HOLDER_STATUS = Column(String(80), doc="股东身份类别")
    HOLDER_TYPE = Column(String(1), doc="股东类型")
    IS_ADJUSTMENT = Column(DECIMAL(1, 0), doc="方案是否有过调整")
    IS_CHANGE_CONTROL = Column(DECIMAL(1, 0), doc="是否导致公司控制权变更")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PLAN_MAX_HOLD_RATIO = Column(DECIMAL(20, 4), doc="拟最大变动数量占持有公司股份的比例(%)")
    PLAN_TRANSACT_MAX = Column(DECIMAL(20, 4), doc="拟变动金额上限(元)")
    PLAN_TRANSACT_MAX_NUM = Column(DECIMAL(20, 4), doc="拟变动数量上限(股/张)")
    PLAN_TRANSACT_MAX_RATIO = Column(DECIMAL(20, 4), doc="拟变动数量上限占比(%)")
    PLAN_TRANSACT_MIN = Column(DECIMAL(20, 4), doc="拟变动金额下限(元)")
    PLAN_TRANSACT_MIN_NUM = Column(DECIMAL(20, 4), doc="拟变动数量下限(股/张)")
    PLAN_TRANSACT_MIN_RATIO = Column(DECIMAL(20, 4), doc="拟变动数量下限占比(%)")
    PROGRAM_ADJUSTMENT_MEMO = Column(String(1000), doc="方案调整说明")
    PROGRAMME_PROGRESS = Column(DECIMAL(9, 0), doc="方案进度代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SPECIAL_CHANGES_MEMO = Column(String(1000), doc="特殊变动说明")
    TOT_ACTUAL_TRANSACT_NUM = Column(DECIMAL(20, 4), doc="实际累计变动证券数量(股/张)")
    TOTAL_CAPITAL_STOCK = Column(DECIMAL(20, 4), doc="公司总股本(股)")
    TRANSACT_OBJECTIVE = Column(String(400), doc="变动目的")
    TRANSACT_PERIOD_DESCRIPTION = Column(String(100), doc="变动期间说明")
    TRANSACT_SOURCE_FUNDS = Column(String(100), doc="变动资金来源")
    TRANSACT_STOCK_SOURCE = Column(String(100), doc="变动股份来源")
    TRANSACT_TYPE = Column(String(4), doc="变动方向")
    TRANSACTION_MODE = Column(String(100), doc="交易方式")
    VARIABLE_PRICE_MEMO = Column(String(100), doc="变动价格说明")


class ASHAREACCOUNTSPAYABLE(Base):

    __tablename__ = 'ASHAREACCOUNTSPAYABLE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="上游公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="上游公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="上游公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_DISCLOSER = Column(String(100), doc="披露公司ID")


class ASHAREADMINISTRATION(Base):

    __tablename__ = 'ASHAREADMINISTRATION'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_MANAGER_NAME = Column(String(80), doc="姓名")
    S_INFO_MANAGER_POST = Column(String(40), doc="职务")
    S_INFO_MANAGER_STARTDATE = Column(String(8), doc="任职日期")
    S_INFO_MANID = Column(String(10), doc="人物id")


class ASHAREANNFINANCIALINDICATOR(Base):

    __tablename__ = 'ASHAREANNFINANCIALINDICATOR'

    ANN_DT = Column(String(8), doc="公告日期")
    CONTRIBUTIONPS = Column(DECIMAL(20, 4), doc="每股社会贡献值(元)")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    GROWTH_BPS_SH = Column(DECIMAL(22, 4), doc="比年初增长率.归属于母公司股东的每股净资产(%)")
    IFLISTED_DATA = Column(DECIMAL(1, 0), doc="是否上市后数据")
    MEMO = Column(String(100), doc="备注")
    NET_PROFIT = Column(DECIMAL(20, 4), doc="国际会计准则净利润(元)")
    NET_PROFIT_YOY = Column(DECIMAL(20, 4), doc="同比增长率.净利润(%)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RD_EXPENSE = Column(DECIMAL(20, 4), doc="研发费用(元)")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    ROE_DILUTED = Column(DECIMAL(20, 4), doc="净资产收益率-摊薄(%)")
    ROE_EX = Column(DECIMAL(20, 4), doc="净资产收益率-扣除(%)")
    ROE_EXWEIGHTED = Column(DECIMAL(20, 4), doc="净资产收益率-扣除/加权(%)")
    ROE_WEIGHTED = Column(DECIMAL(20, 4), doc="净资产收益率-加权(%)")
    S_FA_ARTURN = Column(DECIMAL(20, 4), doc="应收账款周转率(%)")
    S_FA_BPS = Column(DECIMAL(22, 4), doc="每股净资产(元)")
    S_FA_BPS_ADJUST = Column(DECIMAL(20, 4), doc="每股净资产-调整(元)")
    S_FA_BPS_SH = Column(DECIMAL(20, 4), doc="归属于母公司股东的每股净资产(元)")
    S_FA_CURRENT = Column(DECIMAL(20, 4), doc="流动比(%)")
    S_FA_DEDUCTEDPROFIT = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的净利润(扣除少数股东损益)")
    S_FA_DEDUCTEDPROFIT_YOY = Column(DECIMAL(22, 4), doc="同比增长率.扣除非经常性损益后的净利润(扣除少数股东损益)(%)")
    S_FA_EPS_BASIC = Column(DECIMAL(20, 4), doc="每股收益-基本")
    S_FA_EPS_DILUTED = Column(DECIMAL(20, 4), doc="每股收益-摊薄(元)")
    S_FA_EPS_DILUTED2 = Column(DECIMAL(20, 6), doc="每股收益-稀释(元)")
    S_FA_EPS_EX = Column(DECIMAL(20, 4), doc="每股收益-扣除(元)")
    S_FA_EPS_EXBASIC = Column(DECIMAL(20, 4), doc="每股收益-扣除/基本")
    S_FA_EPS_EXDILUTED = Column(DECIMAL(20, 4), doc="每股收益-扣除/稀释(元)")
    S_FA_EXTRAORDINARY = Column(DECIMAL(22, 4), doc="非经常性损益(元)")
    S_FA_INVTURN = Column(DECIMAL(20, 4), doc="存货周转率(%)")
    S_FA_OCFPS = Column(DECIMAL(20, 4), doc="每股经营活动产生的现金流量净额(元)")
    S_FA_QUICK = Column(DECIMAL(20, 4), doc="速动比(%)")
    S_FA_YOYEBT = Column(DECIMAL(20, 4), doc="同比增长率.利润总额(%)")
    S_FA_YOYEPS_BASIC = Column(DECIMAL(22, 4), doc="同比增长率.基本每股收益(%)")
    S_FA_YOYEPS_DILUTED = Column(DECIMAL(22, 4), doc="同比增长率.稀释每股收益(%)")
    S_FA_YOYEQUITY = Column(DECIMAL(22, 4), doc="比年初增长率.归属母公司的股东权益(%)")
    S_FA_YOYOCFPS = Column(DECIMAL(22, 4), doc="同比增长率.每股经营活动产生的现金流量净额(%)")
    S_FA_YOYOP = Column(DECIMAL(20, 4), doc="同比增长率.营业利润(%)")
    S_FT_DEBTTOASSETS = Column(DECIMAL(20, 4), doc="资产负债率(%)")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_DIV = Column(String(40), doc="分红方案")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    STATEMENT_TYPE = Column(DECIMAL(9, 0), doc="报表类型代码")
    YOY_NET_CASH_FLOWS = Column(DECIMAL(22, 4), doc="同比增长率.经营活动产生的现金流量净额(%)")
    YOY_ROE_DILUTED = Column(DECIMAL(22, 4), doc="同比增长率.净资产收益率(摊薄)(%)")


class ASHAREAUDITOPINION(Base):

    __tablename__ = 'ASHAREAUDITOPINION'

    ANN_DT = Column(String(8), doc="公告日期")
    ANN_DT1 = Column(String(8), doc="内控审计报告公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_AUDIT_FEE_MEMO = Column(String(1000), doc="审计费用说明")
    S_AUDIT_RESULT_MEMO = Column(LONGTEXT, doc="审计结果说明")
    S_IN_CONTROL_ACCOUNTANT = Column(String(100), doc="内控签字会计师")
    S_IN_CONTROL_ACCOUNTING_FIRM = Column(String(10), doc="内控会计师事务所ID")
    S_IN_CONTROL_AUDIT = Column(LONGTEXT, doc="内控审计结果说明")
    S_IN_CONTROL_AUDIT_OPINION = Column(DECIMAL(9, 0), doc="内控审计意见类别代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PAY_AUDIT_EXPENSES = Column(DECIMAL(20, 4), doc="当期实付审计费用(总额)(元)")
    S_STMNOTE_AUDIT_AGENCY = Column(String(100), doc="会计师事务所")
    S_STMNOTE_AUDIT_CATEGORY = Column(DECIMAL(9, 0), doc="审计结果类别代码")
    S_STMNOTE_AUDIT_CPA = Column(String(100), doc="签字会计师")


class ASHAREBALANCESHEET(Base):

    __tablename__ = 'ASHAREBALANCESHEET'

    ACC_EXP = Column(DECIMAL(20, 4), doc="预提费用")
    ACCOUNTS_PAYABLE = Column(DECIMAL(20, 4), doc="应付票据及应付账款")
    ACCOUNTS_RECEIVABLE = Column(DECIMAL(20, 4), doc="应收款项")
    ACCOUNTS_RECEIVABLE_BILL = Column(DECIMAL(20, 4), doc="应收票据及应收账款")
    ACCT_PAYABLE = Column(DECIMAL(20, 4), doc="应付账款")
    ACCT_RCV = Column(DECIMAL(20, 4), doc="应收账款")
    ACTING_TRADING_SEC = Column(DECIMAL(20, 4), doc="代理买卖证券款")
    ACTING_UW_SEC = Column(DECIMAL(20, 4), doc="代理承销证券款")
    ACTUAL_ANN_DT = Column(String(8), doc="实际公告日期")
    ADV_FROM_CUST = Column(DECIMAL(20, 4), doc="预收款项")
    AGENCY_BUS_ASSETS = Column(DECIMAL(20, 4), doc="代理业务资产")
    AGENCY_BUS_LIAB = Column(DECIMAL(20, 4), doc="代理业务负债")
    ANN_DT = Column(String(8), doc="公告日期")
    ASSET_DEP_OTH_BANKS_FIN_INST = Column(DECIMAL(20, 4), doc="存放同业和其它金融机构款项")
    BONDS_PAYABLE = Column(DECIMAL(20, 4), doc="应付债券")
    BORROW_CENTRAL_BANK = Column(DECIMAL(20, 4), doc="向中央银行借款")
    CAP_MRGN_PAID = Column(DECIMAL(20, 4), doc="存出资本保证金")
    CAP_RSRV = Column(DECIMAL(20, 4), doc="资本公积金")
    CAP_STK = Column(DECIMAL(20, 4), doc="股本")
    CASH_DEPOSITS_CENTRAL_BANK = Column(DECIMAL(20, 4), doc="现金及存放中央银行款项")
    CLAIMS_PAYABLE = Column(DECIMAL(20, 4), doc="应付赔付款")
    CLIENTS_CAP_DEPOSIT = Column(DECIMAL(20, 4), doc="客户资金存款")
    CLIENTS_RSRV_SETTLE = Column(DECIMAL(20, 4), doc="客户备付金")
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(DECIMAL(20, 4), doc="外币报表折算差额")
    COMP_TYPE_CODE = Column(String(2), doc="公司类型代码")
    CONST_IN_PROG = Column(DECIMAL(20, 4), doc="在建工程")
    CONST_IN_PROG_TOT = Column(DECIMAL(20, 4), doc="在建工程(合计)(元)")
    CONSUMPTIVE_BIO_ASSETS = Column(DECIMAL(20, 4), doc="消耗性生物资产")
    CONTRACT_LIABILITIES = Column(DECIMAL(20, 4), doc="合同负债")
    CONTRACTUAL_ASSETS = Column(DECIMAL(20, 4), doc="合同资产")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    CUST_BANK_DEP = Column(DECIMAL(20, 4), doc="吸收存款")
    DEBT_INVESTMENT = Column(DECIMAL(20, 4), doc="债权投资(元)")
    DEFERRED_EXP = Column(DECIMAL(20, 4), doc="待摊费用")
    DEFERRED_INC = Column(DECIMAL(20, 4), doc="递延收益")
    DEFERRED_INC_NON_CUR_LIAB = Column(DECIMAL(20, 4), doc="递延收益-非流动负债")
    DEFERRED_TAX_ASSETS = Column(DECIMAL(20, 4), doc="递延所得税资产")
    DEFERRED_TAX_LIAB = Column(DECIMAL(20, 4), doc="递延所得税负债")
    DEPOSIT_RECEIVED = Column(DECIMAL(20, 4), doc="存入保证金")
    DEPOSIT_RECEIVED_IB_DEPOSITS = Column(DECIMAL(20, 4), doc="吸收存款及同业存放")
    DERIVATIVE_FIN_ASSETS = Column(DECIMAL(20, 4), doc="衍生金融资产")
    DERIVATIVE_FIN_LIAB = Column(DECIMAL(20, 4), doc="衍生金融负债")
    DVD_PAYABLE = Column(DECIMAL(20, 4), doc="应付股利")
    DVD_PAYABLE_INSURED = Column(DECIMAL(20, 4), doc="应付保单红利")
    DVD_RCV = Column(DECIMAL(20, 4), doc="应收股利")
    EMPL_BEN_PAYABLE = Column(DECIMAL(20, 4), doc="应付职工薪酬")
    FIN_ASSETS_AVAIL_FOR_SALE = Column(DECIMAL(20, 4), doc="可供出售金融资产")
    FIN_ASSETS_COST_SHARING = Column(DECIMAL(20, 4), doc="以摊余成本计量的金融资产")
    FIN_ASSETS_FAIR_VALUE = Column(DECIMAL(20, 4), doc="以公允价值计量且其变动计入其他综合收益的金融资产")
    FIX_ASSETS = Column(DECIMAL(20, 4), doc="固定资产")
    FIX_ASSETS_DISP = Column(DECIMAL(20, 4), doc="固定资产清理")
    FUND_SALES_FIN_ASSETS_RP = Column(DECIMAL(20, 4), doc="卖出回购金融资产款")
    GOODWILL = Column(DECIMAL(20, 4), doc="商誉")
    HANDLING_CHARGES_COMM_PAYABLE = Column(DECIMAL(20, 4), doc="应付手续费及佣金")
    HELD_TO_MTY_INVEST = Column(DECIMAL(20, 4), doc="持有至到期投资")
    HFS_ASSETS = Column(DECIMAL(20, 4), doc="持有待售的资产")
    HFS_SALES = Column(DECIMAL(20, 4), doc="持有待售的负债")
    INCL_PLEDGE_LOAN = Column(DECIMAL(20, 4), doc="其中:质押借款")
    INCL_SEAT_FEES_EXCHANGE = Column(DECIMAL(20, 4), doc="其中:交易席位费")
    INDEPENDENT_ACCT_ASSETS = Column(DECIMAL(20, 4), doc="独立账户资产")
    INDEPENDENT_ACCT_LIAB = Column(DECIMAL(20, 4), doc="独立账户负债")
    INSURED_DEPOSIT_INVEST = Column(DECIMAL(20, 4), doc="保户储金及投资款")
    INSURED_PLEDGE_LOAN = Column(DECIMAL(20, 4), doc="保户质押贷款")
    INT_PAYABLE = Column(DECIMAL(20, 4), doc="应付利息")
    INT_RCV = Column(DECIMAL(20, 4), doc="应收利息")
    INTANG_ASSETS = Column(DECIMAL(20, 4), doc="无形资产")
    INVENTORIES = Column(DECIMAL(20, 4), doc="存货")
    INVEST_REAL_ESTATE = Column(DECIMAL(20, 4), doc="投资性房地产")
    LEASE_LIAB = Column(DECIMAL(20, 4), doc="租赁负债")
    LENDING_FUNDS = Column(DECIMAL(20, 4), doc="融出资金")
    LESS_TSY_STK = Column(DECIMAL(20, 4), doc="减:库存股")
    LIAB_DEP_OTH_BANKS_FIN_INST = Column(DECIMAL(20, 4), doc="同业和其它金融机构存放款项")
    LIFE_INSUR_RSRV = Column(DECIMAL(20, 4), doc="寿险责任准备金")
    LOANS_AND_ADV_GRANTED = Column(DECIMAL(20, 4), doc="发放贷款及垫款")
    LOANS_OTH_BANKS = Column(DECIMAL(20, 4), doc="拆入资金")
    LOANS_TO_OTH_BANKS = Column(DECIMAL(20, 4), doc="拆出资金")
    LONG_TERM_DEFERRED_EXP = Column(DECIMAL(20, 4), doc="长期待摊费用")
    LONG_TERM_EQY_INVEST = Column(DECIMAL(20, 4), doc="长期股权投资")
    LONG_TERM_REC = Column(DECIMAL(20, 4), doc="长期应收款")
    LT_BORROW = Column(DECIMAL(20, 4), doc="长期借款")
    LT_HEALTH_INSUR_V = Column(DECIMAL(20, 4), doc="长期健康险责任准备金")
    LT_PAYABLE = Column(DECIMAL(20, 4), doc="长期应付款")
    LT_PAYABLE_TOT = Column(DECIMAL(20, 4), doc="长期应付款(合计)(元)")
    LT_PAYROLL_PAYABLE = Column(DECIMAL(20, 4), doc="长期应付职工薪酬")
    MINORITY_INT = Column(DECIMAL(20, 4), doc="少数股东权益")
    MONETARY_CAP = Column(DECIMAL(20, 4), doc="货币资金")
    MRGN_PAID = Column(DECIMAL(20, 4), doc="存出保证金")
    NON_CUR_ASSETS_DUE_WITHIN_1Y = Column(DECIMAL(20, 4), doc="一年内到期的非流动资产")
    NON_CUR_LIAB_DUE_WITHIN_1Y = Column(DECIMAL(20, 4), doc="一年内到期的非流动负债")
    NOTES_PAYABLE = Column(DECIMAL(20, 4), doc="应付票据")
    NOTES_RCV = Column(DECIMAL(20, 4), doc="应收票据")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OIL_AND_NATURAL_GAS_ASSETS = Column(DECIMAL(20, 4), doc="油气资产")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OTH_ASSETS = Column(DECIMAL(20, 4), doc="其他资产")
    OTH_CUR_ASSETS = Column(DECIMAL(20, 4), doc="其他流动资产")
    OTH_CUR_LIAB = Column(DECIMAL(20, 4), doc="其他流动负债")
    OTH_LIAB = Column(DECIMAL(20, 4), doc="其他负债")
    OTH_NON_CUR_ASSETS = Column(DECIMAL(20, 4), doc="其他非流动资产")
    OTH_NON_CUR_LIAB = Column(DECIMAL(20, 4), doc="其他非流动负债")
    OTH_PAYABLE = Column(DECIMAL(20, 4), doc="其他应付款")
    OTH_PAYABLE_TOT = Column(DECIMAL(20, 4), doc="其他应付款(合计)(元)")
    OTH_RCV = Column(DECIMAL(20, 4), doc="其他应收款")
    OTH_RCV_TOT = Column(DECIMAL(20, 4), doc="其他应收款(合计)（元）")
    OTHER_COMP_INCOME = Column(DECIMAL(20, 4), doc="其他综合收益")
    OTHER_DEBT_INVESTMENT = Column(DECIMAL(20, 4), doc="其他债权投资(元)")
    OTHER_EQUITY_INVESTMENT = Column(DECIMAL(20, 4), doc="其他权益工具投资(元)")
    OTHER_EQUITY_TOOLS = Column(DECIMAL(20, 4), doc="其他权益工具")
    OTHER_EQUITY_TOOLS_P_SHR = Column(DECIMAL(20, 4), doc="其他权益工具:优先股")
    OTHER_ILLIQUIDFINANCIAL_ASSETS = Column(DECIMAL(20, 4), doc="其他非流动金融资产(元)")
    OTHER_SUSTAINABLE_BOND = Column(DECIMAL(20, 4), doc="其他权益工具:永续债(元)")
    OUT_LOSS_RSRV = Column(DECIMAL(20, 4), doc="未决赔款准备金")
    PAYABLE_TO_REINSURER = Column(DECIMAL(20, 4), doc="应付分保账款")
    PAYABLES = Column(DECIMAL(20, 4), doc="应付款项")
    PRECIOUS_METALS = Column(DECIMAL(20, 4), doc="贵金属")
    PREM_RCV = Column(DECIMAL(20, 4), doc="应收保费")
    PREM_RECEIVED_ADV = Column(DECIMAL(20, 4), doc="预收保费")
    PREPAY = Column(DECIMAL(20, 4), doc="预付款项")
    PRODUCTIVE_BIO_ASSETS = Column(DECIMAL(20, 4), doc="生产性生物资产")
    PROJ_MATL = Column(DECIMAL(20, 4), doc="工程物资")
    PROV_NOM_RISKS = Column(DECIMAL(20, 4), doc="一般风险准备")
    PROVISIONS = Column(DECIMAL(20, 4), doc="预计负债")
    R_AND_D_COSTS = Column(DECIMAL(20, 4), doc="开发支出")
    RCV_CEDED_CLAIM_RSRV = Column(DECIMAL(20, 4), doc="应收分保未决赔款准备金")
    RCV_CEDED_LIFE_INSUR_RSRV = Column(DECIMAL(20, 4), doc="应收分保寿险责任准备金")
    RCV_CEDED_LT_HEALTH_INSUR_RSRV = Column(DECIMAL(20, 4), doc="应收分保长期健康险责任准备金")
    RCV_CEDED_UNEARNED_PREM_RSRV = Column(DECIMAL(20, 4), doc="应收分保未到期责任准备金")
    RCV_FROM_CEDED_INSUR_CONT_RSRV = Column(DECIMAL(20, 4), doc="应收分保合同准备金")
    RCV_FROM_REINSURER = Column(DECIMAL(20, 4), doc="应收分保账款")
    RCV_INVEST = Column(DECIMAL(20, 4), doc="应收款项类投资")
    RECEIVABLES_FINANCING = Column(DECIMAL(20, 4), doc="应收款项融资")
    RED_MONETARY_CAP_FOR_SALE = Column(DECIMAL(20, 4), doc="买入返售金融资产")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    RIGHT_USE_ASSETS = Column(DECIMAL(20, 4), doc="使用权资产")
    RSRV_INSUR_CONT = Column(DECIMAL(20, 4), doc="保险合同准备金")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SETTLE_RSRV = Column(DECIMAL(20, 4), doc="结算备付金")
    SPE_BAL_ASSETS_DIFF = Column(DECIMAL(20, 4), doc="资产差额(特殊报表科目)")
    SPE_BAL_LIAB_DIFF = Column(DECIMAL(20, 4), doc="负债差额(特殊报表科目)")
    SPE_BAL_LIAB_EQY_DIFF = Column(DECIMAL(20, 4), doc="负债及股东权益差额(特殊报表项目)")
    SPE_BAL_SHRHLDR_EQY_DIFF = Column(DECIMAL(20, 4), doc="股东权益差额(特殊报表科目)")
    SPE_CUR_ASSETS_DIFF = Column(DECIMAL(20, 4), doc="流动资产差额(特殊报表科目)")
    SPE_CUR_LIAB_DIFF = Column(DECIMAL(20, 4), doc="流动负债差额(特殊报表科目)")
    SPE_NON_CUR_ASSETS_DIFF = Column(DECIMAL(20, 4), doc="非流动资产差额(特殊报表科目)")
    SPE_NON_CUR_LIAB_DIFF = Column(DECIMAL(20, 4), doc="非流动负债差额(特殊报表科目)")
    SPECIAL_RSRV = Column(DECIMAL(20, 4), doc="专项储备")
    SPECIFIC_ITEM_PAYABLE = Column(DECIMAL(20, 4), doc="专项应付款")
    ST_BONDS_PAYABLE = Column(DECIMAL(20, 4), doc="应付短期债券")
    ST_BORROW = Column(DECIMAL(20, 4), doc="短期借款")
    ST_FINANCING_PAYABLE = Column(DECIMAL(20, 4), doc="应付短期融资款")
    STATEMENT_TYPE = Column(String(10), doc="报表类型")
    STM_BS_TOT = Column(DECIMAL(20, 4), doc="固定资产(合计)(元)")
    SUBR_REC = Column(DECIMAL(20, 4), doc="应收代位追偿款")
    SURPLUS_RSRV = Column(DECIMAL(20, 4), doc="盈余公积金")
    TAXES_SURCHARGES_PAYABLE = Column(DECIMAL(20, 4), doc="应交税费")
    TIME_DEPOSITS = Column(DECIMAL(20, 4), doc="定期存款")
    TOT_ASSETS = Column(DECIMAL(20, 4), doc="资产总计")
    TOT_BAL_ASSETS_DIFF = Column(DECIMAL(20, 4), doc="资产差额(合计平衡项目)")
    TOT_BAL_LIAB_DIFF = Column(DECIMAL(20, 4), doc="负债差额(合计平衡项目)")
    TOT_BAL_LIAB_EQY_DIFF = Column(DECIMAL(20, 4), doc="负债及股东权益差额(合计平衡项目)")
    TOT_BAL_SHRHLDR_EQY_DIFF = Column(DECIMAL(20, 4), doc="股东权益差额(合计平衡项目)")
    TOT_CUR_ASSETS = Column(DECIMAL(20, 4), doc="流动资产合计")
    TOT_CUR_ASSETS_DIFF = Column(DECIMAL(20, 4), doc="流动资产差额(合计平衡项目)")
    TOT_CUR_LIAB = Column(DECIMAL(20, 4), doc="流动负债合计")
    TOT_CUR_LIAB_DIFF = Column(DECIMAL(20, 4), doc="流动负债差额(合计平衡项目)")
    TOT_LIAB = Column(DECIMAL(20, 4), doc="负债合计")
    TOT_LIAB_SHRHLDR_EQY = Column(DECIMAL(20, 4), doc="负债及股东权益总计")
    TOT_NON_CUR_ASSETS = Column(DECIMAL(20, 4), doc="非流动资产合计")
    TOT_NON_CUR_ASSETS_DIFF = Column(DECIMAL(20, 4), doc="非流动资产差额(合计平衡项目)")
    TOT_NON_CUR_LIAB = Column(DECIMAL(20, 4), doc="非流动负债合计")
    TOT_NON_CUR_LIAB_DIFF = Column(DECIMAL(20, 4), doc="非流动负债差额(合计平衡项目)")
    TOT_SHR = Column(DECIMAL(20, 4), doc="期末总股本")
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(DECIMAL(20, 4), doc="股东权益合计(不含少数股东权益)")
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(DECIMAL(20, 4), doc="股东权益合计(含少数股东权益)")
    TRADABLE_FIN_ASSETS = Column(DECIMAL(20, 4), doc="交易性金融资产")
    TRADABLE_FIN_LIAB = Column(DECIMAL(20, 4), doc="交易性金融负债")
    UNCONFIRMED_INVEST_LOSS = Column(DECIMAL(20, 4), doc="未确认的投资损失")
    UNDISTRIBUTED_PROFIT = Column(DECIMAL(20, 4), doc="未分配利润")
    UNEARNED_PREM_RSRV = Column(DECIMAL(20, 4), doc="未到期责任准备金")
    WIND_CODE = Column(String(40), doc="Wind代码")


class ASHAREBANKINDICATOR(Base):

    __tablename__ = 'ASHAREBANKINDICATOR'

    ANN_DT = Column(String(8))
    BAD_LOAD_FIVE_CLASS = Column(DECIMAL(20, 4))
    CAPI_ADE_RATIO = Column(DECIMAL(20, 4))
    CASH_ON_HAND = Column(DECIMAL(20, 4))
    CASH_RESERVE_RATIO_CNY = Column(DECIMAL(20, 4))
    CASH_RESERVE_RATIO_FC = Column(DECIMAL(20, 4))
    CORE_CAPI_ADE_RATIO = Column(DECIMAL(20, 4))
    CORE_CAPI_NET_AMOUNT = Column(DECIMAL(20, 4))
    COST_INCOME_RATIO = Column(DECIMAL(20, 4))
    CRNCY_CODE = Column(String(10))
    IBUSINESS_LOAN_RATIO = Column(DECIMAL(20, 4))
    INTERECT_COLLECTION_RATIO = Column(DECIMAL(20, 4))
    INTEREST_BEARING_ASSET = Column(DECIMAL(20, 4))
    INTEREST_BEARING_ASSET_COMP = Column(DECIMAL(20, 4))
    INTEREST_BEARING_ASSET_IFPUB = Column(DECIMAL(1, 0))
    INTEREST_BEARING_LIA = Column(DECIMAL(20, 4))
    INTEREST_BEARING_LIA_COMP = Column(DECIMAL(20, 4))
    INTEREST_BEARING_LIA_IFPUB = Column(DECIMAL(1, 0))
    LARGEST_CUSTOMER_LOAN = Column(DECIMAL(20, 4))
    LEND_TO_BANKS_RATIO = Column(DECIMAL(20, 4))
    LOAN_DEPO_RATIO = Column(DECIMAL(20, 4))
    LOAN_DEPO_RATIO_NORMB = Column(DECIMAL(20, 4))
    LOAN_DEPO_RATIO_RMB = Column(DECIMAL(20, 4))
    LOAN_FROM_BANKS_RATIO = Column(DECIMAL(20, 4))
    LOAN_LOSS_PROVISION = Column(DECIMAL(20, 4))
    LONGTERM_LOANS_RATIO_CNY = Column(DECIMAL(20, 4))
    LONGTERM_LOANS_RATIO_FC = Column(DECIMAL(20, 4))
    MARKET_RISK_CAPITAL = Column(DECIMAL(20, 4))
    NET_CAPITAL = Column(DECIMAL(20, 4))
    NET_INTEREST_MARGIN = Column(DECIMAL(20, 4))
    NET_INTEREST_MARGIN_IFPUB = Column(DECIMAL(1, 0))
    NET_INTEREST_MARGIN_IS_ANN = Column(DECIMAL(20, 4))
    NET_INTEREST_SPREAD = Column(DECIMAL(20, 4))
    NET_INTEREST_SPREAD_IS_ANN = Column(DECIMAL(20, 4))
    NON_INTEREST_INCOME = Column(DECIMAL(20, 4))
    NON_INTEREST_MARGIN = Column(DECIMAL(20, 4))
    NONEANING_ASSET = Column(DECIMAL(20, 4))
    NONEANING_LIA = Column(DECIMAL(20, 4))
    NPL_PROVISION_COVERAGE = Column(DECIMAL(20, 4))
    NPL_RATIO = Column(DECIMAL(20, 4))
    OBJECT_ID = Column(String(100), primary_key=True)
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OVERDUE_LOAN = Column(DECIMAL(20, 4))
    OVERSEAS_FUNDS_APP_RATIO = Column(DECIMAL(20, 4))
    REPORT_PERIOD = Column(String(8))
    RISK_WEIGHT_ASSET = Column(DECIMAL(20, 4))
    S_INFO_WINDCODE = Column(String(40))
    ST_ASSET_LIQ_RATIO_NORMB = Column(DECIMAL(20, 4))
    ST_ASSET_LIQ_RATIO_RMB = Column(DECIMAL(20, 4))
    STATEMENT_TYPE = Column(String(10))
    TOP_TEN_CUSTOMER_LOAN = Column(DECIMAL(20, 4))
    TOTAL_DEPOSIT = Column(DECIMAL(20, 4))
    TOTAL_INTEREST_EXP = Column(DECIMAL(20, 4))
    TOTAL_INTEREST_INCOME = Column(DECIMAL(20, 4))
    TOTAL_LOAN = Column(DECIMAL(20, 4))


class ASHAREBEGUARANTEED(Base):

    __tablename__ = 'ASHAREBEGUARANTEED'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="担保公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="担保公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="担保公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHARECALENDAR(Base):

    __tablename__ = 'ASHARECALENDAR'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所英文简称")
    TRADE_DAYS = Column(String(8), doc="交易日")


class ASHARECAPITALIZATION(Base):

    __tablename__ = 'ASHARECAPITALIZATION'

    ANN_DT = Column(String(8), doc="公告日期")
    CHANGE_DT = Column(String(8), doc="变动日期")
    CHANGE_DT1 = Column(String(8), doc="变动日期1")
    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    FLOAT_A_SHR = Column(DECIMAL(20, 4), doc="流通A股(万股)")
    FLOAT_B_SHR = Column(DECIMAL(20, 4), doc="流通B股(万股)")
    FLOAT_H_SHR = Column(DECIMAL(20, 4), doc="流通H股(万股)")
    FLOAT_OVERSEAS_SHR = Column(DECIMAL(20, 4), doc="境外流通股(万股)")
    FLOAT_SHR = Column(DECIMAL(20, 4), doc="流通股(万股)")
    IS_VALID = Column(DECIMAL(5, 0), doc="是否有效")
    NON_TRADABLE_SHR = Column(DECIMAL(20, 4), doc="非流通股")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OTHER_RESTRICTED_SHR = Column(DECIMAL(20, 4), doc="其他限售股")
    RESTRICTED_A_SHR = Column(DECIMAL(20, 4), doc="限售A股(万股)")
    RESTRICTED_B_SHR = Column(DECIMAL(20, 4), doc="限售B股(万股)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_SHARE_CHANGEREASON = Column(String(30), doc="股本变动原因")
    S_SHARE_H = Column(DECIMAL(20, 4), doc="香港上市股")
    S_SHARE_NONTRADABLE = Column(DECIMAL(20, 4), doc="股改前非流通股")
    S_SHARE_NTRD_DOMESINITOR = Column(DECIMAL(20, 4), doc="非流通股(境内法人股:境内发起人股)")
    S_SHARE_NTRD_FUNDBAL = Column(DECIMAL(20, 4), doc="非流通股(境内法人股:基金持股)")
    S_SHARE_NTRD_GENJURIS = Column(DECIMAL(20, 4), doc="非流通股(境内法人股:一般法人股)")
    S_SHARE_NTRD_INSDEREMP = Column(DECIMAL(20, 4), doc="内部职工股(万股)")
    S_SHARE_NTRD_IPOINIP = Column(DECIMAL(20, 4), doc="非流通股(自然人股)")
    S_SHARE_NTRD_IPOJURIS = Column(DECIMAL(20, 4), doc="非流通股(境内法人股:募集法人股)")
    S_SHARE_NTRD_NET = Column(DECIMAL(20, 4), doc="NET股(万股)")
    S_SHARE_NTRD_NONLSTFRGN = Column(DECIMAL(20, 4), doc="非流通股(非上市外资股)")
    S_SHARE_NTRD_PRFSHARE = Column(DECIMAL(20, 4), doc="优先股(万股)")
    S_SHARE_NTRD_SNORMNGER = Column(DECIMAL(20, 4), doc="流通股(高管持股)")
    S_SHARE_NTRD_STAQ = Column(DECIMAL(20, 4), doc="STAQ股(万股)")
    S_SHARE_NTRD_STATE = Column(DECIMAL(20, 4), doc="非流通股(国家股)")
    S_SHARE_NTRD_STATE_PCT = Column(DECIMAL(20, 4), doc="非流通股(国有股)")
    S_SHARE_NTRD_STATJUR = Column(DECIMAL(20, 4), doc="非流通股(国有法人股)")
    S_SHARE_NTRD_STRTINVESTOR = Column(DECIMAL(20, 4), doc="非流通股(境内法人股:战略投资者持股)")
    S_SHARE_NTRD_SUBDOMESJUR = Column(DECIMAL(20, 4), doc="非流通股(境内法人股)")
    S_SHARE_NTRD_TRFNSHARE = Column(DECIMAL(20, 4), doc="转配股(万股)")
    S_SHARE_OTCA = Column(DECIMAL(20, 4), doc="三板A股")
    S_SHARE_OTCB = Column(DECIMAL(20, 4), doc="三板B股")
    S_SHARE_RTD_DOMESJUR = Column(DECIMAL(20, 4), doc="限售A股(其他内资持股:境内法人持股)")
    S_SHARE_RTD_DOMESNP = Column(DECIMAL(20, 4), doc="限售A股(其他内资持股:境内自然人持股)")
    S_SHARE_RTD_FRGNJUR = Column(DECIMAL(20, 4), doc="限售A股(境外法人持股)")
    S_SHARE_RTD_FRGNNP = Column(DECIMAL(20, 4), doc="限售A股(境外自然人持股)")
    S_SHARE_RTD_INST = Column(DECIMAL(20, 4), doc="限售A股(其他内资持股:机构配售股)")
    S_SHARE_RTD_SENMANAGER = Column(DECIMAL(20, 4), doc="限售股份(高管持股)(万股)")
    S_SHARE_RTD_STATE = Column(DECIMAL(20, 4), doc="限售A股(国家持股)")
    S_SHARE_RTD_STATEJUR = Column(DECIMAL(20, 4), doc="限售A股(国有法人持股)")
    S_SHARE_RTD_SUBFRGN = Column(DECIMAL(20, 4), doc="限售A股(外资持股)")
    S_SHARE_RTD_SUBOTHERDOMES = Column(DECIMAL(20, 4), doc="限售A股(其他内资持股)")
    S_SHARE_TOTALA = Column(DECIMAL(20, 4), doc="A股合计")
    S_SHARE_TOTALB = Column(DECIMAL(20, 4), doc="B股合计")
    S_SHARE_TOTALOTC = Column(DECIMAL(20, 4), doc="三板合计")
    S_SHARE_TOTALRESTRICTED = Column(DECIMAL(20, 4), doc="限售股合计")
    S_SHARE_TOTALTRADABLE = Column(DECIMAL(20, 4), doc="流通股合计")
    TOT_SHR = Column(DECIMAL(20, 4), doc="总股本(万股)")
    WIND_CODE = Column(String(40), doc="Wind代码")


class ASHARECAPITALOPERATION(Base):

    __tablename__ = 'ASHARECAPITALOPERATION'

    ANN_DT = Column(String(8))
    CRNCY_CODE = Column(String(3))
    OBJECT_ID = Column(String(100), primary_key=True)
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CAPITALOPERAT_COMPWINDCODE = Column(String(40))
    S_CAPITALOPERATION_AMOUNT = Column(DECIMAL(20, 4))
    S_CAPITALOPERATION_COMPANYNAME = Column(String(100))
    S_CAPITALOPERATION_ENDDATE = Column(String(8))
    S_CAPITALOPERATION_SHARE = Column(DECIMAL(20, 4))
    S_INFO_WINDCODE = Column(String(40))


class ASHARECASHFLOW(Base):

    __tablename__ = 'ASHARECASHFLOW'

    ACTUAL_ANN_DT = Column(String(8), doc="实际公告日期")
    AMORT_INTANG_ASSETS = Column(DECIMAL(20, 4), doc="无形资产摊销")
    AMORT_LT_DEFERRED_EXP = Column(DECIMAL(20, 4), doc="长期待摊费用摊销")
    ANN_DT = Column(String(8), doc="公告日期")
    CASH_CASH_EQU_BEG_PERIOD = Column(DECIMAL(20, 4), doc="期初现金及现金等价物余额")
    CASH_CASH_EQU_END_PERIOD = Column(DECIMAL(20, 4), doc="期末现金及现金等价物余额")
    CASH_PAID_INVEST = Column(DECIMAL(20, 4), doc="投资支付的现金")
    CASH_PAY_ACQ_CONST_FIOLTA = Column(DECIMAL(20, 4), doc="购建固定资产、无形资产和其他长期资产支付的现金")
    CASH_PAY_BEH_EMPL = Column(DECIMAL(20, 4), doc="支付给职工以及为职工支付的现金")
    CASH_PAY_CLAIMS_ORIG_INCO = Column(DECIMAL(20, 4), doc="支付原保险合同赔付款项的现金")
    CASH_PAY_DIST_DPCP_INT_EXP = Column(DECIMAL(20, 4), doc="分配股利、利润或偿付利息支付的现金")
    CASH_PAY_GOODS_PURCH_SERV_REC = Column(DECIMAL(20, 4), doc="购买商品、接受劳务支付的现金")
    CASH_PREPAY_AMT_BORR = Column(DECIMAL(20, 4), doc="偿还债务支付的现金")
    CASH_RECP_BORROW = Column(DECIMAL(20, 4), doc="取得借款收到的现金")
    CASH_RECP_CAP_CONTRIB = Column(DECIMAL(20, 4), doc="吸收投资收到的现金")
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(DECIMAL(20, 4), doc="收回投资收到的现金")
    CASH_RECP_PREM_ORIG_INCO = Column(DECIMAL(20, 4), doc="收到原保险合同保费取得的现金")
    CASH_RECP_RETURN_INVEST = Column(DECIMAL(20, 4), doc="取得投资收益收到的现金")
    CASH_RECP_SG_AND_RS = Column(DECIMAL(20, 4), doc="销售商品、提供劳务收到的现金")
    COMM_INSUR_PLCY_PAID = Column(DECIMAL(20, 4), doc="支付保单红利的现金")
    COMP_TYPE_CODE = Column(String(2), doc="公司类型代码")
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(DECIMAL(20, 4), doc="一年内到期的可转换公司债券")
    CONV_DEBT_INTO_CAP = Column(DECIMAL(20, 4), doc="债务转为资本")
    CREDIT_IMPAIRMENT_LOSS = Column(DECIMAL(20, 4), doc="信用减值损失")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    DECR_DEFERRED_EXP = Column(DECIMAL(20, 4), doc="待摊费用减少")
    DECR_DEFERRED_INC_TAX_ASSETS = Column(DECIMAL(20, 4), doc="递延所得税资产减少")
    DECR_INVENTORIES = Column(DECIMAL(20, 4), doc="存货的减少")
    DECR_OPER_PAYABLE = Column(DECIMAL(20, 4), doc="经营性应收项目的减少")
    DEPR_FA_COGA_DPBA = Column(DECIMAL(20, 4), doc="固定资产折旧、油气资产折耗、生产性生物资产折旧")
    EFF_FX_FLU_CASH = Column(DECIMAL(20, 4), doc="汇率变动对现金的影响")
    END_BAL_CASH = Column(DECIMAL(20, 4), doc="现金的期末余额")
    FA_FNC_LEASES = Column(DECIMAL(20, 4), doc="融资租入固定资产")
    FIN_EXP = Column(DECIMAL(20, 4), doc="财务费用")
    FREE_CASH_FLOW = Column(DECIMAL(20, 4), doc="企业自由现金流量(FCFF)")
    HANDLING_CHRG_PAID = Column(DECIMAL(20, 4), doc="支付手续费的现金")
    IM_NET_CASH_FLOWS_OPER_ACT = Column(DECIMAL(20, 4), doc="间接法-经营活动产生的现金流量净额")
    IM_NET_INCR_CASH_CASH_EQU = Column(DECIMAL(20, 4), doc="间接法-现金及现金等价物净增加额")
    INCL_CASH_REC_SAIMS = Column(DECIMAL(20, 4), doc="其中:子公司吸收少数股东投资收到的现金")
    INCL_DVD_PROFIT_PAID_SC_MS = Column(DECIMAL(20, 4), doc="其中:子公司支付给少数股东的股利、利润")
    INCR_ACC_EXP = Column(DECIMAL(20, 4), doc="预提费用增加")
    INCR_DEFERRED_INC_TAX_LIAB = Column(DECIMAL(20, 4), doc="递延所得税负债增加")
    INCR_OPER_PAYABLE = Column(DECIMAL(20, 4), doc="经营性应付项目的增加")
    INVEST_LOSS = Column(DECIMAL(20, 4), doc="投资损失")
    IS_CALCULATION = Column(DECIMAL(5, 0), doc="是否计算报表")
    LESS_BEG_BAL_CASH = Column(DECIMAL(20, 4), doc="减:现金的期初余额")
    LESS_BEG_BAL_CASH_EQU = Column(DECIMAL(20, 4), doc="减:现金等价物的期初余额")
    LOSS_DISP_FIOLTA = Column(DECIMAL(20, 4), doc="处置固定、无形资产和其他长期资产的损失")
    LOSS_FV_CHG = Column(DECIMAL(20, 4), doc="公允价值变动损失")
    LOSS_SCR_FA = Column(DECIMAL(20, 4), doc="固定资产报废损失")
    NET_CASH_FLOWS_FNC_ACT = Column(DECIMAL(20, 4), doc="筹资活动产生的现金流量净额")
    NET_CASH_FLOWS_INV_ACT = Column(DECIMAL(20, 4), doc="投资活动产生的现金流量净额")
    NET_CASH_FLOWS_OPER_ACT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额")
    NET_CASH_PAY_AQUIS_SOBU = Column(DECIMAL(20, 4), doc="取得子公司及其他营业单位支付的现金净额")
    NET_CASH_RECEIVED_REINSU_BUS = Column(DECIMAL(20, 4), doc="收到再保业务现金净额")
    NET_CASH_RECP_DISP_FIOLTA = Column(DECIMAL(20, 4), doc="处置固定资产、无形资产和其他长期资产收回的现金净额")
    NET_CASH_RECP_DISP_SOBU = Column(DECIMAL(20, 4), doc="处置子公司及其他营业单位收到的现金净额")
    NET_INCR_CASH_CASH_EQU = Column(DECIMAL(20, 4), doc="现金及现金等价物净增加额")
    NET_INCR_CLIENTS_LOAN_ADV = Column(DECIMAL(20, 4), doc="客户贷款及垫款净增加额")
    NET_INCR_DEP_CBOB = Column(DECIMAL(20, 4), doc="存放央行和同业款项净增加额")
    NET_INCR_DEP_COB = Column(DECIMAL(20, 4), doc="客户存款和同业存放款项净增加额")
    NET_INCR_DISP_FAAS = Column(DECIMAL(20, 4), doc="处置可供出售金融资产净增加额")
    NET_INCR_DISP_TFA = Column(DECIMAL(20, 4), doc="处置交易性金融资产净增加额")
    NET_INCR_FUND_BORR_OFI = Column(DECIMAL(20, 4), doc="向其他金融机构拆入资金净增加额")
    NET_INCR_INSURED_DEP = Column(DECIMAL(20, 4), doc="保户储金净增加额")
    NET_INCR_INT_HANDLING_CHRG = Column(DECIMAL(20, 4), doc="收取利息和手续费净增加额")
    NET_INCR_LOANS_CENTRAL_BANK = Column(DECIMAL(20, 4), doc="向中央银行借款净增加额")
    NET_INCR_LOANS_OTHER_BANK = Column(DECIMAL(20, 4), doc="拆入资金净增加额")
    NET_INCR_PLEDGE_LOAN = Column(DECIMAL(20, 4), doc="质押贷款净增加额")
    NET_INCR_REPURCH_BUS_FUND = Column(DECIMAL(20, 4), doc="回购业务资金净增加额")
    NET_PROFIT = Column(DECIMAL(20, 4), doc="净利润")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(DECIMAL(20, 4), doc="支付其他与筹资活动有关的现金")
    OTHER_CASH_PAY_RAL_INV_ACT = Column(DECIMAL(20, 4), doc="支付其他与投资活动有关的现金")
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(DECIMAL(20, 4), doc="支付其他与经营活动有关的现金")
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(DECIMAL(20, 4), doc="收到其他与筹资活动有关的现金")
    OTHER_CASH_RECP_RAL_INV_ACT = Column(DECIMAL(20, 4), doc="收到其他与投资活动有关的现金")
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(DECIMAL(20, 4), doc="收到其他与经营活动有关的现金")
    OTHER_IMPAIR_LOSS_ASSETS = Column(DECIMAL(20, 4), doc="其他资产减值损失")
    OTHERS = Column(DECIMAL(20, 4), doc="其他")
    PAY_ALL_TYP_TAX = Column(DECIMAL(20, 4), doc="支付的各项税费")
    PLUS_END_BAL_CASH_EQU = Column(DECIMAL(20, 4), doc="加:现金等价物的期末余额")
    PLUS_PROV_DEPR_ASSETS = Column(DECIMAL(20, 4), doc="加:资产减值准备")
    PROC_ISSUE_BONDS = Column(DECIMAL(20, 4), doc="发行债券收到的现金")
    RECP_TAX_RENDS = Column(DECIMAL(20, 4), doc="收到的税费返还")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    RIGHT_USE_ASSETS_DEP = Column(DECIMAL(20, 4), doc="使用权资产折旧")
    S_DISMANTLE_CAPITAL_ADD_NET = Column(DECIMAL(20, 4), doc="拆出资金净增加额")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SECURITIE_NETCASH_RECEIVED = Column(DECIMAL(20, 4), doc="代理买卖证券收到的现金净额(元)")
    SPE_BAL_CASH_INFLOWS_FNC = Column(DECIMAL(20, 4), doc="筹资活动现金流入差额(特殊报表科目)")
    SPE_BAL_CASH_INFLOWS_INV = Column(DECIMAL(20, 4), doc="投资活动现金流入差额(特殊报表科目)")
    SPE_BAL_CASH_INFLOWS_OPER = Column(DECIMAL(20, 4), doc="经营活动现金流入差额(特殊报表科目)")
    SPE_BAL_CASH_OUTFLOWS_FNC = Column(DECIMAL(20, 4), doc="筹资活动现金流出差额(特殊报表科目)")
    SPE_BAL_CASH_OUTFLOWS_INV = Column(DECIMAL(20, 4), doc="投资活动现金流出差额(特殊报表科目)")
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(DECIMAL(20, 4), doc="经营活动现金流出差额(特殊报表科目)")
    SPE_BAL_NETCASH_EQU_UNDIR = Column(DECIMAL(20, 4), doc="间接法-经营活动现金流量净额差额(特殊报表科目)")
    SPE_BAL_NETCASH_INC = Column(DECIMAL(20, 4), doc="现金净增加额差额(特殊报表科目)")
    SPE_BAL_NETCASH_INC_UNDIR = Column(DECIMAL(20, 4), doc="间接法-现金净增加额差额(特殊报表科目)")
    STATEMENT_TYPE = Column(String(10), doc="报表类型")
    STOT_CASH_INFLOWS_FNC_ACT = Column(DECIMAL(20, 4), doc="筹资活动现金流入小计")
    STOT_CASH_INFLOWS_INV_ACT = Column(DECIMAL(20, 4), doc="投资活动现金流入小计")
    STOT_CASH_INFLOWS_OPER_ACT = Column(DECIMAL(20, 4), doc="经营活动现金流入小计")
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(DECIMAL(20, 4), doc="筹资活动现金流出小计")
    STOT_CASH_OUTFLOWS_INV_ACT = Column(DECIMAL(20, 4), doc="投资活动现金流出小计")
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(DECIMAL(20, 4), doc="经营活动现金流出小计")
    TOT_BAL_CASH_INFLOWS_FNC = Column(DECIMAL(20, 4), doc="筹资活动现金流入差额(合计平衡项目)")
    TOT_BAL_CASH_INFLOWS_INV = Column(DECIMAL(20, 4), doc="投资活动现金流入差额(合计平衡项目)")
    TOT_BAL_CASH_INFLOWS_OPER = Column(DECIMAL(20, 4), doc="经营活动现金流入差额(合计平衡项目)")
    TOT_BAL_CASH_OUTFLOWS_FNC = Column(DECIMAL(20, 4), doc="筹资活动现金流出差额(合计平衡项目)")
    TOT_BAL_CASH_OUTFLOWS_INV = Column(DECIMAL(20, 4), doc="投资活动现金流出差额(合计平衡项目)")
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(DECIMAL(20, 4), doc="经营活动现金流出差额(合计平衡项目)")
    TOT_BAL_NETCASH_EQU_UNDIR = Column(DECIMAL(20, 4), doc="间接法-经营活动现金流量净额差额(合计平衡项目)")
    TOT_BAL_NETCASH_INC = Column(DECIMAL(20, 4), doc="现金净增加额差额(合计平衡项目)")
    TOT_BAL_NETCASH_INC_UNDIR = Column(DECIMAL(20, 4), doc="间接法-现金净增加额差额(合计平衡项目)")
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(DECIMAL(20, 4), doc="筹资活动产生的现金流量净额差额(合计平衡项目)")
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(DECIMAL(20, 4), doc="投资活动产生的现金流量净额差额(合计平衡项目)")
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额差额(合计平衡项目)")
    UNCONFIRMED_INVEST_LOSS = Column(DECIMAL(20, 4), doc="未确认投资损失")
    WIND_CODE = Column(String(40), doc="Wind代码")


class ASHARECIRCULATINGHOLDERS(Base):

    __tablename__ = 'ASHARECIRCULATINGHOLDERS'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_ENDDATE = Column(String(10), doc="报告期")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="持股比例")
    S_INFO_COMP_NAME = Column(String(100), doc="股东公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="股东公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="股东公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHARECOCAPITALOPERATION(Base):

    __tablename__ = 'ASHARECOCAPITALOPERATION'

    ANN_DATE = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_EVENT_CATEGORYCODE = Column(DECIMAL(9, 0), doc="事件类型代码")
    S_EVENT_DESCRIPTION = Column(String(1000), doc="事件说明")
    S_EVENT_ID = Column(String(40), doc="事件ID")
    S_FINANCING_AMOUNT = Column(DECIMAL(20, 4), doc="融资金额(人民币)")
    S_FINANCING_AMOUNT_US = Column(DECIMAL(20, 4), doc="融资金额(美元)")
    S_FINANCING_PROCESS = Column(DECIMAL(9, 0), doc="融资进程")
    S_FINANCING_RATE = Column(DECIMAL(20, 4), doc="融资费率")
    S_FINANCING_RT = Column(DECIMAL(20, 4), doc="融资利率")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_PB = Column(DECIMAL(20, 4), doc="市净率(PB)")
    S_PE = Column(DECIMAL(20, 4), doc="市盈率(PE)")
    S_PS = Column(DECIMAL(20, 4), doc="市销率(PS)")
    S_VALUATION_AMOUNT = Column(DECIMAL(20, 4), doc="估值金额(人民币)")
    S_VALUATION_AMOUNT_US = Column(DECIMAL(20, 4), doc="估值金额(美元)")


class ASHARECOMPANYHOLDSHARES(Base):

    __tablename__ = 'ASHARECOMPANYHOLDSHARES'

    ANN_DT = Column(String(8))
    CAPITALCRNCY_CODE = Column(String(10))
    ENDDATE = Column(String(8))
    IS_CONSOLIDATE = Column(DECIMAL(5, 4))
    NOTCONSOLIDATE_REASON = Column(String(500))
    OBJECT_ID = Column(String(100), primary_key=True)
    OPDATE = Column(DateTime)
    OPERATIONCRNCY_CODE = Column(String(10))
    OPMODE = Column(String(1))
    RELATIONS_CODE = Column(String(40))
    S_CAPITALOPERATION_AMOUNT = Column(DECIMAL(20, 4))
    S_CAPITALOPERATION_COMAINBUS = Column(String(100))
    S_CAPITALOPERATION_COMPANYID = Column(String(10))
    S_CAPITALOPERATION_COMPANYNAME = Column(String(100))
    S_CAPITALOPERATION_COREGCAP = Column(DECIMAL(20, 4))
    S_CAPITALOPERATION_PCT = Column(DECIMAL(20, 4))
    S_INFO_WINDCODE = Column(String(40))
    VOTING_RIGHTS = Column(DECIMAL(20, 4))


class ASHARECONCEPTUALPLATE(Base):

    __tablename__ = 'ASHARECONCEPTUALPLATE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMP_NAME = Column(String(100), doc="公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHARECREDITORRIGHTS(Base):

    __tablename__ = 'ASHARECREDITORRIGHTS'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="债务公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="债务公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="债务公司公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHARECUSTOMER(Base):

    __tablename__ = 'ASHARECUSTOMER'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="下游公司名称")
    S_INFO_COMP_SNAME = Column(String(100))
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="下游公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_DISCLOSER = Column(String(100), doc="披露公司ID")


class ASHAREDEFENDANT(Base):

    __tablename__ = 'ASHAREDEFENDANT'

    ANN_DATE = Column(String(8), doc="公告日期")
    LITIGATION_EVENTS_ID = Column(String(40), doc="诉讼事件ID")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CASE_TYPE = Column(String(10), doc="案件类型")
    S_INFO_COMP_NAME = Column(String(100), doc="诉讼公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="诉讼公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="诉讼公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREDESCRIPTION(Base):

    __tablename__ = 'ASHAREDESCRIPTION'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    IS_SHSC = Column(DECIMAL(5, 0), doc="是否在沪股通或深港通范围内")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CODE = Column(String(40), doc="交易代码")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPNAME = Column(String(100), doc="公司中文名称")
    S_INFO_COMPNAMEENG = Column(String(100), doc="公司英文名称")
    S_INFO_DELISTDATE = Column(String(8), doc="退市日期")
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所")
    S_INFO_ISINCODE = Column(String(40), doc="ISIN代码")
    S_INFO_LISTBOARD = Column(String(10), doc="上市板类型")
    S_INFO_LISTBOARDNAME = Column(String(10), doc="上市板")
    S_INFO_LISTDATE = Column(String(8), doc="上市日期")
    S_INFO_NAME = Column(String(50), doc="证券简称")
    S_INFO_PINYIN = Column(String(40), doc="简称拼音")
    S_INFO_SEDOLCODE = Column(String(40))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREDIRECTOR(Base):

    __tablename__ = 'ASHAREDIRECTOR'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_MANAGER_NAME = Column(String(80), doc="姓名")
    S_INFO_MANAGER_POST = Column(String(40), doc="职务")
    S_INFO_MANAGER_STARTDATE = Column(String(8), doc="任职日期")
    S_INFO_MANID = Column(String(10), doc="人物id")


class ASHAREDIVIDEND(Base):

    __tablename__ = 'ASHAREDIVIDEND'

    ANN_DT = Column(String(8), doc="最新公告日期")
    CASH_DVD_PER_SH_AFTER_TAX = Column(DECIMAL(24, 8), doc="每股派息(税后)(元)")
    CASH_DVD_PER_SH_PRE_TAX = Column(DECIMAL(24, 8), doc="每股派息(税前)(元)")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    DVD_ANN_DT = Column(String(8), doc="分红实施公告日")
    DVD_PAYOUT_DT = Column(String(8), doc="派息日")
    EQY_RECORD_DT = Column(String(8), doc="股权登记日")
    EX_DT = Column(String(8), doc="除权除息日")
    IS_CHANGED = Column(DECIMAL(5, 0), doc="方案是否变更")
    IS_TRANSFER = Column(DECIMAL(1, 0), doc="是否不分转")
    LISTING_DT_OF_DVD_SHR = Column(String(8), doc="红股上市日")
    MEMO = Column(String(200), doc="备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="分红年度")
    S_DIV_BASEDATE = Column(String(8), doc="基准日期")
    S_DIV_BASESHARE = Column(DECIMAL(20, 4), doc="基准股本(万股)")
    S_DIV_BONUSRATE = Column(DECIMAL(20, 8), doc="每股送股比例")
    S_DIV_CHANGE = Column(String(500), doc="方案变更说明")
    S_DIV_CONVERSEDRATE = Column(DECIMAL(20, 8), doc="每股转增比例")
    S_DIV_OBJECT = Column(String(100), doc="分红对象")
    S_DIV_PREANNDT = Column(String(8), doc="预案预披露公告日")
    S_DIV_PRELANDATE = Column(String(8), doc="预案公告日")
    S_DIV_PROGRESS = Column(String(10), doc="方案进度")
    S_DIV_SMTGDATE = Column(String(8), doc="股东大会公告日")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    STK_DVD_PER_SH = Column(DECIMAL(20, 8), doc="每股送转")
    WIND_CODE = Column(String(40), doc="Wind代码")


class ASHAREEARNINGEST(Base):

    __tablename__ = 'ASHAREEARNINGEST'

    ANALYST_ID = Column(String(200), doc="分析师id")
    ANALYST_NAME = Column(String(20), doc="分析师名称")
    ANN_DT = Column(String(8), doc="公告日期(内部)")
    COLLECT_TIME = Column(DateTime, doc="收录时间")
    EST_BASE_CAP = Column(DECIMAL(20, 4), doc="预测基准股本(万股)")
    EST_BASE_CAP_DIF_CODE = Column(DECIMAL(9, 0), doc="预测基准股本差异原因代码")
    EST_DT = Column(String(8), doc="预测日期")
    EST_EBIT = Column(DECIMAL(20, 4), doc="预测息税前利润(万元)")
    EST_EBITDA = Column(DECIMAL(20, 4), doc="预测息税折旧摊销前利润(万元)")
    EST_EPS_DILUTED = Column(DECIMAL(20, 4), doc="预测每股收益(摊薄)(元)")
    EST_MAIN_BUS_INC = Column(DECIMAL(20, 4), doc="预测主营业务收入(万元)")
    EST_NET_PROFIT = Column(DECIMAL(20, 4), doc="预测净利润(万元)")
    FIRST_OPTIME = Column(DateTime, doc="首次入库时间")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_NAME = Column(String(1024), doc="报告标题")
    REPORT_SUMMARY = Column(LONGTEXT, doc="报告摘要")
    REPORT_TYPECODE = Column(DECIMAL(9, 0), doc="报告类型")
    REPORTING_PERIOD = Column(String(8), doc="预测报告期")
    RESEARCH_INST_NAME = Column(String(20), doc="研究机构名称")
    S_EST_BPS = Column(DECIMAL(20, 4), doc="预测每股净资产")
    S_EST_CPS = Column(DECIMAL(20, 4), doc="预测每股现金流")
    S_EST_DIVIDENDYIELD = Column(DECIMAL(20, 4), doc="预测股息率")
    S_EST_DPS = Column(DECIMAL(20, 4), doc="预测每股股利")
    S_EST_EBT = Column(DECIMAL(20, 4), doc="预测利润总额（万元）")
    S_EST_ENDDATE = Column(String(8), doc="预测有效截止")
    S_EST_EPSBASIC = Column(DECIMAL(20, 4), doc="预测每股收益(基本)(元)")
    S_EST_EPSCAL = Column(DECIMAL(20, 4), doc="预测每股收益（换算）")
    S_EST_EPSDILUTED = Column(DECIMAL(20, 4), doc="预测每股收益(稀释)(元)")
    S_EST_EPSRATE = Column(DECIMAL(20, 4), doc="预测EPS调整比率")
    S_EST_EVEBITDA = Column(DECIMAL(20, 4), doc="预测EV/EBITDA")
    S_EST_NPCAL = Column(DECIMAL(20, 4), doc="预测净利润（换算）（万元）")
    S_EST_NPRATE = Column(DECIMAL(20, 4), doc="预测净利润调整比率")
    S_EST_OC = Column(DECIMAL(20, 4), doc="预测营业成本及附加（万元）")
    S_EST_OPE = Column(DECIMAL(10, 4), doc="预测主营业务利润率")
    S_EST_OPROFIT = Column(DECIMAL(20, 4), doc="预测营业利润(万元）")
    S_EST_PB = Column(DECIMAL(20, 4), doc="预测市净率")
    S_EST_PE = Column(DECIMAL(20, 4), doc="预测市盈率")
    S_EST_ROA = Column(DECIMAL(20, 4), doc="预测总资产收益率")
    S_EST_ROE = Column(DECIMAL(20, 4), doc="预测净资产收益率")
    S_EST_VALUE_CALCULATION = Column(DECIMAL(5, 0), doc="综合值计算标记")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    WIND_CODE = Column(String(40), doc="Wind代码")


class ASHAREEODPRICES(Base):

    __tablename__ = 'ASHAREEODPRICES'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_ADJCLOSE = Column(DECIMAL(20, 4), doc="复权收盘价(元)")
    S_DQ_ADJFACTOR = Column(DECIMAL(20, 6), doc="复权因子")
    S_DQ_ADJHIGH = Column(DECIMAL(20, 4), doc="复权最高价(元)")
    S_DQ_ADJLOW = Column(DECIMAL(20, 4), doc="复权最低价(元)")
    S_DQ_ADJOPEN = Column(DECIMAL(20, 4), doc="复权开盘价(元)")
    S_DQ_ADJPRECLOSE = Column(DECIMAL(20, 4), doc="复权昨收盘价(元)")
    S_DQ_AMOUNT = Column(DECIMAL(20, 4), doc="成交金额(千元)")
    S_DQ_AVGPRICE = Column(DECIMAL(20, 4), doc="均价(VWAP)")
    S_DQ_CHANGE = Column(DECIMAL(20, 4), doc="涨跌(元)")
    S_DQ_CLOSE = Column(DECIMAL(20, 4), doc="收盘价(元)")
    S_DQ_HIGH = Column(DECIMAL(20, 4), doc="最高价(元)")
    S_DQ_LIMIT = Column(DECIMAL(20, 4), doc="涨停价(元)")
    S_DQ_LOW = Column(DECIMAL(20, 4), doc="最低价(元)")
    S_DQ_OPEN = Column(DECIMAL(20, 4), doc="开盘价(元)")
    S_DQ_PCTCHANGE = Column(DECIMAL(20, 4), doc="涨跌幅(%)")
    S_DQ_PRECLOSE = Column(DECIMAL(20, 4), doc="昨收盘价(元)")
    S_DQ_STOPPING = Column(DECIMAL(20, 4), doc="跌停价(元)")
    S_DQ_TRADESTATUS = Column(String(10), doc="交易状态")
    S_DQ_TRADESTATUSCODE = Column(DECIMAL(5, 0), doc="交易状态代码")
    S_DQ_VOLUME = Column(DECIMAL(20, 4), doc="成交量(手)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")


class ASHAREEQUFROINFO(Base):

    __tablename__ = 'ASHAREEQUFROINFO'

    ANN_DATE = Column(String(8), doc="公告日期")
    DISFROZEN_TIME = Column(String(8), doc="解冻日期")
    FROZEN_INSTITUTION = Column(String(100), doc="执行冻结机构")
    IS_DISFROZEN = Column(DECIMAL(1, 0), doc="是否解冻")
    IS_TURN_FROZEN = Column(DECIMAL(1, 0), doc="是否轮候冻结")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_FRO_BGDATE = Column(String(8), doc="冻结起始时间")
    S_FRO_ENDDATE = Column(String(8), doc="冻结结束时间")
    S_FRO_SHARES = Column(DECIMAL(20, 4), doc="冻结数量(万股)")
    S_FRO_SHR_RATIO = Column(DECIMAL(20, 4), doc="本次冻结股数占公司总股本比例")
    S_HOLDER_ID = Column(String(10), doc="股东ID")
    S_HOLDER_NAME = Column(String(100), doc="股东名称")
    S_HOLDER_TYPE_CODE = Column(DECIMAL(9, 0), doc="股东类型代码")
    S_INFO_COMPCODE = Column(String(10), doc="公司id")
    S_TOTAL_HOLDING_SHR = Column(DECIMAL(20, 4), doc="持股总数（万股）")
    S_TOTAL_HOLDING_SHR_RATIO = Column(DECIMAL(20, 4), doc="持股总数占公司总股本比例")
    SHR_CATEGORY_CODE = Column(DECIMAL(9, 0), doc="股份性质类别代码")


class ASHAREEQUITYPLEDGEINFO(Base):

    __tablename__ = 'ASHAREEQUITYPLEDGEINFO'

    ANN_DT = Column(String(8), doc="公告日期")
    IS_DISCHARGE = Column(DECIMAL(1, 0), doc="是否解押")
    IS_EQUITY_PLEDGE_REPO = Column(DECIMAL(1, 0), doc="是否股权质押回购")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DISCHARGE_DATE = Column(String(8), doc="解押日期")
    S_HOLDER_ID = Column(String(10), doc="股东ID")
    S_HOLDER_NAME = Column(String(200), doc="股东名称")
    S_HOLDER_TYPE_CODE = Column(DECIMAL(9, 0), doc="股东类型代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PLEDGE_BGDATE = Column(String(8), doc="质押起始时间")
    S_PLEDGE_ENDDATE = Column(String(8), doc="质押结束时间")
    S_PLEDGE_SHARES = Column(DECIMAL(20, 4), doc="质押数量(万股)")
    S_PLEDGE_SHR_RATIO = Column(DECIMAL(20, 4), doc="本次质押股数占公司总股本比例")
    S_PLEDGOR = Column(String(200), doc="质押方")
    S_PLEDGOR_ID = Column(String(10), doc="质押方ID")
    S_PLEDGOR_TYPE_CODE = Column(DECIMAL(9, 0), doc="质押方类型代码")
    S_REMARK = Column(String(1000), doc="备注")
    S_SHR_CATEGORY_CODE = Column(DECIMAL(9, 0), doc="股份性质类别代码")
    S_TOTAL_HOLDING_SHR = Column(DECIMAL(20, 4), doc="持股总数")
    S_TOTAL_HOLDING_SHR_RATIO = Column(DECIMAL(20, 4), doc="持股总数占公司总股本比例")
    S_TOTAL_PLEDGE_SHR = Column(DECIMAL(20, 4), doc="累计质押股数")


class ASHAREEQUITYRELATIONSHIPS(Base):

    __tablename__ = 'ASHAREEQUITYRELATIONSHIPS'

    ACTUALCONTROLLER_INTRO = Column(String(1000), doc="实际控制人简介")
    ACTUALCONTROLLER_IS_ANN = Column(DECIMAL(5, 0), doc="股东是否为公布实际控制人")
    ACTUALCONTROLLER_TYPE = Column(String(80), doc="实际控制人类型")
    ANN_DT = Column(String(8), doc="公告日期")
    ENDDATE = Column(String(8), doc="截止日期")
    IS_ACTUALCONTROLLER = Column(DECIMAL(5, 0), doc="股东是否为实际控制人")
    IS_CONTROLLING_SHAREHOLDERS = Column(DECIMAL(1, 0), doc="股东是否为公布控股股东")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RELATION_TYPE = Column(String(40), doc="公司与披露方关系")
    S_HOLDER_CODE = Column(String(10), doc="股东ID")
    S_HOLDER_NAME = Column(String(200), doc="股东名称")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="持股比例(%)")
    S_HOLDER_TYPE = Column(DECIMAL(5, 0), doc="股东类型")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_COMPNAME = Column(String(200), doc="公司名称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREESOPDESCRIPTION(Base):

    __tablename__ = 'ASHAREESOPDESCRIPTION'

    ACT_CAP_RATIO = Column(DECIMAL(20, 4), doc="实际占公司总股本比例")
    ACT_FUNDSIZE = Column(DECIMAL(20, 4), doc="实际资金规模")
    ACT_SHARESNO = Column(DECIMAL(20, 4), doc="实际股票数量")
    ACT_SHARESPRICE = Column(DECIMAL(20, 4), doc="实际股票价格")
    ANN_DATE_IMPLEMENTATION = Column(String(8), doc="实施公告日")
    ANN_DATE_NEW = Column(String(8), doc="最新公告日")
    BM_PREPRO_ANN_DT = Column(String(8), doc="董事会预案公告日")
    CAPITAL_RESOURCE_CODE = Column(DECIMAL(9, 0), doc="资金来源代码")
    CORR_PRONAME = Column(String(100), doc="持股计划对应产品名称")
    DURATION = Column(DECIMAL(20, 0), doc="存续期(月)")
    EMPL_SUBS_AMT = Column(DECIMAL(20, 4), doc="员工认购金额(万)")
    EMPL_SUBS_PROPORTION = Column(DECIMAL(20, 4), doc="员工认购比例(%)")
    ESTIMATED_PRICE = Column(DECIMAL(20, 4), doc="标的股票预估价格")
    ESTIMATED_VOLUMN = Column(DECIMAL(20, 4), doc="预计股票数量(万)")
    EVENT_ID = Column(String(40), doc="事件ID")
    INITIAL_CAPITAL = Column(DECIMAL(20, 4), doc="初始资金规模（万元）")
    INITIAL_LEVERAGE = Column(DECIMAL(20, 4), doc="初始杠杆")
    IS_SELF_MANAGE = Column(DECIMAL(1, 0), doc="是否自行管理")
    LOCK_START_DATE = Column(String(8), doc="锁定起始日")
    LOCKUP_PERIOD_M = Column(DECIMAL(20, 0), doc="锁定期限")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PROGRESS_CODE = Column(DECIMAL(9, 0), doc="方案进度代码")
    RATIO_OWNFUNDS = Column(DECIMAL(20, 4), doc="员工自有资金占比")
    RATIO_TO_TOTALSHARES = Column(DECIMAL(20, 4), doc="预计占公司总股本比例(%)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SENMNGR_SUBS_AMT = Column(DECIMAL(20, 4), doc="高管认购金额(万元)")
    SENMNGR_SUBS_NO = Column(DECIMAL(20, 0), doc="高管认购人数")
    SENMNGR_SUBS_PROPORTION = Column(DECIMAL(20, 4), doc="高管认购比例（%）")
    SHAREHOLD_FINDT = Column(String(8), doc="持股完成日")
    SHARES_RESOURCE_CODE = Column(DECIMAL(9, 0), doc="股票来源代码")
    SHOLDER_MEETING_ANN_DT = Column(String(8), doc="股东大会公告日")
    SHOLDERS_LOAN = Column(DECIMAL(20, 4), doc="股东借款金额")
    SHOLDERS_LOANRATIO = Column(DECIMAL(20, 4), doc="股东借款比例")
    SHOLDERS_NO = Column(DECIMAL(20, 0), doc="持有人数")
    SHOLDERS_PROPORTION = Column(DECIMAL(20, 4), doc="持有人占公司员工比例")


class ASHAREESOPTRADINGINFO(Base):

    __tablename__ = 'ASHAREESOPTRADINGINFO'

    ANN_DT = Column(String(8), doc="公告日期")
    END_DT = Column(String(8), doc="截止日期")
    ESOP_WINDCODE = Column(String(40), doc="员工持股计划证券ID")
    EVENT_ID = Column(String(40), doc="事件ID")
    LOCKUP_PERIOD = Column(DECIMAL(20, 0), doc="锁定期限")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RATIO_TO_TOTALSHARES = Column(DECIMAL(20, 4), doc="占公司总股本比例")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_AVG_PRICE = Column(DECIMAL(20, 4), doc="成交均价")
    TRADING_VOLUME = Column(DECIMAL(20, 4), doc="成交数量")


class ASHAREFINANCIALDERIVATIVE(Base):

    __tablename__ = 'ASHAREFINANCIALDERIVATIVE'

    ADMINEXPENSETOGR = Column(DECIMAL(20, 4), doc="行政(管理)费用／营业总收入(%)")
    ARTURN = Column(DECIMAL(20, 4), doc="应收账款周转率(次)")
    ARTURNDAYS = Column(DECIMAL(20, 4), doc="应收账款周转天数(天)")
    ASSETSTOEQUITY = Column(DECIMAL(20, 4), doc="权益乘数")
    ASSETSTURN = Column(DECIMAL(20, 4), doc="总资产周转率(次)")
    BEGINDATE = Column(String(8), doc="起始日期")
    BPS = Column(DECIMAL(20, 4), doc="每股净资产(元)")
    CAPITALIZEDTODA = Column(DECIMAL(20, 4), doc="资本支出／折旧和摊销")
    CASHRATIO = Column(DECIMAL(20, 4), doc="保守速动比率")
    CASHTOLIQDEBT = Column(DECIMAL(20, 4), doc="货币资金／流动负债")
    CASHTOLIQDEBTWITHINTEREST = Column(DECIMAL(20, 4), doc="货币资金／带息流动负债")
    CATOASSETS = Column(DECIMAL(20, 4), doc="流动资产／总资产(%)")
    CATURN = Column(DECIMAL(20, 4), doc="流动资产周转率(次)")
    CFPS = Column(DECIMAL(20, 4), doc="每股现金流量净额(元)")
    COGSTOSALES = Column(DECIMAL(20, 4), doc="销售成本率(%)")
    CONTINUED_NET_PROFIT = Column(DECIMAL(20, 4), doc="持续经营净利润／除税后利润(%)")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    CURRENT1 = Column(DECIMAL(20, 4), doc="流动比率")
    CURRENTDEBTTODEBT = Column(DECIMAL(20, 4), doc="流动负债／负债合计(%)")
    DEBTTOASSETS = Column(DECIMAL(20, 4), doc="资产负债率(%)")
    DEBTTOEQUITY = Column(DECIMAL(20, 4), doc="产权比率")
    DUPONT_ASSETSTOEQUITY = Column(DECIMAL(20, 4), doc="权益乘数(用于杜邦分析)")
    EBIT = Column(DECIMAL(20, 4), doc="息税前利润(元)")
    EBITDA = Column(DECIMAL(20, 4), doc="息税折旧摊销前利润(元)")
    EBITDATODEBT = Column(DECIMAL(20, 4), doc="息税折旧摊销前利润／负债合计")
    EBITPS = Column(DECIMAL(20, 4), doc="每股息税前利润(元)")
    EBITTOGR = Column(DECIMAL(20, 4), doc="息税前利润／营业总收入(%)")
    EBITTOINTEREST = Column(DECIMAL(20, 4), doc="已获利息倍数(EBIT／利息费用)")
    ENDDATE = Column(String(8), doc="截止日期")
    EPS_BASIC = Column(DECIMAL(20, 4), doc="基本每股收益(元)")
    EPS_DILUTED = Column(DECIMAL(20, 4), doc="稀释每股收益(元)")
    EPS_DILUTED2 = Column(DECIMAL(20, 4), doc="每股收益(期末摊薄)(元)")
    EPS_DILUTED3 = Column(DECIMAL(20, 4), doc="每股收益(扣除／期末股本摊薄)(元)")
    EQUITYTODEBT = Column(DECIMAL(20, 4), doc="归属于母公司的股东权益／负债合计")
    EQUITYTOINTERESTDEBT = Column(DECIMAL(20, 4), doc="归属于母公司的股东权益／带息债务")
    EQUITYTOTOTALCAPITAL = Column(DECIMAL(20, 4), doc="归属于母公司的股东权益／全部投入资本(%)")
    EXINTERESTDEBT_CURRENT = Column(DECIMAL(20, 4), doc="无息流动负债(元)")
    EXINTERESTDEBT_NONCURRENT = Column(DECIMAL(20, 4), doc="无息非流动负债(元)")
    FATURN = Column(DECIMAL(20, 4), doc="固定资产周转率(次)")
    FCFE = Column(DECIMAL(20, 4), doc="股权自由现金流量(FCFE)(元)")
    FCFEPS = Column(DECIMAL(20, 4), doc="每股股东自由现金流量(元)")
    FCFF = Column(DECIMAL(20, 4), doc="企业自由现金流量(FCFF)(元)")
    FCFFPS = Column(DECIMAL(20, 4), doc="每股企业自由现金流量(元)")
    FINAEXPENSETOGR = Column(DECIMAL(20, 4), doc="财务费用／营业总收入(%)")
    FISCALYEAR = Column(String(8), doc="会计年度(Wind判定)")
    GCTOGR = Column(DECIMAL(20, 4), doc="营业总成本／营业总收入(%)")
    GROSSPROFITMARGIN = Column(DECIMAL(20, 4), doc="销售毛利率(%)")
    GRPS = Column(DECIMAL(20, 4), doc="每股营业总收入(元)")
    INTDEBTTOTOTALCAP = Column(DECIMAL(20, 4), doc="带息债务／全部投入资本(%)")
    INTERESTDEBT = Column(DECIMAL(20, 4), doc="带息债务(元)")
    INTERVAL_LENGTH = Column(DECIMAL(20, 4), doc="区间长度(月)")
    INVESTCAPITAL = Column(DECIMAL(20, 4), doc="全部投入资本(元)")
    INVESTINCOME = Column(DECIMAL(20, 4), doc="价值变动净收益(元)")
    INVESTINCOMETOEBT = Column(DECIMAL(20, 4), doc="价值变动净收益／除税前利润(%)")
    INVTURN = Column(DECIMAL(20, 4), doc="存货周转率(次)")
    INVTURNDAYS = Column(DECIMAL(20, 4), doc="存货周转天数(天)")
    LONGDEBTODEBT = Column(DECIMAL(20, 4), doc="非流动负债／负债合计(%)")
    LONGDEBTTOWORKINGCAPITAL = Column(DECIMAL(20, 4), doc="长期债务与营运资金比率")
    NCATOASSETS = Column(DECIMAL(20, 4), doc="非流动资产／总资产(%)")
    NET_PROFIT5 = Column(DECIMAL(20, 4), doc="归属母公司的净利润／净利润(%)")
    NET_TOTAL_PROFIT = Column(DECIMAL(20, 4), doc="净利润／利润总额(%)")
    NETDEBT = Column(DECIMAL(20, 4), doc="净债务(元)")
    NETPROFITMARGIN = Column(DECIMAL(20, 4), doc="销售净利率(%)")
    NETWORKINGCAPITAL = Column(DECIMAL(20, 4), doc="营运流动资本(元)")
    NONNETOPTOTAXPROFIT = Column(DECIMAL(20, 4), doc="非持续经营净利润/除税后利润(%)")
    NONOPERATEPROFITTOEBT = Column(DECIMAL(20, 4), doc="营业外收支净额／除税前利润(%)")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OCFPS = Column(DECIMAL(20, 4), doc="每股经营活动产生的现金流量净额(元)")
    OCFTODEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／负债合计")
    OCFTOINTERESTDEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／带息债务")
    OCFTOOR = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／营业收入(%)")
    OCFTOOR1 = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／经营活动净收益")
    OCFTOPROFIT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／营业利润(含)(%)")
    OCFTOSHORTDEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／流动负债")
    OPDATE = Column(DateTime)
    OPERATEINCOME = Column(DECIMAL(20, 4), doc="经营活动净收益(元)")
    OPERATEINCOMETOEBT = Column(DECIMAL(20, 4), doc="经营活动净收益／除税前利润(%)")
    OPMODE = Column(String(1))
    OPPROFIT1 = Column(DECIMAL(20, 4), doc="营业利润(含价值变动损益)(元)")
    OPTODEBT = Column(DECIMAL(20, 4), doc="营业利润／负债合计")
    OPTOGR = Column(DECIMAL(20, 4), doc="营业利润(含价值变动损益)／营业总收入(%)")
    OPTOLIQDEBT = Column(DECIMAL(20, 4), doc="营业利润／流动负债")
    ORPS = Column(DECIMAL(20, 4), doc="每股营业收入(元)")
    PROFITTOGR = Column(DECIMAL(20, 4), doc="净利润／营业总收入(%)")
    PROFITTOOP = Column(DECIMAL(20, 4), doc="利润总额／营业总收入(%)")
    QUICK = Column(DECIMAL(20, 4), doc="速动比率")
    REPORT_TYPE = Column(String(20), doc="报告类型")
    RETAINEDEARNINGS = Column(DECIMAL(20, 4), doc="留存收益(元)")
    RETAINEDPS = Column(DECIMAL(20, 4), doc="每股留存收益(元)")
    ROA = Column(DECIMAL(20, 4), doc="总资产净利润(平均)(%)")
    ROA2 = Column(DECIMAL(20, 4), doc="总资产报酬率(平均)(%)")
    ROA2_YEARLY = Column(DECIMAL(20, 4), doc="年化总资产报酬率(%)")
    ROA_YEARLY = Column(DECIMAL(20, 4), doc="年化总资产净利率(%)")
    ROE = Column(DECIMAL(20, 4), doc="净资产收益率(平均)(%)")
    ROE_DEDUCTED = Column(DECIMAL(20, 4), doc="净资产收益率(扣除平均)(%)")
    ROE_YEARLY = Column(DECIMAL(20, 4), doc="年化净资产收益率(%)")
    ROIC = Column(DECIMAL(20, 4), doc="投入资本回报率(平均)(%)")
    ROIC_YEARLY = Column(DECIMAL(20, 4), doc="年化投入资本回报率")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_STM_IS = Column(DECIMAL(20, 4), doc="折旧与摊销(元)")
    SALEEXPENSETOGR = Column(DECIMAL(20, 4), doc="销售费用／营业总收入(%)")
    STATEMENT_TYPE = Column(String(40), doc="报表类型")
    SURPLUSCAPITALPS = Column(DECIMAL(20, 4), doc="每股资本公积(元)")
    TANGASSETTOINTDEBT = Column(DECIMAL(20, 4), doc="有形资产／带息债务")
    TANGIBLEASSET = Column(DECIMAL(20, 4), doc="有形资产(元)")
    TANGIBLEASSETSTOASSETS = Column(DECIMAL(20, 4), doc="有形资产／总资产(%)")
    TANGIBLEASSETTODEBT = Column(DECIMAL(20, 4), doc="有形资产／负债合计")
    TANGIBLEASSETTONETDEBT1 = Column(DECIMAL(20, 4), doc="有形资产／净债务")
    TANGIBLEASSETTONETDEBT2 = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／净债务")
    TAXTOEBT = Column(DECIMAL(20, 4), doc="所得税／利润总额(%)")
    TOT_SHR = Column(DECIMAL(20, 4), doc="期末总股本(股)")
    TOTAL_PROFIT_EBIT = Column(DECIMAL(20, 4), doc="利润总额／EBIT(%)")
    TURNDAYS = Column(DECIMAL(20, 4), doc="营业周期(天)")
    WORKINGCAPITAL = Column(DECIMAL(20, 4), doc="营运资金(元)")
    YOY_OR = Column(DECIMAL(20, 4), doc="营业收入同比增长率(%)")
    YOY_TR = Column(DECIMAL(20, 4), doc="营业总收入同比增长率(%)")
    YOYASSETS = Column(DECIMAL(20, 4), doc="资产总计同比增长率(%)")
    YOYBPS = Column(DECIMAL(20, 4), doc="每股净资产同比增长率(%)")
    YOYEBT = Column(DECIMAL(20, 4), doc="利润总额同比增长率(%)")
    YOYEPS_BASIC = Column(DECIMAL(20, 4), doc="基本每股收益同比增长率(%)")
    YOYEPS_DILUTED = Column(DECIMAL(20, 4), doc="稀释每股收益同比增长率(%)")
    YOYEQUITY = Column(DECIMAL(20, 4), doc="归属母公司的股东权益同比增长率(%)")
    YOYNETPROFIT = Column(DECIMAL(20, 4), doc="归属母公司股东的净利润同比增长率(%)")
    YOYNETPROFIT_DEDUCTED = Column(DECIMAL(20, 4), doc="归属母公司股东的净利润-扣除非经常损益同比增长率(%)")
    YOYOCF = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额同比增长率(%)")
    YOYOCFPS = Column(DECIMAL(20, 4), doc="每股经营活动产生的现金流量净额同比增长率(%)")
    YOYOP = Column(DECIMAL(20, 4), doc="营业利润同比增长率(含)(%)")
    YOYROE = Column(DECIMAL(20, 4), doc="净资产收益率(平均)?同比增长率(%)")


class ASHAREFINANCIALINDICATOR(Base):

    __tablename__ = 'ASHAREFINANCIALINDICATOR'

    ANN_DT = Column(String(8), doc="公告日期")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RD_EXPENSE = Column(DECIMAL(20, 4), doc="研发费用")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_FA_ADMINEXPENSETOGR = Column(DECIMAL(20, 4), doc="管理费用/营业总收入")
    S_FA_ARTURN = Column(DECIMAL(20, 4), doc="应收账款周转率")
    S_FA_ARTURNDAYS = Column(DECIMAL(20, 4), doc="应收账款周转天数")
    S_FA_ASSETSTOEQUITY = Column(DECIMAL(20, 4), doc="权益乘数")
    S_FA_ASSETSTURN = Column(DECIMAL(20, 4), doc="总资产周转率")
    S_FA_BPS = Column(DECIMAL(20, 4), doc="每股净资产")
    S_FA_CAPITALIZEDTODA = Column(DECIMAL(20, 4), doc="资本支出/折旧和摊销")
    S_FA_CASHRATIO = Column(DECIMAL(20, 4), doc="保守速动比率")
    S_FA_CASHTOLIQDEBT = Column(DECIMAL(20, 4), doc="货币资金／流动负债")
    S_FA_CASHTOLIQDEBTWITHINTEREST = Column(DECIMAL(20, 4), doc="货币资金／带息流动负债")
    S_FA_CATOASSETS = Column(DECIMAL(20, 4), doc="流动资产/总资产")
    S_FA_CATURN = Column(DECIMAL(20, 4), doc="流动资产周转率")
    S_FA_CFPS = Column(DECIMAL(20, 4), doc="每股现金流量净额")
    S_FA_COGSTOSALES = Column(DECIMAL(20, 4), doc="销售成本率")
    S_FA_CURRENT = Column(DECIMAL(20, 4), doc="流动比率")
    S_FA_CURRENTDEBTTODEBT = Column(DECIMAL(20, 4), doc="流动负债/负债合计")
    S_FA_DEBTTOASSETS = Column(DECIMAL(20, 4), doc="资产负债率")
    S_FA_DEBTTOEQUITY = Column(DECIMAL(20, 4), doc="产权比率")
    S_FA_DEDUCTEDPROFIT = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的净利润(扣除少数股东损益)")
    S_FA_DEDUCTEDPROFITTOPROFIT = Column(DECIMAL(20, 4), doc="扣除非经常损益后的净利润/净利润")
    S_FA_DUPONT_ASSETSTOEQUITY = Column(DECIMAL(20, 4), doc="权益乘数(用于杜邦分析)")
    S_FA_DUPONT_ROA = Column(DECIMAL(20, 4), doc="总资产净利率(杜邦分析)")
    S_FA_EBIT = Column(DECIMAL(20, 4), doc="息税前利润")
    S_FA_EBITDA = Column(DECIMAL(20, 4), doc="息税折旧摊销前利润")
    S_FA_EBITDATODEBT = Column(DECIMAL(20, 4), doc="息税折旧摊销前利润/负债合计")
    S_FA_EBITPS = Column(DECIMAL(20, 4), doc="每股息税前利润")
    S_FA_EBITTOGR = Column(DECIMAL(20, 4), doc="息税前利润/营业总收入")
    S_FA_EBITTOINTEREST = Column(DECIMAL(20, 4), doc="已获利息倍数(EBIT/利息费用)")
    S_FA_EPS_BASIC = Column(DECIMAL(20, 4), doc="基本每股收益")
    S_FA_EPS_DILUTED = Column(DECIMAL(20, 4), doc="稀释每股收益")
    S_FA_EPS_DILUTED2 = Column(DECIMAL(20, 4), doc="期末摊薄每股收益")
    S_FA_EQUITYTODEBT = Column(DECIMAL(20, 4), doc="归属于母公司的股东权益/负债合计")
    S_FA_EQUITYTOINTERESTDEBT = Column(DECIMAL(20, 4), doc="归属于母公司的股东权益/带息债务")
    S_FA_EQUITYTOTOTALCAPITAL = Column(DECIMAL(20, 4), doc="归属于母公司的股东权益/全部投入资本")
    S_FA_EXINTERESTDEBT_CURRENT = Column(DECIMAL(20, 4), doc="无息流动负债")
    S_FA_EXINTERESTDEBT_NONCURRENT = Column(DECIMAL(20, 4), doc="无息非流动负债")
    S_FA_EXPENSETOSALES = Column(DECIMAL(20, 4), doc="销售期间费用率")
    S_FA_EXTRAORDINARY = Column(DECIMAL(20, 4), doc="非经常性损益")
    S_FA_FATURN = Column(DECIMAL(20, 4), doc="固定资产周转率")
    S_FA_FCFE = Column(DECIMAL(20, 4), doc="股权自由现金流量(FCFE)")
    S_FA_FCFEPS = Column(DECIMAL(20, 4), doc="每股股东自由现金流量")
    S_FA_FCFF = Column(DECIMAL(20, 4), doc="企业自由现金流量(FCFF)")
    S_FA_FCFFPS = Column(DECIMAL(20, 4), doc="每股企业自由现金流量")
    S_FA_FINAEXPENSETOGR = Column(DECIMAL(20, 4), doc="财务费用/营业总收入")
    S_FA_GCTOGR = Column(DECIMAL(20, 4), doc="营业总成本/营业总收入")
    S_FA_GROSSMARGIN = Column(DECIMAL(20, 4), doc="毛利")
    S_FA_GROSSPROFITMARGIN = Column(DECIMAL(20, 4), doc="销售毛利率")
    S_FA_GRPS = Column(DECIMAL(20, 4), doc="每股营业总收入")
    S_FA_IMPAIRTOGR_TTM = Column(DECIMAL(20, 4), doc="资产减值损失/营业总收入")
    S_FA_INTDEBTTOTOTALCAP = Column(DECIMAL(20, 4), doc="带息债务/全部投入资本")
    S_FA_INTERESTDEBT = Column(DECIMAL(20, 4), doc="带息债务")
    S_FA_INVESTCAPITAL = Column(DECIMAL(20, 4), doc="全部投入资本")
    S_FA_INVESTINCOME = Column(DECIMAL(20, 4), doc="价值变动净收益")
    S_FA_INVESTINCOMETOEBT = Column(DECIMAL(20, 4), doc="价值变动净收益/利润总额")
    S_FA_INVTURN = Column(DECIMAL(20, 4), doc="存货周转率")
    S_FA_INVTURNDAYS = Column(DECIMAL(20, 4), doc="存货周转天数")
    S_FA_LONGDEBTODEBT = Column(DECIMAL(20, 4), doc="非流动负债/负债合计")
    S_FA_LONGDEBTTOWORKINGCAPITAL = Column(DECIMAL(20, 4), doc="长期债务与营运资金比率")
    S_FA_NCATOASSETS = Column(DECIMAL(20, 4), doc="非流动资产/总资产")
    S_FA_NETDEBT = Column(DECIMAL(20, 4), doc="净债务")
    S_FA_NETPROFITMARGIN = Column(DECIMAL(20, 4), doc="销售净利率")
    S_FA_NETWORKINGCAPITAL = Column(DECIMAL(20, 4), doc="营运流动资本")
    S_FA_NONOPERATEPROFITTOEBT = Column(DECIMAL(20, 4), doc="营业外收支净额/利润总额")
    S_FA_NONOPPROFIT = Column(DECIMAL(20, 4), doc="非营业利润")
    S_FA_NOPTOEBT = Column(DECIMAL(20, 4), doc="非营业利润／利润总额")
    S_FA_OCFPS = Column(DECIMAL(20, 4), doc="每股经营活动产生的现金流量净额")
    S_FA_OCFTODEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额/负债合计")
    S_FA_OCFTOINTERESTDEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额/带息债务")
    S_FA_OCFTONETDEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额/净债务")
    S_FA_OCFTOOPERATEINCOME = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额/经营活动净收益")
    S_FA_OCFTOOR = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额/营业收入")
    S_FA_OCFTOPROFIT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额／营业利润")
    S_FA_OCFTOSHORTDEBT = Column(DECIMAL(20, 4), doc="经营活动产生的现金流量净额/流动负债")
    S_FA_OPERATEINCOME = Column(DECIMAL(20, 4), doc="经营活动净收益")
    S_FA_OPERATEINCOMETOEBT = Column(DECIMAL(20, 4), doc="经营活动净收益/利润总额")
    S_FA_OPTODEBT = Column(DECIMAL(20, 4), doc="营业利润／负债合计")
    S_FA_OPTOEBT = Column(DECIMAL(20, 4), doc="营业利润／利润总额")
    S_FA_OPTOGR = Column(DECIMAL(20, 4), doc="营业利润/营业总收入")
    S_FA_OPTOLIQDEBT = Column(DECIMAL(20, 4), doc="营业利润／流动负债")
    S_FA_ORPS = Column(DECIMAL(20, 4), doc="每股营业收入")
    S_FA_PREFINEXPENSE_OPPROFIT = Column(DECIMAL(20, 4), doc="扣除财务费用前营业利润")
    S_FA_PROFITTOGR = Column(DECIMAL(20, 4), doc="净利润/营业总收入")
    S_FA_PROFITTOOP = Column(DECIMAL(20, 4), doc="利润总额／营业收入")
    S_FA_QUICK = Column(DECIMAL(20, 4), doc="速动比率")
    S_FA_RETAINEDEARNINGS = Column(DECIMAL(20, 4), doc="留存收益")
    S_FA_RETAINEDPS = Column(DECIMAL(20, 4), doc="每股留存收益")
    S_FA_ROA = Column(DECIMAL(20, 4), doc="总资产净利率")
    S_FA_ROA2 = Column(DECIMAL(20, 4), doc="总资产报酬率")
    S_FA_ROA2_YEARLY = Column(DECIMAL(20, 4), doc="年化总资产报酬率")
    S_FA_ROA_YEARLY = Column(DECIMAL(20, 4), doc="年化总资产净利率")
    S_FA_ROE = Column(DECIMAL(20, 4), doc="净资产收益率")
    S_FA_ROE_AVG = Column(DECIMAL(20, 4), doc="平均净资产收益率(增发条件)")
    S_FA_ROE_DEDUCTED = Column(DECIMAL(20, 4), doc="净资产收益率(扣除非经常损益)")
    S_FA_ROE_YEARLY = Column(DECIMAL(20, 4), doc="年化净资产收益率")
    S_FA_ROIC = Column(DECIMAL(20, 4), doc="投入资本回报率")
    S_FA_ROIC_YEARLY = Column(DECIMAL(20, 4), doc="年化投入资本回报率")
    S_FA_SALEEXPENSETOGR = Column(DECIMAL(20, 4), doc="销售费用/营业总收入")
    S_FA_SALESCASHINTOOR = Column(DECIMAL(20, 4), doc="销售商品提供劳务收到的现金/营业收入")
    S_FA_SURPLUSCAPITALPS = Column(DECIMAL(20, 4), doc="每股资本公积")
    S_FA_SURPLUSRESERVEPS = Column(DECIMAL(20, 4), doc="每股盈余公积")
    S_FA_TANGASSETTOINTDEBT = Column(DECIMAL(20, 4), doc="有形资产/带息债务")
    S_FA_TANGIBLEASSET = Column(DECIMAL(20, 4), doc="有形资产")
    S_FA_TANGIBLEASSETSTOASSETS = Column(DECIMAL(20, 4), doc="有形资产/总资产")
    S_FA_TANGIBLEASSETTODEBT = Column(DECIMAL(20, 4), doc="有形资产/负债合计")
    S_FA_TANGIBLEASSETTONETDEBT = Column(DECIMAL(20, 4), doc="有形资产/净债务")
    S_FA_TAXTOEBT = Column(DECIMAL(20, 4), doc="所得税/利润总额")
    S_FA_TOT_FATURN = Column(DECIMAL(20, 4), doc="固定资产合计周转率")
    S_FA_TURNDAYS = Column(DECIMAL(20, 4), doc="营业周期")
    S_FA_UNDISTRIBUTEDPS = Column(DECIMAL(20, 4), doc="每股未分配利润")
    S_FA_WORKINGCAPITAL = Column(DECIMAL(20, 4), doc="营运资金")
    S_FA_YOY_EQUITY = Column(DECIMAL(20, 4), doc="净资产(同比增长率)")
    S_FA_YOY_OR = Column(DECIMAL(20, 4), doc="营业收入同比增长率(%)")
    S_FA_YOY_TR = Column(DECIMAL(20, 4), doc="营业总收入同比增长率(%)")
    S_FA_YOYASSETS = Column(DECIMAL(20, 4), doc="相对年初增长率-资产总计(%)")
    S_FA_YOYBPS = Column(DECIMAL(20, 4), doc="相对年初增长率-每股净资产(%)")
    S_FA_YOYEBT = Column(DECIMAL(20, 4), doc="同比增长率-利润总额(%)")
    S_FA_YOYEPS_BASIC = Column(DECIMAL(20, 4), doc="同比增长率-基本每股收益(%)")
    S_FA_YOYEPS_DILUTED = Column(DECIMAL(20, 4), doc="同比增长率-稀释每股收益(%)")
    S_FA_YOYEQUITY = Column(DECIMAL(20, 4), doc="相对年初增长率-归属母公司的股东权益(%)")
    S_FA_YOYNETPROFIT = Column(DECIMAL(20, 4), doc="同比增长率-归属母公司股东的净利润(%)")
    S_FA_YOYNETPROFIT_DEDUCTED = Column(DECIMAL(20, 4), doc="同比增长率-归属母公司股东的净利润-扣除非经常损益(%)")
    S_FA_YOYOCF = Column(DECIMAL(20, 4), doc="同比增长率-经营活动产生的现金流量净额(%)")
    S_FA_YOYOCFPS = Column(DECIMAL(20, 4), doc="同比增长率-每股经营活动产生的现金流量净额(%)")
    S_FA_YOYOP = Column(DECIMAL(20, 4), doc="同比增长率-营业利润(%)")
    S_FA_YOYROE = Column(DECIMAL(20, 4), doc="同比增长率-净资产收益率(摊薄)(%)")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_QFA_ADMINEXPENSETOGR = Column(DECIMAL(20, 4), doc="单季度.管理费用／营业总收入")
    S_QFA_CGRGR = Column(DECIMAL(20, 4), doc="单季度.营业总收入环比增长率(%)")
    S_QFA_CGRNETPROFIT = Column(DECIMAL(20, 4), doc="单季度.归属母公司股东的净利润环比增长率(%)")
    S_QFA_CGROP = Column(DECIMAL(20, 4), doc="单季度.营业利润环比增长率(%)")
    S_QFA_CGRPROFIT = Column(DECIMAL(20, 4), doc="单季度.净利润环比增长率(%)")
    S_QFA_CGRSALES = Column(DECIMAL(20, 4), doc="单季度.营业收入环比增长率(%)")
    S_QFA_DEDUCTEDPROFIT = Column(DECIMAL(20, 4), doc="单季度.扣除非经常损益后的净利润")
    S_QFA_DEDUCTEDPROFITTOPROFIT = Column(DECIMAL(20, 4), doc="单季度.扣除非经常损益后的净利润／净利润")
    S_QFA_EPS = Column(DECIMAL(24, 6), doc="单季度.每股收益")
    S_QFA_EXPENSETOSALES = Column(DECIMAL(20, 4), doc="单季度.销售期间费用率")
    S_QFA_FINAEXPENSETOGR = Column(DECIMAL(20, 4), doc="单季度.财务费用／营业总收入")
    S_QFA_GCTOGR = Column(DECIMAL(20, 4), doc="单季度.营业总成本／营业总收入")
    S_QFA_GROSSPROFITMARGIN = Column(DECIMAL(20, 4), doc="单季度.销售毛利率")
    S_QFA_IMPAIRTOGR_TTM = Column(DECIMAL(20, 4), doc="单季度.资产减值损失／营业总收入")
    S_QFA_INVESTINCOME = Column(DECIMAL(20, 4), doc="单季度.价值变动净收益")
    S_QFA_INVESTINCOMETOEBT = Column(DECIMAL(20, 4), doc="单季度.价值变动净收益／利润总额")
    S_QFA_NETPROFITMARGIN = Column(DECIMAL(20, 4), doc="单季度.销售净利率")
    S_QFA_OCFTOOR = Column(DECIMAL(20, 4), doc="单季度.经营活动产生的现金流量净额／经营活动净收益")
    S_QFA_OCFTOSALES = Column(DECIMAL(20, 4), doc="单季度.经营活动产生的现金流量净额／营业收入")
    S_QFA_OPERATEINCOME = Column(DECIMAL(20, 4), doc="单季度.经营活动净收益")
    S_QFA_OPERATEINCOMETOEBT = Column(DECIMAL(20, 4), doc="单季度.经营活动净收益／利润总额")
    S_QFA_OPTOGR = Column(DECIMAL(20, 4), doc="单季度.营业利润／营业总收入")
    S_QFA_PROFITTOGR = Column(DECIMAL(20, 4), doc="单季度.净利润／营业总收入")
    S_QFA_ROA = Column(DECIMAL(20, 4), doc="单季度.总资产净利润")
    S_QFA_ROE = Column(DECIMAL(24, 6), doc="单季度.净资产收益率")
    S_QFA_ROE_DEDUCTED = Column(DECIMAL(24, 6), doc="单季度.净资产收益率(扣除非经常损益)")
    S_QFA_SALEEXPENSETOGR = Column(DECIMAL(20, 4), doc="单季度.销售费用／营业总收入")
    S_QFA_SALESCASHINTOOR = Column(DECIMAL(20, 4), doc="单季度.销售商品提供劳务收到的现金／营业收入")
    S_QFA_YOYGR = Column(DECIMAL(20, 4), doc="单季度.营业总收入同比增长率(%)")
    S_QFA_YOYNETPROFIT = Column(DECIMAL(20, 4), doc="单季度.归属母公司股东的净利润同比增长率(%)")
    S_QFA_YOYOP = Column(DECIMAL(20, 4), doc="单季度.营业利润同比增长率(%)")
    S_QFA_YOYPROFIT = Column(DECIMAL(20, 4), doc="单季度.净利润同比增长率(%)")
    S_QFA_YOYSALES = Column(DECIMAL(20, 4), doc="单季度.营业收入同比增长率(%)")
    S_STM_BS = Column(DECIMAL(20, 4), doc="固定资产合计")
    S_STM_IS = Column(DECIMAL(20, 4), doc="折旧与摊销")
    S_STMNOTE_FINEXP = Column(DECIMAL(20, 4), doc="利息费用")
    WAA_ROE = Column(DECIMAL(24, 6), doc="加权平均净资产收益率")
    WIND_CODE = Column(String(40), doc="Wind代码")


class ASHAREFLOATHOLDER(Base):

    __tablename__ = 'ASHAREFLOATHOLDER'

    ANN_DT = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_HOLDER_ENDDATE = Column(String(8), doc="截止日期")
    S_HOLDER_HOLDERCATEGORY = Column(String(1), doc="股东类型")
    S_HOLDER_NAME = Column(String(300), doc="持有人")
    S_HOLDER_QUANTITY = Column(DECIMAL(20, 4), doc="数量（股）")
    S_HOLDER_WINDNAME = Column(String(200), doc="持有人（容错后）")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREFREEFLOAT(Base):

    __tablename__ = 'ASHAREFREEFLOAT'

    ANN_DT = Column(String(8), doc="公告日期")
    CHANGE_DT = Column(String(8), doc="变动日期(除权日)")
    CHANGE_DT1 = Column(String(8), doc="变动日期(上市日)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_SHARE_FREESHARES = Column(DECIMAL(20, 4), doc="自由流通股本(万股)")


class ASHAREGROUP(Base):

    __tablename__ = 'ASHAREGROUP'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMP_NAME = Column(String(100), doc="集团公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="集团公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="集团公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREGROUPINFORMATION(Base):

    __tablename__ = 'ASHAREGROUPINFORMATION'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMP_NAME = Column(String(100), doc="集团公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="集团公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="集团公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREGUARANTEERELATIONSHIP(Base):

    __tablename__ = 'ASHAREGUARANTEERELATIONSHIP'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="被担保公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="被担保公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="被担保公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREGUARANTEESTATISTICS(Base):

    __tablename__ = 'ASHAREGUARANTEESTATISTICS'

    AMOUNT_OF_GUARANTEE = Column(DECIMAL(20, 4), doc="担保总额")
    AMOUNT_OF_GUARANTEE_RATE = Column(DECIMAL(20, 4), doc="担保总额占净资产比例")
    AMOUNT_OF_GUARANTEE_TOTAL = Column(DECIMAL(20, 4), doc="担保额度合计")
    ANN_DATE = Column(String(8), doc="公告日期")
    CONTROLLING_TOTAL = Column(DECIMAL(20, 4), doc="为控股股东及其他关联方提供担保金额")
    CURRENCY_CODE = Column(String(10), doc="货币代码")
    DEADLINE = Column(String(8), doc="截止日期")
    EXTERNAL_GUARANTEE = Column(DECIMAL(20, 4), doc="对外担保额度合计")
    GUARANTEE_BALANCE_TOTAL = Column(DECIMAL(20, 4), doc="担保余额合计")
    HOLDING_AMOUNT_OF_GUARANTEE = Column(DECIMAL(20, 4), doc="对控股子公司担保额度合计")
    HOLDING_TOTAL = Column(DECIMAL(20, 4), doc="对控股子公司担保余额合计")
    HOLDING_TOTAL_AMOUNT_GUARANTEE = Column(DECIMAL(20, 4), doc="对控股子公司担保发生额合计")
    IS_MORE_THAN_NET_ASSETS = Column(DECIMAL(5, 0), doc="担保总额是否超过净资产50%")
    MORE_THAN_NET_ASSETS_AMOUNT = Column(DECIMAL(20, 4), doc="担保总额超过净资产50%部分的金额")
    NET_ASSETS_RATE = Column(DECIMAL(20, 4), doc="担保总额占净资产比例(%)(计算值)")
    NET_ASSETS_RATE2 = Column(DECIMAL(20, 4), doc="担保额度占净资产比例")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(10), doc="公司id")
    TOTAL_AMOUNT_GUARANTEE = Column(DECIMAL(20, 4), doc="担保发生额合计")
    TOTAL_AMOUNT_GUARANTEE1 = Column(DECIMAL(20, 4), doc="为高负债对象提供担保金额")
    VIOLATION_AMOUNT_GUARANTEE = Column(DECIMAL(20, 4), doc="违规担保总额")


class ASHAREHOLDER(Base):

    __tablename__ = 'ASHAREHOLDER'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_ENDDATE = Column(String(10), doc="报告期")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="持股比例")
    S_INFO_COMP_NAME = Column(String(100), doc="股东公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="股东公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="股东公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREHOLDERNUMBER(Base):

    __tablename__ = 'ASHAREHOLDERNUMBER'

    ANN_DT = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_ENDDATE = Column(String(8), doc="截止日期")
    S_HOLDER_NUM = Column(DECIMAL(20, 4), doc="A股股东户数")
    S_HOLDER_TOTAL_NUM = Column(DECIMAL(20, 4), doc="股东总户数")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREHOLDING(Base):

    __tablename__ = 'ASHAREHOLDING'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_ENDDATE = Column(String(10), doc="报告期")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="持股比例")
    S_INFO_COMP_NAME = Column(String(100), doc="投资公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="投资公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="投资公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREIBROKERINDICATOR(Base):

    __tablename__ = 'ASHAREIBROKERINDICATOR'

    ANN_DT = Column(String(8))
    ASSET_LIABILITY_RATIO = Column(DECIMAL(20, 4))
    ASSET_TURNOVER_RATIO = Column(DECIMAL(20, 4))
    CONTINGENT_LIABILITY_RATIO = Column(DECIMAL(20, 4))
    CONVERTIBLE_BOND = Column(DECIMAL(20, 4))
    CURRENT_RATIO = Column(DECIMAL(20, 4))
    FEE_BUSINESS_RATIO = Column(DECIMAL(20, 4))
    FIXED_CAPITAL_RATIO = Column(DECIMAL(20, 4))
    IFLISTED_DATA = Column(DECIMAL(5, 0))
    INVESTMENT_FUNDS = Column(DECIMAL(20, 4))
    LONGTERM_INVEST_RATIO = Column(DECIMAL(20, 4))
    NET_CAP_NET_ASSETS = Column(DECIMAL(20, 4))
    NET_CAP_TOTAL_RISKPROV = Column(DECIMAL(20, 4))
    NET_CAPITAL = Column(DECIMAL(20, 4))
    NET_CAPITAL_RETURN = Column(DECIMAL(20, 4))
    NET_CAPITAL_YIELD = Column(DECIMAL(20, 4))
    NET_GEARING_RATIO = Column(DECIMAL(20, 4))
    OBJECT_ID = Column(String(100), primary_key=True)
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PER_CAPITA_PROFITS = Column(DECIMAL(20, 4))
    PROP_EQU_DER_NETCAP = Column(DECIMAL(20, 4))
    PROP_EQUITY_RATIO = Column(DECIMAL(20, 4))
    PROP_FIXEDINCOME_NETCAP = Column(DECIMAL(20, 4))
    PROP_SECURITIES = Column(DECIMAL(20, 4))
    REPORT_PERIOD = Column(String(8))
    S_INFO_WINDCODE = Column(String(40))
    STATEMENT_TYPE = Column(String(40))
    STOCKS = Column(DECIMAL(20, 4))
    TOTAL_CAPITAL_RETURN = Column(DECIMAL(20, 4))
    TREASURY_BOND = Column(DECIMAL(20, 4))
    TRUSTED_CAPITAL = Column(DECIMAL(20, 4))


class ASHAREILLEGALITY(Base):

    __tablename__ = 'ASHAREILLEGALITY'

    AMOUNT = Column(DECIMAL(20, 4), doc="处罚金额(元)")
    ANN_DT = Column(String(8), doc="公告日期")
    ANN_ID = Column(DECIMAL(11, 0), doc="公告id")
    BAN_YEAR = Column(DECIMAL(20, 4), doc="市场禁入期限(年)")
    BEHAVIOR = Column(LONGTEXT, doc="违规行为")
    DISPOSAL_DT = Column(String(8), doc="处罚日期")
    DISPOSAL_TYPE = Column(String(100), doc="处分类型")
    ILLEG_TYPE = Column(String(100), doc="违规类型")
    ILLEG_TYPE_CODE = Column(String(1000), doc="违规类型代码")
    METHOD = Column(String(2000), doc="处分措施")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PROCESSOR = Column(String(200), doc="处理人")
    REF_RULE = Column(String(1000), doc="相关法规")
    RELATION_TYPE = Column(DECIMAL(9, 0), doc="与上市公司的关系")
    S_INFO_COMPCODE = Column(String(40), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SUBJECT = Column(String(100), doc="违规主体")
    SUBJECT_TYPE = Column(DECIMAL(9, 0), doc="主体类别代码")


class ASHAREINCDESCRIPTION(Base):

    __tablename__ = 'ASHAREINCDESCRIPTION'

    ANN_DT = Column(String(8), doc="公告日期")
    EQINC_PLAN_EVENT_ID = Column(String(40), doc="股权激励事件ID")
    GM_DATE = Column(String(8), doc="股东大会公告日")
    IMPLEMENT_DATE = Column(String(8), doc="首次实施公告日")
    INC_FUND_DESCRIPTION = Column(String(1000), doc="激励基金说明")
    INC_NUMBERS_RATE = Column(DECIMAL(20, 4), doc="激励数量占当前总股本比例(%)")
    INTERVAL_MONTHS = Column(DECIMAL(20, 4), doc="授权日与首次可行权日间隔时间(月)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PREPLAN_ANN_DATE = Column(String(8), doc="预案公告日")
    PRICE_DESCRIPTION = Column(String(80), doc="价格说明")
    PROGRESS = Column(String(10), doc="方案进度")
    S_INC_ENDINC = Column(String(8), doc="到期日")
    S_INC_EXPIRYDATE = Column(DECIMAL(20, 4), doc="有效期")
    S_INC_FIRSTINC = Column(String(8), doc="起始日")
    S_INC_INCENTCONDITION = Column(String(2000), doc="激励授予条件")
    S_INC_INCENTSHARESALEDESCRIPT = Column(String(1000), doc="激励股票出售说明")
    S_INC_INITEXECPRI = Column(DECIMAL(20, 4), doc="期权初始行权价格(股票转让价格)")
    S_INC_OPTEXESPECIALCONDITION = Column(String(2000), doc="期权行权特别条件")
    S_INC_PROGRAMDESCRIPT = Column(String(3000), doc="方案说明")
    S_INC_QUANTITY = Column(DECIMAL(20, 4), doc="激励总数(万股/万份)")
    S_INC_SEQUENCE = Column(String(6), doc="序号")
    S_INC_SUBJECT = Column(DECIMAL(9, 0), doc="激励标的")
    S_INC_TYPE = Column(DECIMAL(9, 0), doc="激励方式")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINCEXECQTYPRI(Base):

    __tablename__ = 'ASHAREINCEXECQTYPRI'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INC_EXECDATE = Column(String(8), doc="行权日期")
    S_INC_EXECPRI = Column(DECIMAL(20, 4), doc="行权价格")
    S_INC_EXECQTY = Column(DECIMAL(20, 4), doc="行权数量(万份)")
    S_INC_NAME = Column(String(200), doc="姓名")
    S_INC_SEQUENCE = Column(String(10), doc="序号")
    S_INFO_WINDCODE = Column(String(100), doc="Wind代码")


class ASHAREINCEXERCISEPCT(Base):

    __tablename__ = 'ASHAREINCEXERCISEPCT'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INC_EXECBATCH = Column(String(6), doc="行权期")
    S_INC_EXECPCT = Column(DECIMAL(20, 4), doc="行权比例(%)")
    S_INC_INTERVALTIME = Column(DECIMAL(20, 4), doc="首个授权日至行权期间隔时间(月)")
    S_INC_SEQUENCE = Column(String(6), doc="序号")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINCEXERCISEPCTZL(Base):

    __tablename__ = 'ASHAREINCEXERCISEPCTZL'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INC_EXECBATCH = Column(String(6), doc="行权期")
    S_INC_EXECPCT = Column(DECIMAL(20, 4), doc="行权比例(%)")
    S_INC_INTERVALTIME = Column(DECIMAL(20, 4), doc="首个授权日至行权期间隔时间(月)")
    S_INC_SEQUENCE = Column(String(6), doc="序号")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINCOME(Base):

    __tablename__ = 'ASHAREINCOME'

    ACTUAL_ANN_DT = Column(String(8), doc="实际公告日期")
    ADJLOSSGAIN_PREVYEAR = Column(DECIMAL(20, 4), doc="调整以前年度损益")
    ANN_DT = Column(String(8), doc="公告日期")
    ASSET_DISPOSAL_INCOME = Column(DECIMAL(20, 4), doc="资产处置收益")
    CAPITALIZED_COMSTOCK_DIV = Column(DECIMAL(20, 4), doc="转作股本的普通股股利")
    CHG_INSUR_CONT_RSRV = Column(DECIMAL(20, 4), doc="提取保险责任准备金")
    CHG_UNEARNED_PREM_RES = Column(DECIMAL(20, 4), doc="提取未到期责任准备金")
    COMP_TYPE_CODE = Column(String(2), doc="公司类型代码")
    COMSHARE_DVD_PAYABLE = Column(DECIMAL(20, 4), doc="应付普通股股利")
    CONTINUED_NET_PROFIT = Column(DECIMAL(20, 4), doc="持续经营净利润")
    CREDIT_IMPAIRMENT_LOSS = Column(DECIMAL(20, 4), doc="信用减值损失")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    DISTRIBUTABLE_PROFIT = Column(DECIMAL(20, 4), doc="可分配利润")
    DISTRIBUTABLE_PROFIT_SHRHDER = Column(DECIMAL(20, 4), doc="可供股东分配的利润")
    DVD_EXP_INSURED = Column(DECIMAL(20, 4), doc="保户红利支出")
    EBIT = Column(DECIMAL(20, 4), doc="息税前利润")
    EBITDA = Column(DECIMAL(20, 4), doc="息税折旧摊销前利润")
    END_NET_PROFIT = Column(DECIMAL(20, 4), doc="终止经营净利润")
    FIN_EXP_INT_INC = Column(DECIMAL(20, 4), doc="财务费用:利息收入")
    HANDLING_CHRG_COMM_INC = Column(DECIMAL(20, 4), doc="手续费及佣金收入")
    IL_NET_LOSS_DISP_NONCUR_ASSET = Column(DECIMAL(20, 4), doc="其中:减:非流动资产处置净损失")
    INC_TAX = Column(DECIMAL(20, 4), doc="所得税")
    INCL_INC_INVEST_ASSOC_JV_ENTP = Column(DECIMAL(20, 4), doc="其中:对联营企业和合营企业的投资收益")
    INCL_REINSURANCE_PREM_INC = Column(DECIMAL(20, 4), doc="其中:分保费收入")
    INSUR_PREM_UNEARNED = Column(DECIMAL(20, 4), doc="已赚保费")
    INSURANCE_EXPENSE = Column(DECIMAL(20, 4), doc="保险业务支出")
    INT_INC = Column(DECIMAL(20, 4), doc="利息收入")
    IS_CALCULATION = Column(DECIMAL(5, 0), doc="是否计算报表")
    LESS_CEDED_OUT_PREM = Column(DECIMAL(20, 4), doc="减:分出保费")
    LESS_CLAIM_RECB_REINSURER = Column(DECIMAL(20, 4), doc="减:摊回赔付支出")
    LESS_EXP_RECB_REINSURER = Column(DECIMAL(20, 4), doc="减:摊回分保费用")
    LESS_FIN_EXP = Column(DECIMAL(20, 4), doc="减:财务费用")
    LESS_GERL_ADMIN_EXP = Column(DECIMAL(20, 4), doc="减:管理费用")
    LESS_HANDLING_CHRG_COMM_EXP = Column(DECIMAL(20, 4), doc="减:手续费及佣金支出")
    LESS_IMPAIR_LOSS_ASSETS = Column(DECIMAL(20, 4), doc="减:资产减值损失")
    LESS_INS_RSRV_RECB_REINSURER = Column(DECIMAL(20, 4), doc="减:摊回保险责任准备金")
    LESS_INT_EXP = Column(DECIMAL(20, 4), doc="减:利息支出")
    LESS_NON_OPER_EXP = Column(DECIMAL(20, 4), doc="减:营业外支出")
    LESS_OPER_COST = Column(DECIMAL(20, 4), doc="减:营业成本")
    LESS_SELLING_DIST_EXP = Column(DECIMAL(20, 4), doc="减:销售费用")
    LESS_TAXES_SURCHARGES_OPS = Column(DECIMAL(20, 4), doc="减:营业税金及附加")
    MEMO = Column(String(1000), doc="备注")
    MINORITY_INT_INC = Column(DECIMAL(20, 4), doc="少数股东损益")
    NET_AFTER_DED_NR_LP_CORRECT = Column(DECIMAL(20, 4), doc="扣除非经常性损益后的净利润(财务重要指标(更正前))")
    NET_EXPOSURE_HEDGING_BENEFITS = Column(DECIMAL(20, 4), doc="净敞口套期收益")
    NET_HANDLING_CHRG_COMM_INC = Column(DECIMAL(20, 4), doc="手续费及佣金净收入")
    NET_INC_EC_ASSET_MGMT_BUS = Column(DECIMAL(20, 4), doc="受托客户资产管理业务净收入")
    NET_INC_OTHER_OPS = Column(DECIMAL(20, 4), doc="其他经营净收益")
    NET_INC_SEC_TRADING_BROK_BUS = Column(DECIMAL(20, 4), doc="代理买卖证券业务净收入")
    NET_INC_SEC_UW_BUS = Column(DECIMAL(20, 4), doc="证券承销业务净收入")
    NET_INT_INC = Column(DECIMAL(20, 4), doc="利息净收入")
    NET_PROFIT_AFTER_DED_NR_LP = Column(DECIMAL(20, 4), doc="扣除非经常性损益后净利润（扣除少数股东损益）")
    NET_PROFIT_EXCL_MIN_INT_INC = Column(DECIMAL(20, 4), doc="净利润(不含少数股东损益)")
    NET_PROFIT_INCL_MIN_INT_INC = Column(DECIMAL(20, 4), doc="净利润(含少数股东损益)")
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(DECIMAL(20, 4), doc="国际会计准则净利润")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPER_EXP = Column(DECIMAL(20, 4), doc="营业支出")
    OPER_PROFIT = Column(DECIMAL(20, 4), doc="营业利润")
    OPER_REV = Column(DECIMAL(20, 4), doc="营业收入")
    OPMODE = Column(String(1))
    OTHER_BUS_COST = Column(DECIMAL(20, 4), doc="其他业务成本")
    OTHER_BUS_INC = Column(DECIMAL(20, 4), doc="其他业务收入")
    OTHER_COMPREH_INC = Column(DECIMAL(20, 4), doc="其他综合收益")
    OTHER_IMPAIR_LOSS_ASSETS = Column(DECIMAL(20, 4), doc="其他资产减值损失")
    OTHER_INCOME = Column(DECIMAL(20, 4), doc="其他收益")
    PLUS_NET_GAIN_CHG_FV = Column(DECIMAL(20, 4), doc="加:公允价值变动净收益")
    PLUS_NET_GAIN_FX_TRANS = Column(DECIMAL(20, 4), doc="加:汇兑净收益")
    PLUS_NET_INC_OTHER_BUS = Column(DECIMAL(20, 4), doc="加:其他业务净收益")
    PLUS_NET_INVEST_INC = Column(DECIMAL(20, 4), doc="加:投资净收益")
    PLUS_NON_OPER_REV = Column(DECIMAL(20, 4), doc="加:营业外收入")
    PREM_INC = Column(DECIMAL(20, 4), doc="保费业务收入")
    PREPAY_SURR = Column(DECIMAL(20, 4), doc="退保金")
    PRFSHARE_DVD_PAYABLE = Column(DECIMAL(20, 4), doc="应付优先股股利")
    RD_EXPENSE = Column(DECIMAL(20, 4), doc="研发费用")
    REINSURANCE_EXP = Column(DECIMAL(20, 4), doc="分保费用")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_FA_EPS_BASIC = Column(DECIMAL(20, 4), doc="基本每股收益")
    S_FA_EPS_DILUTED = Column(DECIMAL(20, 4), doc="稀释每股收益")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SPE_BAL_NET_PROFIT = Column(DECIMAL(20, 4), doc="净利润差额(特殊报表科目)")
    SPE_BAL_OPER_PROFIT = Column(DECIMAL(20, 4), doc="营业利润差额(特殊报表科目)")
    SPE_BAL_TOT_PROFIT = Column(DECIMAL(20, 4), doc="利润总额差额(特殊报表科目)")
    STATEMENT_TYPE = Column(String(10), doc="报表类型")
    STMNOTE_FINEXP = Column(DECIMAL(20, 4), doc="财务费用:利息费用")
    TOT_BAL_NET_PROFIT = Column(DECIMAL(20, 4), doc="净利润差额(合计平衡项目)")
    TOT_BAL_OPER_PROFIT = Column(DECIMAL(20, 4), doc="营业利润差额(合计平衡项目)")
    TOT_BAL_TOT_PROFIT = Column(DECIMAL(20, 4), doc="利润总额差额(合计平衡项目)")
    TOT_CLAIM_EXP = Column(DECIMAL(20, 4), doc="赔付总支出")
    TOT_COMPREH_INC = Column(DECIMAL(20, 4), doc="综合收益总额")
    TOT_COMPREH_INC_MIN_SHRHLDR = Column(DECIMAL(20, 4), doc="综合收益总额(少数股东)")
    TOT_COMPREH_INC_PARENT_COMP = Column(DECIMAL(20, 4), doc="综合收益总额(母公司)")
    TOT_OPER_COST = Column(DECIMAL(20, 4), doc="营业总成本")
    TOT_OPER_COST2 = Column(DECIMAL(20, 4), doc="营业总成本2")
    TOT_OPER_REV = Column(DECIMAL(20, 4), doc="营业总收入")
    TOT_PROFIT = Column(DECIMAL(20, 4), doc="利润总额")
    TRANSFER_FROM_HOUSINGIMPREST = Column(DECIMAL(20, 4), doc="住房周转金转入")
    TRANSFER_FROM_OTHERS = Column(DECIMAL(20, 4), doc="其他转入")
    TRANSFER_FROM_SURPLUSRESERVE = Column(DECIMAL(20, 4), doc="盈余公积转入")
    UNCONFIRMED_INVEST_LOSS = Column(DECIMAL(20, 4), doc="未确认投资损失")
    UNDISTRIBUTED_PROFIT = Column(DECIMAL(20, 4), doc="年初未分配利润")
    WIND_CODE = Column(String(40), doc="Wind代码")
    WITHDR_BUZEXPWELFARE = Column(DECIMAL(20, 4), doc="提取企业发展基金")
    WITHDR_LEGALPUBWELFUNDS = Column(DECIMAL(20, 4), doc="提取法定公益金")
    WITHDR_LEGALSURPLUS = Column(DECIMAL(20, 4), doc="提取法定盈余公积")
    WITHDR_OTHERSURPRESERVE = Column(DECIMAL(20, 4), doc="提取任意盈余公积金")
    WITHDR_RESERVEFUND = Column(DECIMAL(20, 4), doc="提取储备基金")
    WORKERS_WELFARE = Column(DECIMAL(20, 4), doc="职工奖金福利")


class ASHAREINCQUANTITYDETAILS(Base):

    __tablename__ = 'ASHAREINCQUANTITYDETAILS'

    ANN_DT = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INC_NAME = Column(String(80), doc="姓名")
    S_INC_POST = Column(String(80), doc="职位")
    S_INC_QUANTITY = Column(DECIMAL(20, 4), doc="数量(万股/万份)")
    S_INC_SEQUENCE = Column(String(6), doc="序号")
    S_INC_TOTALQTYPCT = Column(DECIMAL(20, 4), doc="占本次授予总数量比例(%)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINCQUANTITYPRICE(Base):

    __tablename__ = 'ASHAREINCQUANTITYPRICE'

    ANN_DT = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INC_DNEXEC_QUANTITY = Column(DECIMAL(20, 4), doc="已授权未行权的期权数量(万份)")
    S_INC_ENDDATE = Column(String(8), doc="截止日期")
    S_INC_GETFUNDQTY = Column(DECIMAL(20, 4), doc="提取激励基金数量(元)")
    S_INC_GRANTDATE = Column(String(8), doc="期权授权日")
    S_INC_ISCOMPLETED = Column(DECIMAL(5, 0), doc="股权激励是否全部完成")
    S_INC_QUANTITY = Column(DECIMAL(20, 4), doc="激励数量(万份)")
    S_INC_SEQUENCE = Column(String(6), doc="序号")
    S_INC_TRANSFERPRIPER = Column(DECIMAL(20, 4), doc="每股转让价格(行权价格)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINDUSRATING(Base):

    __tablename__ = 'ASHAREINDUSRATING'

    COLLECT_DT = Column(String(8), doc="[内部]公告日期")
    END_DT = Column(String(8), doc="有效期截止日")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RATING = Column(String(100), doc="新评级")
    RATING_ANALYST = Column(String(20), doc="分析师")
    RATING_ANALYST_ID = Column(String(200), doc="[内部]分析师id")
    RATING_DT = Column(String(8), doc="评级日期")
    RATING_INSTITUTE = Column(String(20), doc="机构")
    RATING_INSTITUTE_ID = Column(String(38), doc="[内部]机构id")
    RATING_MEMO = Column(String(2000), doc="[内部]摘要")
    REPORT_IND = Column(String(100), doc="原始行业")
    REPORT_TYPE_CODE = Column(DECIMAL(9, 0), doc="报告类型代码")
    SCORE = Column(DECIMAL(20, 0), doc="得分")
    WIND_IND_CODE = Column(String(50), doc="Wind行业ID")


class ASHAREINDUSTRIESCLASSCITICS(Base):

    __tablename__ = 'ASHAREINDUSTRIESCLASSCITICS'

    CITICS_IND_CODE = Column(String(50), doc="中信行业代码")
    CUR_SIGN = Column(String(10), doc="最新标志")
    ENTRY_DT = Column(String(8), doc="纳入日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REMOVE_DT = Column(String(8), doc="剔除日期")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    WIND_CODE = Column(String(40))


class ASHAREINDUSTRIESCLASSCITICSZL(Base):

    __tablename__ = 'ASHAREINDUSTRIESCLASSCITICSZL'

    CITICS_IND_CODE = Column(String(50), doc="中信行业代码")
    CUR_SIGN = Column(String(10), doc="最新标志")
    ENTRY_DT = Column(String(8), doc="纳入日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REMOVE_DT = Column(String(8), doc="剔除日期")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    WIND_CODE = Column(String(40))


class ASHAREINDUSTRIESCODE(Base):

    __tablename__ = 'ASHAREINDUSTRIESCODE'

    CHINESEDEFINITION = Column(String(600), doc="板块中文定义")
    INDUSTRIESALIAS = Column(String(12), doc="板块别名")
    INDUSTRIESCODE = Column(String(38), doc="行业代码")
    INDUSTRIESCODE_OLD = Column(String(38), doc="行业代码(旧)")
    INDUSTRIESNAME = Column(String(50), doc="行业名称")
    LEVELNUM = Column(DECIMAL(1, 0), doc="级数")
    MEMO = Column(String(100), doc="备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    SEQUENCE = Column(DECIMAL(4, 0), doc="展示序号")
    USED = Column(DECIMAL(1, 0), doc="是否有效")
    WIND_NAME_ENG = Column(String(200), doc="板块英文名称")


class ASHAREINSIDEHOLDER(Base):

    __tablename__ = 'ASHAREINSIDEHOLDER'

    ANN_DT = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(10), doc="报告期")
    S_HOLDER_ANAME = Column(String(100), doc="股东名称")
    S_HOLDER_ENDDATE = Column(String(8), doc="截止日期")
    S_HOLDER_HOLDERCATEGORY = Column(String(1), doc="股东类型")
    S_HOLDER_MEMO = Column(String(1500), doc="股东说明")
    S_HOLDER_NAME = Column(String(100), doc="股东名称")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="持股比例")
    S_HOLDER_QUANTITY = Column(DECIMAL(20, 4), doc="持股数量")
    S_HOLDER_RESTRICTEDQUANTITY = Column(DECIMAL(20, 4), doc="持有限售股份（非流通股）数量")
    S_HOLDER_SEQUENCE = Column(String(200), doc="关联方序号")
    S_HOLDER_SHARECATEGORY = Column(String(40), doc="持股性质代码")
    S_HOLDER_SHARECATEGORYNAME = Column(String(40), doc="持股性质")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINSIDERTRADE(Base):

    __tablename__ = 'ASHAREINSIDERTRADE'

    ACTUAL_ANN_DT = Column(String(8), doc="实际公告日期")
    ANN_DT = Column(String(8), doc="填报日期")
    CHANGE_VOLUME = Column(DECIMAL(20, 4), doc="变动数")
    IS_SHORT_TERM_TRADE = Column(DECIMAL(5, 0), doc="是否为短线交易")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    POSITION_AFTER_TRADE = Column(DECIMAL(20, 4), doc="变动后持股")
    RELATED_MANAGER_NAME = Column(String(100), doc="相关管理层姓名")
    RELATED_MANAGER_POST = Column(String(80), doc="相关管理层职务")
    REPORTED_TRADER_NAME = Column(String(100), doc="变动人姓名")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_AVG_PRICE = Column(DECIMAL(20, 4), doc="成交均价")
    TRADE_DT = Column(String(8), doc="变动日期")
    TRADE_REASON_CODE = Column(DECIMAL(9, 0), doc="变动原因类型代码")
    TRADER_MANAGER_RELATION = Column(String(20), doc="变动人与管理层的关系")


class ASHAREINSTHOLDERDERDATA(Base):

    __tablename__ = 'ASHAREINSTHOLDERDERDATA'

    ANN_DATE = Column(String(8), doc="公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_FLOAT_A_SHR = Column(DECIMAL(20, 4), doc="流通A股")
    S_HOLDER_COMPCODE = Column(String(40), doc="股东公司id")
    S_HOLDER_HOLDERCATEGORY = Column(String(40), doc="股东类型")
    S_HOLDER_NAME = Column(String(200), doc="股东名称")
    S_HOLDER_PCT = Column(DECIMAL(20, 6), doc="持股比例(计算)")
    S_HOLDER_QUANTITY = Column(DECIMAL(20, 4), doc="持股数")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREINSURANCEINDICATOR(Base):

    __tablename__ = 'ASHAREINSURANCEINDICATOR'

    ACTUAL_CAPITAL_GROUP = Column(DECIMAL(20, 4))
    ACTUAL_CAPITAL_LIFE = Column(DECIMAL(20, 4))
    ACTUAL_CAPITAL_PROPERTY = Column(DECIMAL(20, 4))
    ANN_DT = Column(String(8))
    CAP_ADEQUACY_RATIO_LIFE = Column(DECIMAL(20, 4))
    CAP_ADEQUACY_RATIO_PROPERTY = Column(DECIMAL(20, 4))
    CAPITAL_ADEQUACY_RATIO_GROUP = Column(DECIMAL(20, 4))
    COMBINED_COST_PROPERTY = Column(DECIMAL(20, 4))
    CRNCY_CODE = Column(String(10))
    FEE_RATIO_PROPERTY = Column(DECIMAL(20, 4))
    INTRINSIC_VALUE_LIFE = Column(DECIMAL(20, 4))
    LOSS_RATIO_PROPERTY = Column(DECIMAL(20, 4))
    MINIMUN_CAPITAL_GROUP = Column(DECIMAL(20, 4))
    MINIMUN_CAPITAL_LIFE = Column(DECIMAL(20, 4))
    MINIMUN_CAPITAL_PROPERTY = Column(DECIMAL(20, 4))
    NET_INVESTMENT_YIELD = Column(DECIMAL(20, 4))
    OBJECT_ID = Column(String(100), primary_key=True)
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    POLICY_PERSISTENCY_RATE_13M = Column(DECIMAL(20, 4))
    POLICY_PERSISTENCY_RATE_14M = Column(DECIMAL(20, 4))
    POLICY_PERSISTENCY_RATE_25M = Column(DECIMAL(20, 4))
    POLICY_PERSISTENCY_RATE_26M = Column(DECIMAL(20, 4))
    REPORT_PERIOD = Column(String(8))
    REPORT_TYPE = Column(DECIMAL(9, 0))
    RISK_DISCOUNT_RATE = Column(DECIMAL(20, 4))
    S_INFO_WINDCODE = Column(String(40))
    STATEMENT_TYPE = Column(DECIMAL(9, 0))
    SURRENDER_RATE = Column(DECIMAL(20, 4))
    TOTAL_INVESTMENT_YIELD = Column(DECIMAL(20, 4))
    VALUE_EFFECTIVE_BUSINESS_LIFE = Column(DECIMAL(20, 4))
    VALUE_NEW_BUSINESS_LIFE = Column(DECIMAL(20, 4))


class ASHAREINTENSITYTREND(Base):

    __tablename__ = 'ASHAREINTENSITYTREND'

    BBI = Column(DECIMAL(20, 8), doc="BBI多空指数(3,6,12,24日)")
    BOTTOMING_B = Column(DECIMAL(20, 8), doc="筑底指标B(125,5,20日)")
    BOTTOMING_D = Column(DECIMAL(20, 8), doc="筑底指标D(125,5,20日)")
    DDI = Column(DECIMAL(20, 8), doc="DDI方向标准离差指数DDI(13,30,5,10日)")
    DDI_AD = Column(DECIMAL(20, 8), doc="DDI方向标准离差指数AD(13,30,5,10日)")
    DDI_ADDI = Column(DECIMAL(20, 8), doc="DDI方向标准离差指数ADDI(13,30,5,10日)")
    DMA_AMA = Column(DECIMAL(20, 8), doc="DMA平均线差AMA(10,50,10日)")
    DMA_DDD = Column(DECIMAL(20, 8), doc="DMA平均线差DDD(10,50,10日)")
    DMI_ADX = Column(DECIMAL(20, 8), doc="DMI趋向指标ADX(14,6日)")
    DMI_ADXR = Column(DECIMAL(20, 8), doc="DMI趋向指标ADXR(14,6日)")
    DMI_MDI = Column(DECIMAL(20, 8), doc="DMI趋向指标MDI(14,6日)")
    DMI_PDI = Column(DECIMAL(20, 8), doc="DMI趋向指标PDI(14,6日)")
    EXPMA = Column(DECIMAL(20, 8), doc="EXPMA指数平均数(12日)")
    MA_10D = Column(DECIMAL(20, 8), doc="MA简单移动平均(10日)")
    MA_120D = Column(DECIMAL(20, 8), doc="MA简单移动平均(120日)")
    MA_20D = Column(DECIMAL(20, 8), doc="MA简单移动平均(20日)")
    MA_250D = Column(DECIMAL(20, 8), doc="MA简单移动平均(250日)")
    MA_30D = Column(DECIMAL(20, 8), doc="MA简单移动平均30日)")
    MA_5D = Column(DECIMAL(20, 8), doc="MA简单移动平均(5日)")
    MA_60D = Column(DECIMAL(20, 8), doc="MA简单移动平均(60日)")
    MACD_DEA = Column(DECIMAL(20, 8), doc="MACD指数平滑异同平均DEA(26,12,9日)")
    MACD_DIFF = Column(DECIMAL(20, 8), doc="MACD指数平滑异同平均DIFF(26,12,9日)")
    MACD_MACD = Column(DECIMAL(20, 8), doc="MACD指数平滑异同平均MACD(26,12,9日)")
    MARKET = Column(DECIMAL(20, 8), doc="大盘同步指标沪深300(7日)")
    MTM = Column(DECIMAL(20, 8), doc="MTM动力指标MTM(6,6日)")
    MTM_MTMMA = Column(DECIMAL(20, 8), doc="MTM动力指标MTMMA(6,6日)")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICEOSC = Column(DECIMAL(20, 8), doc="PRICEOSC价格振荡指标(26,12日)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SAR = Column(DECIMAL(20, 8), doc="SAR抛物转向(4,2,20日)")
    STRENGTH = Column(DECIMAL(20, 8), doc="阶段强势指标沪深300(20日)")
    TRADE_DT = Column(String(8), doc="日期")
    TRIX = Column(DECIMAL(20, 8), doc="TRIX三重指数平滑平均TRIX(12,20日)")
    TRMA = Column(DECIMAL(20, 8), doc="TRIX三重指数平滑平均TRMA(12,20日)")
    WEAKKNESS = Column(DECIMAL(20, 8), doc="阶段弱势指标沪深300(20日)")


class ASHAREINTENSITYTRENDADJ(Base):

    __tablename__ = 'ASHAREINTENSITYTRENDADJ'

    BBI = Column(DECIMAL(20, 8), doc="BBI多空指数(3,6,12,24日)")
    BOTTOMING_B = Column(DECIMAL(20, 8), doc="筑底指标B(125,5,20日)")
    BOTTOMING_D = Column(DECIMAL(20, 8), doc="筑底指标D(125,5,20日)")
    DDI = Column(DECIMAL(20, 8), doc="DDI方向标准离差指数DDI(13,30,5,10日)")
    DDI_AD = Column(DECIMAL(20, 8), doc="DDI方向标准离差指数AD(13,30,5,10日)")
    DDI_ADDI = Column(DECIMAL(20, 8), doc="DDI方向标准离差指数ADDI(13,30,5,10日)")
    DMA_AMA = Column(DECIMAL(20, 8), doc="DMA平均线差AMA(10,50,10日)")
    DMA_DDD = Column(DECIMAL(20, 8), doc="DMA平均线差DDD(10,50,10日)")
    DMI_ADX = Column(DECIMAL(20, 8), doc="DMI趋向指标ADX(14,6日)")
    DMI_ADXR = Column(DECIMAL(20, 8), doc="DMI趋向指标ADXR(14,6日)")
    DMI_MDI = Column(DECIMAL(20, 8), doc="DMI趋向指标MDI(14,6日)")
    DMI_PDI = Column(DECIMAL(20, 8), doc="DMI趋向指标PDI(14,6日)")
    EXPMA = Column(DECIMAL(20, 8), doc="EXPMA指数平均数(12日)")
    MA_10D = Column(DECIMAL(20, 8), doc="MA简单移动平均(10日)")
    MA_120D = Column(DECIMAL(20, 8), doc="MA简单移动平均(120日)")
    MA_20D = Column(DECIMAL(20, 8), doc="MA简单移动平均(20日)")
    MA_250D = Column(DECIMAL(20, 8), doc="MA简单移动平均(250日)")
    MA_30D = Column(DECIMAL(20, 8), doc="MA简单移动平均30日)")
    MA_5D = Column(DECIMAL(20, 8), doc="MA简单移动平均(5日)")
    MA_60D = Column(DECIMAL(20, 8), doc="MA简单移动平均(60日)")
    MACD_DEA = Column(DECIMAL(20, 8), doc="MACD指数平滑异同平均DEA(26,12,9日)")
    MACD_DIFF = Column(DECIMAL(20, 8), doc="MACD指数平滑异同平均DIFF(26,12,9日)")
    MACD_MACD = Column(DECIMAL(20, 8), doc="MACD指数平滑异同平均MACD(26,12,9日)")
    MARKET = Column(DECIMAL(20, 8), doc="大盘同步指标沪深300(7日)")
    MTM = Column(DECIMAL(20, 8), doc="MTM动力指标MTM(6,6日)")
    MTM_MTMMA = Column(DECIMAL(20, 8), doc="MTM动力指标MTMMA(6,6日)")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICEOSC = Column(DECIMAL(20, 8), doc="PRICEOSC价格振荡指标(26,12日)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SAR = Column(DECIMAL(20, 8), doc="SAR抛物转向(4,2,20日)")
    STRENGTH = Column(DECIMAL(20, 8), doc="阶段强势指标沪深300(20日)")
    TRADE_DT = Column(String(8), doc="日期")
    TRIX = Column(DECIMAL(20, 8), doc="TRIX三重指数平滑平均TRIX(12,20日)")
    TRMA = Column(DECIMAL(20, 8), doc="TRIX三重指数平滑平均TRMA(12,20日)")
    WEAKKNESS = Column(DECIMAL(20, 8), doc="阶段弱势指标沪深300(20日)")


class ASHAREINVESTMENTPEVC(Base):

    __tablename__ = 'ASHAREINVESTMENTPEVC'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_DATE = Column(String(10), doc="投资时间")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="股权比例")
    S_INFO_COMP_NAME = Column(String(100), doc="投资公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="投资公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="投资公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREIPOPRICINGFORECAST(Base):

    __tablename__ = 'ASHAREIPOPRICINGFORECAST'

    ANALYST_ID = Column(String(100), doc="作者ID")
    ANALYST_NAME = Column(String(40), doc="分析师名称")
    COLLECT_TIME = Column(String(8), doc="[内部]公告日期")
    EST_DT = Column(String(8), doc="预测日期")
    EST_MEMO = Column(String(500), doc="预测摘要")
    FIRST_OPTIME = Column(DateTime, doc="[内部]发布日期")
    INQUIRY_PRICE_CEILING = Column(DECIMAL(20, 4), doc="询价建议区间上限")
    INQUIRY_PRICE_FLOOR = Column(DECIMAL(20, 4), doc="询价建议区间下限")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICE_CEILING = Column(DECIMAL(20, 4), doc="定价区间上限")
    PRICE_FLOOR = Column(DECIMAL(20, 4), doc="定价区间下限")
    RESEARCH_INST_ID = Column(String(10), doc="机构ID")
    RESEARCH_INST_ID2 = Column(String(40), doc="机构编码")
    RESEARCH_INST_NAME = Column(String(20), doc="机构名称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHARELONGLOAN(Base):

    __tablename__ = 'ASHARELONGLOAN'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="债务公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="债务公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="债务公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREMAJORHOLDERPLANHOLD(Base):

    __tablename__ = 'ASHAREMAJORHOLDERPLANHOLD'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_NAME = Column(String(200), doc="股东名称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PH_CALCULATEDAYS = Column(DECIMAL(20, 4), doc="计算天数")
    S_PH_CALCULATEPRICEMODE = Column(String(80), doc="价格计算方式")
    S_PH_CONDITIONORNOT = Column(DECIMAL(5, 0), doc="是否无条件增持")
    S_PH_CONTINUOUSDAYS = Column(DECIMAL(20, 4), doc="连续天数")
    S_PH_ENDDATE = Column(String(8), doc="增持计划截止日期")
    S_PH_INTENDPUTMONEYDOWNLIMIT = Column(DECIMAL(20, 4), doc="拟投入金额下限(亿元)")
    S_PH_INTENDPUTMONEYUPLIMIT = Column(DECIMAL(20, 4), doc="拟投入金额上限(亿元)")
    S_PH_PRICEUPLIMIT = Column(DECIMAL(20, 4), doc="增持价格上限")
    S_PH_SHARENUMDOWNLIMIT = Column(DECIMAL(20, 4), doc="增持股数下限(万股)")
    S_PH_SHARENUMUPLIMIT = Column(DECIMAL(20, 4), doc="增持股数上限(万股)")
    S_PH_STARTDATE = Column(String(8), doc="增持计划起始日期")
    S_PH_TRIGGERPRICE = Column(DECIMAL(20, 4), doc="增持触发价格")


class ASHAREMAJORHOLDERPLANHOLDZL(Base):

    __tablename__ = 'ASHAREMAJORHOLDERPLANHOLDZL'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_NAME = Column(String(200), doc="股东名称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PH_CALCULATEDAYS = Column(DECIMAL(20, 4), doc="计算天数")
    S_PH_CALCULATEPRICEMODE = Column(String(80), doc="价格计算方式")
    S_PH_CONDITIONORNOT = Column(DECIMAL(5, 0), doc="是否无条件增持")
    S_PH_CONTINUOUSDAYS = Column(DECIMAL(20, 4), doc="连续天数")
    S_PH_ENDDATE = Column(String(8), doc="增持计划截止日期")
    S_PH_INTENDPUTMONEYDOWNLIMIT = Column(DECIMAL(20, 4), doc="拟投入金额下限(亿元)")
    S_PH_INTENDPUTMONEYUPLIMIT = Column(DECIMAL(20, 4), doc="拟投入金额上限(亿元)")
    S_PH_PRICEUPLIMIT = Column(DECIMAL(20, 4), doc="增持价格上限")
    S_PH_SHARENUMDOWNLIMIT = Column(DECIMAL(20, 4), doc="增持股数下限(万股)")
    S_PH_SHARENUMUPLIMIT = Column(DECIMAL(20, 4), doc="增持股数上限(万股)")
    S_PH_STARTDATE = Column(String(8), doc="增持计划起始日期")
    S_PH_TRIGGERPRICE = Column(DECIMAL(20, 4), doc="增持触发价格")


class ASHAREMANAGEMENT(Base):

    __tablename__ = 'ASHAREMANAGEMENT'

    ANN_DATE = Column(String(8), doc="公告日期")
    DISPLAY_ORDER = Column(DECIMAL(4, 0), doc="展示顺序")
    MANID = Column(String(10), doc="人物ID")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_MANAGER_BIRTHYEAR = Column(String(8), doc="出生年份")
    S_INFO_MANAGER_EDUCATION = Column(String(10), doc="学历")
    S_INFO_MANAGER_GENDER = Column(String(10), doc="性别")
    S_INFO_MANAGER_INTRODUCTION = Column(String(2000), doc="个人简历")
    S_INFO_MANAGER_LEAVEDATE = Column(String(8), doc="离职日期")
    S_INFO_MANAGER_NAME = Column(String(80), doc="姓名")
    S_INFO_MANAGER_NATIONALITY = Column(String(40), doc="国籍")
    S_INFO_MANAGER_POST = Column(String(40), doc="职务")
    S_INFO_MANAGER_STARTDATE = Column(String(8), doc="任职日期")
    S_INFO_MANAGER_TYPE = Column(DECIMAL(5, 0), doc="管理层类别")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHAREMANAGEMENTHOLDREWARD(Base):

    __tablename__ = 'ASHAREMANAGEMENTHOLDREWARD'

    ANN_DATE = Column(String(8), doc="公告日期")
    CRNY_CODE = Column(String(10), doc="货币代码")
    END_DATE = Column(String(8), doc="截止日期")
    MANID = Column(String(10), doc="人物ID")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_MANAGER_NAME = Column(String(80), doc="姓名")
    S_INFO_MANAGER_POST = Column(String(300), doc="职务")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_MANAGER_QUANTITY = Column(DECIMAL(20, 4), doc="持股数量")
    S_MANAGER_RETURN = Column(DECIMAL(20, 4), doc="报酬")
    S_MANAGER_RETURN_OTHER = Column(DECIMAL(5, 0), doc="是否在股东或关联单位领取报酬、津贴")


class ASHAREMARGINSUBJECT(Base):

    __tablename__ = 'ASHAREMARGINSUBJECT'

    OBJECT_ID = Column(String(100), primary_key=True)
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40))
    S_MARGIN_CONVERSIONRATE = Column(DECIMAL(20, 4))
    S_MARGIN_EFFECTDATE = Column(String(8))
    S_MARGIN_ELIMINDATE = Column(String(8))
    S_MARGIN_MARGINRATE = Column(DECIMAL(20, 4))
    S_MARGIN_RATEEFFECTDATE = Column(String(8))
    S_MARGIN_SHARETYPE = Column(DECIMAL(9, 0))


class ASHAREMARGINTRADE(Base):

    __tablename__ = 'ASHAREMARGINTRADE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_MARGIN_MARGINTRADEBALANCE = Column(DECIMAL(20, 4), doc="融资融券余额(元)")
    S_MARGIN_PURCHWITHBORROWMONEY = Column(DECIMAL(20, 4), doc="融资买入额(元,股)")
    S_MARGIN_REPAYMENTOFBORROWSEC = Column(DECIMAL(20, 4), doc="融券偿还量(股,份,手)")
    S_MARGIN_REPAYMENTTOBROKER = Column(DECIMAL(20, 4), doc="融资偿还额(元,股)")
    S_MARGIN_SALESOFBORROWEDSEC = Column(DECIMAL(20, 4), doc="融券卖出量(股,份,手)")
    S_MARGIN_SECLENDINGBALANCE = Column(DECIMAL(20, 4), doc="融券余额(元)")
    S_MARGIN_SECLENDINGBALANCEVOL = Column(DECIMAL(20, 4), doc="融券余量(股,份,手)")
    S_MARGIN_TRADINGBALANCE = Column(DECIMAL(20, 4), doc="融资余额(元)")
    S_REFIN_REPAY_VOL = Column(DECIMAL(20, 0), doc="转融券偿还量")
    S_REFIN_SB_EOD_VOL = Column(DECIMAL(20, 0), doc="转融券融入日成交量")
    S_REFIN_SB_VOL_14D = Column(DECIMAL(20, 0), doc="转融券融入数量(14天)")
    S_REFIN_SB_VOL_3D = Column(DECIMAL(20, 0), doc="转融券融入数量(3天)")
    S_REFIN_SB_VOL_7D = Column(DECIMAL(20, 0), doc="转融券融入数量(7天)")
    S_REFIN_SL_EOD_VOL = Column(DECIMAL(20, 0), doc="转融券融出日成交量")
    S_REFIN_SL_EOP_BAL = Column(DECIMAL(20, 4), doc="转融券期末余额")
    S_REFIN_SL_EOP_VOL = Column(DECIMAL(20, 0), doc="转融券期末余量")
    S_REFIN_SL_VOL_14D = Column(DECIMAL(20, 0), doc="转融券融出数量(14天)")
    S_REFIN_SL_VOL_182D = Column(DECIMAL(20, 0), doc="转融券融出数量(182天)")
    S_REFIN_SL_VOL_28D = Column(DECIMAL(20, 0), doc="转融券融出数量(28天)")
    S_REFIN_SL_VOL_3D = Column(DECIMAL(20, 0), doc="转融券融出数量(3天)")
    S_REFIN_SL_VOL_7D = Column(DECIMAL(20, 0), doc="转融券融出数量(7天)")
    S_SB_VOL_182D = Column(DECIMAL(20, 0), doc="转融券融入数量(182天)")
    S_SB_VOL_28D = Column(DECIMAL(20, 0), doc="转融券融入数量(28天)")
    TRADE_DT = Column(String(8), doc="日期")


class ASHAREMARGINTRADESUM(Base):

    __tablename__ = 'ASHAREMARGINTRADESUM'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_MARSUM_CIRCULATION_VALUE = Column(DECIMAL(20, 4), doc="A股流通市值(万元)")
    S_MARSUM_EXCHMARKET = Column(String(40), doc="交易所英文简称")
    S_MARSUM_FINANCING_MARGIN = Column(DECIMAL(20, 4), doc="融资余量股(份/手)")
    S_MARSUM_FLOW_EQUITY = Column(DECIMAL(20, 4), doc="A股流通股本(万股)")
    S_MARSUM_MARGIN_MARGIN = Column(DECIMAL(20, 4), doc="融券余量")
    S_MARSUM_MARGINTRADEBALANCE = Column(DECIMAL(20, 4), doc="融资融券余额(元)")
    S_MARSUM_PURCHWITHBORROWMONEY = Column(DECIMAL(20, 4), doc="融资买入额(元)")
    S_MARSUM_REPAYMENTTOBROKER = Column(DECIMAL(20, 4), doc="融资偿还额(元)")
    S_MARSUM_SALESOFBORROWEDSEC = Column(DECIMAL(20, 4), doc="融券卖出量(股,份,手)")
    S_MARSUM_SECLENDINGBALANCE = Column(DECIMAL(20, 4), doc="融券余额(元)")
    S_MARSUM_SECURITIES_REPAY = Column(DECIMAL(20, 4), doc="融券偿还额(元)")
    S_MARSUM_SECURITIES_SALES = Column(DECIMAL(20, 4), doc="融券卖出额(元)")
    S_MARSUM_TRADINGBALANCE = Column(DECIMAL(20, 4), doc="融资余额(元)")
    S_MARSUM_TURNOVER_AMOUNT = Column(DECIMAL(20, 4), doc="A股成交金额(万元)")
    TRADE_DT = Column(String(8), doc="日期")


class ASHAREMECHANISMOWNERSHIP(Base):

    __tablename__ = 'ASHAREMECHANISMOWNERSHIP'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_ENDDATE = Column(String(10), doc="报告期")
    S_HOLDER_PCT = Column(DECIMAL(20, 4), doc="持股比例")
    S_INFO_COMP_NAME = Column(String(100), doc="股东公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="股东公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="股东公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREMERGERSUBJECT(Base):

    __tablename__ = 'ASHAREMERGERSUBJECT'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMP_NAME = Column(String(100), doc="并购公司名称")
    S_INFO_COMP_NAME1 = Column(String(100), doc="并购目标公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="并购公司中文简称")
    S_INFO_COMP_SNAME1 = Column(String(40), doc="并购目标公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="并购公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_PROGRESS = Column(String(300), doc="方案进度")
    S_MEETEVENT_ID = Column(String(20), doc="事件ID")
    S_UPDATE_DATE = Column(String(8), doc="最新披露日期")


class ASHAREMJRHOLDERTRADE(Base):

    __tablename__ = 'ASHAREMJRHOLDERTRADE'

    ANN_DT = Column(String(8), doc="公告日期")
    AVG_PRICE = Column(DECIMAL(20, 4), doc="平均价格")
    BLOCKTRADE_QUANTITY = Column(DECIMAL(20, 4), doc="通过大宗交易系统的变动数量")
    HOLDER_NAME = Column(String(200), doc="持有人")
    HOLDER_QUANTITY_NEW = Column(DECIMAL(20, 4), doc="最新持有流通数量")
    HOLDER_QUANTITY_NEW_RATIO = Column(DECIMAL(20, 4), doc="最新持有流通数量占流通量比例(%)")
    HOLDER_TYPE = Column(String(1), doc="持有人类型")
    IS_REANNOUNCED = Column(DECIMAL(1, 0), doc="是否重复披露")
    IS_RESTRICTED = Column(DECIMAL(1, 0), doc="是否为减持限售股份")
    NEW_HOLD_TOT = Column(DECIMAL(20, 4), doc="最新持股总数")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DETAIL = Column(String(1000), doc="变动说明")
    TRANSACT_ENDDATE = Column(String(8), doc="变动截至日期")
    TRANSACT_QUANTITY = Column(DECIMAL(20, 4), doc="变动数量")
    TRANSACT_QUANTITY_RATIO = Column(DECIMAL(20, 4), doc="变动数量占流通量比例(%)")
    TRANSACT_STARTDATE = Column(String(8), doc="变动起始日期")
    TRANSACT_TYPE = Column(String(4), doc="买卖方向")
    WHETHER_AGREED_REPUR_TRANS = Column(DECIMAL(1, 0), doc="是否约定购回式交易")


class ASHAREPEVCINVESTMENT(Base):

    __tablename__ = 'ASHAREPEVCINVESTMENT'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_DATE = Column(String(8), doc="融资时间")
    S_HOLDER_PCT = Column(DECIMAL(12, 4), doc="股权比例")
    S_INFO_COMP_NAME = Column(String(100), doc="股东公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="股东公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="股东公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREPLAINTIFF(Base):

    __tablename__ = 'ASHAREPLAINTIFF'

    ANN_DATE = Column(String(8), doc="公告日期")
    LITIGATION_EVENTS_ID = Column(String(40), doc="诉讼事件ID")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CASE_TYPE = Column(String(10), doc="案件类型")
    S_INFO_COMP_NAME = Column(String(100), doc="诉讼公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="诉讼公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="诉讼公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHAREPLEDGEPROPORTION(Base):

    __tablename__ = 'ASHAREPLEDGEPROPORTION'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_ENDDATE = Column(String(8), doc="截止日期")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PLEDGE_NUM = Column(DECIMAL(20, 0), doc="质押笔数")
    S_PLEDGE_RATIO = Column(DECIMAL(20, 4), doc="质押比例")
    S_SHARE_RESTRICTED_NUM = Column(DECIMAL(20, 4), doc="有限售股份质押数量")
    S_SHARE_UNRESTRICTED_NUM = Column(DECIMAL(20, 4), doc="无限售股份质押数量")
    S_TOT_SHR = Column(DECIMAL(20, 4), doc="A股总股本")


class ASHAREPLEDGETRADE(Base):

    __tablename__ = 'ASHAREPLEDGETRADE'

    INITIAL_NUM = Column(DECIMAL(20, 4), doc="初始交易数量")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPURCHASE_ALLOWANCE = Column(DECIMAL(20, 4), doc="待购回余量")
    REPURCHASE_ALLOWANCE1 = Column(DECIMAL(20, 4), doc="待购回余量(无限售条件)")
    REPURCHASE_ALLOWANCE2 = Column(DECIMAL(20, 4), doc="待购回余量(有限售条件)")
    REPURCHASE_NUM = Column(DECIMAL(20, 4), doc="购回交易数量")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")


class ASHAREPREVIOUSENNAME(Base):

    __tablename__ = 'ASHAREPREVIOUSENNAME'

    CHANGE_DT = Column(String(8), doc="变动日期")
    CUR_SIGN = Column(DECIMAL(1, 0), doc="是否最新")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_ENAME = Column(String(100), doc="英文简称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(10), doc="证券id")


class ASHAREPRODUCT(Base):

    __tablename__ = 'ASHAREPRODUCT'

    FREQUENCY_CODE = Column(DECIMAL(9, 0), doc="频率代码")
    NUMBER_TYPECODE = Column(DECIMAL(9, 0), doc="数量类型代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_ENDDATE = Column(String(8), doc="截止日期")
    S_INFO_COMP_NAME = Column(String(100), doc="公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_PRODUCT_NAME = Column(String(100), doc="产品名称")
    S_PRODUCT_NUMBER = Column(DECIMAL(20, 4), doc="数量")


class ASHAREPROFITEXPRESS(Base):

    __tablename__ = 'ASHAREPROFITEXPRESS'

    ACTUAL_ANN_DT = Column(String(8), doc="[内部]实际公告日期")
    ANN_DT = Column(String(8), doc="公告日期")
    BRIEF_PERFORMANCE = Column(String(2000), doc="业绩简要说明")
    EPS_DILUTED = Column(DECIMAL(20, 4), doc="每股收益-基本(元)")
    GROWTH_BPS_SH = Column(DECIMAL(20, 4), doc="比年初增长率:归属于母公司股东的每股净资产")
    LAST_YEAR_EPS_DILUTED = Column(DECIMAL(20, 4), doc="去年同期每股收益")
    LAST_YEAR_NET_PROFIT_EXCL_INC = Column(DECIMAL(20, 4), doc="去年同期净利润")
    LAST_YEAR_OPER_PROFIT = Column(DECIMAL(20, 4), doc="去年同期营业利润")
    LAST_YEAR_OPER_REV = Column(DECIMAL(20, 4), doc="去年同期营业收入")
    LAST_YEAR_TOT_PROFIT = Column(DECIMAL(20, 4), doc="去年同期利润总额")
    MEMO = Column(String(400), doc="备注")
    NET_PROFIT_EXCL_MIN_INT_INC = Column(DECIMAL(20, 4), doc="净利润(元)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPER_PROFIT = Column(DECIMAL(20, 4), doc="营业利润(元)")
    OPER_REV = Column(DECIMAL(20, 4), doc="营业收入(元)")
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    ROE_DILUTED = Column(DECIMAL(20, 4), doc="净资产收益率-加权(%)")
    S_EARLY_BPS = Column(DECIMAL(20, 4), doc="期初每股净资产")
    S_EARLY_NET_ASSETS = Column(DECIMAL(20, 4), doc="期初净资产")
    S_FA_BPS = Column(DECIMAL(20, 4), doc="每股净资产")
    S_FA_GROWTH_ASSETS = Column(DECIMAL(20, 4), doc="比年初增长率:总资产")
    S_FA_ROE_YEARLY = Column(DECIMAL(20, 4), doc="同比增减:加权平均净资产收益率")
    S_FA_YOYEBT = Column(DECIMAL(20, 4), doc="同比增长率:利润总额")
    S_FA_YOYEPS_BASIC = Column(DECIMAL(20, 4), doc="同比增长率:基本每股收益")
    S_FA_YOYEQUITY = Column(DECIMAL(20, 4), doc="比年初增长率:归属母公司的股东权益")
    S_FA_YOYNETPROFIT_DEDUCTED = Column(DECIMAL(20, 4), doc="同比增长率:归属母公司股东的净利润")
    S_FA_YOYOP = Column(DECIMAL(20, 4), doc="同比增长率:营业利润")
    S_FA_YOYSALES = Column(DECIMAL(20, 4), doc="同比增长率:营业收入")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_ISAUDIT = Column(DECIMAL(5, 0), doc="是否审计")
    TOT_ASSETS = Column(DECIMAL(20, 4), doc="总资产(元)")
    TOT_PROFIT = Column(DECIMAL(20, 4), doc="利润总额(元)")
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(DECIMAL(20, 4), doc="股东权益合计(不含少数股东权益)(元)")
    YOYNET_PROFIT_EXCL_MIN_INT_INC = Column(DECIMAL(20, 4), doc="去年同期修正后净利润")


class ASHAREPROFITNOTICE(Base):

    __tablename__ = 'ASHAREPROFITNOTICE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(40), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_PROFITNOTICE_ABSTRACT = Column(String(200), doc="业绩预告摘要")
    S_PROFITNOTICE_CHANGEMAX = Column(DECIMAL(20, 4), doc="预告净利润变动幅度上限（%）")
    S_PROFITNOTICE_CHANGEMIN = Column(DECIMAL(20, 4), doc="预告净利润变动幅度下限（%）")
    S_PROFITNOTICE_DATE = Column(String(8), doc="公告日期")
    S_PROFITNOTICE_FIRSTANNDATE = Column(String(8), doc="首次公告日")
    S_PROFITNOTICE_NET_PARENT_FIRM = Column(DECIMAL(20, 4), doc="上年同期归母净利润")
    S_PROFITNOTICE_NETPROFITMAX = Column(DECIMAL(20, 4), doc="预告净利润上限（万元）")
    S_PROFITNOTICE_NETPROFITMIN = Column(DECIMAL(20, 4), doc="预告净利润下限（万元）")
    S_PROFITNOTICE_NUMBER = Column(DECIMAL(15, 4), doc="公布次数")
    S_PROFITNOTICE_PERIOD = Column(String(8), doc="报告期")
    S_PROFITNOTICE_REASON = Column(String(2000), doc="业绩变动原因")
    S_PROFITNOTICE_SIGNCHANGE = Column(String(10), doc="是否变脸")
    S_PROFITNOTICE_STYLE = Column(DECIMAL(9, 0), doc="业绩预告类型代码")


class ASHAREPROSECUTION(Base):

    __tablename__ = 'ASHAREPROSECUTION'

    ACCUSER = Column(String(3000), doc="原告方")
    AMOUNT = Column(DECIMAL(20, 4), doc="涉案金额")
    ANN_DT = Column(String(8), doc="公告日期")
    APPELLANT = Column(String(1), doc="二审上诉方(是否原告)")
    BRIEFRESULT = Column(String(100), doc="诉讼结果")
    COURT = Column(String(200), doc="一审受理法院")
    COURT2 = Column(String(200), doc="二审受理法院")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    DEFENDANT = Column(String(3000), doc="被告方")
    EXECUTION = Column(LONGTEXT, doc="执行情况")
    INTRODUCTION = Column(LONGTEXT, doc="案件描述")
    IS_APPEAL = Column(DECIMAL(5, 0), doc="是否上诉")
    JUDGE_DT = Column(String(8), doc="判决日期")
    JUDGE_DT2 = Column(String(8), doc="二审判决日期")
    LITIGATION_EVENTS_ID = Column(String(40), doc="诉讼事件ID")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRO_TYPE = Column(String(10), doc="诉讼类型")
    PROSECUTE_DT = Column(String(8), doc="起诉日期")
    RESULT = Column(LONGTEXT, doc="判决内容")
    RESULT2 = Column(String(2000), doc="二审判决内容")
    RESULTAMOUNT = Column(DECIMAL(20, 4), doc="判决金额")
    S_INFO_COMPCODE = Column(String(40), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TITLE = Column(String(40), doc="案件名称")


class ASHARERECEIVABLES(Base):

    __tablename__ = 'ASHARERECEIVABLES'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PERIOD = Column(String(50), doc="拖欠时间")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="下游公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="下游公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="下游公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_DISCLOSER = Column(String(100), doc="披露公司ID")


class ASHAREREGINV(Base):

    __tablename__ = 'ASHAREREGINV'

    COMP_ID = Column(String(10), doc="公司ID")
    END_ANNDATE = Column(String(8), doc="结束公告日期")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(10), doc="证券id")
    STR_ANNDATE = Column(String(8), doc="开始公告日期")
    STR_DATE = Column(String(8), doc="开始日期")
    SUR_INSTITUTE = Column(String(100), doc="调查机构")
    SUR_REASONS = Column(String(500), doc="调查原因")


class ASHARERELATEDPARTYDEBT(Base):

    __tablename__ = 'ASHARERELATEDPARTYDEBT'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="债权公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="债权公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="债权公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")


class ASHARERIGHTISSUE(Base):

    __tablename__ = 'ASHARERIGHTISSUE'

    ANN_DT = Column(String(8), doc="最新公告日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_ALLOTMENT_OBJECT = Column(String(40), doc="配股对象")
    S_CIRCULATED_SHARE_NUM = Column(DECIMAL(20, 4), doc="已流通股理论配股数量(万股)")
    S_CIRCULATED_SHARE_NUM1 = Column(DECIMAL(20, 4), doc="已流通股实际配股数量(万股)")
    S_EMPLOYEE_STOCK_SHARE_NUM = Column(DECIMAL(20, 4), doc="职工股理论配股数量(万股)")
    S_EMPLOYEE_STOCK_SHARE_NUM1 = Column(DECIMAL(20, 4), doc="职工股实际配股数量(万股)")
    S_EXPECTED_FUND_RAISING = Column(DECIMAL(20, 4), doc="预计募集资金(元)")
    S_HOLDER_HELD_NUMBER = Column(DECIMAL(20, 4), doc="持股5%以上大股东持股数量(万股)")
    S_HOLDER_SUBSCRIPTION_METHOD = Column(String(100), doc="持股5%以上大股东认购方式(万股)")
    S_HOLDER_SUBSCRIPTION_NUMBER = Column(DECIMAL(20, 4), doc="持股5%以上大股东认购股数量(万股)")
    S_HOLDER_SUBSCRIPTION_NUMBER1 = Column(DECIMAL(20, 4), doc="持股5%以上的大股东理论认购股数量(万股)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_LEGAL_PERSON_SHARE_NUM = Column(DECIMAL(20, 4), doc="法人股理论配股数量(万股)")
    S_LEGAL_PERSON_SHARE_NUM1 = Column(DECIMAL(20, 4), doc="法人股实际配股数量(万股)")
    S_LOWER_PRICE_LIMIT = Column(DECIMAL(20, 4), doc="配股预案价下限")
    S_PRICE_CAP = Column(DECIMAL(20, 4), doc="配股预案价上限")
    S_RATIO_DENOMINATOR = Column(DECIMAL(20, 4), doc="配股比例分母")
    S_RATIO_MOLECULAR = Column(DECIMAL(20, 4), doc="配股比例分子")
    S_RIGHTSISSUE_AMOUNT = Column(DECIMAL(20, 4), doc="配股计划数量(万股)")
    S_RIGHTSISSUE_AMOUNTACT = Column(DECIMAL(20, 4), doc="配股实际数量(万股)")
    S_RIGHTSISSUE_ANNCEDATE = Column(String(8), doc="配股实施公告日")
    S_RIGHTSISSUE_APPROVEDDATE = Column(String(8), doc="证监会核准公告日")
    S_RIGHTSISSUE_CODE = Column(String(10), doc="配售代码")
    S_RIGHTSISSUE_CONTENT = Column(String(150), doc="配股说明")
    S_RIGHTSISSUE_COST = Column(DECIMAL(20, 4), doc="配售费用")
    S_RIGHTSISSUE_EXDIVIDENDDATE = Column(String(8), doc="除权日")
    S_RIGHTSISSUE_GUARANTOR = Column(String(8), doc="基准年度")
    S_RIGHTSISSUE_GUARTYPE = Column(DECIMAL(20, 4), doc="基准股本(万股)")
    S_RIGHTSISSUE_LISTANNDATE = Column(String(8), doc="上市公告日")
    S_RIGHTSISSUE_LISTEDDATE = Column(String(8), doc="配股上市日")
    S_RIGHTSISSUE_NAME = Column(String(40), doc="配股简称")
    S_RIGHTSISSUE_NETCOLLECTION = Column(DECIMAL(20, 4), doc="募集资金(元)")
    S_RIGHTSISSUE_PASSDATE = Column(String(8), doc="发审委通过公告日")
    S_RIGHTSISSUE_PAYENDDATE = Column(String(8), doc="缴款终止日")
    S_RIGHTSISSUE_PAYSTARTDATE = Column(String(8), doc="缴款起始日")
    S_RIGHTSISSUE_PREPLANDATE = Column(String(8), doc="预案公告日")
    S_RIGHTSISSUE_PRICE = Column(DECIMAL(20, 4), doc="配股价格(元)")
    S_RIGHTSISSUE_PROGRESS = Column(String(10), doc="方案进度")
    S_RIGHTSISSUE_RATIO = Column(DECIMAL(20, 4), doc="配股比例")
    S_RIGHTSISSUE_REGDATE_BSHARE = Column(String(8), doc="B股股权登记日")
    S_RIGHTSISSUE_REGDATESHAREB = Column(String(8), doc="股权登记日")
    S_RIGHTSISSUE_RESULTDATE = Column(String(8), doc="配股结果公告日")
    S_RIGHTSISSUE_SMTGANNCEDATE = Column(String(8), doc="股东大会公告日")
    S_RIGHTSISSUE_YEAR = Column(String(8), doc="配股年度")
    S_STATE_OWNED_SHARE_NUM = Column(DECIMAL(20, 4), doc="国有股理论配股数量(万股)")
    S_STATE_OWNED_SHARE_NUM1 = Column(DECIMAL(20, 4), doc="国有股实际配股数量(万股)")
    S_SUBSCRIPTION_METHOD = Column(String(30), doc="认购方式")
    S_TRANSFER_SHARE_NUM = Column(DECIMAL(20, 4), doc="转配股理论配股数量(万股)")
    S_TRANSFER_SHARE_NUM1 = Column(DECIMAL(20, 4), doc="转配股实际配股数量(万股)")
    S_UNDERWRITER_SUBSCRIPTION = Column(DECIMAL(20, 4), doc="承销商余额认购数量(万股)")
    S_UNDERWRITING_METHOD = Column(String(20), doc="承销方式")


class ASHARESELLSUBJECT(Base):

    __tablename__ = 'ASHARESELLSUBJECT'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMP_NAME = Column(String(100), doc="并购公司名称")
    S_INFO_COMP_NAME1 = Column(String(100), doc="并购出售目标公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="并购公司中文简称")
    S_INFO_COMP_SNAME1 = Column(String(40), doc="并购出售目标公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="并购出售目标公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_PROGRESS = Column(String(300), doc="方案进度")
    S_MEETEVENT_ID = Column(String(20), doc="事件ID")
    S_UPDATE_DATE = Column(String(8), doc="最新披露日期")


class ASHAREST(Base):

    __tablename__ = 'ASHAREST'

    ANN_DT = Column(String(8), doc="公告日期")
    ENTRY_DT = Column(String(8), doc="实施日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REASON = Column(String(100), doc="实施原因")
    REMOVE_DT = Column(String(8), doc="撤销日期")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_TYPE_ST = Column(String(8), doc="特别处理类型")


class ASHARESTAFF(Base):

    __tablename__ = 'ASHARESTAFF'

    ANN_DT = Column(String(8), doc="公告日期")
    END_DT = Column(String(8), doc="截止日期")
    MEMO = Column(String(1000), doc="特殊情况说明")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(40), doc="公司id")
    S_INFO_TOTALEMPLOYEES = Column(DECIMAL(20, 4), doc="员工人数(人)")
    S_INFO_TOTALEMPLOYEES2 = Column(DECIMAL(20, 0), doc="母公司员工人数(人)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHARESTAFFSTRUCTURE(Base):

    __tablename__ = 'ASHARESTAFFSTRUCTURE'

    ANN_DT = Column(String(8), doc="公告日期")
    END_DT = Column(String(8), doc="截止日期")
    ITEM_CODE = Column(DECIMAL(9, 0), doc="项目代码")
    ITEM_NAME = Column(String(100), doc="项目")
    ITEM_TYPE_CODE = Column(DECIMAL(9, 0), doc="项目分类代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PROPORTION = Column(DECIMAL(20, 4), doc="所占比例")
    REPORT_TYPE_CODE = Column(DECIMAL(9, 0), doc="报告类型代码")
    S_INFO_COMPCODE = Column(String(40), doc="交易代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    STAFF_NUMBER = Column(DECIMAL(20, 0), doc="人数")
    STAFF_TYPE_CODE = Column(DECIMAL(9, 0), doc="人数类别代码")


class ASHARESTIBHOLDERVOTE(Base):

    __tablename__ = 'ASHARESTIBHOLDERVOTE'

    ANN_DATE = Column(String(8), doc="公告日期")
    DEADLINE = Column(String(8), doc="截止日期")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_HOLDER_CODE = Column(String(10), doc="股东ID")
    S_HOLDER_HOLDERCATEGORY = Column(String(1), doc="股东类型")
    S_HOLDER_LSTTYPECODE = Column(DECIMAL(9, 0), doc="股份类型")
    S_HOLDER_NAME = Column(String(100), doc="股东名称")
    S_HOLDER_QUANTITY = Column(DECIMAL(20, 4), doc="持股数量(股)")
    S_HOLDER_VOTING_NUMBER = Column(DECIMAL(20, 4), doc="表决权数量(票)")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")


class ASHARESTOCKRATING(Base):

    __tablename__ = 'ASHARESTOCKRATING'

    ANN_DT = Column(String(8), doc="公告日期(内部)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_EST_ESTNEWTIME_INST = Column(String(8), doc="评级日期")
    S_EST_HIGHPRICE_INST = Column(DECIMAL(20, 4), doc="本次最高目标价")
    S_EST_INSTITUTE = Column(String(100), doc="研究机构名称")
    S_EST_LOWPRICE_INST = Column(DECIMAL(20, 4), doc="本次最低目标价")
    S_EST_PREHIGHPRICE_INST = Column(DECIMAL(20, 4), doc="前次最高目标价")
    S_EST_PRELOWPRICE_INST = Column(DECIMAL(20, 4), doc="前次最低目标价")
    S_EST_PRERATING_INST = Column(String(20), doc="前次评级")
    S_EST_PRESCORERATING_INST = Column(DECIMAL(20, 4), doc="前次标准评级")
    S_EST_RATING_INST = Column(String(20), doc="本次评级")
    S_EST_RATINGANALYST = Column(String(100), doc="分析师名称")
    S_EST_RATINGANALYSTID = Column(String(200), doc="分析师id")
    S_EST_REPORT_TITLE = Column(String(400), doc="报告标题")
    S_EST_REPORT_TYPE = Column(DECIMAL(9, 0), doc="报告类别")
    S_EST_SCORERATING_INST = Column(DECIMAL(20, 4), doc="本次标准评级")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_RATING_CHANGE = Column(DECIMAL(9, 0), doc="评级变动方向")
    S_RATING_VALIDENDDT = Column(String(8), doc="评级有效截止日")


class ASHARESUPERVISOR(Base):

    __tablename__ = 'ASHARESUPERVISOR'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_MANAGER_NAME = Column(String(80), doc="姓名")
    S_INFO_MANAGER_POST = Column(String(40), doc="职务")
    S_INFO_MANAGER_STARTDATE = Column(String(8), doc="任职日期")
    S_INFO_MANID = Column(String(10), doc="人物id")


class ASHARESUPPLIER(Base):

    __tablename__ = 'ASHARESUPPLIER'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_AMOUNT = Column(DECIMAL(20, 4), doc="金额")
    S_INFO_COMP_NAME = Column(String(100), doc="上游公司名称")
    S_INFO_COMP_SNAME = Column(String(40), doc="上游公司中文简称")
    S_INFO_COMPCODE = Column(String(100), doc="公司ID")
    S_INFO_COMPCODE1 = Column(String(100), doc="上游公司ID")
    S_INFO_DIMENSION = Column(String(100), doc="维度")
    S_INFO_DIMENSION1 = Column(String(100), doc="子维度")
    S_INFO_DISCLOSER = Column(String(100), doc="披露公司ID")


class ASHARETRADINGSUSPENSION(Base):

    __tablename__ = 'ASHARETRADINGSUSPENSION'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_CHANGEREASON = Column(String(400), doc="停牌原因")
    S_DQ_CHANGEREASONTYPE = Column(DECIMAL(9, 0), doc="停牌原因代码")
    S_DQ_RESUMPDATE = Column(String(8), doc="复牌日期")
    S_DQ_SUSPENDDATE = Column(String(8), doc="停牌日期")
    S_DQ_SUSPENDTYPE = Column(DECIMAL(9, 0), doc="停牌类型代码")
    S_DQ_TIME = Column(String(200), doc="停复牌时间")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class ASHARETYPECODE(Base):

    __tablename__ = 'ASHARETYPECODE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CLASSIFICATION = Column(String(100), doc="分类")
    S_ORIGIN_TYPCODE = Column(String(40), doc="原始类型代码")
    S_TYPCODE = Column(String(40), doc="类型代码")
    S_TYPNAME = Column(String(300), doc="类型名称")


class CFUNDBANKACCOUNT(Base):

    __tablename__ = 'CFUNDBANKACCOUNT'

    ACCOUNT_NAME = Column(String(100), doc="账户名称")
    BANK_ACCOUNT = Column(String(50), doc="银行账号")
    BANK_NUMBER = Column(String(30), doc="开户行编号")
    COMP_ID = Column(String(10), doc="公司ID")
    COMP_NAME = Column(String(100), doc="公司名称")
    EXCHANGE_NUMBER = Column(String(30), doc="交换行号")
    IS_EFFECTIVE = Column(DECIMAL(1, 0), doc="是否有效")
    LINE_NUMBER = Column(String(30), doc="联行行号")
    LINE_PAYMENT_SYSTEM = Column(String(30), doc="人行支付系统行号")
    NAME_BANK_ACCOUNT = Column(String(100), doc="开户银行名称")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    UPDATE1 = Column(String(8), doc="更新日期")


class CFUNDCHANGEWINDCODE(Base):

    __tablename__ = 'CFUNDCHANGEWINDCODE'

    CHANGE_DATE = Column(String(10), doc="代码变更日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_NEWWINDCODE = Column(String(40), doc="变更后代码")
    S_INFO_OLDWINDCODE = Column(String(40), doc="变更前代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CFUNDCODEANDSNAME(Base):

    __tablename__ = 'CFUNDCODEANDSNAME'

    IS_COMMON = Column(DECIMAL(1, 0), doc="是否通用代码")
    MEMO = Column(String(800), doc="业务说明")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CODE = Column(String(40), doc="业务代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_SNAME = Column(String(100), doc="业务简称")
    SEC_ID = Column(String(40), doc="品种ID")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="业务代码类型")


class CFUNDCOMPANYPREVIOUSNAME(Base):

    __tablename__ = 'CFUNDCOMPANYPREVIOUSNAME'

    ANN_DT = Column(String(8), doc="公告日期")
    CHANGE_DT = Column(String(8), doc="变动日期")
    CHANGE_REASON = Column(String(100), doc="更名原因")
    COMP_NAME = Column(String(200), doc="公司名称")
    COMP_NAME_ENG = Column(String(200), doc="公司英文名称")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")


class CFUNDFACTIONALSTYLE(Base):

    __tablename__ = 'CFUNDFACTIONALSTYLE'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    ENTRY_DT = Column(String(8), doc="纳入日期")
    MEMO = Column(String(500), doc="[内部]备注")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REMOVE_DT = Column(String(8), doc="剔除日期")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    SEC_IND_CODE = Column(String(20), doc="所属板块代码")


class CFUNDHOLDRESTRICTEDCIRCULATION(Base):

    __tablename__ = 'CFUNDHOLDRESTRICTEDCIRCULATION'

    BOOK_VALUE_NET_WORTH = Column(DECIMAL(20, 4), doc="账面价值占净值比例(%)")
    CIRCULATION_DATE = Column(String(8), doc="可流通日期")
    COST_TO_NET_WORTH = Column(DECIMAL(20, 4), doc="成本占净值比例(%)")
    ENDDATE = Column(String(8), doc="截止日期")
    F_INFO_RESTRICTEDCODE = Column(String(20))
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    INVESTMENT_AMOUNT = Column(DECIMAL(20, 4), doc="投资金额(成本)(元)")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PLACING_DATE = Column(String(8), doc="配售日期")
    PLACING_METHOD = Column(String(40), doc="配售方式")
    PLACING_QUANTITY = Column(DECIMAL(20, 4), doc="配售(持有)数量(股/张)")
    RESTRICTED_TYPE = Column(String(20), doc="流通受限类型")
    YEAR_END_VALUATION = Column(DECIMAL(20, 4), doc="年末估值/市价(账面价值)(元)")


class CFUNDINDEXMEMBERS(Base):

    __tablename__ = 'CFUNDINDEXMEMBERS'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_INDATE = Column(String(8), doc="纳入日期")
    S_CON_OUTDATE = Column(String(8), doc="剔除日期")
    S_CON_WINDCODE = Column(String(40), doc="成份股Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")


class CFUNDINDEXTABLE(Base):

    __tablename__ = 'CFUNDINDEXTABLE'

    F_CON_WINDCODE = Column(String(40), doc="指数Wind代码")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_TRACKDEV = Column(DECIMAL(20, 4), doc="日均跟踪偏离度阀值")
    F_TRACKINGERROR = Column(DECIMAL(20, 4), doc="年化跟踪误差阀值")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))


class CFUNDINDUSTRIESCODE(Base):

    __tablename__ = 'CFUNDINDUSTRIESCODE'

    CHINESEDEFINITION = Column(String(600), doc="板块中文定义")
    INDUSTRIESALIAS = Column(String(12), doc="板块别名")
    INDUSTRIESCODE = Column(String(38), doc="板块代码")
    INDUSTRIESNAME = Column(String(50), doc="板块名称")
    LEVELNUM = Column(DECIMAL(1, 0), doc="级数")
    MEMO = Column(String(100), doc="[内部]备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    SEQUENCE1 = Column(DECIMAL(4, 0), doc="展示序号")
    USED = Column(DECIMAL(1, 0), doc="是否使用")


class CFUNDINTRODUCTION(Base):

    __tablename__ = 'CFUNDINTRODUCTION'

    ADDRESS = Column(String(200), doc="注册地址")
    BRIEFING = Column(String(2000), doc="公司简介")
    BUSINESSSCOPE = Column(String(2000), doc="经营范围")
    CHAIRMAN = Column(String(100), doc="法人代表")
    CITY = Column(String(50), doc="城市")
    COMP_ID = Column(String(40), doc="公司ID")
    COMP_NAME = Column(String(100), doc="公司名称")
    COMP_NAME_ENG = Column(String(100), doc="英文名称")
    COMP_PROPERTY = Column(String(100), doc="企业性质")
    COMP_SNAME = Column(String(40), doc="公司中文简称")
    COMP_SNAMEENG = Column(String(100), doc="英文名称缩写")
    COMP_TYPE = Column(String(100), doc="公司类型")
    COMPANY_TYPE = Column(String(10), doc="公司类别")
    COUNTRY = Column(String(20), doc="国籍")
    CURRENCYCODE = Column(String(10), doc="货币代码")
    DISCLOSER = Column(String(500), doc="信息披露人")
    EMAIL = Column(String(80), doc="电子邮件")
    ENDDATE = Column(String(8), doc="公司终止日期")
    FAX = Column(String(50), doc="传真")
    FOUNDDATE = Column(String(8), doc="成立日期")
    MAIN_BUSINESS = Column(String(1000), doc="主要产品及业务")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OFFICE = Column(String(200), doc="办公地址")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PHONE = Column(String(50), doc="电话")
    PRESIDENT = Column(String(100), doc="总经理")
    PROVINCE = Column(String(20), doc="省份")
    REGCAPITAL = Column(DECIMAL(20, 4), doc="注册资本")
    REGISTERNUMBER = Column(String(20), doc="统一社会信用代码")
    S_INFO_ORG_CODE = Column(String(30), doc="组织机构代码")
    S_INFO_TOTALEMPLOYEES = Column(DECIMAL(20, 0), doc="员工总数(人)")
    SOCIAL_CREDIT_CODE = Column(String(30), doc="统一社会信用编码")
    WEBSITE = Column(String(80), doc="公司网址")
    ZIPCODE = Column(String(10), doc="邮编")


class CFUNDMANAGEMENT(Base):

    __tablename__ = 'CFUNDMANAGEMENT'

    ANN_DATE = Column(String(8), doc="公告日期")
    MANID = Column(String(10), doc="人物ID")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(40), doc="公司id")
    S_INFO_MANAGER_BIRTHYEAR = Column(String(8), doc="出生日期")
    S_INFO_MANAGER_EDUCATION = Column(String(10), doc="学历")
    S_INFO_MANAGER_GENDER = Column(String(10), doc="性别代码")
    S_INFO_MANAGER_INTRODUCTION = Column(String(2000), doc="个人简历")
    S_INFO_MANAGER_LEAVEDATE = Column(String(8), doc="离职日期")
    S_INFO_MANAGER_NAME = Column(String(80), doc="姓名")
    S_INFO_MANAGER_NATIONALITY = Column(String(40), doc="国籍")
    S_INFO_MANAGER_POST = Column(String(40), doc="公布职务名称")
    S_INFO_MANAGER_STARTDATE = Column(String(8), doc="任职日期")
    S_INFO_MANAGER_TYPE = Column(String(20), doc="管理层类别")


class CFUNDPCHREDM(Base):

    __tablename__ = 'CFUNDPCHREDM'

    F_INFO_APPROVED_DATE = Column(String(8), doc="获批日期")
    F_INFO_FUNDMANAGEMENTCOMP = Column(DECIMAL(1, 0), doc="是否基金主体")
    F_INFO_INVSHARE = Column(DECIMAL(20, 4), doc="合同生效时管理人员工持有份额")
    F_INFO_INVTOTRTO = Column(DECIMAL(24, 6), doc="合同生效时管理人员工持有比例(%)")
    F_INFO_ISSUE_OBJECT = Column(DECIMAL(9, 0), doc="发行对象代码")
    F_INFO_ISSUEDATE = Column(String(8), doc="发行公告日")
    F_INFO_ISSUETYPE = Column(DECIMAL(9, 0), doc="发行方式代码")
    F_INFO_SETUPDATE = Column(String(8), doc="成立公告日")
    F_INFO_SUB_MODE = Column(DECIMAL(9, 0), doc="投资者认购方式代码")
    F_INFO_SUSPCHDAY = Column(DECIMAL(20, 4), doc="申购确认天数")
    F_INFO_SUSPCHDAY1 = Column(DECIMAL(20, 4), doc="申购确认查询天数")
    F_INFO_SUSREDMDAY1 = Column(DECIMAL(20, 4), doc="赎回交收天数")
    F_INFO_SUSREDMDAY2 = Column(DECIMAL(20, 4), doc="赎回确认天数")
    F_INFO_SUSREDMDAY3 = Column(DECIMAL(20, 4), doc="实际赎回交收天数")
    F_INFO_SUSREDMDAY4 = Column(DECIMAL(20, 4), doc="赎回确认查询天数")
    F_INFO_TDSETMTYPECODE = Column(DECIMAL(9, 0), doc="交易结算模式代码")
    F_INFO_TRADE = Column(DECIMAL(1, 0), doc="是否交易")
    F_INFO_TYPECODE = Column(DECIMAL(9, 0), doc="产品异常状态代码")
    F_INFO_VALMETCODE = Column(DECIMAL(9, 0), doc="估值方法代码")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))


class CFUNDPORTFOLIOCHANGES(Base):

    __tablename__ = 'CFUNDPORTFOLIOCHANGES'

    ACCUMULATED_AMOUNT = Column(DECIMAL(20, 4), doc="累计金额")
    ANN_DT = Column(String(8), doc="公告日期")
    BEGIN_NET_ASSET_RATIO = Column(DECIMAL(20, 4), doc="占期初基金资产净值比例")
    CHANGE_TYPE = Column(String(10), doc="变动类型")
    F_INFO_WINDCODE = Column(String(40), doc="基金代码")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REPORT_PERIOD = Column(String(8), doc="报告期")
    S_INFO_WINDCODE = Column(String(40), doc="股票代码")


class CFUNDPREVIOUSNAME(Base):

    __tablename__ = 'CFUNDPREVIOUSNAME'

    ANN_DT = Column(String(8), doc="公告日期")
    BEGINDATE = Column(String(8), doc="起始日期")
    CHANGEREASON = Column(DECIMAL(9, 0), doc="变动原因代码")
    ENDDATE = Column(String(8), doc="截至日期")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_NAME = Column(String(40), doc="证券简称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CFUNDRALATEDSECURITIESCODE(Base):

    __tablename__ = 'CFUNDRALATEDSECURITIESCODE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_EFFECTIVE_DT = Column(String(8), doc="生效日期")
    S_INFO_INVALID_DT = Column(String(8), doc="失效日期")
    S_INFO_RALATEDCODE = Column(String(40), doc="关联证券Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_RELATION_TYPCODE = Column(DECIMAL(9, 0), doc="关系类型代码")


class CFUNDRATESENSITIVE(Base):

    __tablename__ = 'CFUNDRATESENSITIVE'

    CHANGE_AMOUNT = Column(DECIMAL(20, 4), doc="基金资产净值相对变动额")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICE_FLUNCUATION = Column(DECIMAL(20, 4), doc="价格变动")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="敏感分析价格类型代码")


class CFUNDSTYLECOEFFICIENT(Base):

    __tablename__ = 'CFUNDSTYLECOEFFICIENT'

    AVG_MARKET_VALUE = Column(DECIMAL(20, 4), doc="1年日均市值(万元)")
    DATE_CLOSING_DATE = Column(String(8), doc="引用数据的截止日期")
    GROSS_OPER_NETPROFIT = Column(DECIMAL(20, 4), doc="净利润增长率(%)")
    GROSS_OPER_REV = Column(DECIMAL(20, 4), doc="营业收入增长率(%)")
    GROWTH_Z = Column(DECIMAL(20, 4), doc="成长性Z分值")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CHANGE_DATE = Column(String(8), doc="变动日期")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    STYLE_COEFFICIENT = Column(DECIMAL(20, 4), doc="风格系数")
    VALUE_COEFFICIENT = Column(DECIMAL(20, 4), doc="调整市值系数")
    VALUE_Z = Column(DECIMAL(20, 4), doc="价值因子Z分值(ZVP)")


class CFUNDSTYLETHRESHOLD(Base):

    __tablename__ = 'CFUNDSTYLETHRESHOLD'

    DATE_CLOSING_DATE = Column(String(8), doc="引用数据的截止日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CHANGE_DATE = Column(String(8), doc="变动日期")
    THRESHOLD_GROWTH_STOCK = Column(DECIMAL(20, 4), doc="成长型门限值")
    THRESHOLD_LARGE_STOCK = Column(DECIMAL(20, 4), doc="大盘股门限值(万元)")
    THRESHOLD_MID_STOCK = Column(DECIMAL(20, 4), doc="中盘股门限值(万元)")
    THRESHOLD_VALUE_STOCK = Column(DECIMAL(20, 4), doc="价值型门限值")


class CFUNDTACODE(Base):

    __tablename__ = 'CFUNDTACODE'

    COMP_ID = Column(String(10), doc="品种ID")
    COMP_TYPE_CODE = Column(DECIMAL(9, 0), doc="主体类别代码")
    IS_COMMON = Column(DECIMAL(1, 0), doc="是否通用代码")
    MEMO = Column(String(800), doc="业务说明")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CODE = Column(String(40), doc="业务代码")
    S_SNAME = Column(String(100), doc="业务简称")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="业务代码类型")


class CFUNDTYPECODE(Base):

    __tablename__ = 'CFUNDTYPECODE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CLASSIFICATION = Column(String(100), doc="分类")
    S_ORIGIN_TYPCODE = Column(DECIMAL(9, 0), doc="类型代码")
    S_TYPCODE = Column(String(40), doc="类型代码")
    S_TYPNAME = Column(String(300), doc="类型名称")


class CFUNDWINDCUSTOMCODE(Base):

    __tablename__ = 'CFUNDWINDCUSTOMCODE'

    CRNCY_CODE = Column(String(10), doc="交易币种")
    CRNCY_NAME = Column(String(40), doc="交易币种")
    EXCHMARKET = Column(String(40), doc="交易所英文简称")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_ASHARECODE = Column(String(10), doc="证券id")
    S_INFO_CODE = Column(String(40), doc="交易代码")
    S_INFO_COMPCODE = Column(String(10), doc="公司id")
    S_INFO_COUNTRYCODE = Column(String(10), doc="国家及地区代码")
    S_INFO_COUNTRYNAME = Column(String(100), doc="国家及地区代码")
    S_INFO_ENAME = Column(String(200), doc="[内部]证券英文简称")
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所英文简称")
    S_INFO_EXCHMARKETNAME = Column(String(40), doc="交易所名称(兼容)")
    S_INFO_ISINCODE = Column(String(40), doc="[内部]ISIN代码")
    S_INFO_LOT_SIZE = Column(DECIMAL(20, 4), doc="每手数量")
    S_INFO_MIN_PRICE_CHG_UNIT = Column(DECIMAL(24, 8), doc="最小价格变动单位")
    S_INFO_NAME = Column(String(50), doc="证券中文简称")
    S_INFO_ORG_CODE = Column(String(20), doc="组织机构代码")
    S_INFO_SECTYPENAME = Column(String(40), doc="品种类型(兼容)")
    S_INFO_SECURITIESTYPES = Column(String(10), doc="品种类型(兼容)")
    S_INFO_TYPECODE = Column(DECIMAL(9, 0), doc="[内部]产品用分类代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SECURITY_STATUS = Column(DECIMAL(9, 0), doc="存续状态")


class CFUNDWINDINDEXCOMPONENT(Base):

    __tablename__ = 'CFUNDWINDINDEXCOMPONENT'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_CODE = Column(String(16), doc="成份板块代码")
    S_CON_NAME = Column(String(100), doc="成份板块名称")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")


class CFUNDWINDINDEXMEMBERS(Base):

    __tablename__ = 'CFUNDWINDINDEXMEMBERS'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CON_CODE = Column(String(16), doc="板块代码")
    S_CON_NAME = Column(String(100), doc="板块名称")
    S_INFO_WINDCODE = Column(String(40), doc="成份万得代码")


class CHANGEWINDCODE(Base):

    __tablename__ = 'CHANGEWINDCODE'

    CHANGE_DATE = Column(String(8), doc="Wind代码变更日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CHANGE_REASON = Column(DECIMAL(9, 0), doc="变更原因代码")
    S_INFO_NEWWINDCODE = Column(String(40), doc="变更后Wind代码")
    S_INFO_OLDWINDCODE = Column(String(40), doc="变更前Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CHINACLOSEDFUNDEODPRICE(Base):

    __tablename__ = 'CHINACLOSEDFUNDEODPRICE'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    DISCOUNT_RATE = Column(DECIMAL(20, 6), doc="贴水率（%）")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_ADJCLOSE = Column(DECIMAL(20, 4), doc="复权收盘价(元)")
    S_DQ_ADJFACTOR = Column(DECIMAL(20, 6), doc="复权因子")
    S_DQ_ADJHIGH = Column(DECIMAL(20, 4), doc="复权最高价(元)")
    S_DQ_ADJLOW = Column(DECIMAL(20, 4), doc="复权最低价(元)")
    S_DQ_ADJOPEN = Column(DECIMAL(20, 4), doc="复权开盘价(元)")
    S_DQ_ADJPRECLOSE = Column(DECIMAL(20, 4), doc="复权昨收盘价(元)")
    S_DQ_AMOUNT = Column(DECIMAL(20, 4), doc="成交金额(千元)")
    S_DQ_AVGPRICE = Column(DECIMAL(20, 4), doc="均价(VWAP)")
    S_DQ_CHANGE = Column(DECIMAL(20, 4), doc="涨跌(元)")
    S_DQ_CLOSE = Column(DECIMAL(20, 4), doc="收盘价(元)")
    S_DQ_HIGH = Column(DECIMAL(20, 4), doc="最高价(元)")
    S_DQ_LOW = Column(DECIMAL(20, 4), doc="最低价(元)")
    S_DQ_OPEN = Column(DECIMAL(20, 4), doc="开盘价(元)")
    S_DQ_PCTCHANGE = Column(DECIMAL(20, 4), doc="涨跌幅(%)")
    S_DQ_PRECLOSE = Column(DECIMAL(20, 4), doc="昨收盘价(元)")
    S_DQ_VOLUME = Column(DECIMAL(20, 4), doc="成交量(手)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")
    TRADES_COUNT = Column(DECIMAL(20, 4), doc="成交笔数")


class CHINAFEEDERFUND(Base):

    __tablename__ = 'CHINAFEEDERFUND'

    F_INFO_FEEDER_WINDCODE = Column(String(40), doc="联接基金Wind代码")
    F_INFO_WINDCODE = Column(String(40), doc="被联接基金Wind代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="被联接基金指数Wind代码")


class CHINAGRADINGFUND(Base):

    __tablename__ = 'CHINAGRADINGFUND'

    F_INFO_FEEDER_SHARERATIO = Column(DECIMAL(20, 4), doc="子基金份额占比")
    F_INFO_FEEDER_TYPECODE = Column(DECIMAL(9, 0), doc="子基金类型代码")
    F_INFO_FEEDER_WINDCODE = Column(String(40), doc="子基金Wind代码")
    F_INFO_PERIOD_IFDIV = Column(DECIMAL(1, 0), doc="运作期内是否分红")
    F_INFO_PREFER_FORMULA = Column(String(200), doc="优先份额约定年收益表达式")
    F_INFO_PREFER_IFADD = Column(DECIMAL(1, 0), doc="优先份额约定收益是否得到累计")
    F_INFO_PREFER_IFDIS = Column(DECIMAL(1, 0), doc="优先份额是否参与超额收益分配")
    F_INFO_TERM_IFTRANS = Column(DECIMAL(1, 0), doc="存续期内是否有份额配对转换")
    F_INFO_TERM_TYPECODE = Column(DECIMAL(9, 0), doc="存续期类型代码")
    F_INFO_TRANS_BGNDATE = Column(String(8), doc="份额配对转换起始日期")
    F_INFO_TRANS_ENDDATE = Column(String(8), doc="份额配对转换截止日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="母基金Wind代码")


class CHINAMFMPERFORMANCE(Base):

    __tablename__ = 'CHINAMFMPERFORMANCE'

    ANNRETURNES = Column(DECIMAL(20, 8), doc="履任以来年化回报")
    BESTTOTRETURN_6M = Column(DECIMAL(20, 8), doc="最高连续六月回报")
    FMINDEX_POINT = Column(DECIMAL(20, 8), doc="基金经理指数点位")
    FMINDEX_TYPE = Column(DECIMAL(9, 0), doc="基金经理指数类型")
    FUNDMANAGER_ID = Column(String(10), doc="基金经理ID")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RANKING_10Y = Column(String(20), doc="最近10年同类排名")
    RANKING_1M = Column(String(20), doc="最近1月同类排名")
    RANKING_1W = Column(String(20), doc="最近1周同类排名")
    RANKING_1Y = Column(String(20), doc="最近1年同类排名")
    RANKING_2Y = Column(String(20), doc="最近2年同类排名")
    RANKING_3M = Column(String(20), doc="最近3月同类排名")
    RANKING_3Y = Column(String(20), doc="最近3年同类排名")
    RANKING_5Y = Column(String(20), doc="最近5年同类排名")
    RANKING_6M = Column(String(20), doc="最近6月同类排名")
    RANKING_ES = Column(String(20), doc="履任以来同类排名")
    RANKING_YTD = Column(String(20), doc="今年以来同类排名")
    SUCBASERETURN_10Y = Column(DECIMAL(20, 8), doc="最近10年超越基准回报")
    SUCBASERETURN_1M = Column(DECIMAL(20, 8), doc="最近1月超越基准回报")
    SUCBASERETURN_1W = Column(DECIMAL(20, 8), doc="最近1周超越基准回报")
    SUCBASERETURN_1Y = Column(DECIMAL(20, 8), doc="最近1年超越基准回报")
    SUCBASERETURN_2Y = Column(DECIMAL(20, 8), doc="最近2年超越基准回报")
    SUCBASERETURN_3M = Column(DECIMAL(20, 8), doc="最近3月超越基准回报")
    SUCBASERETURN_3Y = Column(DECIMAL(20, 8), doc="最近3年超越基准回报")
    SUCBASERETURN_5Y = Column(DECIMAL(20, 8), doc="最近5年超越基准回报")
    SUCBASERETURN_6M = Column(DECIMAL(20, 8), doc="最近6月超越基准回报")
    SUCBASERETURN_ES = Column(DECIMAL(20, 8), doc="履任以来超越基准回报")
    SUCBASERETURN_YTD = Column(DECIMAL(20, 8), doc="今年以来超越基准回报")
    TOTRETURN_10Y = Column(DECIMAL(20, 8), doc="最近10年回报")
    TOTRETURN_1M = Column(DECIMAL(20, 8), doc="最近1月回报")
    TOTRETURN_1W = Column(DECIMAL(20, 8), doc="最近1周回报")
    TOTRETURN_1Y = Column(DECIMAL(20, 8), doc="最近1年回报")
    TOTRETURN_2Y = Column(DECIMAL(20, 8), doc="最近2年回报")
    TOTRETURN_3M = Column(DECIMAL(20, 8), doc="最近3月回报")
    TOTRETURN_3Y = Column(DECIMAL(20, 8), doc="最近3年回报")
    TOTRETURN_5Y = Column(DECIMAL(20, 8), doc="最近5年回报")
    TOTRETURN_6M = Column(DECIMAL(20, 8), doc="最近6月回报")
    TOTRETURN_ES = Column(DECIMAL(20, 8), doc="履任以来回报")
    TOTRETURN_YTD = Column(DECIMAL(20, 8), doc="今年以来回报")
    TRADE_DATE = Column(String(8), doc="日期")
    WORSTTOTRETURN_6M = Column(DECIMAL(20, 8), doc="最差连续六月回报")


class CHINAMFPERFORMANCE(Base):

    __tablename__ = 'CHINAMFPERFORMANCE'

    F_ALPHA_1Y = Column(DECIMAL(20, 8), doc="ALPHA(1年)")
    F_ALPHA_2Y = Column(DECIMAL(20, 8), doc="ALPHA(2年)")
    F_ALPHA_3Y = Column(DECIMAL(20, 8), doc="ALPHA(3年)")
    F_ALPHA_6M = Column(DECIMAL(20, 8), doc="ALPHA(6月)")
    F_ANNUALYEILD = Column(DECIMAL(20, 6), doc="年化收益率")
    F_ANNUALYEILD_SINCEFOUND = Column(DECIMAL(20, 6), doc="成立以来年化收益率")
    F_AVGRETURN_DAY = Column(DECIMAL(20, 6), doc="收益率(当天)")
    F_AVGRETURN_FIVEYEAR = Column(DECIMAL(20, 6), doc="收益率(五年)")
    F_AVGRETURN_FOURYEAR = Column(DECIMAL(20, 6), doc="收益率(四年)")
    F_AVGRETURN_HALFYEAR = Column(DECIMAL(20, 6), doc="收益率(六个月)")
    F_AVGRETURN_MONTH = Column(DECIMAL(20, 6), doc="收益率(一个月)")
    F_AVGRETURN_QUARTER = Column(DECIMAL(20, 6), doc="收益率(三个月)")
    F_AVGRETURN_SINCEFOUND = Column(DECIMAL(20, 6), doc="收益率(成立以来)")
    F_AVGRETURN_SIXYEAR = Column(DECIMAL(20, 6), doc="收益率(六年)")
    F_AVGRETURN_THISMONTH = Column(DECIMAL(20, 6), doc="收益率(本月以来)")
    F_AVGRETURN_THISQUARTER = Column(DECIMAL(20, 6), doc="收益率(本季以来)")
    F_AVGRETURN_THISWEEK = Column(DECIMAL(20, 6), doc="收益率(本周以来)")
    F_AVGRETURN_THISYEAR = Column(DECIMAL(20, 6), doc="收益率(本年以来)")
    F_AVGRETURN_THREEYEAR = Column(DECIMAL(20, 6), doc="收益率(三年)")
    F_AVGRETURN_TWOYEA = Column(DECIMAL(20, 6), doc="收益率(两年)")
    F_AVGRETURN_WEEK = Column(DECIMAL(20, 6), doc="收益率(一周)")
    F_AVGRETURN_YEAR = Column(DECIMAL(20, 6), doc="收益率(一年)")
    F_BETA_1Y = Column(DECIMAL(20, 8), doc="BETA(1年)")
    F_BETA_2Y = Column(DECIMAL(20, 8), doc="BETA(2年)")
    F_BETA_3Y = Column(DECIMAL(20, 8), doc="BETA(3年)")
    F_BETA_6M = Column(DECIMAL(20, 8), doc="BETA(6月)")
    F_FUNDTYPE = Column(String(50), doc="基金分类")
    F_SFANNUALYEILD = Column(DECIMAL(20, 6), doc="同类基金年化收益率")
    F_SFRANK_ANNUALYEILD = Column(DECIMAL(20, 0), doc="年化收益率同类排名")
    F_SFRANK_ANNUALYEILDT = Column(String(50), doc="年化收益率同类排名")
    F_SFRANK_DAY = Column(DECIMAL(20, 0), doc="当日同类收益率排名 ")
    F_SFRANK_DAYT = Column(String(50), doc="当日同类收益率排名")
    F_SFRANK_RECENTFIVEYEAR = Column(DECIMAL(20, 0), doc="最近五年同类排名")
    F_SFRANK_RECENTFIVEYEART = Column(String(50), doc="最近五年同类排名")
    F_SFRANK_RECENTHALFYEAR = Column(DECIMAL(20, 0), doc="最近六月同类排名")
    F_SFRANK_RECENTHALFYEART = Column(String(50), doc="最近六月同类排名")
    F_SFRANK_RECENTMONTH = Column(DECIMAL(20, 0), doc="最近一月同类排名")
    F_SFRANK_RECENTMONTHT = Column(String(50), doc="最近一月同类排名")
    F_SFRANK_RECENTQUARTER = Column(DECIMAL(20, 0), doc="最近三月同类排名")
    F_SFRANK_RECENTQUARTERT = Column(String(50), doc="最近三月同类排名")
    F_SFRANK_RECENTTHREEYEAR = Column(DECIMAL(20, 0), doc="最近三年同类排名")
    F_SFRANK_RECENTTHREEYEART = Column(String(50), doc="最近三年同类排名")
    F_SFRANK_RECENTTWOYEAR = Column(DECIMAL(20, 0), doc="最近两年同类排名")
    F_SFRANK_RECENTTWOYEART = Column(String(50), doc="最近两年同类排名")
    F_SFRANK_RECENTWEEK = Column(DECIMAL(20, 0), doc="最近一周同类排名")
    F_SFRANK_RECENTWEEKT = Column(String(50), doc="最近一周同类排名")
    F_SFRANK_RECENTYEAR = Column(DECIMAL(20, 0), doc="最近一年同类排名")
    F_SFRANK_RECENTYEART = Column(String(50), doc="最近一年同类排名")
    F_SFRANK_SINCEFOUND = Column(DECIMAL(20, 0), doc="成立以来同类排名(不建议使用)")
    F_SFRANK_SINCEFOUNDT = Column(String(50), doc="成立以来同类排名")
    F_SFRANK_THISYEAR = Column(DECIMAL(20, 0), doc="今年以来同类排名")
    F_SFRANK_THISYEART = Column(String(50), doc="今年以来同类排名")
    F_SFRETURN_DAY = Column(DECIMAL(20, 6), doc="当日同类收益率")
    F_SFRETURN_RECENTFIVEYEAR = Column(DECIMAL(20, 6), doc="最近五年同类基金收益率")
    F_SFRETURN_RECENTHALFYEAR = Column(DECIMAL(20, 6), doc="最近六月同类基金收益率")
    F_SFRETURN_RECENTMONTH = Column(DECIMAL(20, 6), doc="最近一月同类基金收益率")
    F_SFRETURN_RECENTQUARTER = Column(DECIMAL(20, 6), doc="最近三月同类基金收益率")
    F_SFRETURN_RECENTTHREEYEAR = Column(DECIMAL(20, 6), doc="最近三年同类基金收益率")
    F_SFRETURN_RECENTTWOYEAR = Column(DECIMAL(20, 6), doc="最近两年同类基金收益率")
    F_SFRETURN_RECENTWEEK = Column(DECIMAL(20, 6), doc="最近一周同类基金收益率")
    F_SFRETURN_RECENTYEAR = Column(DECIMAL(20, 6), doc="最近一年同类基金收益率")
    F_SFRETURN_SINCEFOUND = Column(DECIMAL(20, 6), doc="成立以来同类基金收益率")
    F_SFRETURN_THISYEAR = Column(DECIMAL(20, 6), doc="今年以来同类基金收益率")
    F_SHARPRATIO_HALFYEAR = Column(DECIMAL(20, 6), doc="夏普比率(六个月)")
    F_SHARPRATIO_THREEYEAR = Column(DECIMAL(20, 6), doc="夏普比率(三年)")
    F_SHARPRATIO_TWOYEAR = Column(DECIMAL(20, 6), doc="夏普比率(两年)")
    F_SHARPRATIO_YEAR = Column(DECIMAL(20, 6), doc="夏普比率(一年)")
    F_STDARDDEV_FIVEYEAR = Column(DECIMAL(20, 6), doc="标准差(五年)")
    F_STDARDDEV_HALFYEAR = Column(DECIMAL(20, 6), doc="标准差(六个月)")
    F_STDARDDEV_SINCEFOUND = Column(DECIMAL(20, 6), doc="标准差(成立以来)")
    F_STDARDDEV_THREEYEAR = Column(DECIMAL(20, 6), doc="标准差(三年)")
    F_STDARDDEV_TWOYEAR = Column(DECIMAL(20, 6), doc="标准差(两年)")
    F_STDARDDEV_YEAR = Column(DECIMAL(20, 6), doc="标准差(一年)")
    F_TRACKDEV_THISDAY = Column(DECIMAL(20, 6), doc="当天跟踪偏离度")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")


class CHINAMUTUALFUNDASSETPORTFOLIO(Base):

    __tablename__ = 'CHINAMUTUALFUNDASSETPORTFOLIO'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    F_ANN_DATE = Column(String(8), doc="公告日期")
    F_MMF_AVGPTM = Column(DECIMAL(20, 4), doc="投资组合平均剩余期限(天)")
    F_MMF_REPO = Column(DECIMAL(20, 4), doc="卖出回购证券(元)")
    F_MMF_REVERSEREPO = Column(DECIMAL(20, 4), doc="买入返售证券(元)")
    F_PRT_ABSVALUE = Column(DECIMAL(20, 4), doc="持有资产支持证券市值(元)")
    F_PRT_ABSVALUETONAV = Column(DECIMAL(20, 4), doc="持有资产支持证券占资产净值比例(%)")
    F_PRT_BDTONAV_NOGOV = Column(DECIMAL(20, 4), doc="持有债券市值(不含国债)占资产净值比例(%)")
    F_PRT_BDVALUE_NOGOV = Column(DECIMAL(20, 4), doc="持有债券市值(不含国债)(元)")
    F_PRT_BONDTONAV = Column(DECIMAL(20, 4), doc="持有债券市值总计占资产净值比例(%)")
    F_PRT_BONDTONAVCHANGE = Column(DECIMAL(20, 4), doc="持有债券比例较上期变化(%)")
    F_PRT_BONDTOTOT = Column(DECIMAL(20, 4), doc="持有债券市值占资产总值比例(%)")
    F_PRT_BONDVALUE = Column(DECIMAL(20, 4), doc="持有债券市值总计(元)")
    F_PRT_CASH = Column(DECIMAL(20, 4), doc="持有现金(元)")
    F_PRT_CASHTONAV = Column(DECIMAL(20, 4), doc="持有现金占资产净值比例(%)")
    F_PRT_CASHTONAVCHANGE = Column(DECIMAL(20, 4), doc="持有现金比例较上期变化(%)")
    F_PRT_CASHTOTOT = Column(DECIMAL(20, 4), doc="持有现金占资产总值比例(%)")
    F_PRT_CDS = Column(DECIMAL(20, 4), doc="持有同业存单市值(元)")
    F_PRT_CORPBOND = Column(DECIMAL(20, 4), doc="持有企债市值(元)")
    F_PRT_CORPBONDTONAV = Column(DECIMAL(20, 4), doc="持有企债市值占资产净值比例(%)")
    F_PRT_COVERTBOND = Column(DECIMAL(15, 2), doc="持有可转债市值(元)")
    F_PRT_COVERTBONDTONAV = Column(DECIMAL(20, 4), doc="持有可转债市值占资产净值比例(%)")
    F_PRT_CPVALUE = Column(DECIMAL(20, 4), doc="持有短期融资券市值(元)")
    F_PRT_CTRBANKBILL = Column(DECIMAL(20, 4), doc="持有央行票据市值(元)")
    F_PRT_CTRBANKBILLTONAV = Column(DECIMAL(20, 4), doc="持有央行票据市值占资产净值比例(%)")
    F_PRT_DEBCREBALANCE = Column(DECIMAL(20, 4), doc="借贷方差额(元)")
    F_PRT_ENDDATE = Column(String(8), doc="截止日期")
    F_PRT_FINANBOND = Column(DECIMAL(20, 4), doc="持有金融债市值(元)")
    F_PRT_FINANBONDTONAV = Column(DECIMAL(20, 4), doc="持有金融债市值占资产净值比例(%)")
    F_PRT_FUNDTONAV = Column(DECIMAL(20, 4), doc="持有基金市值占资产净值比例(%)")
    F_PRT_FUNDTOTOT = Column(DECIMAL(20, 4), doc="持有基金市值占资产总值比例(%)")
    F_PRT_FUNDVALUE = Column(DECIMAL(20, 4), doc="持有基金市值(元)")
    F_PRT_GOVBOND = Column(DECIMAL(20, 4), doc="持有国债市值(元)")
    F_PRT_GOVBONDTONAV = Column(DECIMAL(20, 4), doc="持有国债市值占资产净值比例(%)")
    F_PRT_GOVCASHTONAV = Column(DECIMAL(20, 4), doc="持有国债及现金占资产净值比例(%)")
    F_PRT_GOVCASHVALUE = Column(DECIMAL(20, 4), doc="持有国债及现金总值(元)")
    F_PRT_HKSTOCKTONAV = Column(DECIMAL(20, 4), doc="港股通投资港股市值占资产净值比")
    F_PRT_HKSTOCKVALUE = Column(DECIMAL(20, 4), doc="港股通投资港股市值")
    F_PRT_MMTONAV = Column(DECIMAL(20, 4), doc="持有货币市场工具市值占资产净值比例(%)")
    F_PRT_MMTOTOT = Column(DECIMAL(20, 4), doc="持有货币市场工具市值占资产总值比例(%)")
    F_PRT_MMVALUE = Column(DECIMAL(20, 4), doc="持有货币市场工具市值(元)")
    F_PRT_MTNVALUE = Column(DECIMAL(20, 4), doc="持有中期票据市值(元)")
    F_PRT_NETASSET = Column(DECIMAL(20, 4), doc="资产净值(元)")
    F_PRT_OTHER = Column(DECIMAL(20, 4), doc="持有其他资产(元)")
    F_PRT_OTHERTONAV = Column(DECIMAL(20, 4), doc="持有其他资产占资产净值比例(%)")
    F_PRT_OTHERTOTOT = Column(DECIMAL(20, 4), doc="持有其他资产占资产总值比例(%)")
    F_PRT_OTHERTOTOTCHANGE = Column(DECIMAL(20, 4), doc="持有其他资产比例较上期变化(%)")
    F_PRT_PASVSTKTONAV = Column(DECIMAL(20, 4), doc="指数投资持有股票市值占资产净值比例(%)")
    F_PRT_PASVSTKVALUE = Column(DECIMAL(15, 2), doc="指数投资持有股票市值(元)")
    F_PRT_POLIFINANBDTONAV = Column(DECIMAL(20, 4), doc="持有政策性金融债市值占资产净值比例(%)")
    F_PRT_POLIFINANBDVALUE = Column(DECIMAL(20, 4), doc="持有政策性金融债市值(元)")
    F_PRT_POSVSTKTONAV = Column(DECIMAL(20, 4), doc="积极投资持有股票市值占资产净值比例(%)")
    F_PRT_POSVSTKVALUE = Column(DECIMAL(20, 4), doc="积极投资持有股票市值(元)")
    F_PRT_REVERSEREPOTONAV = Column(DECIMAL(20, 4), doc="持有买入返售证券占资产净值比例(%)")
    F_PRT_REVERSEREPOTOTOT = Column(DECIMAL(20, 4), doc="持有买入返售证券占资产总值比例(%)")
    F_PRT_STOCKTONAV = Column(DECIMAL(20, 4), doc="持有股票市值占资产净值比例(%)")
    F_PRT_STOCKTONAVCHANGE = Column(DECIMAL(20, 4), doc="持有股票比例较上期变化(%)")
    F_PRT_STOCKTOTOT = Column(DECIMAL(20, 4), doc="持有股票市值占资产总值比例(%)")
    F_PRT_STOCKVALUE = Column(DECIMAL(20, 4), doc="持有股票市值(元)")
    F_PRT_TOTALASSET = Column(DECIMAL(20, 4), doc="资产总值(元)")
    F_PRT_WARRANTONAV = Column(DECIMAL(20, 4), doc="持有权证市值占资产净值比例(%)")
    F_PRT_WARRANTOTOT = Column(DECIMAL(20, 4), doc="持有权证市值占资产总值比例(%)")
    F_PRT_WARRANTVALUE = Column(DECIMAL(20, 4), doc="持有权证市值(元)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CHINAMUTUALFUNDBENCHMARK(Base):

    __tablename__ = 'CHINAMUTUALFUNDBENCHMARK'

    ANN_DT = Column(String(8), doc="公告日期")
    CUR_SIGN = Column(DECIMAL(1, 0), doc="是否最新")
    IS_COMPOUND = Column(DECIMAL(1, 0), doc="是否复利")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INC_SEQUENCE = Column(DECIMAL(2, 0), doc="序号")
    S_INFO_AFTERTAXORNOT = Column(DECIMAL(1, 0), doc="是否税后")
    S_INFO_BGNDT = Column(String(8), doc="起始日期")
    S_INFO_CONSTANT = Column(DECIMAL(20, 4), doc="常数")
    S_INFO_ENDDT = Column(String(8), doc="截止日期")
    S_INFO_FXCODE = Column(String(40), doc="汇率Wind代码")
    S_INFO_INDEXWEG = Column(DECIMAL(20, 4), doc="指数权重")
    S_INFO_INDEXWINDCODE = Column(String(40), doc="指数Wind代码")
    S_INFO_OPERATORS = Column(String(20), doc="运算符")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(10), doc="证券ID")
    SEC_ID2 = Column(String(10), doc="证券ID2")


class CHINAMUTUALFUNDBENCHMARKEOD(Base):

    __tablename__ = 'CHINAMUTUALFUNDBENCHMARKEOD'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_CLOSE = Column(DECIMAL(20, 8), doc="收盘价")
    S_DQ_PCTCHANGE = Column(DECIMAL(20, 8), doc="涨跌幅(%)")
    S_INFO_WINDCODE = Column(String(40), doc="指数Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")


class CHINAMUTUALFUNDBONDPORTFOLIO(Base):

    __tablename__ = 'CHINAMUTUALFUNDBONDPORTFOLIO'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    F_ANN_DATE = Column(String(8), doc="公告日期")
    F_PRT_BDQUANTITY = Column(DECIMAL(20, 4), doc="持有债券数量（张）")
    F_PRT_BDVALUE = Column(DECIMAL(20, 4), doc="持有债券市值(元)")
    F_PRT_BDVALUETONAV = Column(DECIMAL(20, 4), doc="持有债券市值占基金净值比例(%)")
    F_PRT_ENDDATE = Column(String(8), doc="截止日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_BONDWINDCODE = Column(String(40), doc="持有债券Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="基金Wind代码")


class CHINAMUTUALFUNDDESCRIPTION(Base):

    __tablename__ = 'CHINAMUTUALFUNDDESCRIPTION'

    CLOSE_INSTITU_OEF_DOWN = Column(DECIMAL(20, 4), doc="封闭期机构投资者认购下限(万元)")
    CLOSE_INSTITU_OEF_UP = Column(DECIMAL(20, 4), doc="封闭期机构投资者认购上限(万元)")
    CRNY_CODE = Column(String(10), doc="货币代码")
    F_CLOSED_OPERATION_INTERVAL = Column(DECIMAL(20, 4), doc="封闭运作期满开放日间隔")
    F_CLOSED_OPERATION_PERIOD = Column(DECIMAL(20, 4), doc="封闭运作期")
    F_INFO_ANNDATE = Column(String(8), doc="公告日期")
    F_INFO_BACKEND_CODE = Column(String(40), doc="后端代码")
    F_INFO_BENCHMARK = Column(String(500), doc="业绩比较基准")
    F_INFO_CORP_FUNDMANAGEMENTCOMP = Column(String(100), doc="管理人")
    F_INFO_CORP_FUNDMANAGEMENTID = Column(String(10), doc="基金管理人ID")
    F_INFO_CUSTODIANBANK = Column(String(100), doc="托管人")
    F_INFO_CUSTODIANBANKID = Column(String(40), doc="托管人id")
    F_INFO_CUSTODIANFEERATIO = Column(DECIMAL(20, 4), doc="托管费")
    F_INFO_DECISION_BASIS = Column(String(2000), doc="决策依据")
    F_INFO_DELISTDATE = Column(String(8), doc="退市日期")
    F_INFO_EXCHMARKET = Column(String(10), doc="交易所")
    F_INFO_EXPECTEDRATEOFRETURN = Column(DECIMAL(20, 4), doc="预期收益率")
    F_INFO_FIRSTINVESTSTYLE = Column(String(20), doc="投资风格")
    F_INFO_FIRSTINVESTTYPE = Column(String(40), doc="投资类型")
    F_INFO_FRONT_CODE = Column(String(40), doc="前端代码")
    F_INFO_FULLNAME = Column(String(100), doc="名称")
    F_INFO_FUND_ID = Column(String(100), doc="基金品种ID")
    F_INFO_INVESTCONCEPTION = Column(String(2000), doc="投资理念")
    F_INFO_INVESTOBJECT = Column(String(500), doc="投资目标")
    F_INFO_INVESTSCOPE = Column(String(2000), doc="投资范围")
    F_INFO_ISINITIAL = Column(DECIMAL(5, 0), doc="是否为初始基金")
    F_INFO_ISSUEDATE = Column(String(8), doc="发行日期")
    F_INFO_ISSUINGPLACE = Column(String(100), doc="发行地")
    F_INFO_LISTDATE = Column(String(8), doc="上市时间")
    F_INFO_MANAGEMENTFEERATIO = Column(DECIMAL(20, 4), doc="管理费")
    F_INFO_MATURITYDATE = Column(String(8), doc="到期日期")
    F_INFO_MINBUYAMOUNT = Column(DECIMAL(20, 4), doc="起点金额")
    F_INFO_NAME = Column(String(100), doc="简称")
    F_INFO_PARVALUE = Column(DECIMAL(20, 4), doc="面值")
    F_INFO_PINYIN = Column(String(40), doc="简称拼音")
    F_INFO_PTMYEAR = Column(DECIMAL(20, 4), doc="存续期")
    F_INFO_REDMSTARTDATE = Column(String(8), doc="日常赎回起始日")
    F_INFO_REGISTRANT = Column(String(10), doc="基金注册与过户登记人ID")
    F_INFO_RESTRICTEDORNOT = Column(String(20), doc="限定类型")
    F_INFO_SETUPDATE = Column(String(8), doc="成立日期")
    F_INFO_STATUS = Column(DECIMAL(9, 0), doc="存续状态")
    F_INFO_STRUCTUREDORNOT = Column(DECIMAL(1, 0), doc="是否结构化产品")
    F_INFO_TRUSTEE = Column(String(100), doc="受托人")
    F_INFO_TRUSTTYPE = Column(String(40), doc="信托类别")
    F_INFO_TYPE = Column(String(20), doc="基金类型")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_INVESTMENT_AREA = Column(String(20), doc="投资区域")
    F_ISSUE_OEF_DNDDATEINST = Column(String(8), doc="机构投资者认购终止日")
    F_ISSUE_OEF_STARTDATEINST = Column(String(8), doc="机构投资者认购起始日")
    F_ISSUE_TOTALUNIT = Column(DECIMAL(20, 4), doc="发行份额")
    F_PCHREDM_PCHMINAMT = Column(DECIMAL(20, 4), doc="每次最低申购金额(场外)(万元)")
    F_PCHREDM_PCHMINAMT_EX = Column(DECIMAL(20, 4), doc="每次最低申购金额(场内) (万元)")
    F_PCHREDM_PCHSTARTDATE = Column(String(8), doc="日常申购起始日")
    F_PERSONAL_ENDDATEIND = Column(String(8), doc="个人投资者认购终止日")
    F_PERSONAL_STARTDATEIND = Column(String(8), doc="个人投资者认购起始日")
    F_SALES_SERVICE_RATE = Column(DECIMAL(20, 4), doc="销售服务费率")
    INVESTSTRATEGY = Column(LONGTEXT, doc="投资策略")
    IS_INDEXFUND = Column(DECIMAL(5, 0), doc="是否指数基金")
    MAX_NUM_COLTARGET = Column(DECIMAL(20, 4), doc="封闭期目标募集数量上限(亿份)")
    MAX_NUM_HOLDER = Column(DECIMAL(20, 4), doc="单一投资者持有份额上限(亿份)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RISK_RETURN = Column(LONGTEXT, doc="基金风险收益特征")


class CHINAMUTUALFUNDFLOATSHARE(Base):

    __tablename__ = 'CHINAMUTUALFUNDFLOATSHARE'

    F_UNIT_FLOATSHARE = Column(DECIMAL(20, 4), doc="场内份额(份)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="交易日期")


class CHINAMUTUALFUNDINDPORTFOLIO(Base):

    __tablename__ = 'CHINAMUTUALFUNDINDPORTFOLIO'

    F_ANN_DATE = Column(String(8), doc="公告日期")
    F_PRT_ENDDATE = Column(String(8), doc="截止日期")
    F_PRT_INDPASSIVEPRO = Column(DECIMAL(20, 4), doc="指数投资持有行业比例(%)")
    F_PRT_INDPASSIVEVALUE = Column(DECIMAL(20, 4), doc="指数投资持有行业市值(元)")
    F_PRT_INDPOSPRO = Column(DECIMAL(20, 4), doc="积极投资持有行业比例(%)")
    F_PRT_INDPOSVALUE = Column(DECIMAL(20, 4), doc="积极投资持有行业市值(元)")
    F_PRT_INDUSTONAV = Column(DECIMAL(20, 4), doc="持有行业市值占基金净值比例(%)")
    F_PRT_INDUSTONAVCHANGE = Column(DECIMAL(20, 4), doc="持有行业市值比例较上期变化(%)")
    F_PRT_INDUSVALUE = Column(DECIMAL(20, 4), doc="持有行业市值(元)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CSRCINDUSCODE = Column(String(40), doc="证监会行业编号")
    S_INFO_CSRCINDUSNAME = Column(String(50), doc="行业名称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CHINAMUTUALFUNDMANAGER(Base):

    __tablename__ = 'CHINAMUTUALFUNDMANAGER'

    ANN_DATE = Column(String(8), doc="公告日期")
    F_INFO_DIS_SERIAL_NUMBER = Column(DECIMAL(2, 0), doc="展示序号")
    F_INFO_ESCROW_FUNDMANAGER = Column(String(50), doc="代管基金经理")
    F_INFO_ESCROW_LEAVEDATE = Column(String(8), doc="代管结束日期")
    F_INFO_ESCROW_STARTDATE = Column(String(8), doc="代管起始日期")
    F_INFO_FUNDMANAGER = Column(String(40), doc="姓名")
    F_INFO_FUNDMANAGER_ID = Column(String(10), doc="基金经理ID")
    F_INFO_MANAGER_BIRTHYEAR = Column(String(10), doc="出身年份")
    F_INFO_MANAGER_EDUCATION = Column(String(20), doc="学历")
    F_INFO_MANAGER_GENDER = Column(String(10), doc="性别")
    F_INFO_MANAGER_LEAVEDATE = Column(String(8), doc="离职日期")
    F_INFO_MANAGER_NATIONALITY = Column(String(10), doc="国籍")
    F_INFO_MANAGER_RESUME = Column(LONGTEXT, doc="简历")
    F_INFO_MANAGER_STARTDATE = Column(String(8), doc="任职日期")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_MANAGER_POST = Column(String(100), doc="备注")


class CHINAMUTUALFUNDNAV(Base):

    __tablename__ = 'CHINAMUTUALFUNDNAV'

    ANN_DATE = Column(String(8), doc="公告日期")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    F_ASSET_MERGEDSHARESORNOT = Column(DECIMAL(1, 0), doc="是否合计数据")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_NAV_ACCUMULATED = Column(DECIMAL(24, 8), doc="累计净值")
    F_NAV_ADJFACTOR = Column(DECIMAL(24, 8), doc="复权因子")
    F_NAV_ADJUSTED = Column(DECIMAL(22, 8), doc="复权单位净值")
    F_NAV_DISTRIBUTION = Column(DECIMAL(20, 4), doc="累计单位分配")
    F_NAV_DIVACCUMULATED = Column(DECIMAL(20, 4), doc="累计分红(废弃)")
    F_NAV_UNIT = Column(DECIMAL(24, 8), doc="单位净值")
    F_PRT_NETASSET = Column(DECIMAL(20, 4), doc="资产净值")
    IS_EXDIVIDENDDATE = Column(DECIMAL(5, 0), doc="是否净值除权日")
    NETASSET_TOTAL = Column(DECIMAL(20, 4), doc="合计资产净值")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICE_DATE = Column(String(8), doc="截止日期")


class CHINAMUTUALFUNDPCHREDM(Base):

    __tablename__ = 'CHINAMUTUALFUNDPCHREDM'

    F_UNIT_ENDSHARES = Column(DECIMAL(20, 4), doc="期末基金总份额(份)")
    F_UNIT_ENDSHARES_TOTAL = Column(DECIMAL(20, 4), doc="期末基金总份额-合计")
    F_UNIT_PURCHASE = Column(DECIMAL(20, 4), doc="本期基金总申购份额(份)")
    F_UNIT_PURCHASE_TOTAL = Column(DECIMAL(20, 4), doc="本期基金总申购份额-合计")
    F_UNIT_REDEMPTION = Column(DECIMAL(20, 4), doc="本期基金总赎回份额(份)")
    F_UNIT_REDEMPTION_TOTAL = Column(DECIMAL(20, 4), doc="本期基金总赎回份额-合计")
    F_UNIT_RPENDDATE = Column(String(8), doc="报告期结束日期")
    F_UNIT_RPSTARTDATE = Column(String(8), doc="报告期开始日期")
    F_UNIT_STARTSHARES = Column(DECIMAL(20, 4), doc="期初基金总份额(份)")
    F_UNIT_STARTSHARES_TOTAL = Column(DECIMAL(20, 4), doc="期初基金总份额-合计")
    IS_MERGE_DATA = Column(DECIMAL(5, 0), doc="是否为合并数据")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    TRADE_DT = Column(String(8), doc="公告日期")


class CHINAMUTUALFUNDPOSESTIMATION(Base):

    __tablename__ = 'CHINAMUTUALFUNDPOSESTIMATION'

    F_EST_DATE = Column(String(8), doc="估算日期")
    F_EST_LARGECAPWEG = Column(DECIMAL(20, 4), doc="大市值组合权重")
    F_EST_MIDCAPWEG = Column(DECIMAL(20, 4), doc="中市值组合权重")
    F_EST_NAV = Column(DECIMAL(20, 4), doc="估算收盘净值(元)")
    F_EST_POSITION = Column(DECIMAL(20, 4), doc="基金仓位")
    F_EST_SMALLCAPWEG = Column(DECIMAL(20, 4), doc="小市值组合权重")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="基金Wind代码")


class CHINAMUTUALFUNDREPNAVPER(Base):

    __tablename__ = 'CHINAMUTUALFUNDREPNAVPER'

    ANN_DATE = Column(String(8), doc="公告日期")
    F_INFO_REPORTPERIOD = Column(String(8), doc="报告期")
    F_NAV_BENCHDEVRETURN = Column(DECIMAL(20, 4), doc="净值增长率减基准收益率")
    F_NAV_BENCHRETURN = Column(DECIMAL(20, 4), doc="业绩比较基准收益率")
    F_NAV_BENCHSTDDEV = Column(DECIMAL(20, 4), doc="业绩比较基准收益率标准差")
    F_NAV_RETURN = Column(DECIMAL(20, 4), doc="净值增长率")
    F_NAV_STDDEVNAVBENCH = Column(DECIMAL(20, 4), doc="净值增长率标准差减基准收益率标准差")
    F_NAV_STDDEVRETURN = Column(DECIMAL(20, 4), doc="净值增长率标准差")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PERIOD_CODE = Column(String(10), doc="期间代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CHINAMUTUALFUNDSEATTRADING(Base):

    __tablename__ = 'CHINAMUTUALFUNDSEATTRADING'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    F_COMMISSIONAM = Column(DECIMAL(20, 4), doc="交易佣金(元)")
    F_COMMISSIONPRO = Column(DECIMAL(20, 4), doc="交易佣金占比(%)")
    F_TRADE_BONDAM = Column(DECIMAL(20, 4), doc="债券交易金额(元)")
    F_TRADE_BONDPRO = Column(DECIMAL(20, 4), doc="债券交易金额占比(%)")
    F_TRADE_FUNDAM = Column(DECIMAL(20, 4), doc="基金交易金额(元)")
    F_TRADE_FUNDPRO = Column(DECIMAL(20, 4), doc="基金交易金额占比(%)")
    F_TRADE_REPOAM = Column(DECIMAL(20, 4), doc="回购交易金额(元)")
    F_TRADE_REPOPRO = Column(DECIMAL(20, 4), doc="回购交易金额占比(%)")
    F_TRADE_SBAM = Column(DECIMAL(20, 4), doc="股票债券成交金额(元)")
    F_TRADE_SBPRO = Column(DECIMAL(20, 4), doc="股票债券交易量占比(%)")
    F_TRADE_STOCKAM = Column(DECIMAL(20, 4), doc="股票交易金额(元)")
    F_TRADE_STOCKPRO = Column(DECIMAL(20, 4), doc="股票交易金额占比(%)")
    F_TRADE_WARRANTAM = Column(DECIMAL(20, 4), doc="权证交易金额(元)")
    F_TRADE_WARRANTPRO = Column(DECIMAL(20, 4), doc="权证交易金额占比(%)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_REPORTPERIOD = Column(String(8), doc="报告期")
    S_INFO_SECURNAME = Column(String(100), doc="证券公司简称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CHINAMUTUALFUNDSECTOR(Base):

    __tablename__ = 'CHINAMUTUALFUNDSECTOR'

    CUR_SIGN = Column(String(10), doc="最新标志")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_SECTOR = Column(String(40), doc="所属板块")
    S_INFO_SECTORENTRYDT = Column(String(8), doc="起始日期")
    S_INFO_SECTOREXITDT = Column(String(8), doc="截止日期")


class CHINAMUTUALFUNDSHARE(Base):

    __tablename__ = 'CHINAMUTUALFUNDSHARE'

    ANN_DATE = Column(String(8), doc="公告日期")
    CHANGE_DATE = Column(String(8), doc="变动日期")
    CHANGEREASON = Column(String(10), doc="份额变动原因")
    CUR_SIGN = Column(DECIMAL(5, 0), doc="最新标志")
    F_INFO_SHARE = Column(DECIMAL(20, 6), doc="流通份额(万份)")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_UNIT_MERGEDSHARESORNOT = Column(DECIMAL(5, 0), doc="是否为合并数据")
    F_UNIT_TOTAL = Column(DECIMAL(20, 6), doc="基金总份额(万份)")
    FUNDSHARE = Column(DECIMAL(20, 6), doc="基金份额(万份)")
    FUNDSHARE_TOTAL = Column(DECIMAL(20, 6), doc="基金合计份额(万份)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))


class CHINAMUTUALFUNDSTOCKPORTFOLIO(Base):

    __tablename__ = 'CHINAMUTUALFUNDSTOCKPORTFOLIO'

    ANN_DATE = Column(String(8), doc="公告日期")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    F_PRT_ENDDATE = Column(String(8), doc="截止日期")
    F_PRT_PASSTKEVALUE = Column(DECIMAL(20, 4), doc="指数投资持有股票市值(元)")
    F_PRT_PASSTKQUANTITY = Column(DECIMAL(20, 4), doc="指数投资持有股数（股）")
    F_PRT_PASSTKTONAV = Column(DECIMAL(20, 4), doc="指数投资持有股票市值占净资产比例(%)")
    F_PRT_POSSTKQUANTITY = Column(DECIMAL(20, 4), doc="积极投资持有股数（股）")
    F_PRT_POSSTKTONAV = Column(DECIMAL(20, 4), doc="积极投资持有股票市值占净资产比例(%)")
    F_PRT_POSSTKVALUE = Column(DECIMAL(20, 4), doc="积极投资持有股票市值(元)")
    F_PRT_STKQUANTITY = Column(DECIMAL(20, 4), doc="持有股票数量（股）")
    F_PRT_STKVALUE = Column(DECIMAL(20, 4), doc="持有股票市值(元)")
    F_PRT_STKVALUETONAV = Column(DECIMAL(20, 4), doc="持有股票市值占基金净值比例(%)")
    FLOAT_SHR_PER = Column(DECIMAL(24, 4), doc="占流通股本比例(%)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_STOCKWINDCODE = Column(String(10), doc="持有股票Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="基金Wind代码")
    STOCK_PER = Column(DECIMAL(20, 2), doc="占股票市值比")


class CHINAMUTUALFUNDSUSPENDPCHREDM(Base):

    __tablename__ = 'CHINAMUTUALFUNDSUSPENDPCHREDM'

    F_INFO_PURCHASEUPLIMIT = Column(DECIMAL(20, 4), doc="单日申购上限")
    F_INFO_REPCHANNDT = Column(String(8), doc="恢复申购公告日期")
    F_INFO_REPCHDT = Column(String(8), doc="恢复申购日期")
    F_INFO_SUSPCHANNDT = Column(String(8), doc="暂停申购公告日期")
    F_INFO_SUSPCHREASON = Column(String(800), doc="暂停申购原因")
    F_INFO_SUSPCHSTARTDT = Column(String(8), doc="暂停申购起始日期")
    F_INFO_SUSPCHTYPE = Column(DECIMAL(9, 0), doc="暂停申购类型代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CHINAMUTUALFUNDTRACKINGINDEX(Base):

    __tablename__ = 'CHINAMUTUALFUNDTRACKINGINDEX'

    ENTRY_DT = Column(String(8), doc="生效日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    REMOVE_DT = Column(String(8), doc="失效日期")
    S_INFO_INDEXWINDCODE = Column(String(40), doc="跟踪指数Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CLOSEDFUNDPCHREDM(Base):

    __tablename__ = 'CLOSEDFUNDPCHREDM'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PCH_CODE = Column(String(20), doc="场内基金代码")
    PCH_NAME = Column(String(40), doc="场内基金简称")
    PCH_START_DT = Column(String(8), doc="场内申购起始日")
    REDM_START_DT = Column(String(8), doc="场内赎回起始日")
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SUBSTRIPTION_CODE = Column(String(20), doc="场内认购代码")
    SUBSTRIPTION_END_DT = Column(String(8), doc="场内认购截止日")
    SUBSTRIPTION_NAME = Column(String(40), doc="场内认购简称")
    SUBSTRIPTION_PRICE = Column(DECIMAL(20, 4), doc="场内认购价格")
    SUBSTRIPTION_START_DT = Column(String(8), doc="场内认购起始日")


class CMFAIPINFO(Base):

    __tablename__ = 'CMFAIPINFO'

    ANN_DT = Column(String(8), doc="公告日期")
    COMP_ID = Column(String(10), doc="定投代销机构ID")
    COMP_NAME = Column(String(200), doc="定投代销机构名称")
    END_DT = Column(String(8), doc="定投截止日期")
    LEVEL_AMOUNT = Column(DECIMAL(20, 4), doc="投资额级差(元)")
    MAX_PURCHASE = Column(DECIMAL(20, 4), doc="定投最高金额(元)")
    MEMO = Column(String(500), doc="备注")
    MIN_PURCHASE = Column(DECIMAL(20, 4), doc="定投起始金额(元)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEQUENCE = Column(DECIMAL(1, 0), doc="序号")
    START_DT = Column(String(8), doc="定投开始时间")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="定投类型代码")


class CMFCODEANDSNAME(Base):

    __tablename__ = 'CMFCODEANDSNAME'

    IS_COMMON = Column(DECIMAL(1, 0), doc="是否通用代码")
    MEMO = Column(String(800), doc="备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CODE = Column(String(20), doc="业务代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_SNAME = Column(String(100), doc="业务简称")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="业务类型代码")


class CMFCONSEPTION(Base):

    __tablename__ = 'CMFCONSEPTION'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_SECTOR = Column(String(10), doc="所属板块代码")
    S_INFO_SECTORENTRYDT = Column(String(8), doc="起始日期")
    S_INFO_SECTOREXITDT = Column(String(8), doc="截止日期")
    S_INFO_SECTORNAME = Column(String(40), doc="所属板块名称")


class CMFDESCCHANGE(Base):

    __tablename__ = 'CMFDESCCHANGE'

    CHANGE_DT = Column(String(8), doc="变更日期")
    ITEM = Column(String(50), doc="变更字段名称")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_NEW = Column(String(1000), doc="变更后")
    S_INFO_OLD = Column(String(1000), doc="变更前")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CMFFAIRVALUECHANGEPROFIT(Base):

    __tablename__ = 'CMFFAIRVALUECHANGEPROFIT'

    ABS_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="资产支持证券投资公允价值变动收益")
    ANN_DT = Column(String(8), doc="公告日期")
    BOND1_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="债券投资(银行间同业市场)公允价值变动收益")
    BOND_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="债券投资(交易所市场)公允价值变动收益")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    FORWARD_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="外汇远期投资公允价值变动收益")
    FUND_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="基金投资公允价值变动收益")
    MEMO = Column(String(200), doc="备注")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OTHER = Column(DECIMAL(20, 4), doc="其他")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    STOCK_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="股票投资公允价值变动收益")
    TOT_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="合计公允价值变动收益")
    WARRANT_CHANGE_FAIR_VALUE = Column(DECIMAL(20, 4), doc="权证投资公允价值变动收益")


class CMFFIXEDINVESTMENTRATE(Base):

    __tablename__ = 'CMFFIXEDINVESTMENTRATE'

    F_ANNUALYEILD_FIVESYEAR = Column(DECIMAL(20, 6), doc="近五年定投年化收益率")
    F_ANNUALYEILD_FIVEYEAR = Column(String(20), doc="近五年定投年化收益同类排名")
    F_ANNUALYEILD_THISYEAR = Column(DECIMAL(20, 6), doc="近一年定投年化收益率")
    F_ANNUALYEILD_THREESYEAR = Column(DECIMAL(20, 6), doc="近三年定投年化收益率")
    F_ANNUALYEILD_THREEYEAR = Column(String(20), doc="近三年定投年化收益同类排名")
    F_ANNUALYEILD_TWOSYEAR = Column(DECIMAL(20, 6), doc="近二年定投年化收益率")
    F_ANNUALYEILD_TWOYEAR = Column(String(20), doc="近二年定投年化收益同类排名")
    F_AVGRETURN_FIVEYEAR = Column(DECIMAL(20, 6), doc="近五年定投总收益率")
    F_AVGRETURN_THISYEAR = Column(DECIMAL(20, 6), doc="近一年定投总收益率")
    F_AVGRETURN_THREEYEAR = Column(DECIMAL(20, 6), doc="近三年定投总收益率")
    F_AVGRETURN_TWOYEAR = Column(DECIMAL(20, 6), doc="近二年定投总收益率")
    F_DIVIDEND_METHOD = Column(String(20), doc="分红方式")
    F_FIXED_AMOUNT = Column(DECIMAL(20, 0), doc="定投金额")
    F_FIXED_INVESTMENT_CYCLE = Column(String(20), doc="定投周期")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_PURCHASE_RATE = Column(DECIMAL(20, 4), doc="申购费率")
    F_RECENTYEART_THISYEAR = Column(String(20), doc="近一年定投年化收益同类排名")
    F_SFRANK_RECENTYEART = Column(String(20), doc="近一年定投同类排名")
    F_SFRANK_RECENTYEART_FIVESYEAR = Column(String(20), doc="近五年定投同类排名")
    F_SFRANK_RECENTYEART_TWOSYEAR = Column(String(20), doc="近二年定投同类排名")
    F_SFRANK_THREESYEAR = Column(String(20), doc="近三年定投同类排名")
    F_TYPE_CODE = Column(String(20), doc="投资类型代码")
    F_TYPE_NAME = Column(String(40), doc="基金投资类型名称")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    TRADE_DT = Column(String(8), doc="交易日期")


class CMFHOLDER(Base):

    __tablename__ = 'CMFHOLDER'

    ANN_DT = Column(String(8), doc="公告日期")
    B_INFO_HOLDAMOUNT = Column(DECIMAL(20, 4), doc="数量(股张\份)")
    B_INFO_HOLDER = Column(String(300), doc="持有人")
    B_ISSUER_SHARECATEGORY = Column(String(1), doc="[内部]股东类型： 1 个人；2 公司")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_FA_LATELYRD = Column(String(8), doc="报告期")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_ENDDATE = Column(String(8), doc="截止日期")
    S_INFO_WINDCODE = Column(String(40), doc="证券ID")


class CMFHOLDERSTRUCTURE(Base):

    __tablename__ = 'CMFHOLDERSTRUCTURE'

    ANN_DT = Column(String(8), doc="公告日期")
    END_DT = Column(String(8), doc="截止日期")
    HOLDER_AVGHOLDING = Column(DECIMAL(20, 4), doc="平均每户持有基金份额(份)")
    HOLDER_FEEDER_HOLDING = Column(DECIMAL(20, 4), doc="联接基金持有份额(份)")
    HOLDER_FEEDER_HOLDINGPCT = Column(DECIMAL(20, 4), doc="联接基金持有份额占比(%)")
    HOLDER_INSTITUTION_HOLDING = Column(DECIMAL(20, 4), doc="机构投资者持有份额(份)")
    HOLDER_INSTITUTION_HOLDINGPCT = Column(DECIMAL(20, 4), doc="机构投资者持有份额占比(%)")
    HOLDER_MNGEMP_HOLDING = Column(DECIMAL(20, 4), doc="管理人员工持有份额(份)")
    HOLDER_MNGEMP_HOLDINGPCT = Column(DECIMAL(20, 8), doc="管理人员工持有份额占比(%)")
    HOLDER_NUMBER = Column(DECIMAL(20, 0), doc="基金份额持有人户数(户)")
    HOLDER_PERSONAL_HOLDING = Column(DECIMAL(20, 4), doc="个人投资者持有份额(份)")
    HOLDER_PERSONAL_HOLDINGPCT = Column(DECIMAL(20, 4), doc="个人投资者持有份额占比(%)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PUR_COST = Column(DECIMAL(20, 4), doc="报告期买入股票成本总额(元)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SCOPE = Column(String(4), doc="范围")
    SEC_ID = Column(String(40), doc="证券ID")
    SELL_INCOME = Column(DECIMAL(20, 4), doc="报告期卖出股票收入总额(元)")


class CMFHOLDINGRATIOANOMALY(Base):

    __tablename__ = 'CMFHOLDINGRATIOANOMALY'

    F_END_NUM_HOLDER = Column(DECIMAL(20, 4), doc="期末持有份额")
    F_END_NUM_HOLDER_PROPORTION = Column(DECIMAL(20, 4), doc="期末持有份额占基金份额比例")
    F_HOLDING_TIME = Column(String(500), doc="持有时间区间")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_INQUIRER_TYPE = Column(String(100), doc="投资者类别")
    F_INQUIRER_TYPE_NUM = Column(DECIMAL(2, 0), doc="投资者序号")
    F_INQUIRER_TYPECODE = Column(String(1), doc="投资者类别代码")
    F_START_NUM_HOLDER = Column(DECIMAL(20, 4), doc="期初持有份额")
    F_UNIT_PCH = Column(DECIMAL(20, 4), doc="申购份额")
    F_UNIT_REDM = Column(DECIMAL(20, 4), doc="赎回份额")
    F_UNIT_RPENDDATE = Column(String(8), doc="报告期截止日期")
    F_UNIT_RPSTARTDATE = Column(String(8), doc="报告期开始日期")
    IS_MERGE = Column(DECIMAL(1, 0), doc="是否为合并数据")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    TRADE_DT = Column(String(8), doc="公告日期")


class CMFINDEXDESCRIPTION(Base):

    __tablename__ = 'CMFINDEXDESCRIPTION'

    COMPONENT_STOCKS_NUM = Column(DECIMAL(5, 0), doc="成份股数量")
    EXPIRE_DATE = Column(String(8), doc="终止发布日期")
    EXPONENTIAL_SCALE_CODE = Column(DECIMAL(9, 0), doc="指数规模代码")
    INCOME_PROCESSING_METHOD = Column(String(20), doc="收益处理方式")
    INCOME_PROCESSING_METHOD_CODE = Column(DECIMAL(9, 0), doc="收益处理方式代码")
    INDEX_CATEGORY_CODE = Column(DECIMAL(9, 0), doc="指数类别代码")
    INDEX_CATEGORY_TYPE = Column(String(40), doc="指数类别")
    INDEX_INTRO = Column(LONGTEXT, doc="指数简介")
    INDEX_REGION_CODE = Column(DECIMAL(9, 0), doc="指数区域代码")
    MARKET_OWN_CODE = Column(DECIMAL(9, 0), doc="所属市场代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CODE = Column(String(40), doc="交易代码")
    S_INFO_COMPNAME = Column(String(100), doc="指数名称")
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所")
    S_INFO_INDEX_BASEPER = Column(String(8), doc="基期")
    S_INFO_INDEX_BASEPT = Column(DECIMAL(20, 4), doc="基点")
    S_INFO_INDEX_ENAME = Column(String(200), doc="指数英文名称")
    S_INFO_INDEX_WEIGHTSRULE = Column(String(40), doc="加权方式")
    S_INFO_INDEXSTYLE = Column(String(40), doc="指数风格")
    S_INFO_LISTDATE = Column(String(8), doc="发布日期")
    S_INFO_NAME = Column(String(50), doc="证券简称")
    S_INFO_PUBLISHER = Column(String(100), doc="发布方")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    WEIGHT_TYPE = Column(String(100), doc="权重类型")
    WEIGHT_TYPE_CODE = Column(DECIMAL(9, 0), doc="权重类型代码")
    WEIGHTING_METHOD_END_DATE = Column(String(8), doc="【废弃】加权方式终止日期")
    WEIGHTING_METHOD_START_DATE = Column(String(8), doc="【废弃】加权方式起始日期")


class CMFINDEXEOD(Base):

    __tablename__ = 'CMFINDEXEOD'

    CRNCY_CODE = Column(String(10), doc="货币代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_AMOUNT = Column(DECIMAL(20, 4), doc="成交金额(千元)")
    S_DQ_CHANGE = Column(DECIMAL(20, 4), doc="涨跌(点)")
    S_DQ_CLOSE = Column(DECIMAL(20, 4), doc="最新价")
    S_DQ_HIGH = Column(DECIMAL(20, 4), doc="最高价")
    S_DQ_LOW = Column(DECIMAL(20, 4), doc="最低价")
    S_DQ_OPEN = Column(DECIMAL(20, 4), doc="开盘价")
    S_DQ_PCTCHANGE = Column(DECIMAL(20, 4), doc="涨跌幅(%)")
    S_DQ_PRECLOSE = Column(DECIMAL(20, 4), doc="昨收盘价")
    S_DQ_VOLUME = Column(DECIMAL(20, 4), doc="成交量(手)")
    S_INFO_NAME = Column(String(50), doc="指数简称")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(10), doc="证券ID")
    TRADE_DT = Column(String(8), doc="交易日期")


class CMFINDUSTRYPLATE(Base):

    __tablename__ = 'CMFINDUSTRYPLATE'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_NAME = Column(String(100), doc="板块名称")
    S_INFO_SECTOR = Column(String(16), doc="板块代码")
    S_INFO_WINDCODE = Column(String(40), doc="成份万得代码")


class CMFIOPVNAV(Base):

    __tablename__ = 'CMFIOPVNAV'

    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_IOPV_NAV = Column(DECIMAL(20, 8), doc="IOPV收盘净值")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICE_DATE = Column(String(8), doc="日期")


class CMFNAVOPERATIONRECORD(Base):

    __tablename__ = 'CMFNAVOPERATIONRECORD'

    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_NAV_OLD = Column(DECIMAL(11, 6), doc="调整前净值")
    FUND_NAV_OBJECT_ID = Column(String(38), doc="基金净值表记录ID")
    HANDLE_ACTION = Column(String(20), doc="处理动作")
    HANDLE_DATE = Column(String(8), doc="处理日期")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PRICE_DATE = Column(String(8), doc="净值截止日期")


class CMFOTHERPORTFOLIO(Base):

    __tablename__ = 'CMFOTHERPORTFOLIO'

    ANN_DT = Column(String(8), doc="公告日期")
    CRNCY_CODE = Column(String(10), doc="货币代码")
    END_DT = Column(String(8), doc="截止日期")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    QUANTITY = Column(DECIMAL(20, 4), doc="持仓数量(股/张)")
    S_INFO_HOLDWINDCODE = Column(String(40), doc="Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    VALUE = Column(DECIMAL(20, 4), doc="持仓市值")
    VALUETONAV = Column(DECIMAL(20, 4), doc="持仓市值占基金净值比例(%)")


class CMFPREFERENTIALFEE(Base):

    __tablename__ = 'CMFPREFERENTIALFEE'

    AMOUNTDOWNLIMIT = Column(DECIMAL(20, 4), doc="申购金额下限(万元)")
    AMOUNTUPLIMIT = Column(DECIMAL(20, 4), doc="申购金额上限(万元)")
    ANN_DT = Column(String(8), doc="公告日期")
    COMP_ID = Column(String(10), doc="参加优惠活动的代销机构公司ID")
    COMP_NAME = Column(String(200), doc="参加优惠活动的代销机构名称")
    END_DT = Column(String(8), doc="费率优惠截止日期")
    MEMO = Column(String(500), doc="备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PREFERENTIAL_RATE = Column(DECIMAL(20, 4), doc="优惠费率(%)")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(10), doc="证券ID")
    SEQUENCE = Column(DECIMAL(1, 0), doc="序号")
    START_DT = Column(String(8), doc="费率优惠开始日期")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="优惠活动类型代码")
    WAY_TYPE = Column(DECIMAL(9, 0), doc="优惠活动参与方式代码")


class CMFPROPORTIONOFINVEOBJ(Base):

    __tablename__ = 'CMFPROPORTIONOFINVEOBJ'

    BOND_INVEST_PCT_DOWN = Column(DECIMAL(5, 0), doc="债券投资比例下限")
    BOND_INVEST_PCT_UP = Column(DECIMAL(5, 0), doc="债券投资比例上限")
    CHANGE_DT = Column(String(8), doc="变动日期")
    COMM_INVEST_PCT_DOWN = Column(DECIMAL(5, 0), doc="商品衍生品投资比例下限")
    COMM_INVEST_PCT_UP = Column(DECIMAL(5, 0), doc="商品衍生品投资比例上限")
    CONSEPTION_TYPECODE = Column(DECIMAL(9, 0), doc="概念主题类别代码")
    FUND_INVEST_PCT_DOWN = Column(DECIMAL(5, 0), doc="基金投资比例下限")
    FUND_INVEST_PCT_UP = Column(DECIMAL(5, 0), doc="基金投资比例上限")
    INVEST_PCT_TYPECODE = Column(DECIMAL(9, 0), doc="基金投资占比类型代码")
    IS_TOT_PCT = Column(DECIMAL(1, 0), doc="是否合计占比")
    MMT_INVEST_PCT_DOWN = Column(DECIMAL(5, 0), doc="货币工具比例下限")
    MMT_INVEST_PCT_UP = Column(DECIMAL(5, 0), doc="货币工具比例上限")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OTHER_INVEST_PCT_DOWN = Column(DECIMAL(5, 0), doc="其他非股票投资比例下限")
    OTHER_INVEST_PCT_UP = Column(DECIMAL(5, 0), doc="其他非股票投资比例上限")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    STOCK_INVEST_PCT_DOWN = Column(DECIMAL(5, 0), doc="股票投资比例下限")
    STOCK_INVEST_PCT_UP = Column(DECIMAL(5, 0), doc="股票投资比例上限")


class CMFRISKLEVEL(Base):

    __tablename__ = 'CMFRISKLEVEL'

    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RISK_LEVEL = Column(String(40), doc="基金风险等级")


class CMFSECCLASS(Base):

    __tablename__ = 'CMFSECCLASS'

    CUR_SIGN = Column(DECIMAL(1, 0), doc="最新标志")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_SECTOR = Column(String(10), doc="所属板块代码")
    S_INFO_SECTORENTRYDT = Column(String(8), doc="起始日期")
    S_INFO_SECTOREXITDT = Column(String(8), doc="截止日期")
    S_INFO_SECTORNAME = Column(String(40), doc="所属板块名称")


class CMFSELLINGAGENTS(Base):

    __tablename__ = 'CMFSELLINGAGENTS'

    CUR_SIGN = Column(DECIMAL(5, 0), doc="最新标志")
    F_AGENCY_NAME = Column(String(200), doc="机构名称")
    F_AGENCY_NAMEID = Column(String(20), doc="中介机构公司ID")
    F_ANN_DATE = Column(String(8), doc="公告日期")
    F_BEGIN_DATE = Column(String(8), doc="起始日期")
    F_END_DATE = Column(String(8), doc="终止日期")
    F_INFO_WINDCODE = Column(String(40), doc="WIND代码")
    F_RELATION = Column(String(30), doc="关系类型")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))


class CMFSUBREDFEE(Base):

    __tablename__ = 'CMFSUBREDFEE'

    AMOUNTDOWNLIMIT = Column(DECIMAL(20, 4), doc="金额下限(万元)")
    AMOUNTUPLIMIT = Column(DECIMAL(20, 4), doc="金额上限(万元)")
    ANN_DATE = Column(String(8), doc="公告日期")
    CHANGE_DT = Column(String(8), doc="变动日期")
    CHARGEWAY = Column(String(20), doc="收费类型")
    FEE_TYPE_CODE = Column(DECIMAL(9, 0), doc="费率类型代码")
    FEERATIO = Column(DECIMAL(20, 4), doc="费率(%)")
    FEETYPECODE = Column(String(30), doc="费率类型")
    HOLDINGPERIOD_DOWNLIMIT = Column(DECIMAL(20, 4), doc="持有年限下限")
    HOLDINGPERIOD_UPLIMIT = Column(DECIMAL(20, 4), doc="持有年限上限")
    HOLDINGPERIODUNIT = Column(String(20), doc="持有期限单位")
    ISUPLIMITFEE = Column(String(1), doc="是否上限费率")
    MEMO = Column(String(4), doc="区间是否包含掩码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SUPPLEMENTARY = Column(String(800), doc="费率补充说明")
    TRADINGPLACE = Column(String(40), doc="场所")
    TRADINGPLACECODE = Column(DECIMAL(9, 0), doc="投资群体代码")
    USED = Column(DECIMAL(1, 0), doc="是否有效")


class CMFTHEMECONCEPT(Base):

    __tablename__ = 'CMFTHEMECONCEPT'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_NAME = Column(String(100), doc="板块名称")
    S_INFO_SECTOR = Column(String(16), doc="板块代码")
    S_INFO_WINDCODE = Column(String(40), doc="成份万得代码")


class CMFTRADINGSUSPENSION(Base):

    __tablename__ = 'CMFTRADINGSUSPENSION'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_DQ_CHANGEREASON = Column(String(400), doc="停牌原因")
    S_DQ_RESUMPDATE = Column(String(8), doc="复牌日期")
    S_DQ_SUSPENDDATE = Column(String(8), doc="停牌日期")
    S_DQ_SUSPENDTIME = Column(String(200), doc="停复牌时间")
    S_DQ_SUSPENDTYPE = Column(DECIMAL(9, 0), doc="停牌类型代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SEC_ID = Column(String(40), doc="证券id")


class CMFUNDOPERATEPERIOD(Base):

    __tablename__ = 'CMFUNDOPERATEPERIOD'

    ANNUALYEILD = Column(DECIMAL(20, 4), doc="实际年化收益率")
    ANTICIPATE_ANNUALYEILD = Column(DECIMAL(20, 4), doc="预期年化收益率")
    BATCH1 = Column(DECIMAL(5, 0), doc="批次")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    OPR_ENDDT = Column(String(8), doc="运作结束日")
    OPR_PERIOD = Column(DECIMAL(10, 0), doc="期数")
    OPR_STARTDT = Column(String(8), doc="运作起始日")
    PCH_ENDDT = Column(String(8), doc="开放申购截止日")
    PCH_STARTDT = Column(String(8), doc="开放申购起始日")
    REDM_ENDDT = Column(String(8), doc="开放赎回截止日")
    REDM_STARTDT = Column(String(8), doc="开放赎回起始日")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CMMFPORTFOLIOPTM(Base):

    __tablename__ = 'CMMFPORTFOLIOPTM'

    ANN_DT = Column(String(8), doc="公告日期")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    F_PTM_BOTTOM = Column(DECIMAL(20, 4), doc="剩余期上限")
    F_PTM_TOP = Column(DECIMAL(20, 4), doc="剩余期下限")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RATIO_ASSERT_NAV = Column(DECIMAL(20, 4), doc="资产占净值比例(%)")
    RATIO_LIAB_NAV = Column(DECIMAL(20, 4), doc="负债占净值比例(%)")
    REPORT_PERIOD = Column(String(8), doc="报告期")
    TYPECODE = Column(String(200), doc="类型")


class CMMQUARTERLYDATA(Base):

    __tablename__ = 'CMMQUARTERLYDATA'

    ANN_DATE = Column(String(8), doc="公告日期")
    AVG_REMAINDER_PERIOD_MAX = Column(DECIMAL(20, 4), doc="报告期内投资组合平均剩余期限最高值")
    AVG_REMAINDER_PERIOD_MIN = Column(DECIMAL(20, 4), doc="报告期内投资组合平均剩余期限最低值")
    BONDREPO_BALANCE = Column(DECIMAL(20, 4), doc="报告期内债券回购融资余额")
    BONDREPO_BALANCE_RATIO = Column(DECIMAL(20, 4), doc="报告期内债券回购融资余额占资产净值的比例(%)")
    DEVIATION_DEGREE_AVG_VALUE = Column(DECIMAL(20, 4), doc="报告期内每个工作日偏离度的绝对值的简单平均值(%)")
    DEVIATION_DEGREE_FREQUENCY = Column(DECIMAL(20, 4), doc="报告期内偏离度的绝对值在0.25％(含)－0.5％间的次数")
    DEVIATION_DEGREE_MAX = Column(DECIMAL(20, 4), doc="报告期内偏离度的最高值(%)")
    DEVIATION_DEGREE_MIN = Column(DECIMAL(20, 4), doc="报告期内偏离度的最低值(%)")
    END_BONDREPO_BALANCE = Column(DECIMAL(20, 4), doc="报告期末债券回购融资余额")
    END_BONDREPO_BALANCE_RATIO = Column(DECIMAL(20, 4), doc="报告期末债券回购融资余额占资产净值的比例(%)")
    F_INFO_BGNDATE = Column(String(8), doc="报告期起始日期")
    F_INFO_ENDDATE = Column(String(8), doc="报告期截止日期")
    FIXED_DEPOSIT = Column(DECIMAL(20, 4), doc="商业银行定期存款")
    FLOATING_BOND_AMOUNT = Column(DECIMAL(20, 4), doc="剩余存续期超过397天的浮动利率债券金额")
    FLOATING_BOND_AMOUNT_RATIO = Column(DECIMAL(20, 4), doc="剩余存续期超过397天的浮动利率债券占资产净值比例(%)")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CMONEYMARKETDAILYFINCOME(Base):

    __tablename__ = 'CMONEYMARKETDAILYFINCOME'

    ANN_DATE = Column(String(8), doc="公告日期")
    F_ACCUNITNAV = Column(DECIMAL(20, 4), doc="累计单位净值")
    F_INCOME_PER_MILLION = Column(DECIMAL(20, 5), doc="万份收益")
    F_INFO_BGNDATE = Column(String(8), doc="起始日期")
    F_INFO_ENDDATE = Column(String(8), doc="截止日期")
    F_INFO_UNITYIELD = Column(DECIMAL(20, 4), doc="单位净值")
    F_INFO_YEARLYROE = Column(DECIMAL(20, 4), doc="七日年化收益率")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CMONEYMARKETFINCOME(Base):

    __tablename__ = 'CMONEYMARKETFINCOME'

    ANN_DATE = Column(String(8), doc="公告日期")
    F_INFO_BGNDATE = Column(String(8), doc="起始日期")
    F_INFO_ENDDATE = Column(String(8), doc="截止日期")
    F_INFO_UNITYIELD = Column(DECIMAL(20, 5), doc="每万份基金单位收益")
    F_INFO_YEARLYROE = Column(DECIMAL(20, 4), doc="最近七日收益所折算的年资产收益率")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class CMONEYMARKETFSCARRYOVERM(Base):

    __tablename__ = 'CMONEYMARKETFSCARRYOVERM'

    CHANGE_DATE = Column(String(8), doc="变动日期")
    F_INFO_INCOMESCARRYOVERDTCODE = Column(DECIMAL(9, 0), doc="收益分配份额结转日期类型代码")
    F_INFO_INCOMESCARRYOVERM = Column(String(20), doc="收益分配份额结转方式")
    F_IS_NEW = Column(DECIMAL(1, 0), doc="是否最新")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_WINDCODE = Column(String(40), doc="基金Wind代码")


class CODEANDSNAME(Base):

    __tablename__ = 'CODEANDSNAME'

    BEGINDATE = Column(String(8), doc="代码有效起始日期")
    ENDDATE = Column(String(8), doc="代码有效截止日期")
    IS_COMMON = Column(DECIMAL(1, 0), doc="是否通用代码")
    MEMO = Column(String(800), doc="备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CODE = Column(String(40), doc="业务代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_SNAME = Column(String(100), doc="业务简称")
    SEC_ID = Column(String(40), doc="证券ID")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="业务类型代码")


class COMPANYPREVIOUSNAME(Base):

    __tablename__ = 'COMPANYPREVIOUSNAME'

    ANN_DT = Column(String(8), doc="公告日期")
    CHANGE_DT = Column(String(8), doc="变动日期")
    CHANGE_REASON = Column(String(100), doc="更名原因")
    COMP_NAME = Column(String(200), doc="公司名称")
    COMP_NAME_ENG = Column(String(200), doc="公司英文名称")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")


class COMPINTRODUCTION(Base):

    __tablename__ = 'COMPINTRODUCTION'

    ADDRESS = Column(String(200), doc="注册地址")
    BRIEFING = Column(String(2000), doc="公司简介")
    BUSINESSSCOPE = Column(LONGTEXT, doc="经营范围")
    CHAIRMAN = Column(String(100), doc="法人代表")
    CITY = Column(String(50), doc="城市")
    COMP_ID = Column(String(40), doc="公司ID")
    COMP_NAME = Column(String(200), doc="公司名称")
    COMP_NAME_ENG = Column(String(100), doc="英文名称")
    COMP_PROPERTY = Column(String(100), doc="企业性质")
    COMP_SNAME = Column(String(40), doc="公司中文简称")
    COMP_SNAMEENG = Column(String(100), doc="英文名称缩写")
    COMP_TYPE = Column(String(100), doc="公司类型")
    COMPANY_TYPE = Column(String(10), doc="公司类别")
    COUNTRY = Column(String(20), doc="国籍")
    CURRENCYCODE = Column(String(10), doc="货币代码")
    DISCLOSER = Column(String(500), doc="信息披露人")
    EMAIL = Column(String(200), doc="电子邮件")
    ENDDATE = Column(String(8), doc="公司终止日期")
    FAX = Column(String(50), doc="传真")
    FOUNDDATE = Column(String(8), doc="成立日期")
    IS_LISTED = Column(DECIMAL(1, 0), doc="是否上市公司")
    MAIN_BUSINESS = Column(String(1000), doc="主要产品及业务")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OFFICE = Column(String(400), doc="办公地址")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PHONE = Column(String(50), doc="电话")
    PRESIDENT = Column(String(100), doc="总经理")
    PROVINCE = Column(String(20), doc="省份")
    REGCAPITAL = Column(DECIMAL(20, 4), doc="注册资本")
    REGISTERNUMBER = Column(String(20), doc="统一社会信用代码")
    S_INFO_COMPTYPE = Column(String(10), doc="公司类型")
    S_INFO_ORG_CODE = Column(String(30), doc="组织机构代码")
    S_INFO_TOTALEMPLOYEES = Column(DECIMAL(20, 0), doc="员工总数(人)")
    SOCIAL_CREDIT_CODE = Column(String(30), doc="统一社会信用编码(废弃)")
    WEBSITE = Column(String(200), doc="公司网址")
    ZIPCODE = Column(String(10), doc="邮编")


class COMPORGANIZATIONCODE(Base):

    __tablename__ = 'COMPORGANIZATIONCODE'

    COMP_ID = Column(String(40), doc="公司ID")
    IS_COMMON = Column(DECIMAL(1, 0), doc="是否通用代码")
    MEMO = Column(String(800), doc="备注")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_CODE = Column(String(40), doc="业务代码")
    S_SNAME = Column(String(100), doc="业务名称")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="业务类型代码")


class COUNTRYANDAREACODE(Base):

    __tablename__ = 'COUNTRYANDAREACODE'

    CONTINENT = Column(String(20), doc="所属洲")
    COUNTRY_CODE_2 = Column(String(10), doc="国家及地区代码(2位)")
    COUNTRY_CODE_3 = Column(String(10), doc="国家及地区代码(3位)")
    IS_VALID = Column(DECIMAL(5, 0), doc="是否有效")
    NAME = Column(String(40), doc="国家及地区名称")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RELEASE_DATE = Column(DateTime, doc="发布日期")


class COUNTRYANDAREACODEZL(Base):

    __tablename__ = 'COUNTRYANDAREACODEZL'

    CONTINENT = Column(String(20), doc="所属洲")
    COUNTRY_CODE_2 = Column(String(10), doc="国家及地区代码(2位)")
    COUNTRY_CODE_3 = Column(String(10), doc="国家及地区代码(3位)")
    IS_VALID = Column(DECIMAL(5, 0), doc="是否有效")
    NAME1 = Column(String(40), doc="国家及地区名称")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    RELEASE_DATE = Column(DateTime, doc="发布日期")


class CPFUNDDESCRIPTION(Base):

    __tablename__ = 'CPFUNDDESCRIPTION'

    ANN_DT = Column(String(8), doc="公告日期")
    CP_PERIOD = Column(DECIMAL(20, 4), doc="保本周期(年)")
    END_DT = Column(String(8), doc="保本周期终止日期")
    F_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    GUARANT_FEE = Column(DECIMAL(20, 4), doc="保证费率(%)")
    GUARANTOR = Column(String(200), doc="保证人名称")
    GUARANTOR_INFO = Column(String(800), doc="保证人简介")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    START_DT = Column(String(8), doc="保本周期起始日期")
    TRIGGER_INFO = Column(String(2000), doc="触发机制说明")
    TRIGGER_YIELD = Column(DECIMAL(20, 4), doc="触发收益率(%)")


class CURRENCYCODE(Base):

    __tablename__ = 'CURRENCYCODE'

    CRNCY_NAME = Column(String(40), doc="货币名称")
    CURRENCY_CODE = Column(String(10), doc="货币代码")
    LATEST_LOGO = Column(DECIMAL(1, 0), doc="最新标志")
    MAIN_CURRENCY_CODE = Column(String(10), doc="主币货币代码")
    MAIN_CURRENCY_RATIO = Column(DECIMAL(20, 0), doc="主辅币比例")
    MEMO = Column(String(100), doc="备注")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PIP_VALUE = Column(DECIMAL(20, 4), doc="pip value")


class ETFPCHREDM(Base):

    __tablename__ = 'ETFPCHREDM'

    CONVERSION_DT = Column(String(8), doc="份额折算日")
    CONVERSION_RATIO = Column(DECIMAL(20, 8), doc="份额折算比例")
    LIST_DT = Column(String(8), doc="上市日期")
    LIST_SHARE = Column(DECIMAL(20, 4), doc="上市交易份额")
    NETWORKCASHBUYDOWNLIMIT = Column(DECIMAL(20, 4), doc="网上现金认购份额下限(份)")
    NETWORKCASHBUYENDDT = Column(String(8), doc="网上现金认购截止日")
    NETWORKCASHBUYSTARTDT = Column(String(8), doc="网上现金认购起始日")
    NETWORKCASHBUYUPLIMIT = Column(DECIMAL(20, 4), doc="网上现金认购份额上限(份)")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OFFNETWORKBUYENDDT = Column(String(8), doc="网下现金认购截止日")
    OFFNETWORKBUYSTARTDT = Column(String(8), doc="网下现金认购起始日")
    OFFNETWORKCASHBUYDOWNLIMIT = Column(DECIMAL(20, 4), doc="网下现金认购份额下限(份)")
    ONLINE_OFFERING_CODE = Column(String(10), doc="网上现金发售代码")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PCH_CODE = Column(String(10), doc="申购赎回代码")
    PCH_NAME = Column(String(40), doc="申购赎回简称")
    PCH_START_DT = Column(String(8), doc="申购起始日")
    REDM_START_DT = Column(String(8), doc="赎回起始日")
    S_INFO_EXCHMARKET = Column(String(20), doc="交易所")
    S_INFO_WINDCODE = Column(String(40), doc="基金Wind代码")


class FINANCIALQUALIFICATION(Base):

    __tablename__ = 'FINANCIALQUALIFICATION'

    ACQUISITION_DATE = Column(String(8), doc="获得日期")
    AGENCY_TYPCODE = Column(String(80), doc="机构类型")
    FINANCIAL_TYPE = Column(String(100), doc="金融机构资格类型")
    FINANCIAL_TYPE_NUM = Column(DECIMAL(9, 0), doc="金融机构资格类型代码")
    IS_EFFECTIVE = Column(DECIMAL(5, 0), doc="是否有效")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    ORGANIZATION_NAME = Column(String(100), doc="机构公布名称")
    QUALIFICATION_CODE = Column(String(100), doc="资格编码")
    REVOKE_DATE = Column(String(8), doc="撤销日期")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_NAME = Column(String(200), doc="公司简称")


class FINDEXPERFORMANCE(Base):

    __tablename__ = 'FINDEXPERFORMANCE'

    ANNUALYEILD = Column(DECIMAL(20, 6), doc="年化收益率")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PCT_CHG_RECENT1M = Column(DECIMAL(20, 6), doc="最近1月涨跌幅")
    PCT_CHG_RECENT1W = Column(DECIMAL(20, 6), doc="最近1周涨跌幅")
    PCT_CHG_RECENT1Y = Column(DECIMAL(20, 6), doc="最近1年涨跌幅")
    PCT_CHG_RECENT2Y = Column(DECIMAL(20, 6), doc="最近2年涨跌幅")
    PCT_CHG_RECENT3M = Column(DECIMAL(20, 6), doc="最近3月涨跌幅")
    PCT_CHG_RECENT3Y = Column(DECIMAL(20, 6), doc="最近3年涨跌幅")
    PCT_CHG_RECENT4Y = Column(DECIMAL(20, 6), doc="最近4年涨跌幅")
    PCT_CHG_RECENT5Y = Column(DECIMAL(20, 6), doc="最近5年涨跌幅")
    PCT_CHG_RECENT6M = Column(DECIMAL(20, 6), doc="最近6月涨跌幅")
    PCT_CHG_RECENT6Y = Column(DECIMAL(20, 6), doc="最近6年涨跌幅")
    PCT_CHG_THISMONTH = Column(DECIMAL(20, 6), doc="本月以来涨跌幅")
    PCT_CHG_THISQUARTER = Column(DECIMAL(20, 6), doc="本季以来涨跌幅")
    PCT_CHG_THISWEEK = Column(DECIMAL(20, 6), doc="本周以来涨跌幅")
    PCT_CHG_THISYEAR = Column(DECIMAL(20, 6), doc="本年以来涨跌幅")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SHARPRATIO_1Y = Column(DECIMAL(20, 6), doc="1年夏普比率")
    SHARPRATIO_2Y = Column(DECIMAL(20, 6), doc="2年夏普比率")
    SHARPRATIO_3Y = Column(DECIMAL(20, 6), doc="3年夏普比率")
    SHARPRATIO_6M = Column(DECIMAL(20, 6), doc="6个月夏普比率")
    SI_PCT_CHG = Column(DECIMAL(20, 6), doc="发布以来涨跌幅")
    STD_DEV_1Y = Column(DECIMAL(20, 6), doc="1年标准差")
    STD_DEV_2Y = Column(DECIMAL(20, 6), doc="2年标准差")
    STD_DEV_3Y = Column(DECIMAL(20, 6), doc="3年标准差")
    STD_DEV_6M = Column(DECIMAL(20, 6), doc="6个月标准差")
    TRADE_DT = Column(String(8), doc="交易日期")


class FUNDCREDITRECORD(Base):

    __tablename__ = 'FUNDCREDITRECORD'

    ANN_DATE = Column(String(8), doc="公告日期")
    BUSINESS_RESTRICTIVE_MEASURES = Column(DECIMAL(9, 0), doc="业务资格限制措施代码")
    DEBAR_MEASURES_CODE = Column(DECIMAL(9, 0), doc="市场禁入措施代码")
    DETAILED_CONTENT = Column(LONGTEXT, doc="详细内容")
    EFFECTIVE_DATE = Column(String(8), doc="生效日期")
    EVENT_ID = Column(String(20), doc="事件ID")
    INSTITUTION_ID = Column(String(10), doc="处罚时所在机构ID")
    INVOLVING_COMP_ID = Column(String(10), doc="涉及公司ID")
    IRREGULARITIES = Column(String(1000), doc="违规事项")
    IS_EFFECTIVE = Column(DECIMAL(1, 0), doc="是否生效")
    LEGAL_BASIS = Column(String(1000), doc="法律依据")
    MEASURES_DISPOSITION = Column(String(1000), doc="处分措施")
    MEASURES_DISPOSITION_CODE = Column(DECIMAL(9, 0), doc="处分措施代码")
    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PENALTY_AMOUNT = Column(DECIMAL(24, 8), doc="处罚金额")
    PUNISHMENT_MEASURES_CODE = Column(DECIMAL(9, 0), doc="处罚措施代码")
    PUNISHMENT_TIME_CODE = Column(DECIMAL(9, 0), doc="处分期限代码")
    REGULATORS_ID = Column(String(10), doc="监管机构ID")
    REGULATORY_OBJECT_CODE = Column(DECIMAL(9, 0), doc="监管对象类别代码")
    REGULATORY_OBJECT_ID = Column(String(10), doc="监管对象ID")
    REGULATORY_OBJECT_NAME = Column(String(100), doc="监管对象名称")
    REGULATORY_OBJECT_TYPE = Column(DECIMAL(9, 0), doc="监管对象类型代码")
    TYPE_CODE = Column(DECIMAL(9, 0), doc="业务类型代码")


class GLOBALMARKETTRADINGTIME(Base):

    __tablename__ = 'GLOBALMARKETTRADINGTIME'

    EXCHANGE_ENG_NAME = Column(String(200), doc="交易所英文名称")
    EXCHANGE_NAME = Column(String(40), doc="交易所中文名称")
    EXCHANGE_SNAME_ENG = Column(String(40), doc="交易所英文简称")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    SECURITIES_TYPE = Column(String(1000), doc="交易品种描述")
    TRADING_HOURS = Column(String(500), doc="交易时段")
    TRADING_HOURS_2 = Column(String(1000), doc="交易时段(新)")
    TRADING_HOURS_CODE = Column(String(5), doc="交易时段编码")


class GLOBALWORKINGDAY(Base):

    __tablename__ = 'GLOBALWORKINGDAY'

    COUNTRY_CODE = Column(String(10), doc="国家或地区代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    WORKING_DATE = Column(String(8), doc="日期")


class INDEXCONTRASTSECTOR(Base):

    __tablename__ = 'INDEXCONTRASTSECTOR'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_INDEXCODE = Column(String(40), doc="指数万得代码")
    S_INFO_INDUSTRYCODE = Column(String(16), doc="板块代码")
    S_INFO_INDUSTRYCODE2 = Column(String(16), doc="板块代码2")
    S_INFO_INDUSTRYNAME = Column(String(50), doc="板块名称")
    S_INFO_INDUSTRYNAME_ENG = Column(String(200), doc="板块英文名称")
    S_INFO_NAME = Column(String(50), doc="指数简称")


class LOFDESCRIPTION(Base):

    __tablename__ = 'LOFDESCRIPTION'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_LISTBOARDNAME = Column(String(10), doc="上市板")
    S_INFO_LISTDATE = Column(String(8), doc="上市日期")
    S_INFO_OUTSTANDINGBALANCE = Column(DECIMAL(20, 4), doc="上市交易份额")
    S_INFO_WINDCODE = Column(String(40), doc="wind代码")


class LOFPCHREDM(Base):

    __tablename__ = 'LOFPCHREDM'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    PCH_CODE = Column(String(20), doc="场内申购赎回基金代码")
    PCH_NAME = Column(String(40), doc="场内申购赎回基金简称")
    PCH_START_DT = Column(String(8), doc="场内申购起始日")
    REDM_START_DT = Column(String(8), doc="场内赎回起始日")
    S_INFO_EXCHMARKET = Column(String(20), doc="交易所")
    S_INFO_WINDCODE = Column(String(40), doc="基金Wind代码")
    SUBSTRIPTION_CODE = Column(String(20), doc="场内认购基金代码")
    SUBSTRIPTION_END_DT = Column(String(8), doc="场内认购截止日")
    SUBSTRIPTION_NAME = Column(String(40), doc="场内认购基金简称")
    SUBSTRIPTION_PRICE = Column(DECIMAL(20, 4), doc="场内认购价格")
    SUBSTRIPTION_START_DT = Column(String(8), doc="场内认购起始日")


class RALATEDSECURITIESCODE(Base):

    __tablename__ = 'RALATEDSECURITIESCODE'

    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_EFFECTIVE_DT = Column(String(8), doc="生效日期")
    S_INFO_INVALID_DT = Column(String(8), doc="失效日期")
    S_INFO_RALATEDCODE = Column(String(40), doc="关联证券Wind代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    S_RELATION_TYPCODE = Column(String(10), doc="关系类型代码")


class SHSCCHANNELHOLDINGS(Base):

    __tablename__ = 'SHSCCHANNELHOLDINGS'

    OBJECT_ID = Column(String(38), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_CODE = Column(String(40), doc="[内部]股份代码")
    S_INFO_EXCHMARKETNAME = Column(String(40), doc="交易所英文简称")
    S_INFO_WINDCODE = Column(String(40), doc="WIND代码")
    S_QUANTITY = Column(DECIMAL(20, 4), doc="中央结算系统持股量")
    S_RATIO = Column(DECIMAL(20, 4), doc="[内部]中央结算系统持股量占比")
    TRADE_DT = Column(String(8), doc="持股日期")


class SHSCDAILYSTATISTICS(Base):

    __tablename__ = 'SHSCDAILYSTATISTICS'

    ITEM_CODE = Column(DECIMAL(9, 0), doc="项目代码")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_EXCHMARKET = Column(String(40), doc="交易所英文简称")
    TRADE_DT = Column(String(100), doc="日期")
    UNIT = Column(String(20), doc="单位")
    VALUE = Column(DECIMAL(20, 4), doc="数据")


class WINDCUSTOMCODE(Base):

    __tablename__ = 'WINDCUSTOMCODE'

    CRNCY_CODE = Column(String(10), doc="币种编号")
    CRNCY_NAME = Column(String(40), doc="币种")
    EXCHMARKET = Column(String(10), doc="交易所")
    OBJECT_ID = Column(String(100), primary_key=True, doc="%s")
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    S_INFO_ASHARECODE = Column(String(10), doc="证券ID")
    S_INFO_CODE = Column(String(40), doc="交易代码")
    S_INFO_COMPCODE = Column(String(10), doc="公司ID")
    S_INFO_COUNTRYCODE = Column(String(10), doc="国别编号")
    S_INFO_COUNTRYNAME = Column(String(100), doc="国别")
    S_INFO_ENAME = Column(String(200), doc="证券英文简称")
    S_INFO_EXCHMARKET = Column(String(10), doc="交易所编号")
    S_INFO_EXCHMARKETNAME = Column(String(40), doc="交易所")
    S_INFO_ISINCODE = Column(String(40), doc="ISIN代码")
    S_INFO_LOT_SIZE = Column(DECIMAL(20, 4), doc="每手数量")
    S_INFO_MIN_PRICE_CHG_UNIT = Column(DECIMAL(24, 8), doc="最小价格变动单位")
    S_INFO_NAME = Column(String(50), doc="证券中文简称")
    S_INFO_ORG_CODE = Column(String(20), doc="组织机构代码")
    S_INFO_PINYIN = Column(String(40), doc="简称拼音")
    S_INFO_SECTYPEBCODE = Column(DECIMAL(9, 0), doc="品种大类代码")
    S_INFO_SECTYPENAME = Column(String(40), doc="类型名称")
    S_INFO_SECTYPESCODE = Column(DECIMAL(9, 0), doc="品种细类代码")
    S_INFO_SECURITIESTYPES = Column(String(10), doc="证券类型")
    S_INFO_TYPECODE = Column(DECIMAL(9, 0), doc="分类代码")
    S_INFO_WINDCODE = Column(String(40), doc="Wind代码")
    SECURITY_STATUS = Column(DECIMAL(9, 0), doc="存续状态")
    TRADING_HOURS_CODE = Column(String(10), doc="交易时段编码")


class WIND_PDUPDATE_LOG(Base):

    __tablename__ = 'WIND_PDUPDATE_LOG'

    CURFILE = Column(String(512))
    CURFILEDESC = Column(String(1000))
    CURFILETIME = Column(DateTime)
    OPDATE = Column(DateTime)
    OPMODE = Column(String(1))
    SERVERFILE = Column(String(512))
    SERVERFILETIME = Column(DateTime)
    TABLENAME = Column(String(40), primary_key=True)


wind_class_dict = {
    'AEQUFROPLEINFOREPPEREND': AEQUFROPLEINFOREPPEREND,
    'AINDEXCSI500WEIGHT': AINDEXCSI500WEIGHT,
    'AINDEXDESCRIPTION': AINDEXDESCRIPTION,
    'AINDEXEODPRICES': AINDEXEODPRICES,
    'AINDEXFINANCIALDERIVATIVE': AINDEXFINANCIALDERIVATIVE,
    'AINDEXHS300CLOSEWEIGHT': AINDEXHS300CLOSEWEIGHT,
    'AINDEXHS300WEIGHT': AINDEXHS300WEIGHT,
    'AINDEXINDUSTRIESEODCITICS': AINDEXINDUSTRIESEODCITICS,
    'AINDEXMEMBERS': AINDEXMEMBERS,
    'AINDEXMEMBERSCITICS': AINDEXMEMBERSCITICS,
    'AINDEXMEMBERSCITICS2': AINDEXMEMBERSCITICS2,
    'AINDEXMEMBERSCITICS2ZL': AINDEXMEMBERSCITICS2ZL,
    'AINDEXMEMBERSCITICS3': AINDEXMEMBERSCITICS3,
    'AINDEXMEMBERSCITICSZL': AINDEXMEMBERSCITICSZL,
    'ASAREPLANTRADE': ASAREPLANTRADE,
    'ASHAREACCOUNTSPAYABLE': ASHAREACCOUNTSPAYABLE,
    'ASHAREADMINISTRATION': ASHAREADMINISTRATION,
    'ASHAREANNFINANCIALINDICATOR': ASHAREANNFINANCIALINDICATOR,
    'ASHAREAUDITOPINION': ASHAREAUDITOPINION,
    'ASHAREBALANCESHEET': ASHAREBALANCESHEET,
    'ASHAREBANKINDICATOR': ASHAREBANKINDICATOR,
    'ASHAREBEGUARANTEED': ASHAREBEGUARANTEED,
    'ASHARECALENDAR': ASHARECALENDAR,
    'ASHARECAPITALIZATION': ASHARECAPITALIZATION,
    'ASHARECAPITALOPERATION': ASHARECAPITALOPERATION,
    'ASHARECASHFLOW': ASHARECASHFLOW,
    'ASHARECIRCULATINGHOLDERS': ASHARECIRCULATINGHOLDERS,
    'ASHARECOCAPITALOPERATION': ASHARECOCAPITALOPERATION,
    'ASHARECOMPANYHOLDSHARES': ASHARECOMPANYHOLDSHARES,
    'ASHARECONCEPTUALPLATE': ASHARECONCEPTUALPLATE,
    'ASHARECREDITORRIGHTS': ASHARECREDITORRIGHTS,
    'ASHARECUSTOMER': ASHARECUSTOMER,
    'ASHAREDEFENDANT': ASHAREDEFENDANT,
    'ASHAREDESCRIPTION': ASHAREDESCRIPTION,
    'ASHAREDIRECTOR': ASHAREDIRECTOR,
    'ASHAREDIVIDEND': ASHAREDIVIDEND,
    'ASHAREEARNINGEST': ASHAREEARNINGEST,
    'ASHAREEODPRICES': ASHAREEODPRICES,
    'ASHAREEQUFROINFO': ASHAREEQUFROINFO,
    'ASHAREEQUITYPLEDGEINFO': ASHAREEQUITYPLEDGEINFO,
    'ASHAREEQUITYRELATIONSHIPS': ASHAREEQUITYRELATIONSHIPS,
    'ASHAREESOPDESCRIPTION': ASHAREESOPDESCRIPTION,
    'ASHAREESOPTRADINGINFO': ASHAREESOPTRADINGINFO,
    'ASHAREFINANCIALDERIVATIVE': ASHAREFINANCIALDERIVATIVE,
    'ASHAREFINANCIALINDICATOR': ASHAREFINANCIALINDICATOR,
    'ASHAREFLOATHOLDER': ASHAREFLOATHOLDER,
    'ASHAREFREEFLOAT': ASHAREFREEFLOAT,
    'ASHAREGROUP': ASHAREGROUP,
    'ASHAREGROUPINFORMATION': ASHAREGROUPINFORMATION,
    'ASHAREGUARANTEERELATIONSHIP': ASHAREGUARANTEERELATIONSHIP,
    'ASHAREGUARANTEESTATISTICS': ASHAREGUARANTEESTATISTICS,
    'ASHAREHOLDER': ASHAREHOLDER,
    'ASHAREHOLDERNUMBER': ASHAREHOLDERNUMBER,
    'ASHAREHOLDING': ASHAREHOLDING,
    'ASHAREIBROKERINDICATOR': ASHAREIBROKERINDICATOR,
    'ASHAREILLEGALITY': ASHAREILLEGALITY,
    'ASHAREINCDESCRIPTION': ASHAREINCDESCRIPTION,
    'ASHAREINCEXECQTYPRI': ASHAREINCEXECQTYPRI,
    'ASHAREINCEXERCISEPCT': ASHAREINCEXERCISEPCT,
    'ASHAREINCEXERCISEPCTZL': ASHAREINCEXERCISEPCTZL,
    'ASHAREINCOME': ASHAREINCOME,
    'ASHAREINCQUANTITYDETAILS': ASHAREINCQUANTITYDETAILS,
    'ASHAREINCQUANTITYPRICE': ASHAREINCQUANTITYPRICE,
    'ASHAREINDUSRATING': ASHAREINDUSRATING,
    'ASHAREINDUSTRIESCLASSCITICS': ASHAREINDUSTRIESCLASSCITICS,
    'ASHAREINDUSTRIESCLASSCITICSZL': ASHAREINDUSTRIESCLASSCITICSZL,
    'ASHAREINDUSTRIESCODE': ASHAREINDUSTRIESCODE,
    'ASHAREINSIDEHOLDER': ASHAREINSIDEHOLDER,
    'ASHAREINSIDERTRADE': ASHAREINSIDERTRADE,
    'ASHAREINSTHOLDERDERDATA': ASHAREINSTHOLDERDERDATA,
    'ASHAREINSURANCEINDICATOR': ASHAREINSURANCEINDICATOR,
    'ASHAREINTENSITYTREND': ASHAREINTENSITYTREND,
    'ASHAREINTENSITYTRENDADJ': ASHAREINTENSITYTRENDADJ,
    'ASHAREINVESTMENTPEVC': ASHAREINVESTMENTPEVC,
    'ASHAREIPOPRICINGFORECAST': ASHAREIPOPRICINGFORECAST,
    'ASHARELONGLOAN': ASHARELONGLOAN,
    'ASHAREMAJORHOLDERPLANHOLD': ASHAREMAJORHOLDERPLANHOLD,
    'ASHAREMAJORHOLDERPLANHOLDZL': ASHAREMAJORHOLDERPLANHOLDZL,
    'ASHAREMANAGEMENT': ASHAREMANAGEMENT,
    'ASHAREMANAGEMENTHOLDREWARD': ASHAREMANAGEMENTHOLDREWARD,
    'ASHAREMARGINSUBJECT': ASHAREMARGINSUBJECT,
    'ASHAREMARGINTRADE': ASHAREMARGINTRADE,
    'ASHAREMARGINTRADESUM': ASHAREMARGINTRADESUM,
    'ASHAREMECHANISMOWNERSHIP': ASHAREMECHANISMOWNERSHIP,
    'ASHAREMERGERSUBJECT': ASHAREMERGERSUBJECT,
    'ASHAREMJRHOLDERTRADE': ASHAREMJRHOLDERTRADE,
    'ASHAREPEVCINVESTMENT': ASHAREPEVCINVESTMENT,
    'ASHAREPLAINTIFF': ASHAREPLAINTIFF,
    'ASHAREPLEDGEPROPORTION': ASHAREPLEDGEPROPORTION,
    'ASHAREPLEDGETRADE': ASHAREPLEDGETRADE,
    'ASHAREPREVIOUSENNAME': ASHAREPREVIOUSENNAME,
    'ASHAREPRODUCT': ASHAREPRODUCT,
    'ASHAREPROFITEXPRESS': ASHAREPROFITEXPRESS,
    'ASHAREPROFITNOTICE': ASHAREPROFITNOTICE,
    'ASHAREPROSECUTION': ASHAREPROSECUTION,
    'ASHARERECEIVABLES': ASHARERECEIVABLES,
    'ASHAREREGINV': ASHAREREGINV,
    'ASHARERELATEDPARTYDEBT': ASHARERELATEDPARTYDEBT,
    'ASHARERIGHTISSUE': ASHARERIGHTISSUE,
    'ASHARESELLSUBJECT': ASHARESELLSUBJECT,
    'ASHAREST': ASHAREST,
    'ASHARESTAFF': ASHARESTAFF,
    'ASHARESTAFFSTRUCTURE': ASHARESTAFFSTRUCTURE,
    'ASHARESTIBHOLDERVOTE': ASHARESTIBHOLDERVOTE,
    'ASHARESTOCKRATING': ASHARESTOCKRATING,
    'ASHARESUPERVISOR': ASHARESUPERVISOR,
    'ASHARESUPPLIER': ASHARESUPPLIER,
    'ASHARETRADINGSUSPENSION': ASHARETRADINGSUSPENSION,
    'ASHARETYPECODE': ASHARETYPECODE,
    'CFUNDBANKACCOUNT': CFUNDBANKACCOUNT,
    'CFUNDCHANGEWINDCODE': CFUNDCHANGEWINDCODE,
    'CFUNDCODEANDSNAME': CFUNDCODEANDSNAME,
    'CFUNDCOMPANYPREVIOUSNAME': CFUNDCOMPANYPREVIOUSNAME,
    'CFUNDFACTIONALSTYLE': CFUNDFACTIONALSTYLE,
    'CFUNDHOLDRESTRICTEDCIRCULATION': CFUNDHOLDRESTRICTEDCIRCULATION,
    'CFUNDINDEXMEMBERS': CFUNDINDEXMEMBERS,
    'CFUNDINDEXTABLE': CFUNDINDEXTABLE,
    'CFUNDINDUSTRIESCODE': CFUNDINDUSTRIESCODE,
    'CFUNDINTRODUCTION': CFUNDINTRODUCTION,
    'CFUNDMANAGEMENT': CFUNDMANAGEMENT,
    'CFUNDPCHREDM': CFUNDPCHREDM,
    'CFUNDPORTFOLIOCHANGES': CFUNDPORTFOLIOCHANGES,
    'CFUNDPREVIOUSNAME': CFUNDPREVIOUSNAME,
    'CFUNDRALATEDSECURITIESCODE': CFUNDRALATEDSECURITIESCODE,
    'CFUNDRATESENSITIVE': CFUNDRATESENSITIVE,
    'CFUNDSTYLECOEFFICIENT': CFUNDSTYLECOEFFICIENT,
    'CFUNDSTYLETHRESHOLD': CFUNDSTYLETHRESHOLD,
    'CFUNDTACODE': CFUNDTACODE,
    'CFUNDTYPECODE': CFUNDTYPECODE,
    'CFUNDWINDCUSTOMCODE': CFUNDWINDCUSTOMCODE,
    'CFUNDWINDINDEXCOMPONENT': CFUNDWINDINDEXCOMPONENT,
    'CFUNDWINDINDEXMEMBERS': CFUNDWINDINDEXMEMBERS,
    'CHANGEWINDCODE': CHANGEWINDCODE,
    'CHINACLOSEDFUNDEODPRICE': CHINACLOSEDFUNDEODPRICE,
    'CHINAFEEDERFUND': CHINAFEEDERFUND,
    'CHINAGRADINGFUND': CHINAGRADINGFUND,
    'CHINAMFMPERFORMANCE': CHINAMFMPERFORMANCE,
    'CHINAMFPERFORMANCE': CHINAMFPERFORMANCE,
    'CHINAMUTUALFUNDASSETPORTFOLIO': CHINAMUTUALFUNDASSETPORTFOLIO,
    'CHINAMUTUALFUNDBENCHMARK': CHINAMUTUALFUNDBENCHMARK,
    'CHINAMUTUALFUNDBENCHMARKEOD': CHINAMUTUALFUNDBENCHMARKEOD,
    'CHINAMUTUALFUNDBONDPORTFOLIO': CHINAMUTUALFUNDBONDPORTFOLIO,
    'CHINAMUTUALFUNDDESCRIPTION': CHINAMUTUALFUNDDESCRIPTION,
    'CHINAMUTUALFUNDFLOATSHARE': CHINAMUTUALFUNDFLOATSHARE,
    'CHINAMUTUALFUNDINDPORTFOLIO': CHINAMUTUALFUNDINDPORTFOLIO,
    'CHINAMUTUALFUNDMANAGER': CHINAMUTUALFUNDMANAGER,
    'CHINAMUTUALFUNDNAV': CHINAMUTUALFUNDNAV,
    'CHINAMUTUALFUNDPCHREDM': CHINAMUTUALFUNDPCHREDM,
    'CHINAMUTUALFUNDPOSESTIMATION': CHINAMUTUALFUNDPOSESTIMATION,
    'CHINAMUTUALFUNDREPNAVPER': CHINAMUTUALFUNDREPNAVPER,
    'CHINAMUTUALFUNDSEATTRADING': CHINAMUTUALFUNDSEATTRADING,
    'CHINAMUTUALFUNDSECTOR': CHINAMUTUALFUNDSECTOR,
    'CHINAMUTUALFUNDSHARE': CHINAMUTUALFUNDSHARE,
    'CHINAMUTUALFUNDSTOCKPORTFOLIO': CHINAMUTUALFUNDSTOCKPORTFOLIO,
    'CHINAMUTUALFUNDSUSPENDPCHREDM': CHINAMUTUALFUNDSUSPENDPCHREDM,
    'CHINAMUTUALFUNDTRACKINGINDEX': CHINAMUTUALFUNDTRACKINGINDEX,
    'CLOSEDFUNDPCHREDM': CLOSEDFUNDPCHREDM,
    'CMFAIPINFO': CMFAIPINFO,
    'CMFCODEANDSNAME': CMFCODEANDSNAME,
    'CMFCONSEPTION': CMFCONSEPTION,
    'CMFDESCCHANGE': CMFDESCCHANGE,
    'CMFFAIRVALUECHANGEPROFIT': CMFFAIRVALUECHANGEPROFIT,
    'CMFFIXEDINVESTMENTRATE': CMFFIXEDINVESTMENTRATE,
    'CMFHOLDER': CMFHOLDER,
    'CMFHOLDERSTRUCTURE': CMFHOLDERSTRUCTURE,
    'CMFHOLDINGRATIOANOMALY': CMFHOLDINGRATIOANOMALY,
    'CMFINDEXDESCRIPTION': CMFINDEXDESCRIPTION,
    'CMFINDEXEOD': CMFINDEXEOD,
    'CMFINDUSTRYPLATE': CMFINDUSTRYPLATE,
    'CMFIOPVNAV': CMFIOPVNAV,
    'CMFNAVOPERATIONRECORD': CMFNAVOPERATIONRECORD,
    'CMFOTHERPORTFOLIO': CMFOTHERPORTFOLIO,
    'CMFPREFERENTIALFEE': CMFPREFERENTIALFEE,
    'CMFPROPORTIONOFINVEOBJ': CMFPROPORTIONOFINVEOBJ,
    'CMFRISKLEVEL': CMFRISKLEVEL,
    'CMFSECCLASS': CMFSECCLASS,
    'CMFSELLINGAGENTS': CMFSELLINGAGENTS,
    'CMFSUBREDFEE': CMFSUBREDFEE,
    'CMFTHEMECONCEPT': CMFTHEMECONCEPT,
    'CMFTRADINGSUSPENSION': CMFTRADINGSUSPENSION,
    'CMFUNDOPERATEPERIOD': CMFUNDOPERATEPERIOD,
    'CMMFPORTFOLIOPTM': CMMFPORTFOLIOPTM,
    'CMMQUARTERLYDATA': CMMQUARTERLYDATA,
    'CMONEYMARKETDAILYFINCOME': CMONEYMARKETDAILYFINCOME,
    'CMONEYMARKETFINCOME': CMONEYMARKETFINCOME,
    'CMONEYMARKETFSCARRYOVERM': CMONEYMARKETFSCARRYOVERM,
    'CODEANDSNAME': CODEANDSNAME,
    'COMPANYPREVIOUSNAME': COMPANYPREVIOUSNAME,
    'COMPINTRODUCTION': COMPINTRODUCTION,
    'COMPORGANIZATIONCODE': COMPORGANIZATIONCODE,
    'COUNTRYANDAREACODE': COUNTRYANDAREACODE,
    'COUNTRYANDAREACODEZL': COUNTRYANDAREACODEZL,
    'CPFUNDDESCRIPTION': CPFUNDDESCRIPTION,
    'CURRENCYCODE': CURRENCYCODE,
    'ETFPCHREDM': ETFPCHREDM,
    'FINANCIALQUALIFICATION': FINANCIALQUALIFICATION,
    'FINDEXPERFORMANCE': FINDEXPERFORMANCE,
    'FUNDCREDITRECORD': FUNDCREDITRECORD,
    'GLOBALMARKETTRADINGTIME': GLOBALMARKETTRADINGTIME,
    'GLOBALWORKINGDAY': GLOBALWORKINGDAY,
    'INDEXCONTRASTSECTOR': INDEXCONTRASTSECTOR,
    'LOFDESCRIPTION': LOFDESCRIPTION,
    'LOFPCHREDM': LOFPCHREDM,
    'RALATEDSECURITIESCODE': RALATEDSECURITIESCODE,
    'SHSCCHANNELHOLDINGS': SHSCCHANNELHOLDINGS,
    'SHSCDAILYSTATISTICS': SHSCDAILYSTATISTICS,
    'WINDCUSTOMCODE': WINDCUSTOMCODE,
    'WIND_PDUPDATE_LOG': WIND_PDUPDATE_LOG,
}
