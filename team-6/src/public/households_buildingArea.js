function hb(res) {
  const data = res['fangs'];
  const city = res['city'];

  households_buildingArea.hideLoading();
  buildingAreas = [];
  for (const d of data) {
    const households = parseInt(d['households']);
    const building_area = parseInt(d['building_area'].replace('㎡').replace(',', '')) / 10000;
    buildingAreas.push([households, building_area]);
  }

  const option = {
    backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
      offset: 0,
      color: '#f7f8fa'
    }, {
      offset: 1,
      color: '#cdd0d5'
    }]),
    title: {
      text: `${city}房区面积和规划户数分布`,
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
        return `<div>房区面积：${params.value[1]} 万m²</div><div>户数：${params.value[0]} 户</div>`
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
      name: '户数/户'
    },
    yAxis: {
      type: 'value',
      name: '万m²'
    },
    series: [{
      type: 'scatter',
      symbolSize: 40,
      itemStyle: {
        normal: {
          shadowBlur: 10,
          shadowColor: 'rgba(25, 100, 150, 0.1)',
          shadowOffsetY: 5,
          color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
            offset: 0,
            color: 'rgb(129, 227, 238)'
          }, {
            offset: 1,
            color: 'rgb(25, 183, 207)'
          }])
        }
      },
      data: buildingAreas
    }]
  };
  households_buildingArea.setOption(option);
}