function filter(arr, type, index) {
  return arr.concat().filter(item => item.type === type).map(item => [index, item.avg])
}

function ptavg(res) {
  const data = res['fangs'];
  const city = res['city'];
  propertyType_avg.hideLoading();

  let property_type = [];
  for (const d of data) {
    property_type.push({
      type: d['property_type'],
      avg: parseInt(d['average_price'].replace(' ', ''))
    });
  };
  const zz = filter(property_type, '住宅', 0);
  const sy = filter(property_type, '商业', 1);
  const ds = filter(property_type, '底商', 2);
  const bs = filter(property_type, '别墅', 3);

  const names = ['住宅', '商业', '底商', '别墅'];

  const option = {
    title: {
      text: `${city}房屋物业类型和平均房价分布`,
      subtext: '数据来自：链家网',
      left: 'center'
    },
    legend: {
      data: names,
      right: 0,
      top: '10%',
      orient: 'vertical',
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
        return `<div>类型：${names[params.seriesIndex]}</div><div>均价：${params.value[1]}</div>`
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
      type: 'category',
      data: names,
      name: '类型'
    },
    yAxis: {
      type: 'value',
      name: '平均房价/元'

    },
    series: [{
        name: '住宅',
        type: 'scatter',
        symbolSize: 20,
        data: zz,
      },
      {
        name: '商业',
        type: 'scatter',
        symbolSize: 20,
        data: sy,
      },
      {
        name: '底商',
        type: 'scatter',
        symbolSize: 20,
        data: ds,
      },
      {
        name: '别墅',
        type: 'scatter',
        symbolSize: 20,
        data: bs,
      },
    ]
  };
  propertyType_avg.setOption(option)
}