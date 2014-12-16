var GNR = {};
GNR.Ui = {};

$(document).ready( function () {
    GNR.init();
});

GNR.init = function () {
    GNR.components = {};
    GNR.components.loader = GNR.Ui.CompanyLoader('#company-details');
}

GNR.Ui.CompanyLoader = function (container) {

    var _loader = {};
    var _container = $(container);

    function init() {
        $('#process-companies').click(function(e){
            e.preventDefault();
            var links = $('.company-link');
            var linkArr = [];
            links.each(function(i){
                var link = $(this).attr('href');
                var comp = $(this).text();
                linkArr.push({link:link, comp:comp});
                //_loader.ProcessCompany(companyRef);
            });
            getLink(linkArr, 0);
        });
        initAjax();
    }

    function getLink(linkArr, curIndex){
        $.ajax(
            {
              type: "POST",
              url: linkArr[curIndex].link,
              success: linkSuccess,
              dataType: 'json',
              complete: linkComplete
            }

        );
        function linkSuccess( data ) {
            _container.removeClass('hidden');
            $('.process-status', _container).html(linkArr[curIndex].comp + '<br>' + JSON.stringify(data));

        }
        function linkComplete(){
            if(curIndex < linkArr.length -1) getLink(linkArr, curIndex+1)
        }
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function initAjax(){
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    _loader.ProcessCompany = function (data) {
        _container.removeClass('hidden');
        $('.process-status', _container).html(data)
    };

    init();
    return _loader;

};