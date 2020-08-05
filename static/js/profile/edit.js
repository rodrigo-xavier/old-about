$(document).ready(function(){
    // Puta gambiarra, mas dah para fazer melhor. 
    $("input[type='tel']").each(function(){
        
            var output, $this = $(this), input = $this.val();
            
            if (input[0] == '+'){
                input = input.replace(/[^0-9]/g, '');
                input = input.substr(2, 11);
                
                var area = input.substr(0, 2);
                var pre = input.substr(2, 5);
                var tel = input.substr(7, 5);

                if (area.length < 2){
                    output = "(" + area;
                } else if (area.length == 2 && pre.length < 5){
                    output = "(" + area + ")" + " " + pre;
                } else if (area.length == 2 && pre.length == 5){
                    output = "(" + area + ")" + " " + pre + "-" + tel;
                }
                $this.val(output);
            }
            
            $(this).on("change keyup paste", function (e){
                var output, $this = $(this), input = $this.val();

                if(e.keyCode != 8){

                input = input.replace(/[^0-9]/g, '');
                var area = input.substr(0, 2);
                var pre = input.substr(2, 5);
                var tel = input.substr(7, 5);

                if (area.length < 2){
                    output = "(" + area;
                } else if (area.length == 2 && pre.length < 5){
                    output = "(" + area + ")" + " " + pre;
                } else if (area.length == 2 && pre.length == 5){
                    output = "(" + area + ")" + " " + pre + "-" + tel;
                }
                $this.val(output);
            }
        });
    });

    $("label:contains('Delete')").next().hide()
    $("label:contains('Delete')").hide()

    // function save_form(){
    //     var method = $(".cv_edit").attr('method');
    //     if (method == 'post') {
    //         alert("tentando")
    //         $("form").filter('.cv_edit').submit(function(){});
    //         alert("conseguiu")
    //     }
    // }

    // $('[href]').click(function(){
    //     save_form();
    // });
});