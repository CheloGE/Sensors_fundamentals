def get_topK_amp_freq(Fourier_coeffs, frequencies_vector, top_k=5):
    """
        This functions gets fourier coefficients and frequencies vector and returns
        the top_k Fourier coefficient amplitudes and their respective frequencies
    """
    # Order highest amplitude frequencies from higher to lower
    ind = np.argsort(abs(Fourier_coeffs))[::-1]
    sorted_Fcoeffs = Fourier_coeffs[ind]
    maxFreqs = []
    maxFcoeffs_amp = []
    for i, freq in enumerate(frequencies_vector[ind]):
        if len(maxFreqs) >= top_k:
            break
        if np.round(freq,0) not in np.round(maxFreqs,0):
            maxFreqs.append(freq)
            maxFcoeffs_amp.append(2*abs(sorted_Fcoeffs[i]))
    return maxFreqs, maxFcoeffs_amp