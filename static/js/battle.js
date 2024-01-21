
const WIDTH = 1200;
const HEIGHT = 300;

const app = new PIXI.Application({ background: '#FEF9EF', width: WIDTH, height: HEIGHT });
const ticker = PIXI.Ticker.shared;
ticker.add(gameLoop)

document.querySelector("#pixi").appendChild(app.view);

app.stage.eventMode = 'static';
app.stage.hitArea = app.screen;

async function loadArsenals() { 
    const urlParams = new URLSearchParams(window.location.search);
    const arsenalId = urlParams.get('arsenal');
    const arsenal = await getArsenal(arsenalId);

    const opponentArsenalId = urlParams.get('opponent');
    let opponentArsenal = null;
    if (opponentArsenalId) {
        opponentArsenal = await getArsenal(opponentArsenalId);
    } else {
        opponentArsenal = await getRandomArsenal(arsenalId);
    }

    return [arsenal, opponentArsenal];
}

async function gameLoop(delta) {
    console.log(delta);
}

async function main() {
    const [myArsenal, opponentArsenal] = await loadArsenals();
    console.log(myArsenal);
    console.log(opponentArsenal);

}

main();