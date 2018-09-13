function aptpr(res) {
  const data = res['fangs'];
  const city = res['city'];
  areas_propertyPrice.hideLoading();
  let propertyPrice = [];
  for (let d of data) {
    let areas = d['areas'].map(area => (parseInt(area.replace('建面', '').replace('㎡', ''))));
    let pp = d['property_fee'];
    pp = pp === '暂无' ? 0 : parseFloat(pp.replace('元/m²/月', ''));
    for (let area of areas) {
      propertyPrice.push([pp, area]);
    }
  }
  const option = {
    title: {
      text: `${city}房屋面积和物业费用分布`,
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
        return `<div>面积：${params.value[0]}</div><div>物业费用：${params.value[1]}</div>`
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
      name: '物业费用/元/m²/月'
    },
    yAxis: {
      type: 'value',
      name: '面积/m²'
    },
    series: [{
      name: 'areas_propertyPrice',
      type: 'scatter',
      symbolSize: 20,
      data: propertyPrice,
    }]
  };
  areas_propertyPrice.setOption(option)
}