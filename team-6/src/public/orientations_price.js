function op(res) {
  orientations_price.hideLoading();
  $('#loading').html('加载完毕！耗时' + res['time']);
  let data = res['fangs'];
  let city = res['city']
  let areas_price = [];
  for (let d of data) {
    let areas = d['areas'].map(area => (parseInt(area.replace('建面', '').replace('㎡', ''))));
    let fang_price = d['fang_price'];
    for (let i = 0; i < areas.length; i++) {
      areas_price.push([areas[i], fang_price[i]]);
    }
  }

  const option = {
    title: {
      text: `${city}房屋面积与其价格的分布`,
      subtext: '数据来自:链家网',
      left: 'center'
    },
    series: [{
      name: '房价',
      type: 'scatter',
      data: areas_price,
      symbolSize: 20,
      itemStyle: {
        normal: {
          color: 'rgba(25, 100, 150, 1)'
        }
      },
      markArea: {
        silent: true,
        itemStyle: {
          normal: {
            color: 'transparent',
            borderWidth: 1,
            borderType: 'dashed'
          }
        },
        data: [
          [{
            name: '房价分布区间',
            xAxis: 'min',
            yAxis: 'min'
          }, {
            xAxis: 'max',
            yAxis: 'max'
          }]
        ]
      },
      markPoint: {
        data: [{
            type: 'max',
            name: '最大值'
          },
          {
            type: 'min',
            name: '最小值'
          }
        ]
      }
    }],
    grid: {
      left: '3%',
      right: '7%',
      bottom: '3%',
      containLabel: true
    },
    tooltip: {
      // trigger: 'axis',
      showDelay: 0,
      formatter: function (params) {
        if (params.value.length > 1) {
          return params.seriesName + ' :<br/>' +
            params.value[0] + '㎡\n' +
            params.value[1] + '万元 ';
        } else {
          return params.seriesName + ' :<br/>' +
            params.name + ' : ' +
            params.value + '万元 ';
        }
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
    toolbox: {
      feature: {
        dataZoom: {},
        brush: {
          type: ['rect', 'polygon', 'clear']
        }
      }
    },
    brush: {},
    xAxis: [{
      type: 'value',
      scale: true,
      name: '房屋面积/㎡',
      splitLine: {
        show: false
      }
    }],
    yAxis: [{
      type: 'value',
      scale: true,
      name: '房价/万元',
      splitLine: {
        show: false
      }
    }]
  };
  orientations_price.setOption(option);
}