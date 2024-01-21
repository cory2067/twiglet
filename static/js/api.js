function sanitizeObjects(objects) {
    return objects.map(object => ({
        ...object,
        texture: undefined,
        sprite: undefined,
    }));
}

async function getObjects() {
    const response = await fetch('/api/objects');
    const data = await response.json();
    return data.objects;
}

async function craft(objects, prompt) {
    const apiObjects = sanitizeObjects(objects);
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

async function submitArsenal(objects, name) {
    const apiObjects = sanitizeObjects(objects);
    const response = await fetch('/api/arsenal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({objects: apiObjects, name}),
    });
    const data = await response.json();
    return data.arsenal_id;
}

async function getRandomArsenal(excludeId) {
    const response = await fetch(`/api/random-arsenal?exclude_id=${excludeId}`);
    const data = await response.json();
    return data.arsenal;
}

async function getArsenal(id) {
    const response = await fetch(`/api/arsenal/${id}`);
    const data = await response.json();
    return data.arsenal;
}