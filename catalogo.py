def exibir_catalogo(produtos):
    print("=== CATÁLOGO DIGITAL - CROCHÊ DA ELEN ===\n")

    for produto, preco in produtos.items():
        print(f"{produto} - R$ {preco:.2f}")


def main():
    produtos = {
        "Bolsa de Crochê Floral": 120.00,
        "Bolsa de Crochê Verde": 130.00,
        "Suplá Artesanal": 35.00,
        "Kit para Banheiro": 80.00,
        "Porta Garrafa": 40.00
    }

    exibir_catalogo(produtos)


if __name__ == "__main__":
    main()
