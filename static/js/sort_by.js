$(document).ready(function (){
    $('.sort').on('click', function(e) {
        e.preventDefault();
        console.log("Clicking sort by")
        let sort_by_value = e.target.textContent;
        console.log(sort_by_value)
        $.ajax({
            url: '/?sort_by='+ sort_by_value,
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
                $(".sort").val('');
            },
            error: function(xhr, status, error) {
                //TODO: Show toastr
                console.error(error);
            }
        });
    });
});