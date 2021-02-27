function snakeToCamel(snake) {
    const word_array = snake.split("_");

    let camel = word_array[0];

    for (i = 1; i < word_array.length; i++) {
        camel += capitalize(word_array[i])
    }

    return camel
}

function capitalize(word) {
    return word.charAt(0).toUpperCase() + word.slice(1)
}

