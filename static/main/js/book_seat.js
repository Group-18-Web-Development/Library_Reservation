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