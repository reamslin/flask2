function starOutGrid(grid) {
    const stars = [];
    const N = grid.length;
    const M = grid[0].length;
    for (n = 0; n < N; n++) {
        for (m = 0; m < M; m++) {
            if (grid[n][m] == '*') {
                stars.push([n, m])
            }
        }
    }

    for (star of stars) {
        for (m = 0; m < M; m++) {
            grid[star[0]][m] = '*';
        }
        for (n = 0; n < N; n++) {
            grid[n][star[1]] = '*';
        }
    }
    return grid
}
