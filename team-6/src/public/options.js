function $$(el) {
  return document.getElementById(el);
}

const orientations_price = echarts.init($$('orientations_price'));
const areas_price = echarts.init($$('areas_price'));
const propertyType_avg = echarts.init($$('propertyType_avg'));
const areas_propertyPrice = echarts.init($$('areas_propertyPrice'));
const households_buildingArea = echarts.init($$('households_buildingArea'));
const avg_propertyPrice = echarts.init($$('avg_propertyPrice'));
