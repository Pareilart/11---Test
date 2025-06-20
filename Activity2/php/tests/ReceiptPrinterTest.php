<?php

declare(strict_types=1);

namespace Tests\Supermarket;

use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\MockObject\MockObject;
use Supermarket\Model\Product;
use Supermarket\Model\ProductUnit;
use Supermarket\Model\Receipt;
use Supermarket\Model\ReceiptItem;
use Supermarket\Model\Discount;
use Supermarket\ReceiptPrinter;

class ReceiptPrinterTest extends TestCase
{
    private ReceiptPrinter $printer;

    protected function setUp(): void
    {
        $this->printer = new ReceiptPrinter(40);
    }

    /**
     * Première doublure : Mock de Receipt
     * Nous utilisons un mock pour vérifier les interactions avec l'objet Receipt
     */
    public function testPrintReceiptWithMock(): void
    {
        // Création du mock de Receipt
        /** @var Receipt&MockObject $receiptMock */
        $receiptMock = $this->createMock(Receipt::class);
        
        // Configuration du mock
        $receiptMock->expects($this->once())
            ->method('getItems')
            ->willReturn([]);
            
        $receiptMock->expects($this->once())
            ->method('getDiscounts')
            ->willReturn([]);
            
        $receiptMock->expects($this->once())
            ->method('getTotalPrice')
            ->willReturn(0.0);

        // Test
        $result = $this->printer->printReceipt($receiptMock);
        
        // Vérification
        $this->assertStringContainsString('Total: ', $result);
    }

    /**
     * Deuxième doublure : Stub de Product
     * Nous utilisons un stub pour simuler un produit avec des valeurs prédéfinies
     */
    public function testPresentReceiptItemWithProductStub(): void
    {
        // Création du stub de Product
        /** @var Product&MockObject $productStub */
        $productStub = $this->createStub(Product::class);
        $productStub->method('getName')
            ->willReturn('Test Product');
        $productStub->method('getUnit')
            ->willReturn(ProductUnit::EACH());

        // Création d'un ReceiptItem avec le stub
        $receiptItem = new ReceiptItem(
            $productStub,
            2.0,
            10.0,
            20.0
        );

        // Test direct de l'item via la méthode protected
        $reflection = new \ReflectionClass(ReceiptPrinter::class);
        $method = $reflection->getMethod('presentReceiptItem');
        $method->setAccessible(true);

        $result = $method->invoke($this->printer, $receiptItem);

        // Vérifications
        $this->assertStringContainsString('Test Product', $result);
        $this->assertStringContainsString('20.00', $result);
    }

    /**
     * Test avec une quantité unitaire (pas d'affichage du détail)
     */
    public function testPresentReceiptItemWithSingleQuantity(): void
    {
        /** @var Product&MockObject $productStub */
        $productStub = $this->createStub(Product::class);
        $productStub->method('getName')->willReturn('Single Item');
        $productStub->method('getUnit')->willReturn(ProductUnit::EACH());

        $receiptItem = new ReceiptItem(
            $productStub,
            1.0,
            10.0,
            10.0
        );

        $reflection = new \ReflectionClass(ReceiptPrinter::class);
        $method = $reflection->getMethod('presentReceiptItem');
        $method->setAccessible(true);

        $result = $method->invoke($this->printer, $receiptItem);

        $this->assertStringContainsString('Single Item', $result);
        $this->assertStringContainsString('10.00', $result);
        $this->assertStringNotContainsString('*', $result);
    }

    /**
     * Test avec une unité de type KILO
     */
    public function testPresentReceiptItemWithKiloUnit(): void
    {
        /** @var Product&MockObject $productStub */
        $productStub = $this->createStub(Product::class);
        $productStub->method('getName')->willReturn('Bananas');
        $productStub->method('getUnit')->willReturn(ProductUnit::KILO());

        $receiptItem = new ReceiptItem(
            $productStub,
            2.5,
            4.0,
            10.0
        );

        $reflection = new \ReflectionClass(ReceiptPrinter::class);
        $method = $reflection->getMethod('presentReceiptItem');
        $method->setAccessible(true);

        $result = $method->invoke($this->printer, $receiptItem);

        $this->assertStringContainsString('Bananas', $result);
        $this->assertStringContainsString('2.500', $result);
    }

    /**
     * Test de présentation d'une remise
     */
    public function testPresentDiscount(): void
    {
        /** @var Product&MockObject $productStub */
        $productStub = $this->createStub(Product::class);
        $productStub->method('getName')->willReturn('Apples');

        $discount = new Discount(
            $productStub,
            "3 for 2",
            -5.0
        );

        $reflection = new \ReflectionClass(ReceiptPrinter::class);
        $method = $reflection->getMethod('presentDiscount');
        $method->setAccessible(true);

        $result = $method->invoke($this->printer, $discount);

        $this->assertStringContainsString('3 for 2(Apples)', $result);
        $this->assertStringContainsString('-5.00', $result);
    }

    /**
     * Test avec un reçu complet contenant plusieurs éléments
     */
    public function testCompleteReceiptWithMultipleItems(): void
    {
        /** @var Product&MockObject $product1 */
        $product1 = $this->createStub(Product::class);
        $product1->method('getName')->willReturn('Apple');
        $product1->method('getUnit')->willReturn(ProductUnit::EACH());

        /** @var Product&MockObject $product2 */
        $product2 = $this->createStub(Product::class);
        $product2->method('getName')->willReturn('Banana');
        $product2->method('getUnit')->willReturn(ProductUnit::KILO());

        $item1 = new ReceiptItem($product1, 3.0, 1.0, 3.0);
        $item2 = new ReceiptItem($product2, 1.5, 2.0, 3.0);
        $discount = new Discount($product1, "3 for 2", -1.0);

        /** @var Receipt&MockObject $receipt */
        $receipt = $this->createMock(Receipt::class);
        $receipt->method('getItems')->willReturn([$item1, $item2]);
        $receipt->method('getDiscounts')->willReturn([$discount]);
        $receipt->method('getTotalPrice')->willReturn(5.0);

        $result = $this->printer->printReceipt($receipt);

        $this->assertStringContainsString('Apple', $result);
        $this->assertStringContainsString('Banana', $result);
        $this->assertStringContainsString('3 for 2', $result);
        $this->assertStringContainsString('5.00', $result);
    }

    /**
     * Test avec une largeur de colonne personnalisée
     */
    public function testCustomColumnWidth(): void
    {
        $customPrinter = new ReceiptPrinter(20);
        
        /** @var Product&MockObject $productStub */
        $productStub = $this->createStub(Product::class);
        $productStub->method('getName')->willReturn('Test');
        $productStub->method('getUnit')->willReturn(ProductUnit::EACH());

        $receiptItem = new ReceiptItem($productStub, 1.0, 10.0, 10.0);

        $reflection = new \ReflectionClass(ReceiptPrinter::class);
        $method = $reflection->getMethod('presentReceiptItem');
        $method->setAccessible(true);

        $result = $method->invoke($customPrinter, $receiptItem);

        $this->assertEquals(20, strlen(trim($result)));
    }
} 