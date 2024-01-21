
const WIDTH = 1200;
const HEIGHT = 300;
const RATE = 1200; // the higher this number, the slower the battle goes

const player = {
    name: "you",
    hp: 30,
    activeWeapon: null,
    activeWeaponIndex: 0,
    timeToNextAction: null,
    arsenal: null,
    activeModifiers: [], // {stat: stat, remainingTurns: int, modifierValue: int, isDebuff: boolean}
}
const opponent = {
    name: "opponent",
    hp: 30,
    activeWeapon: null,
    activeWeaponIndex: 0,
    timeToNextAction: null,
    arsenal: null,
    activeModifiers: [], // {stat: stat, remainingTurns: int, modifierValue: int, isDebuff: boolean}
}

const app = new PIXI.Application({ background: '#FEF9EF', width: WIDTH, height: HEIGHT });
const ticker = PIXI.Ticker.shared;


document.querySelector("#pixi").appendChild(app.view);

app.stage.eventMode = 'static';
app.stage.hitArea = app.screen;

function updateWeapon(baseWeapon, activeModifiers) {
    return baseWeapon;
}

function doTurn(actor, oppActor) {
    const battleLog = document.querySelector("#log")
    const baseWeapon = actor.activeWeapon;
    const weapon = updateWeapon(baseWeapon, actor.activeModifiers);
    const randNum = Math.random()

    // if hit
    if (randNum < weapon.accuracy/100) {
        oppActor.hp -= weapon.strength; // subtract damage from opp health
        battleLog.innerText += `${actor.name} dealt ${weapon.strength} damage to ${oppActor.name} with ${weapon.name}!\n`

        actor.activeWeapon.durability -= 1; // decrement durability, then replace weapon if needed
        if (actor.activeWeapon.durability <= 0) { 
            actor.activeWeaponIndex += 1;
            actor.activeWeapon = actor.arsenal.objects[actor.activeWeaponIndex];

            if (!actor.activeWeapon) ticker.stop()
            battleLog.innerText += `${actor.name} changed weapons to ${actor.activeWeapon.name}\n`
        }

        // add new buffs and debuffs associated with hit
    } else {
        battleLog.innerText += `${actor.name} tried to attack ${oppActor.name} with ${weapon.name} but missed!\n`
    }

    // update all modifiers

    // use modifiers + weapon to update time to next action
    actor.timeToNextAction = Math.ceil(RATE/(actor.activeWeapon.speed + 5));

}

function checkVictory() {
    const battleLog = document.querySelector("#log")
    
    if (opponent.hp <= 0) {
        if (player.hp > 0) {
            battleLog.innerText += "You Win!";
            ticker.stop();
        } else {
            battleLog.innerText += "Tie!";
            ticker.stop();
        }
    } else if (player.hp <= 0) {
        battleLog.innerText += "You lose!";
        ticker.stop();
    }
}

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
    // for every delta:
    // decrement the timeToNextAction by delta
    // if the time is no longer positive, use the active weapon on the opponent after applying
    // all activeModifiers
    // decrement the remainingTurns on each activeModifier
    // if the move hits, decrement the durability of the active weapon, update opponent hp, update opponent modifiers
    // if the durability hits 0, use the next active weapon
    // do the same logic with the opponent
    // reset timeToNextAction
    player.timeToNextAction -= delta;
    opponent.timeToNextAction -= delta;

    // player's turn
    if (player.timeToNextAction <= 0) {
        doTurn(player, opponent)
    }

    // opponent's turn
    if (opponent.timeToNextAction <= 0) {
        doTurn(opponent, player)
    }

    // check victory condition
    checkVictory()
}

async function main() {
    const [myArsenal, opponentArsenal] = await loadArsenals();
    console.log(myArsenal);
    console.log(opponentArsenal);

    // initialize the player's first weapon and the time to their first action
    // before kicking off the gameLoop
    player.activeWeapon = myArsenal.objects[0];
    player.timeToNextAction = Math.ceil(RATE/(player.activeWeapon.speed + 5));
    player.arsenal = myArsenal;
    opponent.activeWeapon = opponentArsenal.objects[0];
    opponent.timeToNextAction = Math.ceil(RATE/(opponent.activeWeapon.speed + 5));
    opponent.arsenal = opponentArsenal;
    ticker.add(gameLoop)
}

main();