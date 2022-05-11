$(document).ready(function (){
    $('#search_button').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search').val();
        $.ajax({
            url: '/?search_filter='+ searchText,
            type: 'GET',
            success: function (resp) {
                console.log(resp.data)
                var newHtml = resp.data.map(d => {
                    return `<div class="eachItem">
                        <a href="/${d.id}">
                            <img class="itemImg" src="${d.firstImage}" />
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                        </a>

                    </div>`
                });
                $(".allItems").html(newHtml.join(''));
                $("#search").val('');
            },
            error: function(xhr, status, error) {
                //TODO: Show toastr
                console.error(error);
            }
        });
    });
});