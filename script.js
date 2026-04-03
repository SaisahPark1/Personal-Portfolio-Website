$(document).ready(function() {
    $("li").hover(
        function() {
            $(this).stop().toggleClass('active').animate({ fontSize: '3rem' }, 500);;
        }
    );
    $('li').on('mouseleave', function() {
        $(this).stop().toggleClass('inactive').animate({ fontSize: '2rem' }, 500);;
    });
});

currentIndex = 0
cards = ["about_me", "projects", "goals", "contact"]
function travelRight(){
    if(currentIndex != 3){
        $(document.getElementById(cards[currentIndex])).fadeTo(500, 0, function(){
            document.getElementById(cards[currentIndex]).style.display = "none";
            document.getElementById(cards[currentIndex+1]).style.display = "block";
            $(document.getElementById(cards[currentIndex+1])).fadeTo(500, .8);
            currentIndex += 1
        });
    }
}
function travelLeft(){
    if(currentIndex){
        $(document.getElementById(cards[currentIndex])).fadeTo(500, 0, function(){
        document.getElementById(cards[currentIndex]).style.display = "none";
        document.getElementById(cards[currentIndex-1]).style.display = "block";
        $(document.getElementById(cards[currentIndex-1])).fadeTo(500, .8);
        currentIndex -= 1
    })}
}