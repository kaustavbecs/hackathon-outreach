import { readFileSync } from 'fs';

export const handler = async (event) => {
    try {
        const staticText = readFileSync('staticText.txt', 'utf8');
        const response = {
            statusCode: 200,
            body: staticText
        };
        return response;
    } catch (err) {
        console.error('Error reading file:', err);
        return {
            statusCode: 500,
            body: 'Internal Server Error'
        };
    }
};
