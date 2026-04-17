$(document).ready(function() {
    $("li").hover(
        function() {
            $(this).stop().removeClass("inactive").addClass("active");
        }
    );
    $(".hexagon").hover(
        function() {
            $(this).children().stop().fadeTo(500, .8)
        }
    );
    $('li').on('mouseleave', function() {
        $(this).stop().removeClass("active").addClass("inactive");
    });
    $('.hexagon').on('mouseleave', function() {
        $(this).children().stop().fadeTo(500, 0)
    });
    $(".the_box").animate({top: '1rem' }, 1000)
    $(".the_box p").animate({top: '-10rem' }, 1000)
    $(".glitchbox>section").hover(
        function() {
            if (window.innerWidth >= 768) {
                let index = $(".glitchbox > section").index(this);
                setActive(index);
            }
        }
    );
});

currentIndex = 0
cards = ["about_me", "projects", "goals", "contact"]

function travelRight() {
    if (currentIndex != 3 && document.body.clientWidth < 768) {
        let current = $("#" + cards[currentIndex]).closest(".glitchbox");
        let next = $("#" + cards[currentIndex + 1]).closest(".glitchbox");
        current.fadeTo(500, 0, function () {
            current.removeClass("active").addClass("inactive");
            next.removeClass("inactive").addClass("active").fadeTo(500, 0.8);
            currentIndex += 1;
        });
    }
    update();
}

function travelLeft() {
    if (currentIndex && document.body.clientWidth < 768) {
        let current = $("#" + cards[currentIndex]).closest(".glitchbox");
        let prev = $("#" + cards[currentIndex - 1]).closest(".glitchbox");
        current.fadeTo(500, 0, function () {
            current.removeClass("active").addClass("inactive");
            prev.removeClass("inactive").addClass("active").fadeTo(500, 0.8);
            currentIndex -= 1;
        });
    }
}

let currentOrder = [6, 4, 5, 3, 1, 2]
let solved = false
function update(){
    if(!solved){
        solved = true
        document.getElementById("puzzle").style.gridTemplateAreas = 
        `"hexagon${currentOrder[0]} hexagon${currentOrder[1]}" 
        "turn1 turn1" 
        "hexagon${currentOrder[2]} hexagon${currentOrder[3]}" 
        "turn2 turn2" 
        "hexagon${currentOrder[4]} hexagon${currentOrder[5]}"`
        for(let i = 0; i < 6; i++){
            let el = document.querySelector("#puzzle #project" + (i + 1));
            if(currentOrder[i] == i + 1){
                el.style.color = "var(--highlight)";
            } else {
                el.style.color = "var(--special)";
                solved = false;
            }
        }
        if(solved){
            console.log("YAYAYA");
        }
    }
}

function rotateClockwise(){
    [currentOrder[0], currentOrder[1], currentOrder[2], currentOrder[3]] = [currentOrder[2], currentOrder[0], currentOrder[3], currentOrder[1]];
    update()
}
function rotateCounterClockwise(){
    [currentOrder[2], currentOrder[3], currentOrder[4], currentOrder[5]] = [currentOrder[3], currentOrder[5], currentOrder[2], currentOrder[4]];
    update()
}

let startX = 0;
let endX = 0;

document.addEventListener("touchstart", (e) => {
  startX = e.touches[0].clientX;
});

document.addEventListener("touchend", (e) => {
  endX = e.changedTouches[0].clientX;
  handleSwipe();
});

function handleSwipe() {
  let diff = startX - endX;

  if (diff > 50) {
    travelRight();
  } else if (diff < -50) {
    travelLeft();
  }
}

window.addEventListener("resize", () => {
    if (window.innerWidth >= 768) {
        $(".glitchbox>section").css("opacity", .8).removeClass("active").addClass("inactive");
        $("#" + cards[currentIndex]).removeClass("inactive").addClass("active");
    }
});

function setActive(index) {
    $(".glitchbox").removeClass("active").addClass("inactive");
    let box = $(".glitchbox").eq(index);
    box.removeClass("inactive").addClass("active");
    currentIndex = index;
}