const WIDTH = 1000;
const HEIGHT = 900;
const CRAFTING_AREA_WIDTH = 150;
const MAIN_AREA_WIDTH = WIDTH - CRAFTING_AREA_WIDTH;

const app = new PIXI.Application({ background: '#eeeeee', width: WIDTH, height: HEIGHT });

document.querySelector("#pixi").appendChild(app.view);

let hoveredObject = null;
let draggingObject = null;
let displayedObjects = [];

app.stage.on('pointerup', onDragEnd);
app.stage.on('pointerupoutside', onDragEnd);

app.stage.eventMode = 'static';
app.stage.hitArea = app.screen;

async function main() {
    // get all possible objects and their textures
    const objects = await getObjects();
    for (const object of objects) {
        initTexture(object);
    }

    // build crafting area
    let obj = new PIXI.Graphics();
    obj.beginFill(0xcccccc);
    obj.drawRect(MAIN_AREA_WIDTH, 0, CRAFTING_AREA_WIDTH, HEIGHT);
    app.stage.addChild(obj);
   
    const numObjects = 25;
    for (let i = 0; i < numObjects; i++) {
        const randomObj = objects[Math.floor(Math.random() * objects.length)];
        displayedObjects.push({...randomObj});
    }

    for (const object of displayedObjects) {
        createObject(
            object,
            Math.floor(Math.random() * (MAIN_AREA_WIDTH - 50)),
            Math.floor(Math.random() * HEIGHT),
        );
    }
}

function initTexture(object) {
    const texture = PIXI.Texture.from(`/sprites/${object.file}`);
    texture.baseTexture.scaleMode = PIXI.SCALE_MODES.NEAREST;
    object.texture = texture;
}

function createObject(object, x, y) {
    const sprite = new PIXI.Sprite(object.texture);
    
    // allows intereaction
    sprite.eventMode = 'static';
    sprite.cursor = 'pointer';
    sprite.anchor.set(0.5);
    sprite.scale.set(0.5);
    object.sprite = sprite;
    sprite.on('pointerdown', () => onDragStart(object));
    sprite.on('pointerover', () => onHover(object));
    sprite.on('pointerout', () => onHoverEnd());

    sprite.x = x;
    sprite.y = y;

    app.stage.addChild(sprite);
}

function onDragStart(object) {
    draggingObject = object;
    object.sprite.alpha = 0.5;
    app.stage.on('pointermove', onDragMove);
}

function onHover(object) {
    hoveredObject = object;
    object.sprite.alpha = 0.7;
    renderSidebar(object);
}

function onHoverEnd() {
    if (!hoveredObject) return;
    hoveredObject.sprite.alpha = 1;
    hoveredObject = null;
    renderSidebar();
}

function onDragEnd() {
    if (!draggingObject) return;
    const sprite = draggingObject.sprite;
    sprite.alpha = hoveredObject ? 0.7 : 1;
    draggingObject = null;
    app.stage.off('pointermove', onDragMove);
    renderSidebar();
}

function onDragMove(event) {
    if (draggingObject) {
        const sprite = draggingObject.sprite;
        sprite.parent.toLocal(event.global, null, sprite.position);
    }
}

function getCraftingObjects() {
    return displayedObjects.filter(o => o.sprite.position.x > MAIN_AREA_WIDTH);
}

function renderSidebar(selectedObject) {
    if (selectedObject) {
        const selected = document.querySelector("#selected")
        renderObjectDescription(selected, selectedObject)
    }

    const craftingObjects = getCraftingObjects();
    const craftingEl = document.querySelector("#crafting");
    renderCraftingList(craftingEl, craftingObjects);
}

function renderObjectDescription(el, o) {
    el.style.display = 'block';
    el.innerHTML = `
        <strong>${o.name}</strong>
        <p>${o.object_description}</p>
        <ul>
            <li>Attack: ${o.attack_description}</li>
            <li>Strength: ${o.strength}</li>
            <li>Durability: ${o.durability}</li>
            <li>Accuracy: ${o.accuracy}</li>
            <li>Speed: ${o.speed}</li>
        </ul>
    `
}

function renderCraftingList(el, objs) {
    const listElements = objs.map(o => 
        `<li><strong>${o.name}</strong> - ${o.object_description}</li>`
    );

    el.innerHTML = `
        <ul>
            ${listElements.join('')}
        </ul>
    `
}

async function submit() {
    const prompt = document.querySelector("#prompt").value;
    const objects = getCraftingObjects();
    const craftedObject = await craft(objects, prompt);
    initTexture(craftedObject);

    for (const object of objects) {
        object.sprite.destroy();
    }
    // remove destroyed objects from displayedObjects
    displayedObjects = displayedObjects.filter(o => !!o.sprite.transform);
    renderSidebar(craftedObject);
   
    createObject(
        craftedObject,
        MAIN_AREA_WIDTH + CRAFTING_AREA_WIDTH / 2,
        HEIGHT / 2,
    );
    displayedObjects.push(craftedObject);
}
 

main();