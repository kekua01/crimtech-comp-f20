
// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];
// some baby yoda quotes
let baby_quotes = ["Frogs", "Mando", "Mwahhh", "Yes"]

function respond() {
	var image = "";
	var quote = "";
	var hm = "m".repeat(2 + Math.floor(Math.random() * 13));

	message = document.getElementById("chat-box");
	chat = message.value;
	console.log(chat);

	//check to see if the words 'force' and 'dark' are in the chat message
	var force = chat.includes('force');
	var dark = chat.includes('dark');

	//flowchart
	if (chat.includes('cute') || chat.includes('baby')) {
		//pick a random thing to say from baby quotes
		quote = baby_quotes[Math.floor(Math.random() * baby_quotes.length)] + ", " + hm;
		if (force) {
			image = dark ? "img/cute-dark.jpg" : "img/cute-force.jpg";
		}
		else {
			image = "img/cute-std.jpg"
		}
	}
	else {
		quote = "H" + hm + ". "
		if (force) {
			if (dark) {
				image = "img/regular-dark.jpg";
				quote += dark_quotes[Math.floor(Math.random() * dark_quotes.length)]
			}
			else {
				image = "img/regular-force.jpg";
				quote += force_quotes[Math.floor(Math.random() * force_quotes.length)]
			}
		}
		else {
			image = "img/regular-std.jpg"
			quote += std_quotes[Math.floor(Math.random() * std_quotes.length)]
		}
	}
 	document.getElementById("yoda-pic").setAttribute("src", image);
    document.getElementById("yoda-quote").innerHTML = quote;
   	message.value = "";
}

