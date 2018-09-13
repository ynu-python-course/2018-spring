function avPfee(res) {
  avg_propertyPrice.hideLoading();
  const data = res['fangs'];
  const city = res['city'];

  const avg_fee = []
  for (let d of data) {
    const ap = parseInt(d['average_price'].replace(' ', ''));
    let pf = d['property_fee'];
    pf = pf === '暂无' ? 0 : parseFloat(pf.replace('元/m²/月', ''));
    avg_fee.push([ap, pf]);
  }
  const option = {
    title: {
      text: `${city}物业费用和平均房价分布`,
      subtext: '数据来自：链家网',
      left: 'center'
    },
    toolbox: {
      feature: {
        dataZoom: {},
        brush: {
          type: ['rect', 'polygon', 'clear']
        }
      }
    },
    tooltip: {
      // trigger: 'axis',
      showDelay: 0,
      formatter: function (params) {
        return `<div>物业费用：${params.value[1]} 元/m²/月</div><div>平均房价：${params.value[0]} 元</div>`
      },
      axisPointer: {
        show: true,
        type: 'cross',
        lineStyle: {
          type: 'dashed',
          width: 1
        }
      }
    },
    xAxis: {
      type: 'value',
      name: '平均房价/元',
    },
    yAxis: {
      type: 'value',
      name: '物业费用/ 元/m²/月'
    },
    series: [{
      type: 'scatter',
      symbolSize: 20,
      data: avg_fee
    }]
  };
  avg_propertyPrice.setOption(option)
}