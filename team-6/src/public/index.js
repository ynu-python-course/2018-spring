$('#analyze').on('click', function () {
  orientations_price.showLoading();
  areas_price.showLoading();
  propertyType_avg.showLoading();
  areas_propertyPrice.showLoading();
  households_buildingArea.showLoading();
  avg_propertyPrice.showLoading();
  $(this).attr("disabled", true);
  $('#loading').html('爬虫正在获取中')
  $.ajax({
    type: 'GET',
    url: '/query',
    data: {
      city: $('#city').val()
    }
  }).done(function (res) {
    $('#analyze').attr("disabled", false);
    op(res);
    aprice(res);
    ptavg(res);
    aptpr(res);
    hb(res);
    avPfee(res)
    console.log(res);
  })
})