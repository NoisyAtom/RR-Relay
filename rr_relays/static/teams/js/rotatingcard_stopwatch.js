
/*Javascript function for Stopwatch*/

  let hr = min = sec = ms = "0" + 0,
    startTimer;

  const startBtn = document.querySelector(".start"),
   stopBtn = document.querySelector(".stop"),
   resetBtn = document.querySelector(".reset"),
   setTimerBtn = document.querySelector(".setTime");

   startBtn.addEventListener("click", start);
   stopBtn.addEventListener("click", stop);
   resetBtn.addEventListener("click", reset);

  function start() {
    startBtn.classList.add("active");
    stopBtn.classList.remove("stopActive");

    startTimer = setInterval(()=>{
      ms++
      ms = ms < 10 ? "0" + ms : ms;

      if(ms == 100){
        sec++;
        sec = sec < 10 ? "0" + sec : sec;
        ms = "0" + 0;
      }
      if(sec == 60){
        min++;
        min = min < 10 ? "0" + min : min;
        sec = "0" + 0;
      }
      if(min == 60){
        hr++;
        hr = hr < 10 ? "0" + hr : hr;
        min = "0" + 0;
      }
      putValue();
    },10); //1000ms = 1s

  }

  function stop() {
    startBtn.classList.remove("active");
    stopBtn.classList.add("stopActive");
    clearInterval(startTimer);
  }
  function reset() {
    startBtn.classList.remove("active");
    stopBtn.classList.remove("stopActive");
    clearInterval(startTimer);
    hr = min = sec = ms = "0" + 0;
    putValue();
  }

  function putValue() {
    document.querySelector(".millisecond").innerText = ms;
    document.querySelector(".second").innerText = sec;
    document.querySelector(".minute").innerText = min;
    document.querySelector(".hour").innerText = hr;
  }
  
 /* function setTime() {
	document.getElementById("hour_in").value = document.querySelector(".hour").innerText;
	
	} */
  

/*Javascript function for CSS Cards flipping automatically*/

var elems = document.getElementsByClassName("card");
var totalSecond = 0;
var myTimer2;

function Refresh(){
    window.location.reload(1);
}


myTimer2 = setTimeout(Refresh, timeout: 30000);

function RotationCard() {
    totalSecond = totalSecond + 1;
    for (var i = 0; i < elems.length; i++) 
    {
         if(!elems[i].classList.contains("myAnim"))
            elems[i].classList.add("myAnim");

          else
            elems[i].classList.remove("myAnim");
     }
                  
   if (totalSecond <= 14400000) { // needs to be at least a 4 hour race              
       myTimer = setTimeout(RotationCard, 10000);
   }
   else
   {
       ResetAndClearCard();
   }
}
