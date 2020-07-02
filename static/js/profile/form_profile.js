$(document).ready(function(){
    $("input[type='tel']").each(function(){
      $(this).on("change keyup paste", function (e){
        var output, $this = $(this), input = $this.val();

        if (input[0] == '+') {
            input = input.replace(/[^0-9]/g, '');
            output = input.substr(2, 11);
            $this.val(output);
        }

        else if(e.keyCode != 8) {
            input = input.replace(/[^0-9]/g, '');
            var area = input.substr(0, 2);
            var pre = input.substr(2, 5);
            var tel = input.substr(7, 5);

            if (area.length < 2) {
                output = "(" + area;
            } else if (area.length == 2 && pre.length < 5) {
                output = "(" + area + ")" + " " + pre;
            } else if (area.length == 2 && pre.length == 5) {
                output = "(" + area + ")" + " " + pre + "-" + tel;
            }
            $this.val(output);
        }
      });
    });

    function remove_non_number() {
        $("tel").replace(/\D/g,'');
    }
  });