=============
install
=============

.. note::

    simons目前处于活跃开发状态(alpha版本)，API接口设计和文档会时常变化

option1: from source
---------------------------------
.. code-block:: bash

    $ git clone https://github.com/quantitative-trading-research/simonsc
    $ cd simonsc
    $ python setup.py develop


===============
quick-start
===============

.. code-block:: python
   
    
    from simonsc import auth
    #login
    auth(username="quantresearch", password="quantresearch")
    
    
    import pandas as pd
    from simonsc.api import history_bars
    
    # 获取中国平安 2020-04-20之前10天的交易数据
    dt = pd.Timestamp("2020-04-20")
    fields=["datetime","open","high","low","close"]
    data = history_bars(order_book_id="000001.XSHE", dt=dt, bar_count=10, frequency="1d", fields=fields)

    Out[1]: 
    array([(20200407000000, 12.89, 12.94, 12.81, 12.88),
           (20200408000000, 12.88, 12.92, 12.72, 12.78),
           (20200409000000, 12.88, 12.89, 12.72, 12.74),
           (20200410000000, 12.76, 12.98, 12.65, 12.79),
           (20200413000000, 12.67, 12.71, 12.47, 12.59),
           (20200414000000, 12.65, 12.86, 12.57, 12.86),
           (20200415000000, 12.86, 12.93, 12.78, 12.87),
           (20200416000000, 12.79, 12.79, 12.54, 12.68),
           (20200417000000, 12.77, 13.04, 12.65, 12.89),
           (20200420000000, 12.86, 13.05, 12.77, 12.99)],
          dtype={'names':['datetime','open','high','low','close'], 'formats':['<i8','<f8','<f8','<f8','<f8'], 'offsets':[0,8,24,32,16], 'itemsize':72})