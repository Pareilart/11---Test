const { calculateDiscount, calculateFinalAmount } = require('./discount');

describe('Tests du module de remise', () => {
    describe('calculateDiscount', () => {
        test('calcule correctement une remise de 20% sur 100€', () => {
            expect(calculateDiscount(100, 20)).toBe(20);
        });

        test('calcule correctement une remise de 0%', () => {
            expect(calculateDiscount(100, 0)).toBe(0);
        });

        test('calcule correctement une remise de 100%', () => {
            expect(calculateDiscount(100, 100)).toBe(100);
        });

        test('lance une erreur pour un montant négatif', () => {
            expect(() => calculateDiscount(-100, 20)).toThrow('Le montant ne peut pas être négatif');
        });

        test('lance une erreur pour un pourcentage de remise invalide', () => {
            expect(() => calculateDiscount(100, 150)).toThrow('Le pourcentage de remise doit être entre 0 et 100');
        });
    });

    describe('calculateFinalAmount', () => {
        test('calcule correctement le montant final avec une remise de 20%', () => {
            expect(calculateFinalAmount(100, 20)).toBe(80);
        });

        test('calcule correctement le montant final avec une remise de 0%', () => {
            expect(calculateFinalAmount(100, 0)).toBe(100);
        });

        test('calcule correctement le montant final avec une remise de 100%', () => {
            expect(calculateFinalAmount(100, 100)).toBe(0);
        });
    });
}); 