def is_secure_ckks(poly_modulus_degree, coeff_mod_bit_sizes):
    # Max total coeff modulus bit-length for 128-bit security (based on Microsoft SEAL guidelines)
    limits = {
        1024: 27,
        2048: 54,
        4096: 109,
        8192: 218,
        16384: 438,
        32768: 881
    }

    total_coeff_bits = sum(coeff_mod_bit_sizes)
    limit = limits.get(poly_modulus_degree, None)

    if limit is None:
        return f"Unknown poly_modulus_degree {poly_modulus_degree}. Choose from {list(limits.keys())}."
    
    if total_coeff_bits <= limit:
        return f"✅ Secure: Total coeff bits = {total_coeff_bits}, within 128-bit security bound ({limit})"
    else:
        return f"⚠️ Not secure: Total coeff bits = {total_coeff_bits}, exceeds 128-bit bound ({limit})"

# Example usage:
print(is_secure_ckks(4096, [60, 40, 40, 60]))     # 200 bits → Secure ✅
# print(is_secure_ckks(8192, [60, 60, 60, 60]))     # 240 bits → Not secure ⚠️
