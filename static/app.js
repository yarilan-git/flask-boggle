
$("button").on('click', checkWord);
$("input").on('focus', function() {$("input").val("")});
$("#result").attr("class", "hidden");

let score = 0;
let games = 0;
let timer = 60;
let timeoutID = setTimeout(stopGame, 60000);
let intervalID = setInterval(function() {$("#time_left").text(`Time left: ${timer--} seconds`);}, 1000);
let usedWords = [];


function stopGame() {
    // At the end of a game:
    //    1) Disables the word entry form
    //    2) Announces that the game is over
    //    3) Stops the remaining time display
    //    4) Sends the game's statistics to the server for storage

    $("form").attr("class", "hidden");
    $("#result").text("Game is over");
    $("#time_left").text('Time left: 0 seconds');
    clearInterval(intervalID);
    updateStats();
}

async function updateStats() {
    // Updates the game's statistics on the server
    // and displays the overall game activity

    let res = await axios.post('/update_stats', {score: score});  
    $("#games").text(`Games played: ${res.data['games']}`);
    $("#high_score").text(`High score: ${res.data['high_score']}`);
}


async function checkWord(e) {
    // 1) If the word entered has already been used, notifies the user
    //    and takes no further actions
    // 2) Otherwise, asks the server to check the validity of the new word, 
    //    informs the user what the result was, and updates the score

    e.preventDefault();
    word=$("input").val();
    if (usedWords.includes(word)) {
        $("#result").text("You already used this word. Try again.");
        return;    
    }

    usedWords.push(word);
    let msg;
    let result = await axios.get('/check_word', {params :{a_word : word}});
   
    switch (result.data.result) {
        case "ok":
            score += word.length;    
            msg = `You entered a valid word`;
            break;
        case "not-on-board":
            msg = "Your word is a valid dictionary word but not on the board";
            break;
        case "not-word":
            msg = "Your word is not a valid word"
            break;
    }

    $("#result").text(msg);
    $("#result").attr("class", "show");
    $("#score").text(`Total score : ${score}`);
    
}

