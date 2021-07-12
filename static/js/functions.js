function message_error(obj) {
    var html = '<ul>';
    $.each(obj, function (key, value) {
        html+='<li>'+key+': '+value+'</li>';
    });
    html+='</ul>';
}