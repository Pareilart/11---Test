<?php

namespace App\Services;

class DiscountService
{
    /**
     * Calcule le montant de la remise
     *
     * @param float $amount Montant initial
     * @param float $discountPercentage Pourcentage de remise (0-100)
     * @return float Montant de la remise
     * @throws \InvalidArgumentException Si le montant est négatif ou le pourcentage invalide
     */
    public function calculateDiscount(float $amount, float $discountPercentage): float
    {
        if ($amount < 0) {
            throw new \InvalidArgumentException('Le montant ne peut pas être négatif');
        }

        if ($discountPercentage < 0 || $discountPercentage > 100) {
            throw new \InvalidArgumentException('Le pourcentage de remise doit être entre 0 et 100');
        }

        return $amount * ($discountPercentage / 100);
    }

    /**
     * Calcule le montant final après remise
     *
     * @param float $amount Montant initial
     * @param float $discountPercentage Pourcentage de remise (0-100)
     * @return float Montant final après remise
     */
    public function calculateFinalAmount(float $amount, float $discountPercentage): float
    {
        $discount = $this->calculateDiscount($amount, $discountPercentage);
        return $amount - $discount;
    }
} 