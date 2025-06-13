/**
 * Calcule la remise applicable sur un montant donné
 * @param {number} amount - Le montant total du panier
 * @param {number} discountPercentage - Le pourcentage de remise (entre 0 et 100)
 * @returns {number} Le montant de la remise
 */
function calculateDiscount(amount, discountPercentage) {
    if (amount < 0) {
        throw new Error('Le montant ne peut pas être négatif');
    }
    if (discountPercentage < 0 || discountPercentage > 100) {
        throw new Error('Le pourcentage de remise doit être entre 0 et 100');
    }
    return (amount * discountPercentage) / 100;
}

/**
 * Calcule le montant final après remise
 * @param {number} amount - Le montant total du panier
 * @param {number} discountPercentage - Le pourcentage de remise (entre 0 et 100)
 * @returns {number} Le montant final après remise
 */
function calculateFinalAmount(amount, discountPercentage) {
    const discount = calculateDiscount(amount, discountPercentage);
    return amount - discount;
}

module.exports = {
    calculateDiscount,
    calculateFinalAmount
}; 