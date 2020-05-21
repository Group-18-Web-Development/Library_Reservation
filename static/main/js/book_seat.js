function Selected(a) {
  var label = a.value;
    if (label==="quiet")
    {
        document.getElementById("quietmore").style.display='block';
        document.getElementById("noisymore").style.display='none';
    }
    else if (label==="noisy")
    {
        document.getElementById("noisymore").style.display='block';
        document.getElementById("quietmore").style.display='none';
    }
    else
    {
        document.getElementById("noisymore").style.display='none';
        document.getElementById("quietmore").style.display='none';
    }
}
function Confirm(title, msg, $true, $false, $link) {
        var $content =  "<div class='dialog-ovelay'>" +
                        "<div class='dialog'><header>" +
                         " <h3> " + title + " </h3> " +
                         "<i class='fa fa-close'></i>" +
                     "</header>" +
                     "<div class='dialog-msg'>" +
                         " <p> " + msg + " </p> " +
                     "</div>" +
                     "<footer>" +
                         "<div class='controls'>" +
                             " <button class='button button-danger doAction'>" + $true + "</button> " +
                             " <button class='button button-default cancelAction'>" + $false + "</button> " +
                         "</div>" +
                     "</footer>" +
                  "</div>" +
                "</div>";
         $('body').prepend($content);
      $('.doAction').click(function () {
        window.open($link, "_blank");
        $(this).parents('.dialog-ovelay').fadeOut(500, function () {
          $(this).remove();
        });
      });
$('.cancelAction, .fa-close').click(function () {
        $(this).parents('.dialog-ovelay').fadeOut(500, function () {
          $(this).remove();
        });
      });
   }
$('a.QuietTable').click(function () {
        Confirm('你在预约安静区的座位', '你确定吗？', 'Yes', 'Cancel',href="{% url 'book:book_success' table_id=seat_q.id time_id=time_choice date=day %}");
    });
$('a.NoisyTable').click(function () {
        Confirm('你在预约非安静区的座位', '你确定吗？', 'Yes', 'Cancel', href="{% url 'book:book_success' table_id=seat_n.id time_id=time_choice date=day %}");
    });
