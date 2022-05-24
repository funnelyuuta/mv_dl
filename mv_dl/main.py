from pathlib import Path
import requests
import click

@click.command()
@click.option('--url', '-u',
              help='保存対象のURL',
              required=True)
@click.option('--save','-s',
              help='保存先',
              required=True)
@click.option('--name','-n',
              help='ファイル名',
              required=True)
def main(url, save, name):
    '''
    動画のurlのurlから動画をダウンロードするよう
    '''
    try:
        mv = requests.get(url)
    except Exception as e:
        print(e)
        print('このプログラムでは保存できません')
    print('保存実施します')
    save_mv_path = Path(save,f"{name}")
    with open(save_mv_path, 'wb') as savefile:
        savefile.write(mv.content)
    print('保存完了')

