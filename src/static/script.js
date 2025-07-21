function getDIv () {
    var inpt = $("#inpt").val()
    $.ajax({
        url:`/client/${inpt}`,
        success: (data) => {
            alert(
                `on the ${inpt} ${data.divNum} divs`
            )
        },
        error: () => {
            alert("something went wrong")
        }
    });
}