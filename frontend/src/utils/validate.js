export const isMobile = () => {
    if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        return true
    } else {
        return false
    }
}

export const helperFormatDateYYYMMDD = (stringDate) => {
    // "2024-7-1" => 2024-07-01;
    const originalDate = stringDate
    const dateParts = originalDate.split("-");
    const year = dateParts[0];
    const month = dateParts[1].padStart(2, "0");
    const day = dateParts[2].padStart(2, "0");

    const formattedDate = `${year}-${month}-${day}`;
    return formattedDate;
}
