import { describe, expect, test } from 'vitest';
import { isMobile, helperFormatDateYYYMMDD } from './validate';

class Navigator {
    constructor(userAgent) {
        Object.defineProperty(this, 'userAgent', {
            value: userAgent,
            configurable: true,
            writable: true
        });
    }
}

describe('isMobile function', () => {
    test('returns true for a mobile user agent', () => {
        var userAgent =
        'Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36';
        global.navigator = new Navigator();
        navigator.userAgent = userAgent;

        const result = isMobile();
        expect(result).toBe(true);
    });

    test('returns false for a non-mobile user agent', () => {
        var userAgent =
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36';
        global.navigator = new Navigator(userAgent);
        navigator.userAgent = userAgent;

        const result = isMobile();
        expect(result).toBe(false);
    });
});

describe('helperFormatDateYYYMMDD function', () => {
    test('formats stringDate "YYYY-M-D" to "YYYY-MM-DD"', () => {
        const stringDate = '2024-7-1';
        const expectedDate = '2024-07-01';
        const formattedDate = helperFormatDateYYYMMDD(stringDate);
        expect(formattedDate).toEqual(expectedDate);
    });

    test('formats stringDate "YYYY-MM-DD" to "YYYY-MM-DD"', () => {
        const stringDate = '2024-12-25';
        const expectedDate = '2024-12-25';
        const formattedDate = helperFormatDateYYYMMDD(stringDate);
        expect(formattedDate).toEqual(expectedDate);
    });

    test('formats stringDate "YYYY-MM-DD" with leading zeros to "YYYY-MM-DD"', () => {
        const stringDate = '2024-05-03';
        const expectedDate = '2024-05-03';
        const formattedDate = helperFormatDateYYYMMDD(stringDate);
        expect(formattedDate).toEqual(expectedDate);
    });
});