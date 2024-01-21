
const WIDTH = 1200;
const HEIGHT = 250;
const RATE = 600; // the higher this number, the slower the battle goes

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


let textures = {};
let activeSprites = [];

document.querySelector("#pixi").appendChild(app.view);

app.stage.eventMode = 'static';
app.stage.hitArea = app.screen;

function updateWeapon(baseWeapon, activeModifiers) {
    return baseWeapon;
}

function computeTimeToNextAction(weapon, activeModifiers) {
    return Math.ceil(RATE/(weapon.speed + 5));
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
    } else {
        battleLog.innerText += `${actor.name} tried to attack ${oppActor.name} with ${weapon.name} but missed!\n`
    }

    // update durability no matter what
    actor.activeWeapon.durability -= 1; // decrement durability, then replace weapon if needed
    if (actor.activeWeapon.durability <= 0) { 
        actor.activeWeaponIndex += 1;
        actor.activeWeapon = actor.arsenal.objects[actor.activeWeaponIndex];

        if (!actor.activeWeapon) ticker.stop()
        battleLog.innerText += `${actor.name} changed weapons to ${actor.activeWeapon.name}\n`
    }

    // update all modifiers

    // use modifiers + weapon to update time to next action
    actor.timeToNextAction = computeTimeToNextAction(actor.activeWeapon, actor.activeModifiers);
    setDisplayedWeapons(player.activeWeapon, opponent.activeWeapon);
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

function addSprite(sprite) {
    app.stage.addChild(sprite);
    activeSprites.push(sprite);
    sprite.scale.set(1);
}

function setDisplayedWeapons(weaponLeft, weaponRight) {
    for (const sprite of activeSprites) {
        app.stage.removeChild(sprite);
    }
    activeSprites = [];

    const leftSprite = createSprite(weaponLeft, 0, 100, textures);
    const rightSprite = createSprite(weaponRight, WIDTH-0, 100, textures);

    addSprite(leftSprite);
    addSprite(rightSprite);
}

async function loadArsenals() { 
    const objects = await getObjects();
    textures = getTextures(objects);

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

function handleAnimation() {
    const getProgress = (actor) => {
        return 1 - actor.timeToNextAction / computeTimeToNextAction(actor.activeWeapon, actor.activeModifiers);
    };

    const leftProgress = getProgress(player);
    const rightProgress = getProgress(opponent);

    const [leftSprite, rightSprite] = activeSprites;
    leftSprite.scale.set(1+ 0.3 * leftProgress);
    rightSprite.scale.set(1 + 0.3 * rightProgress);

    leftSprite.x = 1200 * leftProgress;
    rightSprite.x = WIDTH - 1200 * rightProgress;

    leftSprite.rotation = 6.28 * leftProgress;
    rightSprite.rotation = -6.28 * rightProgress;
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

    handleAnimation()
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
    setDisplayedWeapons(player.activeWeapon, opponent.activeWeapon);
    ticker.add(gameLoop)
}

main();