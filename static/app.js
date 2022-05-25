
$("button").on('click', checkWord);
$("input").on('focus', function() {$("input").val("")});
$("#result").attr("class", "hidden");
let score = 0;
let games = 0;
var timeoutID = setTimeout(stopGame, 60000);

function stopGame() {
    $("form").attr("class", "hidden");
    $("#result").text("Game is over");

    updateStats();

}

async function updateStats() {
    // let data = `'${score}'`;
    let res = await axios.get('/update_stats', {params : {score : score}});      
    $("#games").text(`Games played: ${res.data['games']}`);
    $("#high_score").text(`High score: ${res.data['high_score']}`);
}


async function checkWord(e) {
    e.preventDefault();
    console.log($("input").val())
    guess=$("input").val();
    // let data = `{"word" : "${guess}"}`;

    let endPoint = '/check_guess';
    let msg;
    // console.log("data: ", data, "end point: ", endPoint);
    let result = await axios.post('/check_guess', {a_guess : guess});
    console.log("result back on client was:" , result.data.result);    
    switch (result.data.result) {
        case "ok":
            score += guess.length;    
            msg = `You guessed correctly`;
            break;
        case "not-on-board":
            msg = "Your guess is a valid word but not on the board";
            break;
        case "not-word":
            msg = "Your guess is not a valid word"
            break;
    }
    console.log("result from axios is:", result);
    console.log("the message is:", msg);

    $("#result").text(msg);
    $("#result").attr("class", "show");
    $("#score").text(`Total score : ${score}`);
    
}

