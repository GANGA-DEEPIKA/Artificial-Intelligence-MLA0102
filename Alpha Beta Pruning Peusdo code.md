FUNCTION alphabeta(depth, node, isMaximizingPlayer, values, alpha, beta)
    IF depth == 3 THEN
        RETURN values[node]    // Leaf node value

    IF isMaximizingPlayer THEN
        best = -INFINITY
        FOR i = 0 TO 1 DO
            val = alphabeta(depth + 1, node * 2 + i, FALSE, values, alpha, beta)
            best = MAX(best, val)
            alpha = MAX(alpha, best)
            IF beta <= alpha THEN
                BREAK            // Beta cut-off
        END FOR
        RETURN best

    ELSE  // Minimizing player
        best = +INFINITY
        FOR i = 0 TO 1 DO
            val = alphabeta(depth + 1, node * 2 + i, TRUE, values, alpha, beta)
            best = MIN(best, val)
            beta = MIN(beta, best)
            IF beta <= alpha THEN
                BREAK            // Alpha cut-off
        END FOR
        RETURN best
END FUNCTION

// Main Program
values = [2, 3, 5, 9, 0, 1, 7, 5]   // Leaf node values
CALL alphabeta(0, 0, TRUE, values, -INFINITY, +INFINITY)
PRINT result
