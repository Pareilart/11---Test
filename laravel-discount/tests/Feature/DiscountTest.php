<?php

use App\Services\DiscountService;

beforeEach(function () {
    $this->discountService = new DiscountService();
});

test('calcul de remise avec des valeurs valides', function () {
    expect($this->discountService->calculateDiscount(100, 20))->toBeFloat(20.0);
    expect($this->discountService->calculateDiscount(100, 0))->toBeFloat(0.0);
    expect($this->discountService->calculateDiscount(100, 100))->toBeFloat(100.0);
});

test('calcul de remise avec un montant négatif', function () {
    expect(fn () => $this->discountService->calculateDiscount(-100, 20))
        ->toThrow(InvalidArgumentException::class, 'Le montant ne peut pas être négatif');
});

test('calcul de remise avec un pourcentage invalide', function () {
    expect(fn () => $this->discountService->calculateDiscount(100, 150))
        ->toThrow(InvalidArgumentException::class, 'Le pourcentage de remise doit être entre 0 et 100');
});

test('calcul du montant final avec des valeurs valides', function () {
    expect($this->discountService->calculateFinalAmount(100, 20))->toBeFloat(80.0);
    expect($this->discountService->calculateFinalAmount(100, 0))->toBeFloat(100.0);
    expect($this->discountService->calculateFinalAmount(100, 100))->toBeFloat(0.0);
});