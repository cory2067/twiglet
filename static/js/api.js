async function getObjects() {
    const response = await fetch('/api/objects');
    const data = await response.json();
    return data.objects;
}

async function craft(objects, prompt) {
    const apiObjects = objects.map(object => ({
        ...object,
        texture: undefined,
        sprite: undefined,
    }));
    const response = await fetch('/api/craft', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({objects: apiObjects, prompt}),
    });
    const data = await response.json();
    return data.crafted_object;
}