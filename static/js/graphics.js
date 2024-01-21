
function getTextures(objects) {
    const textures = {};
    for (const object of objects) {
        for (const filename of object.sprites) {
            const texture = PIXI.Texture.from(`/sprites/${filename}`);
            texture.baseTexture.scaleMode = PIXI.SCALE_MODES.NEAREST;
            textures[filename] = texture;
        }
    }
    return textures;
}

function createSprite(object, x, y, textures) {
    let sprite;
    if (object.sprites.length === 1) {
        sprite = new PIXI.Sprite(textures[object.sprites[0]]);
        sprite.anchor.set(0.5);
    } else {
        // try to merge sprites together
        sprite = new PIXI.Container();
        const numSprites = object.sprites.length;
        for (const i in object.sprites) {
            const filename = object.sprites[i];
            const texture = textures[filename];
            const subSprite = new PIXI.Sprite(texture);
            subSprite.anchor.set(0.5);
            subSprite.alpha = (numSprites - i + 2) / (numSprites + 2); // opacity fade
            sprite.addChild(subSprite);
        }
    }

    // allows interaction
    sprite.eventMode = 'static';
    //sprite.anchor.set(0.5); // doesn't work on container
    object.sprite = sprite;

    sprite.x = x;
    sprite.y = y;
    return sprite;
}